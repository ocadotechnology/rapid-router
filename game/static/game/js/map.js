'use strict';

var ocargo = ocargo || {};

var forwardAngle = Math.PI;
var leftCutoffAngle = 5 * Math.PI / 6;
var rightCutoffAngle = 7 * Math.PI / 6;

ocargo.Map = function(nodeData, destinationCoordinates) {
	this.nodeData = nodeData;
	this.nodes = this.createNodes(nodeData);

    this.destinations = [];
    for(var i = 0; i < destinationCoordinates.length; i++) {
        var destinationNode = this.findByCoordinate(destinationCoordinates[i], this.nodes);
        this.destinations.push(new ocargo.Destination(i,destinationNode));
    }
};

ocargo.Map.prototype.createNodes = function(nodeData) {
    var nodes = [];

    var i;
    // Create nodes with coords
    for (i = 0; i < nodeData.length; i++) {
         var coordinate = new ocargo.Coordinate(
            nodeData[i]['coordinate'][0], nodeData[i]['coordinate'][1]);
         nodes.push(new ocargo.Node(coordinate));
    }

    // Link nodes (must be done in second loop so that linked nodes have definitely been created)
    for (i = 0; i < nodeData.length; i++) {
        var node = nodes[i];
        var connectedNodes = nodeData[i]['connectedNodes'];
        for (var j = 0; j < connectedNodes.length; j++) {
            node.addConnectedNode(nodes[connectedNodes[j]]);
        }
    }
    
    return nodes;
};

ocargo.Map.prototype.findByCoordinate = function(coordinate, nodes) {
    for (var i = 0; i < nodes.length; i++) {
        var coord = nodes[i].coordinate;
        if (coord.x === coordinate[0] && coord.y === coordinate[1]) {
            return nodes[i];
        }
    }
    return null;
}

ocargo.Map.prototype.getStartingPosition = function() {
	var previousNode = this.nodes[0];
	var currentNode = previousNode.connectedNodes[0];
    return { previousNode: previousNode, currentNode: currentNode };
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
