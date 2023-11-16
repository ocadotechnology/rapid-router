"use strict";

var ocargo = ocargo || {};

ocargo.BlocklyCompiler = function () {};

ocargo.BlocklyCompiler.prototype.procedureBindings = null;
ocargo.BlocklyCompiler.prototype.procedures = null;
ocargo.BlocklyCompiler.prototype.events = null;
ocargo.BlocklyCompiler.prototype.program = null;

ocargo.BlocklyCompiler.prototype.compile = function () {
    this.compileProcedures();
    this.compileEvents();
    this.compileProgram();
    this.bindProcedureCalls();

  return this.program;
};

ocargo.BlocklyCompiler.prototype.compileProcedures = function () {
  this.procedures = {};
  this.procedureBindings = [];

  var procBlocks = ocargo.blocklyControl.procedureBlocks();
  for (var i = 0; i < procBlocks.length; i++) {
    var block = procBlocks[i];
    var name = block.inputList[0].fieldRow[1].text_;
    if (name === "") {
      throw gettext_noop("Perhaps try looking at your 'define' blocks?");
    }

    var bodyBlock = block.inputList[1].connection.targetBlock();
    if (bodyBlock === null) {
      throw gettext_noop("Perhaps try looking at your 'define' blocks?");
    }

    if (!(name in this.procedures)) {
      this.procedures[name] = new Procedure(
        name,
        this.createSequence(bodyBlock),
        block
      );
    } else {
      throw gettext_noop(
        "Perhaps try checking the names of your 'define' blocks?"
      );
    }
  }
};

ocargo.BlocklyCompiler.prototype.compileEvents = function() {
    var newEvents = [];

    var eventBlocks = ocargo.blocklyControl.onEventDoBlocks();
    for (var i = 0; i < eventBlocks.length; i++) {
        var block = eventBlocks[i];
        var condition = this.getCondition(block);

        var bodyBlock = block.inputList[1].connection.targetBlock();
        if (bodyBlock === null) {
            throw gettext_noop('Perhaps try looking at your \'event\' blocks?');
        }

        var conditionType = block.type;

        newEvents.push(new Event(condition, this.createSequence(bodyBlock), block, conditionType));
    }

    this.events = newEvents;
};

ocargo.BlocklyCompiler.prototype.compileProgram = function() {
    this.program = new ocargo.Program(this.events);
    var startBlock = ocargo.blocklyControl.startBlock();
    var thread = new ocargo.Thread(this.program);
    thread.startBlock = startBlock;
    thread.stack = this.createSequence(thread.startBlock);
    this.program.thread = thread;
};

ocargo.BlocklyCompiler.prototype.bindProcedureCalls = function () {
  this.program.procedures = this.procedures;
  for (var i = 0; i < this.procedureBindings.length; i++) {
    var name = this.procedureBindings[i].name;
    var call = this.procedureBindings[i].call;

    if (name in this.procedures) {
      call.bind(this.procedures[name]);
    } else {
      throw gettext_noop(
        "Perhaps try checking the names in your 'call' blocks?"
      );
    }
  }
};

/** Instructions **/

// New completely custom repeat until and repeat while blocks

ocargo.BlocklyCompiler.prototype.createRepeatUntil = function (block) {
  var conditionBlock = block.inputList[0].connection.targetBlock();
  if (conditionBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  var condition = this.getCondition(conditionBlock);
  // negate condition for repeat until
  condition = this.negateCondition(condition);

  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(condition, this.createSequence(bodyBlock), block);
};

ocargo.BlocklyCompiler.prototype.createRepeatWhile = function (block) {
  var conditionBlock = block.inputList[0].connection.targetBlock();
  if (conditionBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  var condition = this.getCondition(conditionBlock);

  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(condition, this.createSequence(bodyBlock), block);
};

ocargo.BlocklyCompiler.prototype.createProcedureCall = function (block) {
  var name = block.inputList[0].fieldRow[2].text_;
  if (name === "") {
    throw gettext_noop("Perhaps try checking the names in your 'call' blocks?");
  }

  var procCall = new ProcedureCall(block);
  this.procedureBindings.push({ call: procCall, name: name });
  return procCall;
};

ocargo.BlocklyCompiler.prototype.createVariable = function (block) {
  var variableName = block.inputList[0].fieldRow[1].text_;
  if (variableName === "") {
    throw gettext_noop(
      "Perhaps try checking the names in your 'set variable' blocks?"
    );
  }

  var self = this;
  var variableValueFunction = function () {
    return self.getValue(block.inputList[0].connection.targetBlock());
  };

  return new SetVariableCommand(block, variableName, variableValueFunction);
};

ocargo.BlocklyCompiler.prototype.createVariableNumeric = function (block) {
  var variableName = block.inputList[0].fieldRow[1].text_;
  if (variableName === "") {
    throw gettext_noop(
      "Perhaps try checking the names in your 'set variable' blocks?"
    );
  }

  var variableValueFunction = function () {
    var variableValue = parseInt(block.getFieldValue("VALUE"));
    if (variableValue === "") {
      throw gettext_noop(
        "Perhaps try checking the values in your 'set variable' blocks?"
      );
    }
    return variableValue;
  };

  return new SetVariableCommand(block, variableName, variableValueFunction);
};

ocargo.BlocklyCompiler.prototype.incrementVariable = function (block) {
  var variableName = block.inputList[0].fieldRow[1].text_;
  if (variableName === "") {
    throw gettext_noop(
      "Perhaps try checking the names in your 'increment variable' blocks?"
    );
  }

  var variableIncrValue = parseInt(block.getFieldValue("VALUE"));
  if (variableIncrValue === "") {
    throw gettext_noop(
      "Perhaps try checking the values in your 'increment variable' blocks?"
    );
  }

  return new IncrementVariableCommand(block, variableName, variableIncrValue);
};

ocargo.BlocklyCompiler.prototype.createRepeat = function (block) {
  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(
    this.counterCondition(
      block,
      parseInt(block.inputList[0].fieldRow[1].text_)
    ),
    this.createSequence(bodyBlock),
    block
  );
};

ocargo.BlocklyCompiler.prototype.createWhileUntil = function (block) {
  var conditionBlock = block.inputList[0].connection.targetBlock();
  if (conditionBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  var condition = this.getCondition(conditionBlock);
  if (block.inputList[0].fieldRow[1].value_ == "UNTIL") {
    condition = this.negateCondition(condition);
  }

  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(condition, this.createSequence(bodyBlock), block);
};

ocargo.BlocklyCompiler.prototype.getCondition = function (conditionBlock) {
  if (conditionBlock.type === "road_exists") {
    var selection = conditionBlock.inputList[0].fieldRow[1].value_;
    return this.roadCondition(conditionBlock, selection);
  } else if (conditionBlock.type === "dead_end") {
    return this.deadEndCondition(conditionBlock);
  } else if (conditionBlock.type === "at_destination") {
    return this.atDestinationCondition(conditionBlock);
  } else if (conditionBlock.type === "logic_negate") {
    return this.negateCondition(
      this.getCondition(conditionBlock.inputList[0].connection.targetBlock())
    );
  } else if (conditionBlock.type === "traffic_light") {
    return this.trafficLightCondition(conditionBlock);
  } else if (conditionBlock.type === "cow_crossing") {
    return this.cowCrossingCondition(conditionBlock);
  } else if (conditionBlock.type === "logic_compare") {
    return this.logicCompareCondition(conditionBlock);
  }
};

ocargo.BlocklyCompiler.prototype.getValue = function (block) {
  if (block.type === "variables_get") {
    var variableName = block.inputList[0].fieldRow[0].text_;
    return parseInt(this.program.variables[variableName]);
  } else if (block.type === "math_number") {
    return parseInt(block.getFieldValue("NUM"));
  } else if (block.type === "math_arithmetic") {
    var leftBlock = block.inputList[0].connection.targetBlock();
    var rightBlock = block.inputList[1].connection.targetBlock();
    if (leftBlock === null || rightBlock === null) {
      throw gettext_noop(
        "Perhaps try looking at your 'math arithmetic' blocks?"
      );
    }

    var operator = block.getFieldValue("OP");
    var leftValue = this.getValue(leftBlock);
    var rightValue = this.getValue(rightBlock);

    if (operator == "ADD") {
      return leftValue + rightValue;
    } else if (operator == "MINUS") {
      return leftValue - rightValue;
    } else if (operator == "MULTIPLY") {
      return leftValue * rightValue;
    } else if (operator == "DIVIDE") {
      return leftValue / rightValue;
    } else if (operator == "POWER") {
      return leftValue ** rightValue;
    }
  }
};

ocargo.BlocklyCompiler.prototype.createIf = function (block) {
  var conditionalCommandSets = [];

  var elseCount = block.elseCount_ || 0;
  var i = 0;
  while (i < block.inputList.length - elseCount) {
    var input = block.inputList[i];
    var condition;

    if (input.name.indexOf("IF") === 0) {
      var conditionBlock = input.connection.targetBlock();
      if (conditionBlock === null) {
        throw gettext_noop("Perhaps try looking at your 'if' blocks?");
      }
      condition = this.getCondition(conditionBlock);
    } else if (input.name.indexOf("DO") === 0) {
      var conditionalCommandSet = {};
      conditionalCommandSet.condition = condition;
      conditionalCommandSet.commands = this.createSequence(
        input.connection.targetBlock()
      );
      conditionalCommandSets.push(conditionalCommandSet);
    }

    i++;
  }

  if (elseCount === 1) {
    var elseBody = this.createSequence(
      block.inputList[block.inputList.length - 1].connection.targetBlock()
    );
  }

  return new If(conditionalCommandSets, elseBody, block);
};

ocargo.BlocklyCompiler.prototype.createSequence = function (block) {
  var commands = [];

  while (block) {
    if (block.type === "move_forwards") {
      commands.push(new ForwardCommand(block));
    } else if (block.type === "turn_left") {
      commands.push(new TurnLeftCommand(block));
    } else if (block.type === "turn_right") {
      commands.push(new TurnRightCommand(block));
    } else if (block.type === "turn_around") {
      commands.push(new TurnAroundCommand(block));
    } else if (block.type === "wait") {
      commands.push(new WaitCommand(block));
    } else if (block.type === "deliver") {
      commands.push(new DeliverCommand(block));
    } else if (block.type === "sound_horn") {
      commands.push(new SoundHornCommand(block));
    } else if (block.type === "controls_repeat_until") {
      commands.push(this.createRepeatUntil(block));
    } else if (block.type === "controls_repeat_while") {
      commands.push(this.createRepeatWhile(block));
    } else if (block.type === "controls_repeat") {
      commands.push(this.createRepeat(block));
    } else if (block.type === "controls_whileUntil") {
      commands.push(this.createWhileUntil(block));
    } else if (block.type === "controls_if") {
      commands.push(this.createIf(block));
    } else if (block.type === "call_proc") {
      commands.push(this.createProcedureCall(block));
    } else if (block.type === "variables_set") {
      commands.push(this.createVariable(block));
    } else if (block.type === "variables_numeric_set") {
      commands.push(this.createVariableNumeric(block));
    } else if (block.type === "variables_increment") {
      commands.push(this.incrementVariable(block));
    }

    block = block.nextConnection ? block.nextConnection.targetBlock() : null;
  }

  return commands;
};

ocargo.BlocklyCompiler.prototype.simplifyBlock = function (block) {
  return new Block(block.id, block.type);
};

/** Conditions **/

ocargo.BlocklyCompiler.prototype.trafficLightCondition = function (block) {
  var lightColour = block.getFieldValue("CHOICE");
  return function (model) {
    queueHighlight(model, block);
    if (lightColour === ocargo.TrafficLight.RED) {
      return model.isTrafficLightRed();
    } else if (lightColour === ocargo.TrafficLight.GREEN) {
      return model.isTrafficLightGreen();
    }
  };
};

ocargo.BlocklyCompiler.prototype.roadCondition = function (block, selection) {
  return function (model) {
    queueHighlight(model, block);
    if (selection === "FORWARD") {
      return model.isRoadForward();
    } else if (selection === "LEFT") {
      return model.isRoadLeft();
    } else if (selection === "RIGHT") {
      return model.isRoadRight();
    }
  };
};

ocargo.BlocklyCompiler.prototype.deadEndCondition = function (block) {
  return function (model) {
    queueHighlight(model, block);
    return model.isDeadEnd();
  };
};

ocargo.BlocklyCompiler.prototype.cowCrossingCondition = function (block) {
  return function (model) {
    queueHighlight(model, block);
    return model.isCowCrossing(block.getFieldValue("TYPE"));
  };
};

ocargo.BlocklyCompiler.prototype.negateCondition = function (otherCondition) {
  return function (model) {
    return !otherCondition(model);
  };
};

ocargo.BlocklyCompiler.prototype.atDestinationCondition = function (block) {
  return function (model) {
    queueHighlight(model, block);
    return model.isAtADestination();
  };
};

ocargo.BlocklyCompiler.prototype.counterCondition = function (block, count) {
  var startCount = count;
  return function (model) {
    queueHighlight(model, block);
    if (count > 0) {
      count--;
      return true;
    }
    // Resets the counter for nested loops
    count = startCount;
    return false;
  };
};

ocargo.BlocklyCompiler.prototype.logicCompareCondition = function (block) {
  // check left and right blocks
  var leftBlock = block.inputList[0].connection.targetBlock();
  var rightBlock = block.inputList[1].connection.targetBlock();
  if (leftBlock === null || rightBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'compare' blocks?");
  }

  var operator = block.getFieldValue("OP");
  var self = this;

  return function (model) {
    queueHighlight(model, block);

    // get values of left and right blocks - must be evaluated on each step because of variables
    var leftValue = self.getValue(leftBlock);
    var rightValue = self.getValue(rightBlock);

    if (operator == "EQ") {
      return leftValue === rightValue;
    } else if (operator == "NEQ") {
      return leftValue !== rightValue;
    } else if (operator == "LT") {
      return leftValue < rightValue;
    } else if (operator == "LTE") {
      return leftValue <= rightValue;
    } else if (operator == "GT") {
      return leftValue > rightValue;
    } else if (operator == "GTE") {
      return leftValue >= rightValue;
    }
  };
};

/** Mobile Code **/
/* Block types in the list passed in from mobile are converted to simplified Block objects
   id is assigned to each block in the order it appears in the array
 */
ocargo.BlocklyCompiler.prototype.mobileCompile = function (types) {
  var blocks = [];
  for (var i = 0; i < types.length; i++) {
    blocks.push(new Block(i + 1, types[i]));
  }

  this.program = new ocargo.Program([]);
  var thread = new ocargo.Thread(this.program);
  thread.stack = this.mobileCreateSequence(blocks);
  this.program.thread = thread;
  return this.program;
};

ocargo.BlocklyCompiler.prototype.mobileCreateSequence = function (blocks) {
  var commands = [];

  var block = blocks.shift();
  while (block) {
    if (block.type === "move_forwards") {
      commands.push(new ForwardCommand(block));
    } else if (block.type === "turn_left") {
      commands.push(new TurnLeftCommand(block));
    } else if (block.type === "turn_right") {
      commands.push(new TurnRightCommand(block));
    } else if (block.type === "turn_around") {
      commands.push(new TurnAroundCommand(block));
    } else if (block.type === "wait") {
      commands.push(new WaitCommand(block));
    } else if (block.type === "deliver") {
      commands.push(new DeliverCommand(block));
    }
    //} else if (block.type === 'controls_repeat_until') {
    //    commands.push(this.mobileCreateRepeatUntil(block));
    //} else if (block.type === 'controls_repeat_while') {
    //    commands.push(this.mobileCreateRepeatWhile(block));
    //} else if (block.type === 'controls_repeat') {
    //    commands.push(this.mobileCreateRepeat(block));
    //} else if (block.type === 'controls_whileUntil') {
    //    commands.push(this.mobileCreateWhileUntil(block));
    //} else if (block.type === 'controls_if') {
    //    commands.push(this.mobileCreateIf(block));
    //} else if (block.type === 'call_proc') {
    //    commands.push(this.mobileCreateProcedureCall(block));
    //}

    block = blocks.shift();
  }

  return commands;
};

/** Instructions **/

// New completely custom repeat until and repeat while blocks

ocargo.BlocklyCompiler.prototype.mobileCreateRepeatUntil = function (
  block,
  conditionBlock
) {
  var condition;
  if (
    conditionBlock === null ||
    (condition = this.mobileGetCondition(conditionBlock)) === null
  ) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }

  // negate condition for repeat until
  condition = this.negateCondition(condition);

  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(condition, this.createSequence(bodyBlock), block);
};

ocargo.BlocklyCompiler.prototype.mobileCreateRepeatWhile = function (block) {
  var conditionBlock = block.inputList[0].connection.targetBlock();
  if (conditionBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  var condition = this.getCondition(conditionBlock);

  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(condition, this.createSequence(bodyBlock), block);
};

ocargo.BlocklyCompiler.prototype.mobileCreateRepeat = function (block) {
  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(
    this.counterCondition(
      block,
      parseInt(block.inputList[0].fieldRow[1].text_)
    ),
    this.createSequence(bodyBlock),
    block
  );
};

ocargo.BlocklyCompiler.prototype.mobileCreateWhileUntil = function (block) {
  var conditionBlock = block.inputList[0].connection.targetBlock();
  if (conditionBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  var condition = this.getCondition(conditionBlock);
  if (block.inputList[0].fieldRow[1].value_ == "UNTIL") {
    condition = this.negateCondition(condition);
  }

  var bodyBlock = block.inputList[1].connection.targetBlock();
  if (bodyBlock === null) {
    throw gettext_noop("Perhaps try looking at your 'repeat' blocks?");
  }
  return new While(condition, this.createSequence(bodyBlock), block);
};

ocargo.BlocklyCompiler.prototype.mobileCreateIf = function (block) {
  var conditionalCommandSets = [];

  var elseCount = block.elseCount_ || 0;
  var i = 0;
  while (i < block.inputList.length - elseCount) {
    var input = block.inputList[i];
    var condition;

    if (input.name.indexOf("IF") === 0) {
      var conditionBlock = input.connection.targetBlock();
      if (conditionBlock === null) {
        throw gettext_noop("Perhaps try looking at your 'if' blocks?");
      }
      condition = this.getCondition(conditionBlock);
    } else if (input.name.indexOf("DO") === 0) {
      var conditionalCommandSet = {};
      conditionalCommandSet.condition = condition;
      conditionalCommandSet.commands = this.createSequence(
        input.connection.targetBlock()
      );
      conditionalCommandSets.push(conditionalCommandSet);
    }

    i++;
  }

  if (elseCount === 1) {
    var elseBody = this.createSequence(
      block.inputList[block.inputList.length - 1].connection.targetBlock()
    );
  }

  return new If(conditionalCommandSets, elseBody, block);
};

ocargo.BlocklyCompiler.prototype.mobileCreateProcedureCall = function (block) {
  var name = block.inputList[0].fieldRow[2].text_;
  if (name === "") {
    throw gettext_noop("Perhaps try checking the names in your 'call' blocks?");
  }

  var procCall = new ProcedureCall(block);
  this.procedureBindings.push({ call: procCall, name: name });
  return procCall;
};

ocargo.BlocklyCompiler.prototype.mobileGetCondition = function (
  conditionBlock
) {
  if (conditionBlock.type === "road_exists") {
    var selection = conditionBlock.inputList[0].fieldRow[1].value_;
    return this.roadCondition(conditionBlock, selection);
  } else if (conditionBlock.type === "dead_end") {
    return this.deadEndCondition(conditionBlock);
  } else if (conditionBlock.type === "at_destination") {
    return this.atDestinationCondition(conditionBlock);
  } else if (conditionBlock.type === "logic_negate") {
    return this.negateCondition(
      this.getCondition(conditionBlock.inputList[0].connection.targetBlock())
    );
  } else if (conditionBlock.type === "traffic_light") {
    return this.trafficLightCondition(conditionBlock);
  } else {
    return null;
  }
};

ocargo.BlocklyCompiler.prototype.workspaceToPython = function () {
  Blockly.Python.variableDB_.reset();

  var procBlocks = ocargo.blocklyControl.procedureBlocks();

  var code = "";

  for (var i = 0; i < procBlocks.length; i++) {
    code += "\n" + Blockly.Python.blockToCode(procBlocks[i]);
  }

  // TODO support events in python
  //var eventBlocks = ocargo.blocklyControl.onEventDoBlocks();
  //for (var i = 0; i < eventBlocks.length; i++) {
  //	code += '\n' + Blockly.Python.blockToCode(eventBlocks[i]);
  //}

  var startBlock = ocargo.blocklyControl.startBlock();
  code += "\n" + Blockly.Python.blockToCode(startBlock);

  return code;
};
