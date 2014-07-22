'use strict';

var ocargo = ocargo || {};

/* Program */

ocargo.Program = function() {
	this.threads = [];
	this.procedures = {};
};

ocargo.Program.prototype.run = function(model) {
	for (var i = 0; i < this.threads.length; i++) {
		model.reset(i);
		this.threads[i].run(model);
	}
};



/* Thread */

ocargo.Thread = function() {
	this.stack = [];
};

ocargo.Thread.prototype.run = function(model) {
	while (this.canStep()) {
		this.step(model);
	}
};

ocargo.Thread.prototype.step = function(model) {
	var stackLevel = this.stack[this.stack.length - 1];
	var commandToProcess = stackLevel.shift();

	if (stackLevel.length === 0) {
		this.stack.pop();
	}

	var successful = commandToProcess.execute(this, model);

	if (!successful) {
		// Program crashed
		ocargo.blocklyControl.highlightIncorrectBlock(commandToProcess.block);
	}
};

ocargo.Thread.prototype.canStep = function() {
	return this.stack.length !== 0 && this.stack[0].length !== 0;
};

ocargo.Thread.prototype.addNewStackLevel = function(commands) {
	this.stack.push(commands);
};



/* Instructions */

function TurnLeftCommand(block) {
	this.block = block;
}

TurnLeftCommand.prototype.execute = function(thread, model) {
	queueHighlight(this.block);
	return model.turnLeft();
};



function TurnRightCommand(block) {
	this.block = block;
}

TurnRightCommand.prototype.execute = function(thread, model) {
	queueHighlight(this.block);
	return model.turnRight();
};



function ForwardCommand(block) {
	this.block = block;
}

ForwardCommand.prototype.execute = function(thread, model) {
	queueHighlight(this.block);
	return model.moveForwards();
};



function TurnAroundCommand(block) {
    this.block = block;
}

TurnAroundCommand.prototype.execute = function(thread, model) {
	queueHighlight(this.block);
	return model.turnAround();
};



function WaitCommand(block) {
    this.block = block;
}

WaitCommand.prototype.execute = function(thread, model) {
	queueHighlight(this.block);
	return model.wait();
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
			return;
		}

		i++;
	}

	if(this.elseBody) {
		thread.addNewStackLevel(this.elseBody.slice());
	}
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
};



function Procedure(name,body,block) {
	this.name = name;
	this.body = body;
	this.block = block;
};

Procedure.prototype.execute = function(thread) {
	thread.addNewStackLevel(this.body.slice());
}



function ProcedureCall(block) {
	this.block = block;
};

ProcedureCall.prototype.bind = function(proc) {
	this.proc = proc;
}

ProcedureCall.prototype.execute = function(thread) {
	thread.addNewStackLevel([this.proc]);
}



/* Highlighting of blocks */

function queueHighlight(block) {
	ocargo.animation.queueAnimation(model.timestamp, {
		type: 'callable',
		functionCall: makeHighLightCallable(this.block),
	});
}

function makeHighLightCallable(block) {
	return function() {
		ocargo.blocklyControl.selectBlock(block);
	};
}