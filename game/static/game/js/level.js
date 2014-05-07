'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, van, destination, ui) {
    this.map = map;
    this.van = van;
    this.destination = destination;
    this.ui = ui;
    this.correct = 0;
}

ocargo.Level.prototype.play = function(program){
//    $.post('/game/submit', JSON.stringify(program.stack));
	
	program.startBlock.select();
	
    var stepFunction = stepper(this);
    
    program.stepCallback = stepFunction;
    this.program = program;
    setTimeout(stepFunction, 500);
};

ocargo.Level.prototype.step = function(){
	if(this.program.canStep()) {
        this.program.step(this);

    } else {
    	if (this.van.currentNode === this.destination && !this.program.isTerminated) {
            console.debug('You win!');
            window.alert('You win!');
        }
    }
};

function stepper(level){
	return function(){
		if(level.program.canStep()) {
            level.correct = level.correct + 1;
			level.program.step(level);
	    } else {
	    	if (level.van.currentNode === level.destination && !level.program.isTerminated) {
	            console.debug('You win!');
                    ocargo.sound.win();
                window.alert('You win!');
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
        var n = this.level.correct - 1;
        var total = this.level.map.nodes.length - 2;
        console.debug('Oh dear! :(');
        ocargo.sound.failure();
        window.alert("Oh dear! :( Your first " + n + " out of " +  total 
            + " instructions were right. Click clear to remove the incorrect blocks "
            + "and try again!");
        program.terminate();
        return; //TODO: animate the crash
    }

    this.level.van.move(nextNode, instruction, program.stepCallback);
};
