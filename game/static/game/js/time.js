var ocargo = ocargo || {};

ocargo.Time = function() {
    this.timestamp = 0;
    this.resetListeners = [];
    this.incrementListeners = [];
    this.decrementListeners = [];
};

ocargo.Time.prototype.resetTime = function(){
	this.timestamp = 0;
	for (var i = 0; i < this.resetListeners.length; i++) {
		console.log("calling reset listener");
		this.resetListeners[i][0].call(this.resetListeners[i][1]);
	}
};

ocargo.Time.prototype.incrementTime = function(delay){
	var delay = delay || 250;
	this.timestamp++;
	for (var i = 0; i < this.incrementListeners.length; i++) {
		console.log("calling increment listener");
		this.incrementListeners[i][0].call(this.incrementListeners[i][1]);
	}
	
};

ocargo.Time.prototype.decrementTime = function(delay){
	var delay = delay || 250;
	this.timestamp--;
	for (var i = 0; i < this.decrementListeners.length; i++) {
		console.log("calling decrement listener");
		this.decrementListeners[i][0].call(this.decrementListeners[i][1]);
	}
};

ocargo.Time.prototype.registerResetListener = function(func, me) {
	this.resetListeners.push([func, me]);
}

ocargo.Time.prototype.registerIncrementListener = function(func, me) {
	this.incrementListeners.push([func, me]);
}

ocargo.Time.prototype.registerDecrementListener = function(func, me) {
	this.decrementListeners.push([func, me]);
}