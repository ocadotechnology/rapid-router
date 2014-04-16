'use strict';

function Program(instructions) {
    this.instructions = instructions;
    this.instructionPosition = 0;
}

Program.prototype.step = function(instructionHandler) {
    var instruction = this.instructions[this.instructionPosition];
    this.instructionPosition++;

    instructionHandler.handleInstruction(instruction);
};

Program.prototype.canStep = function() {
    return this.instructionPosition < this.instructions.length;
};

Program.prototype.terminate = function() {
	this.instructionPosition = this.instructions.length;
};