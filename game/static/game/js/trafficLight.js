var ocargo = ocargo || {};

ocargo.TrafficLight = function(id, startingState, startTime, redDuration, greenDuration, sourceNode, controlledNode) {
    this.id = id;
    this.startingState = startingState;
    this.state = startingState;
    this.startTime = startTime;
    this.redDuration = redDuration;
    this.greenDuration = greenDuration;
    this.currentTime = 0;
    this.currentLightTime = startTime;
    this.sourceNode = sourceNode;
    this.controlledNode = controlledNode;
    var me = this;
    ocargo.time.registerIncrementListener(me.incrementTime, me);
    ocargo.time.registerResetListener(me.reset, me);
};

ocargo.TrafficLight.prototype.incrementTime = function() {
    this.currentTime++;
    this.currentLightTime++;

    if (this.state === ocargo.TrafficLight.RED && this.currentLightTime >= this.redDuration) {
    	this.state = ocargo.TrafficLight.GREEN;
    	this.currentLightTime = 0;
        changeTrafficLight(this.id, ocargo.TrafficLight.GREEN);
    }
    else if (this.state === ocargo.TrafficLight.GREEN && this.currentLightTime >= this.greenDuration) {
    	this.state = ocargo.TrafficLight.RED;
    	this.currentLightTime = 0;
        changeTrafficLight(this.id, ocargo.TrafficLight.RED);
    }
};

ocargo.TrafficLight.prototype.reset = function() {
    this.currentTime = 0;
    this.currentLightTime = this.startTime;
    this.state = this.startingState;
    resetTrafficLightAnimation(this.id, this.startingState);
};

ocargo.TrafficLight.RED = 'RED';
ocargo.TrafficLight.GREEN = 'GREEN';