'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, van, destination, ui) {
    this.map = map;
    this.van = van;
    this.destination = destination;
    this.ui = ui;
}

ocargo.Level.prototype.play = function(program){
    $.post('/game/submit', JSON.stringify(program.instructions));
	
    while(program.canStep()) {
        var instruction = program.step(new InstructionHandler(this, program));
    }
    
    this.ui.animateUpdates();
};

function InstructionHandler(level, program){
	this.level = level;
	this.program = program;
}

InstructionHandler.prototype.handleInstruction = function(instruction){
	console.debug('Calculating next node for instruction ' + instruction.name);
    var nextNode = instruction.getNextNode(this.level.van.previousNode, this.level.van.currentNode);

    if (nextNode === this.level.destination && !this.program.canStep()) {
        console.debug('You win!');
        this.program.terminate();
    } else if (!nextNode) {
        console.debug('Oh dear! :(');
        this.program.terminate();
    }

    this.level.van.move(nextNode, instruction);
};
