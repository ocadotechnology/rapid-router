'use strict';

var ocargo = ocargo || {};

ocargo.Van = function(position, maxFuel) {
    this.startingPosition = position;

    /**
     * Keeps track of where the van has been
     *
     * Position at index 0 is the previous position at the start of the run, so
     * this array is effectively indexed from 1 onwards. It's guaranteed to have
     * at least two elements in it (the starting node and previous node at the
     * start).
     *
     * @type {ocargo.Node[]}
     */
    this.visitedNodes = [position.previousNode, position.currentNode];
    this.maxFuel = maxFuel;
    this.fuel = maxFuel;
    this.crashStatus = 'NOT_CRASHED';
    this.sizeOfVan = 1;
};

ocargo.Van.prototype.reset = function() {
    this.visitedNodes = [this.startingPosition.previousNode, this.startingPosition.currentNode];
    this.fuel = this.maxFuel;
    this.crashStatus = 'NOT_CRASHED';
    this.sizeOfVan = 1;
};

ocargo.Van.prototype.move = function(nextNode) {
    if (nextNode !== this.visitedNodes[this.visitedNodes.length - 1]) {
        this.visitedNodes.push(nextNode);
    }

    this.fuel -= 1 * this.sizeOfVan;
};

ocargo.Van.prototype.getPosition = function() {
    return { previousNode: this.visitedNodes[this.visitedNodes.length - 2], currentNode: this.visitedNodes[this.visitedNodes.length - 1] };
};

ocargo.Van.prototype.getFuelPercentage = function() {
    return 100 * this.fuel / this.maxFuel;
};

ocargo.Van.prototype.getDistanceTravelled = function() {
    return this.visitedNodes.length - 2; // Don't count starting position, or previous position at start
};

