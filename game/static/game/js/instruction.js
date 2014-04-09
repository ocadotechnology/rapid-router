'use strict';

function Instruction(name) {
    this.name = name;
}

//TODO: actually do javascript inheritance by extending prototypes
var FORWARD = new Instruction("FORWARD");
var TURN_LEFT = new Instruction("TURN_LEFT");
var TURN_RIGHT = new Instruction("TURN_RIGHT");


FORWARD.getNextNode = function(previousNode, currentNode){

};

TURN_LEFT.getNextNode = function(previousNode, currentNode){
    var index = currentNode.connectedNodes.indexOf(previousNode) + 1;
    if(index === currentNode.connectedNodes.length){
        return currentNode.connectedNodes[0];
    }
    return currentNode.connectedNodes[index];
};

TURN_RIGHT.getNextNode = function(previousNode, currentNode){
    var index = currentNode.connectedNodes.indexOf(previousNode) - 1;
    if(index === -1){
        return currentNode.connectedNodes[currentNode.connectedNodes.length - 1];
    }
    return currentNode.connectedNodes[index];
};