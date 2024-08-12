'use strict';

var ocargo = ocargo || {};

ocargo.Model = function(nodeData, origin, destinations, trafficLightData, cowData, maxFuel) {
    this.map = new ocargo.Map(nodeData, origin, destinations);
    this.van = new ocargo.Van(this.map.startingPosition(), maxFuel);

    this.trafficLights = [];
    for(var i = 0; i < trafficLightData.length; i++) {
        this.trafficLights.push(new ocargo.TrafficLight(i, trafficLightData[i], this.map.nodes));
    }

    this.cows = [];
    for(var i = 0; i < cowData.length; i++) {
        this.cows.push(new ocargo.Cow(i, cowData[i], this.map.nodes));
    }

    this.timestamp = 0;
    this.movementTimestamp = 0;

    this.pathFinder = new ocargo.PathFinder(this);
    this.reasonForTermination = null;

    // false if evaluation of conditions etc. should be hidden from user.
    // used for evaluation of event handlers before each statement.
    this.shouldObserve = true;
};

// Resets the entire model to how it was when it was just constructed
ocargo.Model.prototype.reset = function() {
    this.van.reset();

    var destinations = this.map.getDestinations();
    for(var i = 0; i < destinations.length; i++) {
        destinations[i].reset();
    }

    for (var j = 0; j < this.trafficLights.length; j++) {
        this.trafficLights[j].reset();
    }

    for (var j = 0; j < this.cows.length; j++) {
        this.cows[j].reset();
    }

    this.timestamp = 0;
    this.movementTimestamp = 0;
    this.reasonForTermination  =  null;
};


///////////////////////
// Begin observation function, each tests something about the model
// and returns a boolean

ocargo.Model.prototype.observe = function(desc) {
    if (this.shouldObserve) {
        ocargo.animation.appendAnimation({
            type: 'van',
            vanAction: 'OBSERVE',
            fuel: this.van.getFuelPercentage(),
            description: 'van observe: ' + desc
        });

        this.incrementTime();
    }
};

ocargo.Model.prototype.isRoadForward = function() {
    this.observe('forward');
    return (this.map.isRoadForward(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isRoadLeft = function() {
    this.observe('left');
    return (this.map.isRoadLeft(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isRoadRight = function() {
    this.observe('right');
    return (this.map.isRoadRight(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isDeadEnd = function() {
    this.observe('dead end');
    return (this.map.isDeadEnd(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isCowCrossing = function(type) {
    const currentNode = this.van.getPosition().currentNode;
    this.observe('cow crossing');
    return this.getCowForNode(currentNode, [ocargo.Cow.ACTIVE, ocargo.Cow.READY]);
};

ocargo.Model.prototype.isTrafficLightRed = function() {
    this.observe('traffic light red');
    var light = this.getTrafficLightForNode(this.van.getPosition());
    return (light !== null && light.getState() === ocargo.TrafficLight.RED);
};

ocargo.Model.prototype.isTrafficLightGreen = function() {
    this.observe('traffic light green');
    var light = this.getTrafficLightForNode(this.van.getPosition());
    return (light !== null && light.getState() === ocargo.TrafficLight.GREEN);
};

ocargo.Model.prototype.isAtADestination = function() {
    this.observe('at a destination');
    return this.getDestinationForNode(this.van.getPosition().currentNode) != null;
};

ocargo.Model.prototype.getCurrentCoordinate = function() {
    var node = this.van.getPosition().currentNode;
    return node.coordinate;
};

ocargo.Model.prototype.getPreviousCoordinate = function() {
    this.observe('previous coordinate');
    var node = this.van.getPosition().previousNode;
    return node.coordinate;
};

///////////////////////
// Begin action functions, each changes something and returns
// true if it was a valid action or false otherwise

ocargo.Model.prototype.moveVan = function(nextNode, action) {
    // Crash?
    let checkedNode = action == "WAIT" ? this.van.getPosition().previousNode : this.van.getPosition().currentNode
    let currentNodeHasCow = this.getCowForNode(checkedNode, [ocargo.Cow.ACTIVE, ocargo.Cow.READY]);

    if (currentNodeHasCow) {
        handleCrash(this, gettext('You ran into a cow! '),
            'COLLISION_WITH_COW', 'collision with cow van move action: ');
        return false;
    }

    let offRoad = nextNode === null;
    let offRoadPopupMessage = function(correctSteps){
        if (correctSteps === 0) {
            return gettext('Your first move was a crash. What went wrong?');
        }
        return interpolate(ngettext(
            'Your first move was right. What went wrong after that?',
            'Your first %(correct_steps)s moves worked. What went wrong after that?',
            correctSteps
        ), {correct_steps: correctSteps}, true);
    };
    if (offRoad) {
        handleCrash(this, offRoadPopupMessage(this.van.getDistanceTravelled()), 'CRASH', 'crashing van move action: ');
        return false;
    }

    if (this.van.fuel < 0) {
        // Van ran out of fuel last step
        ocargo.event.sendEvent("LevelRunOutOfFuel", { levelName: LEVEL_NAME,
                                                      defaultLevel: DEFAULT_LEVEL,
                                                      workspace: ocargo.blocklyControl.serialize(),
                                                      failures: this.failures,
                                                      pythonWorkspace: ocargo.pythonControl.getCode() });

        ocargo.game.sendAttempt(0);

        let noFuelMessage = CHARACTER_NAME == "Electric van" ? 'Your battery ran out of charge!' : 'You ran out of fuel!'

        ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'FAIL',
            failSubtype: 'OUT_OF_FUEL',
            popupMessage: gettext(noFuelMessage + ' Try to find a shorter route to the destination.'),
            popupHint: ocargo.game.registerFailure(),
            description: 'no fuel popup'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.failure,
            description: 'failure sound'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.stop_engine,
            description: 'stopping engine'
        });

        this.reasonForTermination = 'OUT_OF_FUEL';
        return false;
    }

    let light = this.getTrafficLightForNode(this.van.getPosition());
    if (light !== null && light.getState() === ocargo.TrafficLight.RED && nextNode !== light.controlledNode) {
        ocargo.game.sendAttempt(0);

        // Ran a red light
        ocargo.event.sendEvent("LevelThroughRedLight", { levelName: LEVEL_NAME,
                                                         defaultLevel: DEFAULT_LEVEL,
                                                         workspace: ocargo.blocklyControl.serialize(),
                                                         failures: this.failures,
                                                         pythonWorkspace: ocargo.pythonControl.getCode() });

        ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'FAIL',
            failSubtype: 'THROUGH_RED_LIGHT',
            popupMessage: gettext('Uh oh, you just sent the van through a red light! Stick to the Highway ' +
                'Code - the van must wait for green.'),
            popupHint: ocargo.game.registerFailure(),
            description: 'ran red traffic light popup'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.failure,
            description: 'failure sound'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.stop_engine,
            description: 'stopping engine'
        });

        this.reasonForTermination = 'THROUGH_RED_LIGHT';
        return false;
    }

    this.van.move(nextNode);

    // Van movement animation
    ocargo.animation.appendAnimation({
        type: 'van',
        vanAction: action,
        fuel: this.van.getFuelPercentage(),
        description: 'van move action: ' + action,
        pause: true
    });

    this.incrementMovementTime();

    return true;


    function handleCrash(model, popupMessage, vanAction, actionDescription) {
        model.van.crashStatus = 'CRASHED';
        ocargo.game.sendAttempt(0);

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.stop_engine,
            description: 'stopping engine'
        });

        ocargo.animation.appendAnimation({
            type: 'crashSound',
            functionType: 'playSound',
            functionCall: ocargo.sound.crash,
            description: 'crash sound'
        });

        ocargo.animation.appendAnimation({
            type: 'van',
            vanAction: vanAction,
            previousNode: model.van.getPosition().previousNode,
            currentNode: model.van.getPosition().currentNode,
            attemptedAction: action,
            startNode: model.van.currentNodeOriginal,
            fuel: model.van.getFuelPercentage(),
            description: actionDescription + action
        });

        model.incrementMovementTime();

        ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'FAIL',
            failSubtype: 'CRASH',
            popupMessage: popupMessage,
            popupHint: ocargo.game.registerFailure(),
            description: 'crash popup'
        });

        model.reasonForTermination = 'CRASH'; // used to determine whether the play controls ('forward', 'left' and 'right' arrows) are still usable
    }
};

ocargo.Model.prototype.makeDelivery = function(destination) {
    // We're at a destination node and making a delivery!
    destination.visited = true;
    ocargo.animation.appendAnimation({
        type: 'van',
        destinationID: destination.id,
        vanAction: 'DELIVER',
        fuel: this.van.getFuelPercentage(),
        description: 'Van making a delivery'
    });

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'playSound',
        functionCall: ocargo.sound.delivery,
        description: 'van sound: delivery'
    });

    this.incrementMovementTime();
};

ocargo.Model.prototype.moveForwards = function() {
    var nextNode = this.map.isRoadForward(this.van.getPosition());
    return this.moveVan(nextNode, 'FORWARD');
};

ocargo.Model.prototype.turnLeft = function() {
    var nextNode = this.map.isRoadLeft(this.van.getPosition());
    return this.moveVan(nextNode, 'TURN_LEFT');
};

ocargo.Model.prototype.turnRight = function() {
    var nextNode = this.map.isRoadRight(this.van.getPosition());
    return this.moveVan(nextNode, 'TURN_RIGHT');
};

ocargo.Model.prototype.turnAround = function() {
    var position = this.van.getPosition();
    var turnAroundDirection;
    if(this.map.isRoadForward(position)) {
        turnAroundDirection = 'FORWARD'
    }
    else if(this.map.isRoadRight(position)) {
        turnAroundDirection = 'RIGHT'
    }
    else if(this.map.isRoadLeft(position)) {
        turnAroundDirection = 'LEFT';
    }
    else {
        turnAroundDirection = 'FORWARD';
    }
    return this.moveVan(this.van.getPosition().previousNode, 'TURN_AROUND_' + turnAroundDirection);
};

ocargo.Model.prototype.wait = function() {
    return this.moveVan(this.van.getPosition().currentNode, 'WAIT');
};

ocargo.Model.prototype.deliver = function() {
    var destination = this.getDestinationForNode(this.van.getPosition().currentNode);
    if(destination) {
        if(destination.visited){
            //fail if already visited
            ocargo.animation.appendAnimation({
                type: 'popup',
                popupType: 'FAIL',
                failSubtype: 'ALREADY_DELIVERED',
                popupMessage: gettext('You have already delivered to that destination! You must only deliver ' +
                    'once to each destination.'),
                popupHint: ocargo.game.registerFailure(),
                description: 'already delivered to destination popup'
            });

            ocargo.animation.appendAnimation({
                type: 'callable',
                functionType: 'playSound',
                functionCall: ocargo.sound.failure,
                description: 'failure sound'
            });

            ocargo.animation.appendAnimation({
                type: 'callable',
                functionType: 'playSound',
                functionCall: ocargo.sound.stop_engine,
                description: 'stopping engine'
            });

            ocargo.event.sendEvent("LevelAlreadyDelivered", { levelName: LEVEL_NAME,
                                                              defaultLevel: DEFAULT_LEVEL,
                                                              workspace: ocargo.blocklyControl.serialize(),
                                                              failures: this.failures,
                                                              pythonWorkspace: ocargo.pythonControl.getCode() });

            this.reasonForTermination = 'ALREADY_DELIVERED';
            return false;
        }
        this.makeDelivery(destination, 'DELIVER');
    } else {
        ocargo.game.sendAttempt(0);
        ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'FAIL',
            failSubtype: 'DELIVER_NON_DESTINATION',
            popupMessage: gettext("You tried to deliver to a destination that doesn't exist."),
            popupHint: ocargo.game.registerFailure(),
            description: 'tried to deliver at non-destination'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.failure,
            description: 'failure sound'
        });

        ocargo.event.sendEvent("DeliverNonDestination", { levelName: LEVEL_NAME,
                                                          defaultLevel: DEFAULT_LEVEL,
                                                          workspace: ocargo.blocklyControl.serialize(),
                                                          failures: this.failures,
                                                          pythonWorkspace: ocargo.pythonControl.getCode()
        });
        this.reasonForTermination = 'DELIVER_AT_NON_DESTINATION';
        return false;
    }
    return destination;
};

ocargo.Model.prototype.sound_horn = function() {
    const currentNode = this.van.getPosition().currentNode
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'playSound',
        functionCall: ocargo.sound.sound_horn,
        description: 'van sound: sounding the horn'
    });
    let cow = this.getCowForNode(currentNode, [ocargo.Cow.ACTIVE, ocargo.Cow.READY]);
    if (cow) {
        cow.queueLeaveAnimation(this, currentNode);
        cow.setInactive(this, currentNode);
    }
    this.moveVan(this.van.getPosition().currentNode, 'SOUND_HORN');
    return true;
};

// Signal that the program has ended and we should calculate whether
// the play has won or not and send off those events
ocargo.Model.prototype.programExecutionEnded = function () {
    var success;
    var destinations = this.map.getDestinations();
    var failType = 'OUT_OF_INSTRUCTIONS';
    var failMessage = gettext('The van ran out of instructions before it reached a destination. '  +
        'Make sure there are enough instructions to complete the delivery.');

    if (destinations.length === 1) {
        // If there's only one destination, check that the car stopped on the destination node
        success = this.van.getPosition().currentNode === destinations[0].node;

        if (success) {
            ocargo.animation.appendAnimation({
                type: 'van',
                destinationID: destinations[0].id,
                vanAction: 'DELIVER',
                fuel: this.van.getFuelPercentage(),
                description: 'van delivering'
            });
        } else {
            if ($.inArray(destinations[0].node, this.van.visitedNodes) != -1) {
                failMessage = gettext('The van visited the destination, but didn\'t stop there!');
            }
        }
    } else {
        // Checks whether all the destinations have been delivered
        success = true;
        for (var i = 0; i < destinations.length; i++) {
            success &= destinations[i].visited;
        }
        if (!success) {
            failType = 'UNDELIVERED_DESTINATIONS';
            failMessage = gettext('There are destinations that have not been delivered to. ' +
                'Ensure you visit all destinations and use the deliver command at each one.');

            ocargo.event.sendEvent("LevelUndeliveredDestinations", {
                levelName: LEVEL_NAME,
                defaultLevel: DEFAULT_LEVEL,
                workspace: ocargo.blocklyControl.serialize(),
                failures: this.failures,
                pythonWorkspace: ocargo.pythonControl.getCode()
            });
        }
    }

    // check for disconnected start block
    if (ocargo.blocklyControl.disconnectedStartBlock()) {
        failMessage = gettext('Make sure your blocks are connected to the Start block.');
    }

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'playSound',
        functionCall: ocargo.sound.stop_engine,
        description: 'stopping engine'
    });

    if (success) {
        var result = this.pathFinder.getScore();
        ocargo.game.sendAttempt(result.totalScore);

        // Winning popup
        ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'WIN',
            popupMessage: result.popupMessage,
            totalScore: result.totalScore,
            maxScore: result.maxScore,
            routeCoins: result.routeCoins,
            instrCoins: result.instrCoins,
            pathLengthScore: result.pathLengthScore,
            maxScoreForPathLength: result.maxScoreForPathLength,
            instrScore: result.instrScore,
            maxScoreForNumberOfInstructions: result.maxScoreForNumberOfInstructions,
            performance: result.performance,
            pathScoreDisabled: result.pathScoreDisabled,
            description: 'win popup'
        });

        // Winning sound
        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.win,
            description: 'win sound'
        });

        ocargo.event.sendEvent("LevelSuccess", {
            levelName: LEVEL_NAME,
            defaultLevel: DEFAULT_LEVEL,
            workspace: ocargo.blocklyControl.serialize(),
            failures: this.failures,
            pythonWorkspace: ocargo.pythonControl.getCode(),
            score: result.totalScore
        });

        this.reasonForTermination = 'SUCCESS';
    } else {
        ocargo.game.sendAttempt(0);

        // Failure popup
        ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'FAIL',
            failSubtype: failType,
            popupMessage: failMessage,
            popupHint: ocargo.game.registerFailure(),
            description: 'failure popup'
        });

        // Failure sound
        ocargo.animation.appendAnimation({
            type: 'callable',
            functionType: 'playSound',
            functionCall: ocargo.sound.failure,
            description: 'failure sound'
        });

        ocargo.event.sendEvent("LevelFailure", {
            levelName: LEVEL_NAME,
            defaultLevel: DEFAULT_LEVEL,
            workspace: ocargo.blocklyControl.serialize(),
            failures: this.failures,
            pythonWorkspace: ocargo.pythonControl.getCode()
        });

        this.reasonForTermination = failType;
    }
};

// A helper function which returns the traffic light associated
// with a particular node and orientation
ocargo.Model.prototype.getTrafficLightForNode = function(position) {

    for (var i = 0; i < this.trafficLights.length; i++) {
        var light = this.trafficLights[i];
        if (light.sourceNode === position.previousNode && light.controlledNode === position.currentNode) {
            return light;
        }
    }
    return null;
};

// A helper function which returns the destination associated with the node
ocargo.Model.prototype.getDestinationForNode = function(node) {
    var destinations = this.map.getDestinations();
    for(var i = 0; i < destinations.length; i++) {
        if(destinations[i].node === node && !destinations[i].visited) {
            return destinations[i];
        }
    }
    return null;
};

ocargo.Model.prototype.getCowForNode = function(node, state) {
    var jsonCoordinate = JSON.stringify(node.coordinate);
    for(var i = 0; i < this.cows.length; i++) {
        var cow = this.cows[i];
        if (jsonCoordinate in cow.activeNodes) {
            if (state === undefined){
                return cow;
            } else {
                if (typeof(state) === "string") {
                    state = [state];
                }
                if (state.includes(cow.activeNodes[jsonCoordinate])) {
                    return cow;
                }
            }
        }
    }
    return null;
};

ocargo.Model.prototype.incrementMovementTime = function(){
    this.movementTimestamp ++;
    this.incrementTrafficLightsTime();
    this.incrementTime();
};

// Helper functions which handles telling all parts of the model
// that time has incremented and they should generate events
ocargo.Model.prototype.incrementTime = function() {
    this.timestamp += 1;

    ocargo.animation.startNewTimestamp();

};

ocargo.Model.prototype.incrementTrafficLightsTime = function() {
    for (var i = 0; i < this.trafficLights.length; i++) {
        this.trafficLights[i].incrementTime(this);
    }
};

ocargo.Model.prototype.getNodesAhead = function(node) {
    var nodes = [];
    for (var i = 0 ; i < node.connectedNodes.length ; i++){
        for (var j = 0 ; j < node.connectedNodes[i].connectedNodes.length ; j++ ) {
            nodes.push(node.connectedNodes[i].connectedNodes[j]);
        }
    }
    return nodes;
};

ocargo.Model.prototype.startingPosition = function() {
    return this.map.startingPosition();
};
