'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, van, ui) {
    this.levelId = null;
    this.map = map;
    this.van = van;
    this.ui = ui;
    this.correct = 0;
    this.attemptData = {};
    this.blockLimit = null;
};

ocargo.Level.prototype.play = function(program){

    this.attemptData = {};
    var commandStack = [];
    
    if (ocargo.level.blockLimit 
        && ocargo.blocklyControl.getBlocksCount() > ocargo.level.blockLimit) {
        startPopup("You used too many blocks!");
        return;
    }


    ocargo.level.attemptData.level = ocargo.level.levelId.toString(); 

    for (var i = 0; i < program.stack.length; i++) {
        ocargo.level.recogniseStack(program.stack[i], commandStack);
    }

    this.attemptData.commandStack = JSON.stringify(commandStack);
    program.startBlock.select();

    var stepFunction = stepper(this);

    program.stepCallback = stepFunction;
    this.program = program;
    setTimeout(stepFunction, 500);
};

ocargo.Level.prototype.recogniseStack = function(stack, returnStack) {
    if(stack) {
        for (var i = 0; i < stack.length; i++) {
            var command = recogniseCommand(stack[i], returnStack);
            returnStack.push(command);
        } 
    }
    
    function recogniseCommand(command, returnStack) {
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
            var block = [];
            ocargo.level.recogniseStack(command.body, block);
            parsedCommand.command = 'While';
            parsedCommand.condition = command.condition.toString();
            parsedCommand.block = block;
       
        } else if (command instanceof If) {
            var commands = command.conditionalCommandSets[0];
            var ifBlock = [];
            parsedCommand.condition = commands.condition.toString();
            ocargo.level.recogniseStack(commands.commands, ifBlock);

            if (command.elseCommands) {
                commands = command.elseCommands;
                var elseBlock = [];
                ocargo.level.recogniseStack(commands, elseBlock);
                parsedCommand.elseBlock = elseBlock;
            }
            parsedCommand.command = 'If';
            parsedCommand.ifBlock = ifBlock;
        }
        return parsedCommand;
    }
};

ocargo.Level.prototype.step = function() {
    if (this.program.canStep()) {
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
    console.debug("Przed");
    var message = '<center> You win! <br><br>' + '<button onclick="window.location.href=' + 
            "'/game/" + (ocargo.level.levelId + 1) + "'" + '"">Next lesson</button> </center>';
    startPopup(message);
    console.debug("Po");
};

ocargo.Level.prototype.fail = function(msg) {
    console.debug('Oh dear! :(');
    ocargo.sound.failure();
    startPopup(msg);
};

function stepper(level) {
	return function(){
        try {
    		if (level.program.canStep()) {
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

InstructionHandler.prototype.handleInstruction = function(instruction, program) {
	console.debug('Calculating next node for instruction ' + instruction.name);
    var nextNode = instruction.getNextNode(this.level.van.previousNode, this.level.van.currentNode);

    if (!nextNode) {
        var n = this.level.correct - 1;
        ocargo.blocklyControl.blink();

        this.level.fail("Oh dear! :( <br> Your first " + n + " instructions were right." + 
            " Click 'Clear Incorrect' to remove the incorrect blocks and try again!");

        program.terminate();
        return; //TODO: animate the crash
    }

    this.level.van.move(nextNode, instruction, program.stepCallback);
};
