var ocargo = ocargo || {};

ocargo.Time = function() {
    this.timestamp = 0;
};

ocargo.Time.prototype.resetTime = function(){
	this.timestamp = 0;
	$(this).trigger('reset');
};

ocargo.Time.prototype.incrementTime = function(delay){
	var delay = delay || 250;
	var me = this;
	setTimeout(function(){
		me.timestamp++;
		$(me).trigger('increment');
	}, delay);
	
};

ocargo.Time.prototype.decrementTime = function(delay){
	var delay = delay || 250;
	var me = this;
	setTimeout(function(){
		me.timestamp--;
		$(me).trigger('increment');
	}, delay);
};
