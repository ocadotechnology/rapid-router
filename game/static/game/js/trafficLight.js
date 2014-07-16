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
    $(ocargo.time).on('increment', $.proxy(me.incrementTime, me));
    $(ocargo.time).on('reset', $.proxy(me.reset, me));
};

ocargo.TrafficLight.prototype.incrementTime = function() {
    this.currentLightTime++;
    var r = this.state;
    var r2 = ocargo.TrafficLight.RED;
    var t = r == r2;
    if(this.state === ocargo.TrafficLight.RED && this.currentLightTime >= this.redDuration){
    	this.state = ocargo.TrafficLight.GREEN;
    	this.currentLightTime = 0;
    	$(this).trigger(ocargo.TrafficLight.GREEN);
    } else if(this.state === ocargo.TrafficLight.GREEN && this.currentLightTime >= this.greenDuration){
    	this.state = ocargo.TrafficLight.RED;
    	this.currentLightTime = 0;
    	$(this).trigger(ocargo.TrafficLight.RED);
    }
};

ocargo.TrafficLight.prototype.reset = function() {
    this.currentLightTime = this.startTime;
    this.state = this.startingState;
   	$(this).trigger(this.startingState);
};

ocargo.TrafficLight.RED = 'RED';
ocargo.TrafficLight.GREEN = 'GREEN';