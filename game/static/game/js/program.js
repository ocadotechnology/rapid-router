'use strict';

function Program(instructions) {
    this.instructions = instructions;
    this.instructionPosition = 0;

    this.step = function(){
        var instruction = this.instructions[this.instructionPosition];
        this.instructionPosition++;

        return instruction;
    };

    this.canStep = function() {
        return this.instructionPosition < this.instructions.length;
    };
}