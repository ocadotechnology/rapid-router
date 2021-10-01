'use strict';

var ocargo = ocargo || {};

var forwardAngle = Math.PI;
var leftCutoffAngle = 5 * Math.PI / 6;
var rightCutoffAngle = 7 * Math.PI / 6;

ocargo.Map = function(nodeData, origin, destinationCoordinates) {
	this.nodeData = nodeData;
	this.nodes = ocargo.Node.parsePathData(nodeData);

    this.destinations = [];
    for(var i = 0; i < destinationCoordinates.length; i++) {
        var coordinate = new ocargo.Coordinate(destinationCoordinates[i][0],destinationCoordinates[i][1]);
        var destinationNode = this.nodes[ocargo.Node.findNodeIndexByCoordinate(coordinate, this.nodes)];
        this.destinations.push(new ocargo.Destination(i,destinationNode));
    }

    this.originCoordinate = new ocargo.Coordinate(origin.coordinate[0], origin.coordinate[1]);
    this.originDirection = origin.direction;

    var originCurrentCoord = this.originCoordinate.getNextInDirection(this.originDirection);
    this.originPreviousNode = ocargo.Node.findNodeByCoordinate(this.originCoordinate, this.nodes);
    this.originCurrentNode = ocargo.Node.findNodeByCoordinate(originCurrentCoord, this.nodes);
};

ocargo.Map.prototype.startingPosition = function() {
    return {previousNode: this.originPreviousNode,
            currentNode: this.originCurrentNode};
};

ocargo.Map.prototype.getDestinations = function() {
	return this.destinations;
};

/////////////////////////
// The following four functions test if a road exists and return the
// next node if it exists or null otherwise

ocargo.Map.prototype.isRoadForward = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;

	var nextNode = null;
    var nextNodeDeviation = null;

    var nodes = currentNode.connectedNodes;
    for (var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, node);
        var deviation = Math.abs(forwardAngle - angle);
        if (angle >= leftCutoffAngle && angle <= rightCutoffAngle &&
            (nextNode === null || deviation < nextNodeDeviation)) {
            nextNode = node;
            nextNodeDeviation = deviation;
        }
    }
    return nextNode;
};

ocargo.Map.prototype.isRoadLeft = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;

    var index = currentNode.connectedNodes.indexOf(previousNode) + 1;
    var nextNode;
    if (index === currentNode.connectedNodes.length) {
        nextNode = currentNode.connectedNodes[0];
    } else {
        nextNode = currentNode.connectedNodes[index];
    }

    var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, nextNode);
    return (angle > 0 && angle < leftCutoffAngle) ? nextNode : null;
};

ocargo.Map.prototype.isRoadRight = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;

	var index = currentNode.connectedNodes.indexOf(previousNode) - 1;
    var nextNode;
    if (index === -1) {
        nextNode = currentNode.connectedNodes[currentNode.connectedNodes.length - 1];
    } else {
        nextNode = currentNode.connectedNodes[index];
    }

    var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, nextNode);
    return (angle > rightCutoffAngle && angle < 2 * Math.PI) ? nextNode : null;
};

ocargo.Map.prototype.isDeadEnd = function(position) {
	var connectedNodes = position.currentNode.connectedNodes;
	if (connectedNodes.length === 1) {
		return connectedNodes[0];
	}
	return null;
};
