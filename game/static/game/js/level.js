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
	
    var stepFunction = stepper(this);
    
    program.instructionHandler.callback = stepFunction;
    this.program = program;
    stepFunction();
};

ocargo.Level.prototype.step = function(){
	if(this.program.canStep()) {
        this.program.step(this);
    } else {
    	if (this.van.currentNode === this.destination && !this.program.isTerminated) {
            console.debug('You win!');//TODO: tell user
        }
    }
};

function stepper(level){
	return function(){
		if(level.program.canStep()) {
			level.program.step(level);
	    } else {
	    	if (level.van.currentNode === level.destination && !level.program.isTerminated) {
	            console.debug('You win!');//TODO: tell user
	        }
	    }
	};
}

function InstructionHandler(level){
	this.level = level;
}

InstructionHandler.prototype.handleInstruction = function(instruction, program){
	console.debug('Calculating next node for instruction ' + instruction.name);
    var nextNode = instruction.getNextNode(this.level.van.previousNode, this.level.van.currentNode);

    if (!nextNode) {
        console.debug('Oh dear! :(');
        program.terminate();
        return; //TODO: animate crash, tell user
    }

    this.level.van.move(nextNode, instruction, this.callback);
};
