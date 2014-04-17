function Stack(){
	this.levels = [];
}

Stack.prototype.step = function() {
	var level = this.levels[this.levels.length - 1];
	
	var commandToProcess = level.splice(0, 1)[0];
	if(level.length === 0){
		this.levels.pop();
	}
	
	commandToProcess.execute(this);
}

Stack.prototype.addNewLevel = function(commands) {
	this.levels.push(commands);
}

function IF(condition, ifContents, elseContents){
	this.condition = condition;
	this.ifContents = ifContents;
	this.elseContents = elseContents;
}

IF.prototype.execute = function(stack) {
	if(this.condition()) {
		stack.addNewLevel(this.ifCommands);
	} else if(elseContents){
		stack.addNewLevel(this.elseCommands);
	} else {
		stack.step();
	}
}

var WHILE = {};

function broadcast(instruction){
	console.debug(instruction);
}

TURN_LEFT_COMMAND = {};
TURN_LEFT_COMMAND.execute = function(stack){
	broadcast(TURN_LEFT);
}

TURN_RIGHT_COMMAND = {};
TURN_RIGHT_COMMAND.execute = function(stack){
	broadcast(TURN_RIGHT);
}

FORWARD_COMMAND = {};
FORWARD_COMMAND.execute = function(stack){
	broadcast(FORWARD);
}

// Usage:
//var stack = new Stack();
//stack.addNewLevel([TURN_LEFT_COMMAND, TURN_LEFT_COMMAND]);
//stack.step();
//stack.step();