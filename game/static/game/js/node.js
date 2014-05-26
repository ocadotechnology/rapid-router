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

ocargo.calculateNodeAngle = function(nodeA, nodeB) {
    var coordinateA = nodeA.coordinate;
    var coordinateB = nodeB.coordinate;

    return Math.atan2(coordinateB.y - coordinateA.y, coordinateB.x - coordinateA.x);
};

ocargo.calculateClockwiseNodeAngle = function(nodeA, nodeB, nodeC) {
    var angleAB = ocargo.calculateNodeAngle(nodeA, nodeB);
    var angleBC = ocargo.calculateNodeAngle(nodeB, nodeC);
    var angle = (Math.PI + angleAB - angleBC) % (2 * Math.PI);
    return angle < 0 ? angle + 2 * Math.PI : angle;
};
