'use strict';

var ocargo = ocargo || {};

ocargo.BlocklyCompiler = function() {}

ocargo.BlocklyCompiler.prototype.procedureBindings = null;
ocargo.BlocklyCompiler.prototype.procedures = null;
ocargo.BlocklyCompiler.prototype.program = null;


ocargo.BlocklyCompiler.prototype.compile = function() 
{
    this.compileProcedures();
    this.compileProgram();
    this.bindProcedureCalls();

    return this.program;
};

ocargo.BlocklyCompiler.prototype.compileProcedures = function() {
    this.procedures = {};
    this.procedureBindings = [];

    var topBlocks = Blockly.mainWorkspace.getTopBlocks();
    for (var i = 0; i < topBlocks.length; i++)
    {
        var block = topBlocks[i];
        if(topBlocks[i].type === 'declare_proc') {
            var nameBlock = block.inputList[0].connection.targetBlock();
            if(nameBlock == null) {
                throw ocargo.messages.procMissingNameError;
            }
            var name = nameBlock.inputList[0].fieldRow[1].text_;
            if (name === "") {
                throw ocargo.messages.procMissingNameError;
            }

            var bodyBlock = block.inputList[1].connection.targetBlock();

            if (!(name in this.procedures)) {
                this.procedures[name] = new Procedure(name, this.createSequence(bodyBlock),block)
            }
            else {
                throw ocargo.messages.procDupNameError;
            }
        }
    }
}

ocargo.BlocklyCompiler.prototype.compileProgram = function() {
    this.program = new ocargo.Program();
    var startBlocks = ocargo.blocklyControl.getStartBlocks();
    for(var i = 0; i < THREADS; i++) {
        var thread = new ocargo.Thread(i);
        thread.startBlock = startBlocks[i];
        thread.stack.push(this.createSequence(thread.startBlock));
        this.program.threads.push(thread);
    }
}

ocargo.BlocklyCompiler.prototype.bindProcedureCalls = function() {
    this.program.procedures = this.procedures;
    for (var i = 0; i < this.procedureBindings.length; i++) {
        var name = this.procedureBindings[i].name;
        var call = this.procedureBindings[i].call;

        if (name in this.procedures) {
            call.bind(this.procedures[name]);
        } else {
            throw ocargo.messages.procCallNameError;
        }
    }
}

/** Instructions **/

ocargo.BlocklyCompiler.prototype.createProcedureCall = function(block) {
    var nameBlock = block.inputList[0].connection.targetBlock();
    if(nameBlock == null) {
        throw ocargo.messages.procMissingNameError;
    }
    var name = nameBlock.inputList[0].fieldRow[1].text_;
    if (name === "") {
        throw ocargo.messages.procCallNameError;
    }

    var procCall = new ProcedureCall(block);
    this.procedureBindings.push({call:procCall,name:name});
    return procCall;
}

ocargo.BlocklyCompiler.prototype.createWhile = function(block) {
    var bodyBlock = block.inputList[1].connection.targetBlock();
    if (bodyBlock === null) {
        throw ocargo.messages.whileBodyError;
    }
	return new While(
		this.counterCondition(parseInt(block.inputList[0].fieldRow[1].text_)),
		this.createSequence(bodyBlock),
		block);
}

ocargo.BlocklyCompiler.prototype.createWhileUntil = function(block) {
    var conditionBlock = block.inputList[0].connection.targetBlock();
    if (conditionBlock === null) {
        throw ocargo.messages.whileConditionError;
    }
	var condition = this.getCondition(conditionBlock);
	if (block.inputList[0].fieldRow[1].value_ == 'UNTIL') {
		condition = this.negateCondition(condition);
	}

    var bodyBlock = block.inputList[1].connection.targetBlock();
    if (bodyBlock === null) {
        throw ocargo.messages.whileBodyError;
    }
	return new While(condition,	this.createSequence(bodyBlock), block);
}

ocargo.BlocklyCompiler.prototype.getCondition = function(conditionBlock) {
	if (conditionBlock.type === 'road_exists') {
		var selection = conditionBlock.inputList[0].fieldRow[1].value_;
		return this.roadCondition(selection);
	} else if (conditionBlock.type === 'dead_end') {
		return this.deadEndCondition();
    } else if (conditionBlock.type === 'at_destination') {
    	return this.atDestinationCondition();
    } else if (conditionBlock.type === 'logic_negate') {
    	return this.negateCondition(this.getCondition(conditionBlock.inputList[0].connection.targetBlock()));
    } else if (conditionBlock.type === 'traffic_light') {
    	return this.trafficLightCondition(conditionBlock.inputList[0].fieldRow[1].value_);
    }
}

ocargo.BlocklyCompiler.prototype.createIf = function(block) {
	var conditionalCommandSets = [];

    var elseCount = block.elseCount_ || 0;
	var i = 0;
	while (i < block.inputList.length - elseCount) {
		var input = block.inputList[i];
		var condition;

		if (input.name.indexOf('IF') === 0) {
            var conditionBlock = input.connection.targetBlock();
            if (conditionBlock === null) {
                throw ocargo.messages.ifConditionError;
            }
			condition = this.getCondition(conditionBlock);
		} else if (input.name.indexOf('DO') === 0) {
			var conditionalCommandSet = {};
			conditionalCommandSet.condition = condition;
			conditionalCommandSet.commands = this.createSequence(input.connection.targetBlock());
			conditionalCommandSets.push(conditionalCommandSet);
		}

		i++;
	}

	if (elseCount === 1) {
		var elseBody = this.createSequence(block.inputList[block.inputList.length - 1].connection.targetBlock());
	}

	return new If(conditionalCommandSets, elseBody, block);
}

ocargo.BlocklyCompiler.prototype.createSequence = function(block){
	var commands = [];

	while (block) {
		if (block.type === 'move_forwards') {
			commands.push(new ForwardCommand(block));
        } else if (block.type === 'turn_left') {
        	commands.push(new TurnLeftCommand(block));
        } else if (block.type === 'turn_right') {
            commands.push(new TurnRightCommand(block));
        } else if (block.type === 'turn_around') {
            commands.push(new TurnAroundCommand(block));
        } else if (block.type === 'wait') {
            commands.push(new WaitCommand(block));
        } else if (block.type === 'controls_repeat') {
        	commands.push(this.createWhile(block));
        } else if (block.type === 'controls_whileUntil') {
        	commands.push(this.createWhileUntil(block));
        } else if (block.type === 'controls_if') {
        	commands.push(this.createIf(block));            
        } else if (block.type === 'call_proc') {
            commands.push(this.createProcedureCall(block));
        }

		block = block.nextConnection.targetBlock();
	}

    return commands;
}

/** Conditions **/

ocargo.BlocklyCompiler.prototype.trafficLightCondition = function(lightColour) {
    return function(model) {
        if (lightColour === ocargo.TrafficLight.RED) {
            return model.isTrafficLightRed();
        }
        else if (lightColour === ocargo.TrafficLight.GREEN) {
            return model.isTrafficLightGreen();
        }
    };
}

ocargo.BlocklyCompiler.prototype.roadCondition = function(selection) {
    return function(model) {
        if (selection === 'FORWARD') {
            return model.isRoadForward();
        } else if (selection === 'LEFT') {
            return model.isRoadLeft();
        } else if (selection === 'RIGHT') {
            return model.isRoadRight();
        }
    };
}

ocargo.BlocklyCompiler.prototype.deadEndCondition = function() {
    return function(model) {
        return model.isDeadEnd();
    };
}

ocargo.BlocklyCompiler.prototype.negateCondition = function(otherCondition) {
    return function(model) {
        return !otherCondition(model);
    };
}

ocargo.BlocklyCompiler.prototype.atDestinationCondition = function() {
    return function(model) {
        return model.isAtDestination();
    };
}

ocargo.BlocklyCompiler.prototype.counterCondition = function(count) {
    var startCount = count;
    return function(model) {
        if (count > 0) {
            count--;
            return true;
        }
        // Resets the counter for nested loops
        count = startCount;
        return false;
    };
}