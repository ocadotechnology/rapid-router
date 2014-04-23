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
        .appendField('Move forward');
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
        .appendField('Turn left \u21BA');
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
            .appendField('Turn right \u21BB');
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

BlocklyTest.execute = function() {
    BlocklyTest.queue = [];

    var code = Blockly.JavaScript.workspaceToCode();
    try {
        eval(code);
    } catch (e) {
        // Null is thrown for infinite loop.
        // Otherwise, abnormal termination is a user error.
        if (e !== Infinity) {
            alert(e);
        }
    }
  
    resetVan();
    window.setTimeout(BlocklyTest.animate, 100);  
};

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
    var program = new ocargo.Program();
    program.stack.push([]);//TODO: take out 0 depth stack hack once we can cope with loops etc.
    var startBlock = this.getStartBlock();

    function populateBlock(program, block) {
        if (!block) {
            return;
        }
        if (block.type == 'move_van') {
            program.stack[0].push(FORWARD_COMMAND);
        } else if (block.type == 'turn_left') {
            program.stack[0].push(TURN_LEFT_COMMAND);
        } else if (block.type == 'turn_right') {
            program.stack[0].push(TURN_RIGHT_COMMAND);
        }

        if (block.nextConnection) {
            populateBlock(program, block.nextConnection.targetBlock());
        }
    }

    if (startBlock) {
        if (startBlock.nextConnection) {
            populateBlock(program, startBlock.nextConnection.targetBlock());
        }
    }
    return program;
}
