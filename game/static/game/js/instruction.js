'use strict';

var ocargo = ocargo || {};

var forwardAngle = Math.PI;
var leftCutoffAngle = 5 * Math.PI / 6;
var rightCutoffAngle = 7 * Math.PI / 6;

ocargo.Instruction = function(name) {
    this.name = name;
};

//TODO: actually do javascript inheritance by extending prototypes
var FORWARD = new ocargo.Instruction("FORWARD");
var TURN_LEFT = new ocargo.Instruction("TURN_LEFT");
var TURN_RIGHT = new ocargo.Instruction("TURN_RIGHT");
var TURN_AROUND = new ocargo.Instruction("TURN_AROUND");


FORWARD.getNextNode = function(previousNode, currentNode) {
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

TURN_LEFT.getNextNode = function(previousNode, currentNode) {
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

TURN_RIGHT.getNextNode = function(previousNode, currentNode) {
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

TURN_AROUND.getNextNode = function(previousNode, currentNode) {
    return previousNode;
};
