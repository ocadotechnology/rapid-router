'use strict';

var ocargo = ocargo || {};

ocargo.Program = function(instructions) {
    this.instructions = instructions;
    this.instructionPosition = 0;
}

ocargo.Program.prototype.step = function(instructionHandler) {
    var instruction = this.instructions[this.instructionPosition];
    this.instructionPosition++;

    instructionHandler.handleInstruction(instruction);
};

ocargo.Program.prototype.canStep = function() {
    return this.instructionPosition < this.instructions.length;
};

ocargo.Program.prototype.terminate = function() {
	this.instructionPosition = this.instructions.length;
};
