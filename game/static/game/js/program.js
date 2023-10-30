"use strict";

var ocargo = ocargo || {};

var MAX_EXECUTION_STEPS = 10000;

/* Program */

ocargo.Program = function (events) {
  this.thread = null;
  this.procedures = {};
  this.events = events;
  this.variables = {};
};

ocargo.Program.prototype.run = function() {
	ocargo.model.reset();
	this.thread.run(ocargo.model);
};

/* Thread */

ocargo.Thread = function (program) {
  this.stack = []; //each element is an array of commands attached to each start block (currently we only have one start block)
  this.noExecutionSteps = 0;
  this.program = program;
  this.eventLevel = Event.MAX_LEVEL; // no event active
};

ocargo.Thread.prototype.run = function (model) {
  let failed = false;
  while (!failed && this.canStep()) {
    failed = !this.step(model);
  }
  if (!failed) {
    model.programExecutionEnded();
  }
};

ocargo.Thread.prototype.step = function(model) {

  let commandToProcess = this.stack.shift();
  this.noExecutionSteps++;

  if (this.noExecutionSteps > MAX_EXECUTION_STEPS) {
    ocargo.game.sendAttempt(0);
    // alert user to likely infinite loop
    ocargo.animation.appendAnimation({
      type: "popup",
      popupType: "FAIL",
      failSubtype: "QUERY_INFINITE_LOOP",
      popupMessage: gettext(
        "It looks as though your program's been running a while. Check your repeat loops are okay."
      ),
      popupHint: ocargo.game.registerFailure(),
      description: "failure popup",
    });
    return false;
  }

  let successful = true;
  if (commandToProcess) {
    successful = commandToProcess.execute(this, model);
  }

  if (!successful) {
    // Program crashed, queue a block highlight event
    let block = commandToProcess.block;
    queueHighlightIncorrect(model, block);
    return false;
  }

  return true;
};

ocargo.Thread.prototype.canStep = function () {
  return this.stack.length !== 0;
};

ocargo.Thread.prototype.pushToStack = function (commands) {
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

TurnLeftCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  return model.turnLeft();
};

function TurnRightCommand(block) {
  this.block = block;
}

TurnRightCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  return model.turnRight();
};

function ForwardCommand(block) {
  this.block = block;
}

ForwardCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  return model.moveForwards();
};

function TurnAroundCommand(block) {
  this.block = block;
}

TurnAroundCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  return model.turnAround();
};

function WaitCommand(block) {
  this.block = block;
}

WaitCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  return model.wait();
};

function DeliverCommand(block) {
  this.block = block;
}

DeliverCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  return model.deliver();
};

function SoundHornCommand(block) {
  this.block = block;
}

SoundHornCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block, true);
  return model.sound_horn();
};

function SetVariableCommand(block, name, valueFunction) {
  this.block = block;
  this.name = name;
  this.valueFunction = valueFunction;
}

SetVariableCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  thread.program.variables[this.name] = this.valueFunction();
  return model.wait(); // TODO - need to change this if we don't want it to use fuel
};

function IncrementVariableCommand(block, name, incrValue) {
  this.block = block;
  this.name = name;
  this.incrValue = incrValue;
}

IncrementVariableCommand.prototype.execute = function (thread, model) {
  queueHighlight(model, this.block);
  thread.program.variables[this.name] += this.incrValue;
  return model.wait(); // TODO - need to change this if we don't want it to use fuel
};

function If(conditionalCommandSets, elseBody, block) {
  this.conditionalCommandSets = conditionalCommandSets;
  this.elseBody = elseBody;
  this.block = block;
}

If.prototype.execute = function (thread, model) {
  var i = 0;
  while (i < this.conditionalCommandSets.length) {
    if (this.conditionalCommandSets[i].condition(model)) {
      thread.pushToStack(this.conditionalCommandSets[i].commands.slice());
      return true;
    }

    i++;
  }

  if (this.elseBody) {
    thread.pushToStack(this.elseBody.slice());
  }
  return true;
};

function While(condition, body, block) {
  this.condition = condition;
  this.body = body;
  this.block = block;
}

While.prototype.execute = function (thread, model) {
  if (this.condition(model)) {
    thread.pushToStack([this]);
    thread.pushToStack(this.body.slice());
  }
  return true;
};

function Event(condition, body, block, conditionType) {
  this.condition = condition;
  this.body = body;
  this.block = block;
}

Event.prototype.execute = function (thread, model) {
  thread.pushToStack(this.body.slice());

  return true;
};

function Procedure(name, body, block) {
  this.name = name;
  this.body = body;
  this.block = block;
}

Procedure.prototype.execute = function (thread) {
  thread.pushToStack(this.body.slice());
  return true;
};

function ProcedureCall(block) {
  this.block = block;
}

ProcedureCall.prototype.bind = function (proc) {
  this.proc = proc;
};

ProcedureCall.prototype.execute = function (thread) {
  thread.pushToStack([this.proc]);
  return true;
};

/* Highlighting of blocks */

function queueHighlight(model, block, keepHighlighting) {
  if (model.shouldObserve) {
    ocargo.animation.appendAnimation({
      type: "callable",
      functionType: "highlight",
      functionCall: makeHighLightCallable(block.id, keepHighlighting),
      description: "Blockly highlight: " + block.type,
      blockId: block.id,
    });
  }
}

function queueHighlightIncorrect(model, block) {
  if (model.shouldObserve) {
    ocargo.animation.appendAnimation({
      type: "callable",
      functionType: "highlightIncorrect",
      functionCall: makeHighLightIncorrectCallable(block.id),
      description: "Blockly highlight incorrect: " + block.type,
      blockId: block.id,
    });
  }
}

function makeHighLightCallable(id, keepHighlighting) {
  return function () {
    ocargo.blocklyControl.clearAllSelections();
    var block = Blockly.mainWorkspace.getBlockById(id);
    block.keepHighlighting = keepHighlighting;
    ocargo.blocklyControl.setBlockSelected(block, true);
  };
}

function makeHighLightIncorrectCallable(id) {
  return function () {
    ocargo.blocklyControl.highlightIncorrectBlock(
      Blockly.mainWorkspace.getBlockById(id)
    );
  };
}
