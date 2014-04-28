var ocargo = ocargo || {};

ocargo.Program = function(instructionHandler){
	this.instructionHandler = instructionHandler;
	this.stack = [];
	this.isTerminated = false;
};

ocargo.Program.prototype.step = function(level) {
	var stackLevel = this.stack[this.stack.length - 1];
	
	var commandToProcess = stackLevel.splice(0, 1)[0];
	if(stackLevel.length === 0){
		this.stack.pop();
	}
	
	commandToProcess.execute(this, level);
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

function If(conditionalCommandSets, elseCommands){
	this.conditionalCommandSets = conditionalCommandSets;
	this.elseCommands = elseCommands;
}

If.prototype.execute = function(program, level) {
	var i = 0;
	while(i < this.conditionalCommandSets.length){
		if(this.conditionalCommandSets[i].condition(level)) {
			program.addNewStackLevel(this.conditionalCommandSets[i].commands.slice(0));
			return;
		}
		
		i++;
	}
	
	if(this.elseCommands){
		program.addNewStackLevel(this.elseCommands.slice(0));
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

function roadCondition(selection){
	var f = function(level){
		if(selection === 'FORWARD'){
			return FORWARD.getNextNode(level.van.previousNode, level.van.currentNode);
		}else if(selection === 'LEFT'){
			return TURN_LEFT.getNextNode(level.van.previousNode, level.van.currentNode);
		}else if(selection === 'RIGHT'){
			return TURN_RIGHT.getNextNode(level.van.previousNode, level.van.currentNode);
		}
	};
	
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
//var program = new ocargo.Program();
//program.addNewStackLevel([TURN_LEFT_COMMAND, TURN_LEFT_COMMAND]);
//program.step();
//program.step();
