/*
Code for Life

Copyright (C) 2015, Ocado Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
'use strict';

var ocargo = ocargo || {};

var MAX_EXECUTION_STEPS = 10000;

var shouldHighlight = true;

/* Program */

ocargo.Program = function(events) {
	this.threads = [];
	this.procedures = {};
	this.events = events;
};

ocargo.Program.prototype.run = function() {
	ocargo.model.chooseNewCowPositions();
	for (var i = 0; i < this.threads.length; i++) {
		ocargo.model.reset(i);
		this.threads[i].run(ocargo.model);
	}
};

/* Thread */

ocargo.Thread = function(i, program) {
	this.stack = [];
	this.noExecutionSteps = 0;
	this.program = program;
	this.eventsEnabled = true;
	this.eventLevel = Event.MAX_LEVEL; // no event active
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

	var activeEvent = null;

	// check if any event condition is true
	for (var i=0; i<this.program.events.length; i++) {
		var event = this.program.events[i];
		model.shouldObserve = false;
		if (event.condition(model)) {
			if (!activeEvent || event.level() < activeEvent.level()) {
				activeEvent = event;
			}
		}
		model.shouldObserve = true;
	}

	// only execute the event if it raises the event level
	if (activeEvent && this.eventLevel > activeEvent.level()) {
		// tell the event about the old event level
		activeEvent.setOldLevel(this.eventLevel);
		// add event handler to stack (looping)
		activeEvent.execute(this, model);
	}

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



function Event(condition,body,block,conditionType) {
	this.condition = condition;
	this.body = body;
	this.block = block;
	//this.conditionType = conditionType;
	//this.oldLevel = null;
};

Event.prototype.execute = function(thread, model) {
    if (this.condition(model)) {
		// raise event level to our level
		thread.eventLevel = this.level();

        // loop within the event handler as long as condition is true
        thread.addNewStackLevel([this]);
        thread.addNewStackLevel(this.body.slice());
    } else {
		// lower event level to prior value
		thread.eventLevel = this.oldLevel;
    }
	return true;
};

Event.prototype.setOldLevel = function(oldLevel) {
	this.oldLevel = oldLevel;
};

Event.MAX_LEVEL = 1000; // level at which no event is active

Event.prototype.level = function() {
	if (this.conditionType === 'road_exists') {
		return 31;
	} else if (this.conditionType === 'dead_end') {
		return 30;
	} else if (this.conditionType === 'at_destination') {
		return 20;
	} else if (this.conditionType === 'traffic_light') {
		return 11;
	} else if (this.conditionType === 'cow_crossing') {
		return 10;
	} else {
		return 100;
	}
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
		functionType: 'highlight',
		functionCall: makeHighLightCallable(block.id),
		description: 'Blockly highlight: ' + block.type,
		blockId: block.id
	});
}

function queueHighlightIncorrect(block){
	ocargo.animation.appendAnimation({
		type: 'callable',
		functionType: 'highlightIncorrect',
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
