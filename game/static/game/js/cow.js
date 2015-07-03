'use strict';

var ocargo = ocargo || {};

ocargo.Cow = function(id, data, nodes) {
    this.id = id;
    this.startingState = data.startingState;
    this.state = this.startingState;
    this.startTime = data.startTime;

    var sourceCoordinate = new ocargo.Coordinate(data.potentialCoordinates.x, data.potentialCoordinates.y);
    var controlledCoordinate = sourceCoordinate.getNextInDirection(data.direction);

    this.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoordinate, nodes);
    this.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoordinate, nodes);
};

ocargo.Cow.prototype.reset = function() {
    this.currentLightTime = this.startTime;
    this.state = this.startingState;
};

ocargo.Cow.prototype.getState = function() {
    return this.state;
};

ocargo.Cow.prototype.incrementTime = function(model) {
    this.currentLightTime++;

    if (this.state === ocargo.TrafficLight.RED && this.currentLightTime >= this.redDuration) {
    	this.state = ocargo.TrafficLight.GREEN;
    	this.currentLightTime = 0;
        this.queueAnimation(model);
    }
    else if (this.state === ocargo.TrafficLight.GREEN && this.currentLightTime >= this.greenDuration) {
    	this.state = ocargo.TrafficLight.RED;
    	this.currentLightTime = 0;
        this.queueAnimation(model);
    }
};

ocargo.Cow.prototype.queueAnimation = function(model) {
    ocargo.animation.appendAnimation({
        type: 'cow',
        id: this.id,
        state: this.state,
        description: 'Cow: ' + this.state
    });
};

ocargo.Cow.BLOCKING = 'BLOCKING';
ocargo.Cow.NON_BLOCKING = 'NON_BLOCKING';
