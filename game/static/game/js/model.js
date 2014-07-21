'use strict';

var ocargo = ocargo || {};

ocargo.Model = function(nodeData, destination, trafficLightData, maxFuel) {
	this.map = new ocargo.Map(nodeData, destination);
	this.van = new ocargo.Van(this.map.getStartingPosition(), maxFuel);

	this.trafficLights = [];
	var i;
	for (i = 0; i < trafficLightData.length; i++) {
		this.trafficLights.push(new ocargo.TrafficLight(i, trafficLightData[i], this.map));
	}

	this.timestamp = 0;
};

// Resets the entire model to how it was when it was just constructed
ocargo.Model.prototype.reset = function() {
	this.map.reset();
	this.van.reset();

	var i;
	for (i = 0; i < this.trafficLightData.length; i++) {
		this.trafficLights.reset();
	}

	this.timestamp = 0;
};

///////////////////////
// Begin observation function, each tests something about the model
// and returns a boolean

ocargo.Model.prototype.isRoadForward = function() {
	return (this.map.isRoadForward(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isRoadLeft = function() {
	return (this.map.isRoadLeft(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isRoadRight = function() {
	return (this.map.isRoadRight(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isDeadEnd = function() {
	return (this.map.isDeadEnd(this.van.getPosition()) !== null);
};

ocargo.Model.prototype.isTrafficLightRed = function() {
	var light = this.getTrafficLightForNode(this.van.getPosition().currentNode);
	return (light.getState() === ocargo.TrafficLight.RED);
};

ocargo.Model.prototype.isTrafficLightGreen = function() {
	var light = this.getTrafficLightForNode(this.van.getPosition().currentNode);
	return (light.getState() === ocargo.TrafficLight.GREEN);
};

///////////////////////
// Begin action functions, each changes something and returns
// true if it was a valid action or false otherwise

ocargo.Model.prototype.moveForwards = function() {
	var nextNode = this.map.isRoadForward(this.van.getPosition());
	if (nextNode === null) {
		return false;
	}
	if (this.van.fuel <= 0) {
		return false;
	}
	this.van.move(nextNode);
	return true;
};

ocargo.Model.prototype.turnLeft = function() {
	var nextNode = this.map.isRoadLeft(this.van.getPosition());
	if (nextNode === null) {
		return false;
	}
	if (this.van.fuel <= 0) {
		return false;
	}
	this.van.move(nextNode);
	return true;
};

ocargo.Model.prototype.turnRight = function() {
	var nextNode = this.map.isRoadRight(this.van.getPosition());
	if (nextNode === null) {
		return false;
	}
	if (this.van.fuel <= 0) {
		return false;
	}
	this.van.move(nextNode);
	return true;
};

ocargo.Model.prototype.turnAround = function() {
	if (this.van.fuel <= 0) {
		return false;
	}
	this.van.move(this.van.getPosition().previousNode);
	return true;
};

ocargo.Model.prototype.wait = function() {
	if (this.van.fuel <= 0) {
		return false;
	}
	return true;
};

// Signal that the program has ended and we should calculate whether
// the play has won or not and send off those events
ocargo.Model.prototype.programExecutionEnded = function() {
	if (this.van.getPosition().currentNode === this.map.getDestinationNode()) {
		// signalGameWon();
	}
	else {
		// signalGameLost();
	}
};

// A helper function that returns the traffic light associated
// with a particular node of the map
ocargo.Model.prototype.getTrafficLightForNode = function(node) {
	var i;
	for (i = 0; i < this.trafficLights.length; i++) {
		if (trafficLights[i].sourceNode === node) {
			return trafficLights[i];
		}
	}
	return null;
};