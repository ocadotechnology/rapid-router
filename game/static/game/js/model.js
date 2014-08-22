'use strict';

var ocargo = ocargo || {};

ocargo.Model = function(nodeData, origin, destinations, trafficLightData, maxFuel, vanId) {
    this.map = new ocargo.Map(nodeData, origin, destinations);
    this.van = new ocargo.Van(this.map.getStartingPosition(), maxFuel);

    this.trafficLights = [];
    for(var i = 0; i < trafficLightData.length; i++) {
        this.trafficLights.push(new ocargo.TrafficLight(i, trafficLightData[i], this.map.nodes));
    }

    this.timestamp = 0;
    this.subTimestamp = 0;

    this.vanId = vanId || 0;

    this.pathFinder = new ocargo.PathFinder(this);
    this.reasonForTermination = null;
};

// Resets the entire model to how it was when it was just constructed
ocargo.Model.prototype.reset = function(vanId) {
    this.van.reset();

    var destinations = this.map.getDestinations();
    for(var i = 0; i < destinations.length; i++) {
        destinations[i].reset();
    }

    for (var j = 0; j < this.trafficLights.length; j++) {
        this.trafficLights[j].reset();
    }

    this.timestamp = 0;
    this.subTimestamp = 0;
    this.reasonForTermination  =  null;

    if (vanId !== null && vanId !== undefined) {
        this.vanId = vanId;
    }
};

///////////////////////
// Begin observation function, each tests something about the model
// and returns a boolean

ocargo.Model.prototype.observe = function(desc) {
    ocargo.animation.appendAnimation({
        type: 'van',
        id: this.vanId,
        vanAction: 'OBSERVE',
        fuel: this.van.getFuelPercentage(),
        description: 'van observe: ' + desc
    });

    this.incrementSubTime();
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
    this.observe('current coordinate');
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

    if (nextNode === null) {
        // Crash
        ocargo.animation.appendAnimation({
            type: 'van',
            id: this.vanId,
            vanAction: 'CRASH',
            previousNode: this.van.previousNode,
            currentNode: this.van.currentNode,
            attemptedAction: action,
            startNode: this.van.currentNodeOriginal,
            fuel: this.van.getFuelPercentage(),
            description: 'van move action: ' + action
        });

        ocargo.animation.appendAnimation({
            type: 'popup',
            id: this.vanId,
            popupType: 'FAIL',
            failSubtype: 'CRASH',
            popupMessage: ocargo.messages.offRoad(this.van.travelled),
            description: 'crash popup'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionCall: ocargo.sound.crash,
            description: 'crash sound'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionCall: ocargo.sound.stop_engine,
            description: 'stopping engine'
        });

        this.reasonForTermination = 'CRASH';
        return false;
    }

    if (this.van.fuel < 0) {
        // Van ran out of fuel last step
        ocargo.animation.appendAnimation({
            type: 'popup',
            id: this.vanId,
            popupType: 'FAIL',
            failSubtype: 'OUT_OF_FUEL',
            popupMessage: ocargo.messages.outOfFuel,
            description: 'no fuel popup'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionCall: ocargo.sound.failure,
            description: 'failure sound'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionCall: ocargo.sound.stop_engine,
            description: 'stopping engine'
        });

        this.reasonForTermination = 'OUT_OF_FUEL';
        return false;
    }

    var light = this.getTrafficLightForNode(this.van.getPosition());
    if (light !== null && light.getState() === ocargo.TrafficLight.RED && nextNode !== light.controlledNode) {
        // Ran a red light
        ocargo.animation.appendAnimation({
            type: 'popup',
            id: this.vanId,
            popupType: 'FAIL',
            failSubtype: 'THROUGH_RED_LIGHT',
            popupMessage: ocargo.messages.throughRedLight,
            description: 'ran red traffic light popup'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
            functionCall: ocargo.sound.failure,
            description: 'failure sound'
        });

        ocargo.animation.appendAnimation({
            type: 'callable',
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
        id: this.vanId,
        vanAction: action,
        fuel: this.van.getFuelPercentage(),
        description: 'van move action: ' + action
    });

    this.incrementTime();

    return true;
};

ocargo.Model.prototype.makeDelivery = function(destination) {
    // We're at a destination node and making a delivery!
    destination.visited = true;
    ocargo.animation.appendAnimation({
        type: 'van',
        id: this.vanId,
        destinationID: destination.id,
        vanAction: 'DELIVER',
        fuel: this.van.getFuelPercentage(),
        description: 'Van making a delivery'
    });

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: ocargo.sound.delivery,
        description: 'van sound: delivery'
    });

    this.incrementTime();
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
    return this.moveVan(this.van.getPosition().previousNode, 'TURN_AROUND');
};

ocargo.Model.prototype.wait = function() {
    return this.moveVan(this.van.getPosition().currentNode, 'WAIT');
};

ocargo.Model.prototype.deliver = function() {
    var destination = this.getDestinationForNode(this.van.getPosition().currentNode);
    if(destination) {
        this.makeDelivery(destination, 'DELIVER');
    }
    return destination;
};

// Signal that the program has ended and we should calculate whether
// the play has won or not and send off those events
ocargo.Model.prototype.programExecutionEnded = function() {
    var success;
    var destinations = this.map.getDestinations();

    if(destinations.length === 1) {
        success = this.van.getPosition().currentNode === destinations[0].node;

        if(success) {
            ocargo.animation.appendAnimation({
                type: 'van',
                id: this.vanId,
                destinationID: destinations[0].id,
                vanAction: 'DELIVER',
                fuel: this.van.getFuelPercentage(),
                description: 'van delivering'
            });
        }
    }
    else {
        success = true;
        for(var i = 0; i < destinations.length; i++) {
            success &= destinations[i].visited;
        }
    }

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: ocargo.sound.stop_engine,
        description: 'stopping engine'
    });

    if(success) {
        var scoreArray = this.pathFinder.getScore();
        ocargo.game.sendAttempt(scoreArray[0]);

        // Winning popup
        ocargo.animation.appendAnimation({
            type: 'popup',
            id: this.vanId,
            popupType: 'WIN',
            popupMessage: scoreArray[1],
            description: 'win popup'
        });

        // Winning sound
        ocargo.animation.appendAnimation({
            type: 'callable',
            functionCall: ocargo.sound.win,
            description: 'win sound'
        });

        this.reasonForTermination = 'SUCCESS';
    }
    else {
        ocargo.game.sendAttempt(0);

        // Failure popup
        ocargo.animation.appendAnimation({
            type: 'popup',
            id: this.vanId,
            popupType: 'FAIL',
            failSubtype: 'OUT_OF_INSTRUCTIONS',
            popupMessage: ocargo.messages.outOfInstructions,
            hint: ocargo.game.registerFailure(),
            description: 'failure popup'
        });

        // Failure sound
        ocargo.animation.appendAnimation({
            type: 'callable',
            functionCall: ocargo.sound.failure,
            description: 'failure sound'
        });

        this.reasonForTermination ='OUT_OF_INSTRUCTIONS';
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
        if(destinations[i].node === node) {
            return destinations[i];
        }
    }
    return null;
};

// Helper functions which handles telling all parts of the model
// that time has incremented and they should generate events
ocargo.Model.prototype.incrementTime = function() {
    this.timestamp += 1;
    this.subTimestamp = 0;

    ocargo.animation.startNewTimestamp();

    for (var i = 0; i < this.trafficLights.length; i++) {
        this.trafficLights[i].incrementTime(this);
    }
};

ocargo.Model.prototype.incrementSubTime = function() {
    this.subTimestamp += 1;

    ocargo.animation.startNewSubTimestamp();
};
