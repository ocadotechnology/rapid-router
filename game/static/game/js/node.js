'use strict';

var ocargo = ocargo || {};

ocargo.Node = function (coordinate) {
    this.coordinate = coordinate;
    this.connectedNodes = [];
};

ocargo.Node.prototype.addConnectedNode = function(node) {
	this.connectedNodes.push(node);
};

ocargo.Node.prototype.addConnectedNodeWithBacklink = function(node) {
	this.addConnectedNode(node);
	node.addConnectedNode(this);
};
