'use strict';

function Van(previousNode, startNode, ui) {
    this.previousNode = previousNode;
    this.currentNode = startNode;
    this.ui = ui;
}

Van.prototype.move = function(nextNode, instruction) {
	this.ui.queueUpdate(this, nextNode, instruction);
	this.previousNode = this.currentNode;
	this.currentNode = nextNode;
};
