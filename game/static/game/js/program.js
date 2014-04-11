'use strict';

function Program(instructions) {
    this.instructions = instructions;
    this.instructionPosition = 0;
}

Program.prototype.step = function(){
    var instruction = this.instructions[this.instructionPosition];
    this.instructionPosition++;

    return instruction;
};

Program.prototype.canStep = function() {
    return this.instructionPosition < this.instructions.length;
};