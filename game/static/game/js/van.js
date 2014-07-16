'use strict';

var ocargo = ocargo || {};

ocargo.Van = function(id, previousNode, startNode, maxFuel, ui) {
    this.id = id;
    this.previousNode = previousNode;
    this.currentNode = startNode;
    this.maxFuel = maxFuel;
    this.fuel = maxFuel;
    this.ui = ui;
    ocargo.sound.starting();
    this.travelled = 0;
};

ocargo.Van.prototype.move = function(nextNode, instruction, callback) {
    if (instruction === ocargo.FORWARD_ACTION) {
        moveForward(this, callback);
        this.travelled++;
        ocargo.sound.moving();
    } else if (instruction === ocargo.TURN_LEFT_ACTION) {
        moveLeft(this, callback);
        this.travelled++;
        ocargo.sound.turning();
    } else if (instruction === ocargo.TURN_RIGHT_ACTION) {
        moveRight(this, callback);
        this.travelled++;
        ocargo.sound.turning();
    } else if (instruction === ocargo.TURN_AROUND_ACTION) {
        turnAround(this, callback);
        this.travelled++;
        ocargo.sound.turning();
        ocargo.sound.turning();
    } else if (instruction === ocargo.WAIT_ACTION) {
    	wait(this, callback);
        //ocargo.sound.idling();
    }

	if (instruction !== ocargo.WAIT_ACTION) {
        this.previousNode = this.currentNode;
	    this.currentNode = nextNode;
    }

    console.log("Van moving to (" + this.currentNode.coordinate.x + ", " + this.currentNode.coordinate.y + ")");

	ocargo.time.incrementTime();
	this.fuel--;
    updateFuelGuage(this.fuel, this.maxFuel);
};

function updateFuelGuage(fuel, maxFuel) {
    var rotation = 'rotate(' + (((fuel/maxFuel)*240)-120) + 'deg)';
    document.getElementById('fuelGuagePointer').style.transform=rotation;
    document.getElementById('fuelGuagePointer').style.webkitTransform=rotation;
}
