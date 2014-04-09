'use strict';

var forwardAngle = Math.PI;
var leftCutoffAngle = 5 * Math.PI / 6;
var rightCutoffAngle = 7 * Math.PI / 6;

function calculateAngle(nodeA, nodeB) {
    var coordinateA = nodeA.coordinate;
    var coordinateB = nodeB.coordinate;

    return Math.atan2(coordinateB.y - coordinateA.y, coordinateB.x - coordinateA.x);
}

function calculateClockwiseAngle(nodeA, nodeB, nodeC) {
    var angleAB = calculateAngle(nodeA, nodeB);
    var angleBC = calculateAngle(nodeB, nodeC);
    return Math.PI + angleAB - angleBC;
}

function Instruction(name) {
    this.name = name;
}

//TODO: actually do javascript inheritance by extending prototypes
var FORWARD = new Instruction("FORWARD");
var TURN_LEFT = new Instruction("TURN_LEFT");
var TURN_RIGHT = new Instruction("TURN_RIGHT");


FORWARD.getNextNode = function(previousNode, currentNode){
    var nextNode = null;
    var nextNodeDeviation = null;

    var nodes = currentNode.connectedNodes;
    for (var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        var angle = calculateClockwiseAngle(previousNode, currentNode, node);
        var deviation = Math.abs(forwardAngle - angle);
        if (angle >= leftCutoffAngle && angle <= rightCutoffAngle
                && (nextNode === null || deviation < nextNodeDeviation)) {
            nextNode = node;
            nextNodeDeviation = deviation;
        }
    }

    return nextNode;
};

TURN_LEFT.getNextNode = function(previousNode, currentNode){
    var index = currentNode.connectedNodes.indexOf(previousNode) + 1;
    var nextNode;
    if (index === currentNode.connectedNodes.length) {
        nextNode = currentNode.connectedNodes[0];
    } else {
        nextNode = currentNode.connectedNodes[index];
    }

    var angle = calculateClockwiseAngle(previousNode, currentNode, nextNode);
    return angle < leftCutoffAngle ? nextNode : null;
};

TURN_RIGHT.getNextNode = function(previousNode, currentNode){
    var index = currentNode.connectedNodes.indexOf(previousNode) - 1;
    var nextNode;
    if (index === -1) {
        nextNode = currentNode.connectedNodes[currentNode.connectedNodes.length - 1];
    } else {
        nextNode = currentNode.connectedNodes[index];
    }

    var angle = calculateClockwiseAngle(previousNode, currentNode, nextNode);
    return angle > rightCutoffAngle ? nextNode : null;
};