'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, van, ui) {
    this.levelId = null;
    this.map = map;
    this.van = van;
    this.ui = ui;
    this.correct = 0;
    this.attemptData = {};
};

ocargo.Level.prototype.play = function(program){

    this.attemptData = {};
    var commandStack = [];

    ocargo.level.attemptData.level = ocargo.level.levelId.toString(); 

    for (var i = 0; i < program.stack.length; i++) {
        for(var j = 0; j < program.stack[i].length; j++) {
            var command = ocargo.level.recogniseCommand(program.stack[i][j]);
            commandStack.push(command);
        }
    }
    console.debug(JSON.stringify(commandStack));
    this.attemptData.commandStack = JSON.stringify(commandStack);
    // TODO: calculate score
    program.startBlock.select();

    var stepFunction = stepper(this);

    program.stepCallback = stepFunction;
    this.program = program;
    setTimeout(stepFunction, 500);
};

ocargo.Level.prototype.recogniseCommand = function(command) {
    console.debug(command);
    var parsedCommand = {};
    
    if (command instanceof ForwardCommand) {
        parsedCommand.command = 'Forward';
    } else if (command instanceof TurnLeftCommand) {
        parsedCommand.command = 'Left';
    } else if (command instanceof TurnRightCommand) {
        parsedCommand.command = 'Right';
    } else if (command instanceof TurnAroundCommand) {
        parsedCommand.command = 'TurnAround';
   
    } else if (command instanceof While) {
        var condition = command.condition.toString();
        var block = [];
        for(var i = 0; i < command.body.length; i++) {
            block.push(ocargo.level.recogniseCommand(command.body[i]));
        }
        parsedCommand.command = 'While';
        parsedCommand.condition = condition;
        parsedCommand.block = block;
   
    } else if (command instanceof If) {
        var commands = command.conditionalCommandSets;
        var condition = commands.condition;
        var ifBlock = [];
        for(var i = 0; i < commands.commands.length; i++) {
            ifBlock.push(ocargo.level.recogniseCommand(commands.commands[i]));
        }
        if(command.hasOwnProperty('elseCommands')) {
            var elseBlock = [];
            commands = command.elseCommands;
            for(var i = 0; i < commands.commands.length; i++) {
                elseBlock.push(ocargo.level.recogniseCommand(commands.commands[i]));
            }
            parsedCommand.elseBlock = elseBlock;
        }
        parsedCommand.command = 'If';
        parsedCommand.condition = condition;
        parsedCommand.ifBlock = ifBlock;
    }
    return parsedCommand;
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

                    level.program.terminate();
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
        ocargo.blocklyControl.blink();

        this.level.fail("Oh dear! :( Your first " + n + " instructions were right." + 
            " Click 'Clear Incorrect' to remove the incorrect blocks and try again!");

        program.terminate();
        return; //TODO: animate the crash
    }

    this.level.van.move(nextNode, instruction, program.stepCallback);
};
