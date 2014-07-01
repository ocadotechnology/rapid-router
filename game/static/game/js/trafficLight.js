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
    if(this.state == this.RED && this.currentLightTime >= this.redDuration){
    	this.state = this.GREEN;
    	this.currentLightTime = 0;
    	$(this).trigger(this.GREEN);
    } else if(this.state == this.GREEN && this.currentLightTime >= this.greenDuration){
    	this.state = this.RED;
    	this.currentLightTime = 0;
    	$(this).trigger(this.RED);
    }
};

ocargo.TrafficLight.prototype.reset = function() {
    this.currentLightTime = this.startTime;
    this.state = this.startingState;
   	$(this).trigger(this.startingState);
};

ocargo.TrafficLight.prototype.RED = 'RED';
ocargo.TrafficLight.prototype.GREEN = 'GREEN';
