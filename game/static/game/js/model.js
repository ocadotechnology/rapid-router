/*
Code for Life

Copyright (C) 2015, Ocado Innovation Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
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

    this.soundedHorn = {};
    this.puffedUp = {};
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

    // Display cow on origin node if exists
    var node = this.map.originCurrentNode;
    this.setCowsActive(node);

    this.timestamp = 0;
    this.movementTimestamp = 0;
    this.reasonForTermination  =  null;
    this.soundedHorn = {};
    this.puffedUp = {};
};

// Randomly chooses the cow positions, called by program.js
ocargo.Model.prototype.chooseNewCowPositions = function() {
    for (var j = 0; j < this.cows.length; j++) {
        this.cows[j].chooseNewCowPositions();
    }
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
    var result = false;
    this.observe('cow crossing');
    var node = this.van.getPosition().currentNode;
    var nodes = this.getNodesAhead(node);
    for (var i = 0 ; i < nodes.length ; i++) {
        var cow = this.getCowForNode(nodes[i], ocargo.Cow.ACTIVE);
        if (cow != null && cow.type == type && cow.triggerEvent) {
            cow.triggerEvent = false;
            result = true;
        }
    }
    return result;
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
    //Crash?
    var previousNodeCow = this.getCowForNode(this.van.getPosition().currentNode, ocargo.Cow.ACTIVE);
    var collisionWithCow = previousNodeCow && nextNode !== this.van.getPosition().currentNode;

    if(collisionWithCow) {
        handleCrash(this, ocargo.messages.collisionWithCow, 'COLLISION_WITH_COW', 'collision with cow van move action: ');
        return false;
    }

    var offRoad = nextNode === null;
    if (offRoad) {
        handleCrash(this, ocargo.messages.offRoad(this.van.getDistanceTravelled()), 'CRASH', 'crashing van move action: ');
        return false;
    }

    if (this.van.fuel < 0) {
        // Van ran out of fuel last step
        ocargo.event.sendEvent("LevelRunOutOfFuel", { levelName: LEVEL_NAME,
                                                      defaultLevel: DEFAULT_LEVEL,
                                                      workspace: ocargo.blocklyControl.serialize(),
                                                      failures: this.failures,
                                                      pythonWorkspace: ocargo.pythonControl.getCode() });

        ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'FAIL',
            failSubtype: 'OUT_OF_FUEL',
            popupMessage: ocargo.messages.outOfFuel,
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

    var light = this.getTrafficLightForNode(this.van.getPosition());
    if (light !== null && light.getState() === ocargo.TrafficLight.RED && nextNode !== light.controlledNode) {
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
            popupMessage: ocargo.messages.throughRedLight,
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

    // Display cow on node if exists
    this.setCowsActive(nextNode);

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

ocargo.Model.prototype.setCowsActive = function(nextNode) {
    var nodes = this.getNodesAhead(nextNode);
    for (var i = 0 ; i < nodes.length ; i++){
        var cow = this.getCowForNode(nodes[i], ocargo.Cow.READY);
        if (cow){
            cow.setActive(this, nodes[i]);
        }
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
                popupMessage: ocargo.messages.alreadyDelivered,
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
    }
    return destination;
};

ocargo.Model.prototype.sound_horn = function() {
    this.soundedHorn = {timestamp:this.movementTimestamp, coordinates:this.getCurrentCoordinate()};
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'playSound',
        functionCall: ocargo.sound.sound_horn,
        description: 'van sound: sounding the horn'
    });

    return true;
};

ocargo.Model.prototype.puff_up = function(){
    if(!jQuery.isEmptyObject(this.puffedUp)){
        return this.remain_puff_up();
    }else{
        this.van.puffUp();
        this.puffedUp = {timestamp:this.movementTimestamp, coordinates:this.getCurrentCoordinate(), timeout:1};
        ocargo.animation.appendAnimation({
            type: 'van',
            vanAction: 'PUFFUP',
            fuel: this.van.getFuelPercentage(),
            description: 'van move action: puff up'
        });
        return this.puff_down();
    }

};

ocargo.Model.prototype.remain_puff_up = function(){
    this.puffedUp.coordinates = this.getCurrentCoordinate();
    this.puffedUp.timeout++;

    ocargo.animation.appendAnimation({
        type: 'van',
        vanAction: 'REMAINPUFFUP',
        fuel: this.van.getFuelPercentage(),
        description: 'van move action: remain puff up'
    });

    return true;
};

ocargo.Model.prototype.puff_down = function(){

    ocargo.animation.appendAnimation({
        type: 'van',
        vanAction: 'PUFFDOWN',
        fuel: this.van.getFuelPercentage(),
        description: 'van move action: puff down'
    });

    return true;
};

// Signal that the program has ended and we should calculate whether
// the play has won or not and send off those events
ocargo.Model.prototype.programExecutionEnded = function () {
    var success;
    var destinations = this.map.getDestinations();
    var failType = 'OUT_OF_INSTRUCTIONS';
    var failMessage = ocargo.messages.outOfInstructions;

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
                failMessage = ocargo.messages.passedDestination;
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
            failMessage = ocargo.messages.undeliveredDestinations;

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
        failMessage = ocargo.messages.disconnectedStartBlock;
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
        if(destinations[i].node === node) {
            return destinations[i];
        }
    }
    return null;
};

ocargo.Model.prototype.getCowForNode = function(node, status) {
    var jsonCoordinate = JSON.stringify(node.coordinate);
    for(var i = 0; i < this.cows.length; i++) {
        var cow = this.cows[i];
        if (jsonCoordinate in cow.activeNodes && cow.activeNodes[jsonCoordinate] == status) {
            return cow;
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

    this.incrementCowTime();
};

ocargo.Model.prototype.incrementTrafficLightsTime = function() {
    for (var i = 0; i < this.trafficLights.length; i++) {
        this.trafficLights[i].incrementTime(this);
    }
};

ocargo.Model.prototype.incrementCowTime = function() {
    if(this.movementTimestamp - this.puffedUp.timestamp > this.puffedUp.timeout){
        this.puffedUp = {};
        this.van.puffDown();
    }

    for (var i = 0; i < this.cows.length; i++) {
        this.cows[i].incrementTime(this);
    }
    this.soundedHorn = {};

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

