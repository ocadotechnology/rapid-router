'use strict';

function Van(previousNode, startNode) {
    this.previousNode = previousNode;
    this.currentNode = startNode;

    this.move = function(nextNode){
        this.previousNode = this.currentNode;
        this.currentNode = nextNode;
        ui.update(nextNode);
    };
}