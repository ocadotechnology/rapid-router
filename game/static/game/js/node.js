'use strict';

var ocargo = ocargo || {};

ocargo.Node = function (coordinate) {
    this.coordinate = coordinate;
    this.connectedNodes = [];
    this.parent = null;
};

ocargo.Node.prototype.addConnectedNode = function(node) {
	this.connectedNodes.push(node);
};

ocargo.Node.prototype.addConnectedNodeWithBacklink = function(node) {
	this.addConnectedNode(node);
	node.addConnectedNode(this);
};

ocargo.Node.prototype.removeDoublyConnectedNode = function(node) {
    var index = this.connectedNodes.indexOf(node);
    if (index >= -1) {
        this.connectedNodes.splice(index, 1);
    }
    index = node.connectedNodes.indexOf(this);
    if (index >= -1) {
        node.connectedNodes.splice(index, 1);
    }
}

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
