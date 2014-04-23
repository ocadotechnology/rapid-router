var ocargo = ocargo || {};

ocargo.Program = function(instructionHandler){
	this.instructionHandler = instructionHandler;
	this.stack = [];
	this.isTerminated = false;
};

ocargo.Program.prototype.step = function() {
	var level = this.stack[this.stack.length - 1];
	
	var commandToProcess = level.splice(0, 1)[0];
	if(level.length === 0){
		this.stack.pop();
	}
	
	commandToProcess.execute(this);
};

ocargo.Program.prototype.canStep = function() {
	return this.stack.length !== 0;
};

ocargo.Program.prototype.addNewStackLevel = function(commands) {
	this.stack.push(commands);
};

ocargo.Program.prototype.terminate = function() {
	this.stack = [];
	this.isTerminated = true;
};

function IF(condition, ifContents, elseContents){
	this.condition = condition;
	this.ifContents = ifContents;
	this.elseContents = elseContents;
}

IF.prototype.execute = function(program) {
	if(this.condition()) {
		program.addNewStackLevel(this.ifCommands);
	} else if(elseContents){
		program.addNewStackLevel(this.elseCommands);
	} else {
		program.step();
	}
};

function While(condition, body){
	this.condition = condition;
	this.body = body;
}

While.prototype.execute = function(program){
	if(this.condition()){
		program.addNewStackLevel([this]);
		program.addNewStackLevel(this.body.slice(0));
	}
};

function counterCondition(count){
	var f = function(){
		if(count > 0){
			count--;
			return true;
		}
		
		return false;
	}
	
	return f;
}

TURN_LEFT_COMMAND = {};
TURN_LEFT_COMMAND.execute = function(program){
	program.instructionHandler.handleInstruction(TURN_LEFT, program);
};

TURN_RIGHT_COMMAND = {};
TURN_RIGHT_COMMAND.execute = function(program){
	program.instructionHandler.handleInstruction(TURN_RIGHT, program);
};

FORWARD_COMMAND = {};
FORWARD_COMMAND.execute = function(program){
	program.instructionHandler.handleInstruction(FORWARD, program);
};

// Usage:
//var program = new ocargo.Stack();
//program.addNewLevel([TURN_LEFT_COMMAND, TURN_LEFT_COMMAND]);
//program.step();
//program.step();
