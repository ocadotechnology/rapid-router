'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, van, ui, nextLevel, nextEpisode) {
    this.levelId = null;
    this.map = map;
    this.van = van;
    this.ui = ui;
    this.correct = 0;
    this.attemptData = {};
    this.blockLimit = null;
    this.pathFinder = new ocargo.PathFinder(map);
    this.fails = 0;
    this.hintOpened = false;
    this.nextLevel = nextLevel;
    this.nextEpisode = nextEpisode;
};

ocargo.Level.prototype.failsBeforeHintBtn = 3;

ocargo.Level.prototype.play = function(program) {

    this.attemptData = {};
    var commandStack = [];

    if (ocargo.level.blockLimit &&
            ocargo.blocklyControl.getBlocksCount() > ocargo.level.blockLimit) {
        enableDirectControl();
        startPopup("Oh no!", "", ocargo.messages.tooManyBlocks);
        sendAttempt(0);
        return;
    }

    ocargo.level.attemptData.level = ocargo.level.levelId.toString();

    for (var i = 0; i < program.stack.length; i++) {
        ocargo.level.recogniseStack(program.stack[i], commandStack);
    }

    this.attemptData.commandStack = JSON.stringify(commandStack);
    program.startBlock.selectWithConnected();

    var stepFunction = stepper(this, true);

    program.stepCallback = stepFunction;
    this.program = program;    
    setTimeout(stepFunction, 500);
};

ocargo.Level.prototype.recogniseStack = function(stack, returnStack) {
    if (stack) {
        for (var i = 0; i < stack.length; i++) {
            var command = recogniseCommand(stack[i]);
            returnStack.push(command);
        }
    }

    function recogniseCommand(command) {
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
    ocargo.level.pathFinder.getOptimalPath();
    ocargo.level.pathFinder.getOptimalInstructions();
    var score = ocargo.level.pathFinder.getScore(JSON.parse(ocargo.level.attemptData.commandStack));
    console.debug("score: ", score, " out of 200.");
    sendAttempt(score);
    ocargo.sound.win();
    var message = '';
    var subtitle = "Your score: " + score + " / " + ocargo.level.pathFinder.max;
    enableDirectControl();

    if (ocargo.level.nextLevel != null) {
      message = ocargo.messages.nextLevelButton(ocargo.level.nextLevel);
    } else {
        if (ocargo.level.nextEpisode != null) {
            message = ocargo.messages.nextEpisodeButton(ocargo.level.nextEpisode);
        } else {
            message = ocargo.messages.lastLevel;
        }
    }
    startPopup("You win!", subtitle, message);
};

ocargo.Level.prototype.fail = function(msg, send) {
    var title = 'Oh dear! :(';
    $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v3.svg)');
    console.debug(title);
    enableDirectControl();
    ocargo.sound.failure();
    startPopup(title, '', msg + ocargo.messages.closebutton("Try again"));
    var level = this;
    level.fails++;
    if (level.fails >= level.failsBeforeHintBtn) {
	    var hintBtns = $("#hintPopupBtn");
		if (hintBtns.length === null || hintBtns.length === 0) {
			$("#myModal > .mainText").append('<p id="hintBtnPara">' +
                '<button id="hintPopupBtn">'ocargo.messages.needHint'</button>' + 
                '</p><p id="hintText">' + HINT + '</p>');
			if(level.hintOpened){
				$("#hintBtnPara").hide();
			} else {
				$("#hintText" ).hide();
				$("#hintPopupBtn").click( function(){
					$("#hintText").show(500);
					$("#hintBtnPara").hide();
					level.hintOpened = true;
				});
			}
    	}
    }
    if (send) {
        sendAttempt(0);
    }
};

function stepper(level, play) {
    return function() {
        try {
            if (level.program.canStep()) {
                level.correct = level.correct + 1;
                level.program.step(level);
            } else {
                if (level.van.currentNode === level.map.destination && !level.program.isTerminated) {
                    if(play) {
                        level.win();
                    }
                } else if (level.program.isTerminated) {
                    level.fail(ocargo.messages.te, play);
                    $("#myModal > .title").text(ocargo.messages.stoppingTittle);
                }
                else {
                    level.fail(ocargo.messages.outOfInstructions, play);
                    level.program.terminate();
                }
            }
        } catch (error) {
            level.fail(ocargo.messages.crashed, play);
            level.program.terminate();
            throw error;
        }
    };
}

function sendAttempt(score) {

    // Send out the submitted data.
    if (ocargo.level.levelId) {
        var attemptData = JSON.stringify(ocargo.level.attemptData);

        $.ajax({
            url : '/game/submit',
            type : 'POST',
            dataType: 'json',
            data : {
                attemptData : attemptData,
                csrfmiddlewaretoken :$( '#csrfmiddlewaretoken' ).val(),
                score : score
            },
            success : function(json) {
            },
            error : function(xhr,errmsg,err) {
                console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    }
    return false;
}

function InstructionHandler(level, isPlay) {
	this.level = level;
    this.isPlay = isPlay
}

InstructionHandler.prototype.handleInstruction = function(instruction, program) {
	console.debug('Calculating next node for instruction ' + instruction.name);
    var nextNode = instruction.getNextNode(this.level.van.previousNode, this.level.van.currentNode);
    if (!nextNode) {
        var n = this.level.correct - 1;
        ocargo.blocklyControl.blink();
        this.level.fail(ocargo.messages.xcorrect(n) + ocargo.messages.tryagain);

        program.terminate();
        return; //TODO: animate the crash
    }
    
    if (this.level.van.fuel === 0) {
        this.level.fail(ocargo.messages.nofuel);
		program.terminate();
		return;
    }

    this.level.van.move(nextNode, instruction, program.stepCallback);
};
