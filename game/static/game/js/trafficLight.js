var ocargo = ocargo || {};

ocargo.TrafficLight = function(startingState, startTime, redDuration, greenDuration, sourceNode, controlledNode) {
    this.startingState = startingState;
    this.state = startingState;
    this.startTime = startTime;
    this.redDuration = redDuration;
    this.greenDuration = greenDuration;
    this.currentLightTime = startTime;
    this.sourceNode = sourceNode;
    this.controlledNode = controlledNode;
    var me = this;
    ocargo.time.registerIncrementListener(me.incrementTime, me);
    ocargo.time.registerResetListener(me.reset, me);
};

ocargo.TrafficLight.prototype.incrementTime = function() {
    console.log("traffic light increment time called");
    this.currentLightTime++;
    var r = this.state;
    var r2 = ocargo.TrafficLight.RED;
    var t = r == r2;
    if(this.state === ocargo.TrafficLight.RED && this.currentLightTime >= this.redDuration){
    	this.state = ocargo.TrafficLight.GREEN;
    	this.currentLightTime = 0;
    	// $(this).trigger(ocargo.TrafficLight.GREEN);
        console.log("(" + this.sourceNode.coordinate.x + ", " + this.sourceNode.coordinate.x + ") changing to green");
    } else if(this.state === ocargo.TrafficLight.GREEN && this.currentLightTime >= this.greenDuration){
    	this.state = ocargo.TrafficLight.RED;
    	this.currentLightTime = 0;
    	// $(this).trigger(ocargo.TrafficLight.RED);
        console.log("(" + this.sourceNode.coordinate.x + ", " + this.sourceNode.coordinate.x + ") changing to red");
    }
};

ocargo.TrafficLight.prototype.reset = function() {
    this.currentLightTime = this.startTime;
    this.state = this.startingState;
   	// $(this).trigger(this.startingState);
};

ocargo.TrafficLight.RED = 'RED';
ocargo.TrafficLight.GREEN = 'GREEN';