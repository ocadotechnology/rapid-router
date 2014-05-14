'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, van, ui) {
    this.map = map;
    this.van = van;
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
    	if (this.van.currentNode === this.map.destination && !this.program.isTerminated) {
            this.win();
        }
    }
};

ocargo.Level.prototype.win = function() {
    console.debug('You win!');
    ocargo.sound.win();
    window.alert('You win!');
};

ocargo.Level.prototype.fail = function(msg) {
    console.debug('Oh dear! :(');
    ocargo.sound.failure();
    window.alert(msg);
};

function stepper(level){
	return function(){
        try {
    		if(level.program.canStep()) {
                level.correct = level.correct + 1;
    			level.program.step(level);
    	    } else {
                if (level.van.currentNode === level.map.destination && !level.program.isTerminated) {
                    level.win();
                } else {
                    level.fail("Oh dear! :( You ran out of instructions!");

                    program.terminate();
                }
            }
        } catch (error) {
            level.program.terminate();
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
        ocargo.blocklyTest.blink();

        this.level.fail("Oh dear! :( Your first " + n + " instructions were right."
            + " Click 'Clear Incorrect' to remove the incorrect blocks and try again!");

        program.terminate();
        return; //TODO: animate the crash
    }

    this.level.van.move(nextNode, instruction, program.stepCallback);
};
