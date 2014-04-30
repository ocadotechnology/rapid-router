'use strict';

var ocargo = ocargo || {};

ocargo.Van = function(previousNode, startNode, ui) {
    this.previousNode = previousNode;
    this.currentNode = startNode;
    this.ui = ui;
}

ocargo.Van.prototype.move = function(nextNode, instruction, callback) {
	if (instruction == FORWARD) {
        moveForward(callback);
    } else if (instruction == TURN_LEFT) {
        moveLeft(callback);
    } else if (instruction == TURN_RIGHT) {
        moveRight(callback);
    }
	
	this.previousNode = this.currentNode;
	this.currentNode = nextNode;
};
