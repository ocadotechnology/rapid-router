'use strict';

var ocargo = ocargo || {};

ocargo.Van = function(previousNode, startNode, maxFuel, ui) {
    this.previousNode = previousNode;
    this.currentNode = startNode;
    this.maxFuel = maxFuel;
    this.fuel = maxFuel;
    this.ui = ui;
    ocargo.sound.starting();
    this.travelled = 0;
};

ocargo.Van.prototype.move = function(nextNode, instruction, callback) {
    if (instruction === FORWARD) {
        moveForward(callback);
        this.travelled++;
        ocargo.sound.moving();
    } else if (instruction === TURN_LEFT) {
        moveLeft(callback);
        this.travelled++;
        ocargo.sound.turning();
    } else if (instruction === TURN_RIGHT) {
        moveRight(callback);
        this.travelled++;
        ocargo.sound.turning();
    } else if (instruction === TURN_AROUND) {
        turnAround(callback);
        this.travelled++;
        ocargo.sound.turning();
        ocargo.sound.turning();
    } else if (instruction === WAIT) {
    	wait(callback);
        //ocargo.sound.idling();
    }

	if (instruction !== WAIT) {
        this.previousNode = this.currentNode;
	    this.currentNode = nextNode;
    }

	ocargo.time.incrementTime();
	this.fuel--;
    updateFuelGuage(this.fuel, this.maxFuel);
};

function updateFuelGuage(fuel, maxFuel) {
    var rotation = 'rotate(' + (((fuel/maxFuel)*240)-120) + 'deg)';
    document.getElementById('fuelGuagePointer').style.transform=rotation;
    document.getElementById('fuelGuagePointer').style.webkitTransform=rotation;
}
