'use strict';

var ocargo = ocargo || {};

ocargo.Van = function(position, maxFuel) {
    this.previousNodeOriginal = position.previousNode;
    this.currentNodeOriginal = position.currentNode;

    this.previousNode = position.previousNode;
    this.currentNode = position.currentNode;
    this.maxFuel = maxFuel;
    this.fuel = maxFuel;
    this.travelled = 0;
};

ocargo.Van.prototype.reset = function() {
    this.currentNode = this.currentNodeOriginal;
    this.previousNode = this.previousNodeOriginal;
    this.fuel = this.maxFuel;
    this.travelled = 0;
};

ocargo.Van.prototype.move = function(nextNode) {
    if (nextNode !== this.currentNode) {
        this.previousNode = this.currentNode;
        this.currentNode = nextNode;

        this.travelled += 1;
    }

    this.fuel -= 1;
};

ocargo.Van.prototype.getPosition = function() {
    return { previousNode: this.previousNode, currentNode: this.currentNode };
};

ocargo.Van.prototype.getFuelPercentage = function() {
    return 100 * this.fuel / this.maxFuel;
}
