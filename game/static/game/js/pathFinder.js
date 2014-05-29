'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(map) {
	this.nodes = map.nodes;
	this.destination = map.destination;
	this.optimalInstructions = [];
	this.optimalPath = null;
};

ocargo.PathFinder.prototype.getOptimalInstructions = function(data) {
	// For now.
	this.optimalInstructions = data;
};

ocargo.PathFinder.prototype.getScore = function(stack) {
	var instrLengthScore = 100;
	var pathLenScore = 100;
	var lengthScore 
		= Math.max(0, instrLengthScore - (this.optimalInstructions.length - stack.length) * 100);
};

ocargo.PathFinder.prototype.getOptimalPath = function() {
	var node = ocargo.level.pathFinder.nodes[0];
	var startingNode = node;
	while (node != ocargo.level.pathFinder.destination) {
		var next = node.connectedNodes[0];
		node.addConnectedNode(next);
		node = next;
	}
	ocargo.level.pathFinder.optimalPath = node;
};

ocargo.PathFinder.prototype.recogniseInstruction = function(stack){
	
};
