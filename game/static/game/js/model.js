'use strict';

var ocargo = ocargo || {};

ocargo.Model = function(nodeData, destination, trafficLightData, maxFuel, vanId) {
	this.map = new ocargo.Map(nodeData, destination);
	this.van = new ocargo.Van(this.map.getStartingPosition(), maxFuel);

	this.trafficLights = [];
	var i;
	for (i = 0; i < trafficLightData.length; i++) {
		this.trafficLights.push(new ocargo.TrafficLight(i, trafficLightData[i], this.map.nodes));
	}

	this.timestamp = 0;
	this.subTimestamp = 0;

	this.vanId = vanId || 0;

	this.pathFinder = new ocargo.PathFinder(this);
};

// Resets the entire model to how it was when it was just constructed
ocargo.Model.prototype.reset = function(vanId) {
	this.van.reset();

	var i;
	for (i = 0; i < this.trafficLights.length; i++) {
		this.trafficLights[i].reset();
	}

	this.timestamp = 0;
	this.subTimestamp = 0;

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
		description: 'van observe: ' + desc,
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

ocargo.Model.prototype.isAtDestination = function() {
	this.observe('at destination');
	return (this.map.getDestinationNode() === this.van.getPosition().currentNode);
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
			fuel: this.van.getFuelPercentage(),
			description: 'van move action: ' + action,
		});

		ocargo.animation.appendAnimation({
			type: 'popup',
			id: this.vanId,
			popupType: 'FAIL',
			popupMessage: ocargo.messages.offRoad(this.van.travelled),
			description: 'crash popup',
		});
		return false;
	}

	if (this.van.fuel <= 0) {
		// Ran out of fuel
		ocargo.animation.appendAnimation({
			type: 'popup',
			id: this.vanId,
			popupType: 'FAIL',
			popupMessage: ocargo.messages.outOfFuel,
			description: 'no fuel popup',
		});
		return false;
	}

	var light = this.getTrafficLightForNode(this.van.getPosition());
	if (light !== null && light.getState() === ocargo.TrafficLight.RED && nextNode !== light.controlledNode) {
		// Ran a red light
		ocargo.animation.appendAnimation({
			type: 'popup',
			id: this.vanId,
			popupType: 'FAIL',
			popupMessage: ocargo.messages.throughRedLight,
			description: 'ran red traffic light popup',
		});
		return false;
	}

	this.van.move(nextNode);

	// Van movement animation
	ocargo.animation.appendAnimation({
		type: 'van',
		id: this.vanId,
		vanAction: action,
		fuel: this.van.getFuelPercentage(),
		description: 'van move action: ' + action,
	});

	// Van movement sound
	ocargo.animation.appendAnimation({
		type: 'callable',
		functionCall: (action === 'FORWARD') ? ocargo.sound.moving : ocargo.sound.turning,
		description: 'van sound: ' + action,
	});

	this.incrementTime();

	return true;
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

// Signal that the program has ended and we should calculate whether
// the play has won or not and send off those events
ocargo.Model.prototype.programExecutionEnded = function() {
	if (this.van.getPosition().currentNode === this.map.getDestinationNode()) {
		var scoreArray = this.pathFinder.getScore();
	    sendAttempt(scoreArray[0]);

	    // Winning popup
		ocargo.animation.appendAnimation({
			type: 'popup',
			id: this.vanId,
			popupType: 'WIN',
			popupMessage: scoreArray[1],
			description: 'win popup',
		});

		// Winning sound
		ocargo.animation.appendAnimation({
			type: 'callable',
			functionCall: ocargo.sound.win,
			description: 'win sound',
		});
	}
	else {
		sendAttempt(0);

		// Failure popup
		ocargo.animation.appendAnimation({
			type: 'popup',
			id: this.vanId,
			popupType: 'FAIL',
			popupMessage: ocargo.messages.outOfInstructions,
			hint: registerFailure(),
			description: 'failure popup',
		});

		// Failure sound
		ocargo.animation.appendAnimation({
			type: 'callable',
			functionCall: ocargo.sound.failure,
			description: 'failure sound',
		});
	}
};

// A helper function which returns the traffic light associated
// with a particular node and orientation
ocargo.Model.prototype.getTrafficLightForNode = function(position) {
	var i;
	for (i = 0; i < this.trafficLights.length; i++) {
		var light = this.trafficLights[i];
		if (light.sourceNode === position.previousNode && light.controlledNode === position.currentNode) {
			return light;
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

	var i;
	for (i = 0; i < this.trafficLights.length; i++) {
		this.trafficLights[i].incrementTime(this);
	}
};

ocargo.Model.prototype.incrementSubTime = function() {
	this.subTimestamp += 1;

	ocargo.animation.startNewSubTimestamp();
};