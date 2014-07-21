var ocargo = ocargo || {};

ocargo.TrafficLight = function(id, data, map) {
    this.id = id;
    this.startingState = data.startingState;
    this.state = this.startingState;
    this.startTime = data.startTime;
    this.redDuration = data.redDuration;
    this.greenDuration = data.greenDuration;
    this.currentLightTime = this.startTime;
    this.sourceNode = map.nodes[data.sourceNode];
    this.controlledNode = map.noes[data.node];
};

ocargo.TrafficLight.prototype.reset = function() {
    this.currentLightTime = this.startTime;
    this.state = this.startingState;
};

ocargo.TrafficLight.prototype.getState = function() {
    return this.state;
};

ocargo.TrafficLight.prototype.incrementTime = function() {
    this.currentLightTime++;

    if (this.state === ocargo.TrafficLight.RED && this.currentLightTime >= this.redDuration) {
    	this.state = ocargo.TrafficLight.GREEN;
    	this.currentLightTime = 0;
    }
    else if (this.state === ocargo.TrafficLight.GREEN && this.currentLightTime >= this.greenDuration) {
    	this.state = ocargo.TrafficLight.RED;
    	this.currentLightTime = 0;
    }
};

ocargo.TrafficLight.RED = 'RED';
ocargo.TrafficLight.GREEN = 'GREEN';