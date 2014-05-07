'use strict';

var ocargo = ocargo || {};

ocargo.Van = function(previousNode, startNode, ui) {
    this.previousNode = previousNode;
    this.currentNode = startNode;
    this.ui = ui;
    ocargo.sound.starting();
}

ocargo.Van.prototype.move = function(nextNode, instruction, callback) {
    if (instruction == FORWARD) {
        moveForward(callback);
        ocargo.sound.moving();
    } else if (instruction == TURN_LEFT) {
        moveLeft(callback);
        ocargo.sound.turning();
    } else if (instruction == TURN_RIGHT) {
        moveRight(callback);
        ocargo.sound.turning();
    } else if (instruction == TURN_AROUND) {
        turnAround(callback);
        ocargo.sound.turning();
        ocargo.sound.turning();
    }
	
	this.previousNode = this.currentNode;
	this.currentNode = nextNode;
};
