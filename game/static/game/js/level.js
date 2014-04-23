'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, van, destination, ui) {
    this.map = map;
    this.van = van;
    this.destination = destination;
    this.ui = ui;
}

ocargo.Level.prototype.play = function(program){
    $.post('/game/submit', JSON.stringify(program.levels));
	
    while(program.canStep()) {
        program.step();
    }
    
    this.ui.animateUpdates();
};

function InstructionHandler(level){
	this.level = level;
}

InstructionHandler.prototype.handleInstruction = function(instruction, program){
	console.debug('Calculating next node for instruction ' + instruction.name);
    var nextNode = instruction.getNextNode(this.level.van.previousNode, this.level.van.currentNode);

    if (nextNode === this.level.destination && !program.canStep()) {
        console.debug('You win!');
        program.terminate();
    } else if (!nextNode) {
        console.debug('Oh dear! :(');
        program.terminate();
        return; //TODO: animate crash
    }

    this.level.van.move(nextNode, instruction);
};
