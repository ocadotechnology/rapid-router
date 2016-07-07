/*
Code for Life

Copyright (C) 2016, Ocado Innovation Limited

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

/* Program */

ocargo.Program = function(events) {
	this.thread = null;
	this.procedures = {};
	this.events = events;
};

ocargo.Program.prototype.run = function() {
	ocargo.model.chooseNewCowPositions();
	ocargo.model.reset();
	this.thread.run(ocargo.model);
};

/* Thread */

ocargo.Thread = function(program) {
	this.stack = []; //each element is an array of commands attached to each start block (currently we only have one start block)
	this.noExecutionSteps = 0;
	this.program = program;
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
	// check if any event condition is true
	for (var i=0; i<this.program.events.length; i++) {
		var event = this.program.events[i];
		model.shouldObserve = false;
		if (event.condition(model)) {
			event.execute(this, model);
		}
		model.shouldObserve = true;
	}

	var commandToProcess = this.stack.shift();
	this.noExecutionSteps ++;
	if (this.noExecutionSteps > MAX_EXECUTION_STEPS) {
		// alert user to likely infinite loop
		ocargo.animation.appendAnimation({
            type: 'popup',
            popupType: 'FAIL',
            failSubtype: 'QUERY_INFINITE_LOOP',
            popupMessage: gettext('It looks as though your program\'s been running a while. Check your repeat loops are okay.'),
            popupHint: ocargo.game.registerFailure(),
            description: 'failure popup'
        });
		return false;
	}

	var successful = true;
	if (commandToProcess) {
		successful = commandToProcess.execute(this, model);
	}

	if (!successful) {
		// Program crashed, queue a block highlight event
        var block = commandToProcess.block;
		queueHighlightIncorrect(model, block);
		return false;
	}

	return true;
};

ocargo.Thread.prototype.canStep = function() {
	return this.stack.length !== 0;
};

ocargo.Thread.prototype.pushToStack = function(commands) {
    this.stack.unshift.apply(this.stack, commands);
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

function SoundHornCommand(block){
	this.block = block;
}

SoundHornCommand.prototype.execute = function(thread, model){
	queueHighlight(model, this.block, true);
	return model.sound_horn();
};

function PuffUpCommand(block){
	this.block = block;
}

PuffUpCommand.prototype.execute = function(thread, model){
	queueHighlight(model, this.block, true);
	return model.puff_up();
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
			thread.pushToStack(this.conditionalCommandSets[i].commands.slice());
			return true;
		}

		i++;
	}

	if(this.elseBody) {
		thread.pushToStack(this.elseBody.slice());
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
		thread.pushToStack([this]);
		thread.pushToStack(this.body.slice());
	}
	return true;
};



function Event(condition,body,block,conditionType) {
	this.condition = condition;
	this.body = body;
	this.block = block;
}

Event.prototype.execute = function(thread, model) {
	thread.pushToStack(this.body.slice());

	return true;
};

function Procedure(name,body,block) {
	this.name = name;
	this.body = body;
	this.block = block;
}

Procedure.prototype.execute = function(thread) {
	thread.pushToStack(this.body.slice());
	return true;
};

function ProcedureCall(block) {
	this.block = block;
}

ProcedureCall.prototype.bind = function(proc) {
	this.proc = proc;
};

ProcedureCall.prototype.execute = function(thread) {
	thread.pushToStack([this.proc]);
	return true;
};



/* Highlighting of blocks */

function queueHighlight(model, block, keepHighlighting) {
    if (model.shouldObserve) {
        ocargo.animation.appendAnimation({
            type: 'callable',
	    functionType: 'highlight',
	    functionCall: makeHighLightCallable(block.id, keepHighlighting),
	    description: 'Blockly highlight: ' + block.type,
	    blockId: block.id
        });

	}
}

function queueHighlightIncorrect(model, block){
    if (model.shouldObserve){
		ocargo.animation.appendAnimation({
			type: 'callable',
			functionType: 'highlightIncorrect',
			functionCall: makeHighLightIncorrectCallable(block.id),
			description: 'Blockly highlight incorrect: ' + block.type,
			blockId: block.id
		});
	}
}

function makeHighLightCallable(id, keepHighlighting) {
	return function() {
		ocargo.blocklyControl.clearAllSelections();
		var block = Blockly.Block.getById(id, Blockly.mainWorkspace);
		block.keepHighlighting = keepHighlighting;
		ocargo.blocklyControl.setBlockSelected(block, true);

	};
}

function makeHighLightIncorrectCallable(id){
	return function() {
		ocargo.blocklyControl.highlightIncorrectBlock(Blockly.Block.getById(id, Blockly.mainWorkspace));
	}
}
