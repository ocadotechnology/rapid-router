'use strict';

var ocargo = ocargo || {};

var MAX_EXECUTION_STEPS = 10000;

/* Program */

ocargo.Program = function() {
	this.threads = [];
	this.procedures = {};
};

ocargo.Program.prototype.run = function() {
	for (var i = 0; i < this.threads.length; i++) {
		ocargo.model.reset(i);
		this.threads[i].run(ocargo.model);
	}
};

/* Thread */

ocargo.Thread = function() {
	this.stack = [];
	this.noExecutionSteps = 0;
};

ocargo.Thread.prototype.run = function(model) {
	var failed = false;
	while (!failed && this.canStep()) {
		failed = !this.step(model);
	}
	if (!failed) {
		model.programExecutionEnded();
	}
};

ocargo.Thread.prototype.step = function(model) {
	var stackLevel = this.stack[this.stack.length - 1];
	var commandToProcess = stackLevel.shift();
	this.noExecutionSteps ++;
	if (this.noExecutionSteps > MAX_EXECUTION_STEPS) {
		// alert user to likely infinite loop
		ocargo.animation.appendAnimation({
            type: 'popup',
            id: this.vanId,
            popupType: 'FAIL',
            failSubtype: 'QUERY_INFINITE_LOOP',
            popupMessage: ocargo.messages.queryInfiniteLoop,
            popupHint: ocargo.game.registerFailure(),
            description: 'failure popup'
        });
		return false;
	}

	if (stackLevel.length === 0) {
		this.stack.pop();
	}

	var successful = true;
	if (commandToProcess) {
		successful = commandToProcess.execute(this, model);
	}

	if (!successful) {
		// Program crashed, queue a block highlight event
        var block = commandToProcess.block;
		queueHighlightIncorrect(block);
		return false;
	}

	return true;
};

ocargo.Thread.prototype.canStep = function() {
	return this.stack.length !== 0 && this.stack[0].length !== 0;
};

ocargo.Thread.prototype.addNewStackLevel = function(commands) {
	this.stack.push(commands);
};


/* Simplified blocks containing only id, type
 * all methods after comile() uses simplified blocks */
function Block(id, type) {
	this.id = id;
	this.type = type;
}

/* Instructions */

function TurnLeftCommand(block) {
	this.block = block;
}

TurnLeftCommand.prototype.execute = function(thread, model) {
	queueHighlight(model, this.block);
	return model.turnLeft();
};



function TurnRightCommand(block) {
	this.block = block;
}

TurnRightCommand.prototype.execute = function(thread, model) {
	queueHighlight(model, this.block);
	return model.turnRight();
};



function ForwardCommand(block) {
	this.block = block;
}

ForwardCommand.prototype.execute = function(thread, model) {
	queueHighlight(model, this.block);
	return model.moveForwards();
};



function TurnAroundCommand(block) {
    this.block = block;
}

TurnAroundCommand.prototype.execute = function(thread, model) {
	queueHighlight(model, this.block);
	return model.turnAround();
};



function WaitCommand(block) {
    this.block = block;
}

WaitCommand.prototype.execute = function(thread, model) {
	queueHighlight(model, this.block);
	return model.wait();
};



function DeliverCommand(block) {
    this.block = block;
}

DeliverCommand.prototype.execute = function(thread, model) {
	queueHighlight(model, this.block);
	return model.deliver();
};



function If(conditionalCommandSets, elseBody, block) {
	this.conditionalCommandSets = conditionalCommandSets;
	this.elseBody = elseBody;
	this.block = block;
}

If.prototype.execute = function(thread, model) {
	var i = 0;
	while (i < this.conditionalCommandSets.length) {
		if (this.conditionalCommandSets[i].condition(model)) {
			thread.addNewStackLevel(this.conditionalCommandSets[i].commands.slice());
			return true;
		}

		i++;
	}

	if(this.elseBody) {
		thread.addNewStackLevel(this.elseBody.slice());
	}
	return true;
};



function While(condition, body, block) {
	this.condition = condition;
	this.body = body;
	this.block = block;
}

While.prototype.execute = function(thread, model) {
	if (this.condition(model)) {
		thread.addNewStackLevel([this]);
		thread.addNewStackLevel(this.body.slice());
	}
	return true;
};



function Procedure(name,body,block) {
	this.name = name;
	this.body = body;
	this.block = block;
};

Procedure.prototype.execute = function(thread) {
	thread.addNewStackLevel(this.body.slice());
	return true;
};



function ProcedureCall(block) {
	this.block = block;
};

ProcedureCall.prototype.bind = function(proc) {
	this.proc = proc;
};

ProcedureCall.prototype.execute = function(thread) {
	thread.addNewStackLevel([this.proc]);
	return true;
};



/* Highlighting of blocks */

function queueHighlight(model, block) {
	ocargo.animation.appendAnimation({
		type: 'callable',
		functionCall: makeHighLightCallable(block.id),
		description: 'Blockly highlight: ' + block.type,
		blockId: block.id
	});
}

function queueHighlightIncorrect(block){
	ocargo.animation.appendAnimation({
		type: 'callable',
		functionCall: makeHighLightIncorrectCallable(block.id),
		description: 'Blockly highlight incorrect: ' + block.type,
		blockId: block.id
	});
}

function makeHighLightCallable(id) {
	return function() {
		ocargo.blocklyControl.clearAllSelections();
		ocargo.blocklyControl.setBlockSelected(Blockly.Block.getById(id, Blockly.mainWorkspace), true);
	};
}

function makeHighLightIncorrectCallable(id){
	return function() {
		ocargo.blocklyControl.highlightIncorrectBlock(Blockly.Block.getById(id, Blockly.mainWorkspace));
	}
}
