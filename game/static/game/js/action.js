'use strict';

var ocargo = ocargo || {};

var forwardAngle = Math.PI;
var leftCutoffAngle = 5 * Math.PI / 6;
var rightCutoffAngle = 7 * Math.PI / 6;


ocargo.FORWARD_ACTION = {
    name: "FORWARD",
    animationLength: 500,
    getNextNode: function(previousNode, currentNode) {
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
                }
};

ocargo.TURN_LEFT_ACTION = {
    name: "TURN_LEFT",
    animationLength: 500,
    getNextNode: function(previousNode, currentNode) {
                    var index = currentNode.connectedNodes.indexOf(previousNode) + 1;
                    var nextNode;
                    if (index === currentNode.connectedNodes.length) {
                        nextNode = currentNode.connectedNodes[0];
                    } else {
                        nextNode = currentNode.connectedNodes[index];
                    }

                    var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, nextNode);
                    return (angle > 0 && angle < leftCutoffAngle) ? nextNode : null;
                }
};

ocargo.TURN_RIGHT_ACTION = {
    name: "TURN_RIGHT",
    animationLength: 500,
    getNextNode: function(previousNode, currentNode) {
                    var index = currentNode.connectedNodes.indexOf(previousNode) - 1;
                    var nextNode;
                    if (index === -1) {
                        nextNode = currentNode.connectedNodes[currentNode.connectedNodes.length - 1];
                    } else {
                        nextNode = currentNode.connectedNodes[index];
                    }

                    var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, nextNode);
                    return (angle > rightCutoffAngle && angle < 2 * Math.PI) ? nextNode : null;
                }
};


ocargo.TURN_AROUND_ACTION = {
    name: "TURN_AROUND",
    animationLength: 500,
    getNextNode: function(previousNode, currentNode) { 
                    var forward = ocargo.FORWARD_ACTION.getNextNode(previousNode, currentNode);
                    var left = ocargo.TURN_LEFT_ACTION.getNextNode(previousNode, currentNode);
                    var right = ocargo.TURN_RIGHT_ACTION.getNextNode(previousNode, currentNode);

                    return (forward || ((!left) && (!right))) ? previousNode : null;
                }
};


ocargo.WAIT_ACTION = {
    name: "WAIT",
    animationLength: 500,
    getNextNode: function(previousNode, currentNode) { return currentNode; }
};

ocargo.EMPTY_ACTION = {
    name: "EMPTY",
    animationLength: 500,
};