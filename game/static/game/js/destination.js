'use strict';

var ocargo = ocargo || {};

ocargo.Destination = function(id, node) {
	this.id = id;
	this.node = node;
	this.visited = false;
};

ocargo.Destination.prototype.reset = function() {
	this.visited = false;
};