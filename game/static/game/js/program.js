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


/* Conditions */

function counterCondition(count) {
    return function() {
        if (count > 0) {
            count--;
            return true;
        }

        return false;
    };
}

function roadCondition(selection) {
    return function(level,threadID) {
    	van = level.vans[threadID];
        if (selection === 'FORWARD') {
            return ocargo.FORWARD_ACTION.getNextNode(van.previousNode, van.currentNode);
        } else if (selection === 'LEFT') {
            return ocargo.TURN_LEFT_ACTION.getNextNode(van.previousNode, van.currentNode);
        } else if (selection === 'RIGHT') {
            return ocargo.TURN_RIGHT_ACTION.getNextNode(van.previousNode, van.currentNode);
        }
    };
}

function deadEndCondition() {
    return function(level,threadID) {
        var actions = [ocargo.FORWARD_ACTION, ocargo.TURN_LEFT_ACTION, ocargo.TURN_RIGHT_ACTION];
        for (var i = 0; i < actions.length; i++) {
            var action = actions[i];
            var nextNode = action.getNextNode(level.vans[threadID].previousNode, level.vans[threadID].currentNode);
            if (nextNode) {
                return false;
            }
        }
        return true;
    };
}

function negateCondition(otherCondition) {
	return function(level,threadID) {
		return !otherCondition(level,threadID);
	};
}

function atDestinationCondition() {
    return function(level,threadID) {
    	return level.vans[threadID].currentNode === level.map.destination;
    };
}
function trafficLightCondition(lightColour){
	return function(level,threadID) {
        var prevNode = level.vans[threadID].previousNode;
        var currNode = level.vans[threadID].currentNode;
		for(var i = 0; i < currNode.trafficLights.length; i++){
			var tl = currNode.trafficLights[i];
			if(tl.sourceNode == prevNode && tl.state == lightColour){
				return true;
			}
		}
		return false;
    };
}

/* Instructions */

function TurnLeftCommand(block) {
	this.block = block;
}

TurnLeftCommand.prototype.execute = function(thread) {
	this.block.selectWithConnected();
	thread.currentAction = ocargo.TURN_LEFT_ACTION;
};

TurnLeftCommand.prototype.parse = function() {
	return {command: 'Left'};
}


function TurnRightCommand(block) {
	this.block = block;
}

TurnRightCommand.prototype.execute = function(thread) {
	this.block.selectWithConnected();
	thread.currentAction = ocargo.TURN_RIGHT_ACTION;
};

TurnRightCommand.prototype.parse = function() {
	return {command: 'Right'};
}


function ForwardCommand(block) {
	this.block = block;
}

ForwardCommand.prototype.execute = function(thread) {
	this.block.selectWithConnected();
	thread.currentAction = ocargo.FORWARD_ACTION;
};

ForwardCommand.prototype.parse = function() {
	return {command: 'Forward'};
}


function TurnAroundCommand(block) {
    this.block = block;
}

TurnAroundCommand.prototype.execute = function(thread) {
    this.block.selectWithConnected();
    thread.currentAction = ocargo.TURN_AROUND_ACTION;
};

TurnAroundCommand.prototype.parse = function() {
	return {command: 'TurnAround'};
}



function WaitCommand(block) {
    this.block = block;
}

WaitCommand.prototype.execute = function(thread) {
    this.block.selectWithConnected();
    thread.currentAction = ocargo.WAIT_ACTION;
};

WaitCommand.prototype.parse = function() {
	return {command: 'Wait'};
}



function If(conditionalCommandSets, elseBody, block) {
	this.conditionalCommandSets = conditionalCommandSets;
	this.elseBody = elseBody;
	this.block = block;
}

If.prototype.execute = function(thread, level) {
	this.block.selectWithConnected();
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

If.prototype.parse = function() {
	var ifBlocks = [];
	for(var i = 0; i < this.conditionalCommandSets.length; i++) {
		ifBlock = { condition: this.conditionalCommandSets[i].condition.toString(),
					body: parseBody(this.conditionalCommandSets[i].commands)};
		ifBlocks.push(ifBlock);
	}

	var parsedCommand = {command: 'If',
						ifBlocks: ifBlocks};
   	
    if (this.elseCommands) {
        parsedCommand.elseBlock = parseBody(this.elseBody);
    }

    return parsedCommand;
}



function While(condition, body, block) {
	this.condition = condition;
	this.body = body;
	this.block = block;
}

While.prototype.execute = function(thread, level) {
	this.block.selectWithConnected();
	thread.currentAction = ocargo.EMPTY_ACTION;

	if (this.condition(level,thread.id)) {
		thread.addNewStackLevel([this]);
		thread.addNewStackLevel(this.body.slice());
	}
};

While.prototype.parse = function() {
    return {command: 'While',
			condition: this.condition.toString(),
			body: parseBody(this.body)};
}


function Procedure(name,body,block) {
	this.name = name;
	this.body = body;
	this.block = block;
};

Procedure.prototype.execute = function(thread) {
	this.block.selectWithConnected();
	thread.currentAction = ocargo.EMPTY_ACTION;

	thread.addNewStackLevel(this.body.slice());
}

Procedure.prototype.parse = function() {
	return {command: "Procedure",
			name: this.name,
			body: parseBody(this.body)};
}



function ProcedureCall(block) {
	this.block = block;
};

ProcedureCall.prototype.bind = function(proc) {
	this.proc = proc;
}

ProcedureCall.prototype.execute = function(thread) {
	this.block.selectWithConnected();
	thread.currentAction = ocargo.EMPTY_ACTION;

	thread.addNewStackLevel([this.proc]);
}

ProcedureCall.prototype.parse = function() {
	return {command: "ProcedureCall",
			name: this.proc.name};
}



function parseBody(body) {
	var parses = [];
	for (var i = 0; i < body.length; i++) {
		parses.push(body[i].parse())
	}
	return parses;
}