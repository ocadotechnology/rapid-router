'use strict';

function Node(coordinate) {
    this.coordinate = coordinate;
    this.connectedNodes = [];
}

Node.prototype.addConnectedNode = function(node) {
	this.connectedNodes.push(node);
}

Node.prototype.addConnectedNodeWithBacklink = function(node) {
	this.addConnectedNode(node);
	node.addConnectedNode(this);
}
