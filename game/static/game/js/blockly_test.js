'use strict';

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

Blockly.Blocks['turn_van'] = {
  // Block for turning left or right.
  init: function() {
    var DIRECTIONS =
        [['Turn left', 'moveLeft'],
         ['Turn right', 'moveRight']];
    // Append arrows to direction messages.
    DIRECTIONS[0][0] += ' \u21BB';
    DIRECTIONS[1][0] += ' \u21BA';
    this.setColour(160);
    this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown(DIRECTIONS), 'DIR');
    this.setPreviousStatement(true);
    this.setNextStatement(true);
    this.setTooltip('Turn the van');
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
    var command = BlocklyTest.queue.shift();
    if (!command) {
        return;
    }
    switch (command) {
        case 'F':
            moveForward(BlocklyTest.animate);
            break;

        case 'L':
            moveLeft(BlocklyTest.animate);
            break;

        case 'R':
            moveRight(BlocklyTest.animate);
            break;
    } 
};


BlocklyTest.moveForward = function() {
    BlocklyTest.queue.push('F');
};

BlocklyTest.moveLeft = function() {
    BlocklyTest.queue.push('L');
};

BlocklyTest.moveRight = function() {
    BlocklyTest.queue.push('R');
};
