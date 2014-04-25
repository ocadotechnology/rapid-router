'use strict';

var ocargo = ocargo || {};

Blockly.Blocks['start'] = {
    // Beginning block - identifies the start of the program
    init: function() {
        this.setColour(50);
        this.appendDummyInput()
            .appendField('Start');
        this.setNextStatement(true);
        this.setTooltip('The beginning of the program');
        this.setDeletable(false);
    }
};

Blockly.Blocks['move_van'] = {
  // Block for moving forward
  init: function() {
    this.setColour(160);
    this.appendDummyInput()
        .appendField('\u2191');
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('Move the van forwards');
  }
};

Blockly.JavaScript['move_van'] = function(block) {
    // Generate JavaScript for moving forward
    return 'BlocklyTest.moveForward();\n';
};

Blockly.Blocks['turn_left'] = {
  // Block for turning left or right.
  init: function() {
    this.setColour(160);
    this.appendDummyInput()
        .appendField('\u21BA');
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('Turn the van left');
  }
};

Blockly.Blocks['turn_right'] = {
    // Block for turning left or right.
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('\u21BB');
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Turn the van right');
    }
};

Blockly.JavaScript['turn_van'] = function(block) {
    // Generate JavaScript for turning left or right.
    return 'BlocklyTest.' + block.getFieldValue('DIR') + '()\n';
};

var BlocklyTest = {};

BlocklyTest.init = function() {
    Blockly.inject(document.getElementById('blockly'),
        {path: '/static/game/js/blockly/', toolbox: document.getElementById('toolbox')});

    var startBlock = Blockly.Block.obtain(Blockly.mainWorkspace, 'start');
    startBlock.initSvg();
    startBlock.render();
} ;

window.addEventListener('load', BlocklyTest.init);

BlocklyTest.queue = [];

BlocklyTest.animate = function() {
    var instruction = BlocklyTest.queue.shift();
    if (!instruction) {
        return;
    }
    switch (instruction) {
        case FORWARD:
            moveForward(BlocklyTest.animate);
            break;

        case TURN_LEFT:
            moveLeft(BlocklyTest.animate);
            break;

        case TURN_RIGHT:
            moveRight(BlocklyTest.animate);
            break;
    } 
};

BlocklyTest.addInstruction = function(instruction) {
    BlocklyTest.queue.push(instruction);
};

BlocklyTest.moveForward = function() {
    BlocklyTest.addInstruction(FORWARD);
};

BlocklyTest.moveLeft = function() {
    BlocklyTest.addInstruction(TURN_LEFT);
};

BlocklyTest.moveRight = function() {
    BlocklyTest.addInstruction(TURN_RIGHT);
};

BlocklyTest.getStartBlock = function() {
    var startBlock = null;
    Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
        if (block.type == 'start') {
            startBlock = block;
        }
    });
    return startBlock;
};

BlocklyTest.populateProgram = function() {
	function getCommandsAtThisLevel(block){
    	var commands = [];
    	
    	while(block){
    		if (block.type == 'move_van') {
    			commands.push(FORWARD_COMMAND);
            } else if (block.type == 'turn_left') {
            	commands.push(TURN_LEFT_COMMAND);
            } else if (block.type == 'turn_right') {
            	commands.push(TURN_RIGHT_COMMAND);
            } else if (block.type == 'controls_repeat') {
            	commands.push(
            			new While(
            					counterCondition(block.inputList[0].fieldRow[1].text_), 
            					getCommandsAtThisLevel(block.inputList[1].connection.targetBlock())));
            }
    		
    		block = block.nextConnection.targetBlock();
    	}
    	
    	return commands;
    }
	
    var program = new ocargo.Program();
    var startBlock = this.getStartBlock();
    program.stack.push(getCommandsAtThisLevel(startBlock));
    return program;
};
