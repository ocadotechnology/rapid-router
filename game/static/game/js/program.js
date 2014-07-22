'use strict';

var ocargo = ocargo || {};

/* Program */

ocargo.Program = function() {
	this.threads = [];
	this.isFinished = false;
	this.procedures = {};
};

ocargo.Program.prototype.step = function(level) {
	this.isFinished = true;
	for (var i = 0; i < this.threads.length; i++) {
		if (this.threads[i].canStep()) {
			this.threads[i].step(level);
		}
		else {
			this.threads[i].currentAction = ocargo.EMPTY_ACTION;
		}
		this.isFinished = this.isFinished && this.threads[i].isFinished;
	}
};

ocargo.Program.prototype.canStep = function() {
	for (var i = 0; i < this.threads.length; i++) {
		if (this.threads[i].canStep()) {
			return true;
		}
	}
	return false;
};

ocargo.Program.prototype.terminate = function() {
	for (var i = 0; i < this.threads.length; i++) {
		this.threads[i].terminate();
	}
	this.isFinished = true;
};


/* Thread */

ocargo.Thread = function(id) {
	this.id = id;
	this.stack = [];
	this.isFinished = false;
	this.instructionHandler = null;
	this.currentAction = null;
	this.currentBlock = null;
};

ocargo.Thread.prototype.step = function(level) {
	var stackLevel = this.stack[this.stack.length - 1];
	var commandToProcess = stackLevel.splice(0, 1)[0];

	if (stackLevel.length === 0) {
		this.stack.pop();
	}
	commandToProcess.execute(this, level);

	if(this.stack.length == 0) {
		this.isFinished = true;
	}
};

ocargo.Thread.prototype.canStep = function() {
	return this.stack.length !== 0 && this.stack[0].length !== 0;
};

ocargo.Thread.prototype.addNewStackLevel = function(commands) {
	this.stack.push(commands);
};

ocargo.Thread.prototype.terminate = function() {
	this.stack = [];
	this.isFinished = true;
};



/* Instructions */

function TurnLeftCommand(block) {
	this.block = block;
}

TurnLeftCommand.prototype.execute = function(thread) {
	thread.currentBlock = this.block;
	thread.currentAction = ocargo.TURN_LEFT_ACTION;
};



function TurnRightCommand(block) {
	this.block = block;
}

TurnRightCommand.prototype.execute = function(thread) {
	thread.currentBlock = this.block;
	thread.currentAction = ocargo.TURN_RIGHT_ACTION;
};



function ForwardCommand(block) {
	this.block = block;
}

ForwardCommand.prototype.execute = function(thread) {
	thread.currentBlock = this.block;
	thread.currentAction = ocargo.FORWARD_ACTION;
};



function TurnAroundCommand(block) {
    this.block = block;
}

TurnAroundCommand.prototype.execute = function(thread) {
    thread.currentBlock = this.block;
    thread.currentAction = ocargo.TURN_AROUND_ACTION;
};



function WaitCommand(block) {
    this.block = block;
}

WaitCommand.prototype.execute = function(thread) {
    thread.currentBlock = this.block;
    thread.currentAction = ocargo.WAIT_ACTION;
};



function If(conditionalCommandSets, elseBody, block) {
	this.conditionalCommandSets = conditionalCommandSets;
	this.elseBody = elseBody;
	this.block = block;
}

If.prototype.execute = function(thread, level) {
	thread.currentBlock = this.block;
	thread.currentAction = ocargo.EMPTY_ACTION;

	var i = 0;
	while (i < this.conditionalCommandSets.length) {
		if (this.conditionalCommandSets[i].condition(level,thread.id)) {
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

While.prototype.execute = function(thread, level) {
	thread.currentBlock = this.block;
	thread.currentAction = ocargo.EMPTY_ACTION;

	if (this.condition(level,thread.id)) {
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
	thread.currentBlock = this.block;
	thread.currentAction = ocargo.EMPTY_ACTION;

	thread.addNewStackLevel(this.body.slice());
}



function ProcedureCall(block) {
	this.block = block;
};

ProcedureCall.prototype.bind = function(proc) {
	this.proc = proc;
}

ProcedureCall.prototype.execute = function(thread) {
	thread.currentBlock = this.block;
	thread.currentAction = ocargo.EMPTY_ACTION;

	thread.addNewStackLevel([this.proc]);
}