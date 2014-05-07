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

Blockly.Blocks['turn_left'] = {
    // Block for turning left
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
    // Block for turning right
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('\u21BB');
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Turn the van right');
    }
};

Blockly.Blocks['turn_around'] = {
    // Block for turning around
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('turn around');
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Turn the van around');
    }
};

Blockly.Blocks['road_exists'] = {
    init: function() {
        var BOOLEANS =
            [['road exists forward', 'FORWARD'],
             ['road exists left', 'LEFT'],
             ['road exists right', 'RIGHT']];
        this.setColour(210);
        this.setOutput(true, 'Boolean');
        this.appendDummyInput()
            .appendField(new Blockly.FieldDropdown(BOOLEANS), 'CHOICE');
    }
};

Blockly.Blocks['dead_end'] = {
    init: function() {
        this.setColour(210);
        this.setOutput(true, 'Boolean');
        this.appendDummyInput()
            .appendField('is dead end');
    }
};

Blockly.Blocks['at_destination'] = {
    init: function() {
        this.setColour(210);
        this.setOutput(true, 'Boolean');
        this.appendDummyInput()
            .appendField('is destination');
    }
};

var BlocklyTest = {};

BlocklyTest.createBlock = function(blockType) {
	var block = Blockly.Block.obtain(Blockly.mainWorkspace, blockType);
	block.initSvg();
	block.render();
    return block;
};

BlocklyTest.addBlockToEndOfProgram = function(typeOfBlockToAdd) {
	var blockToAdd = BlocklyTest.createBlock(typeOfBlockToAdd);
	
	var block = this.getStartBlock();
	while(block.nextConnection.targetBlock()){
		block = block.nextConnection.targetBlock();
	}
	
	block.nextConnection.connect(blockToAdd.previousConnection);
};

BlocklyTest.init = function() {
    var blockly = document.getElementById('blockly');
    var toolbox = document.getElementById('toolbox');
    Blockly.inject(blockly, {
        path: '/static/game/js/blockly/',
        toolbox: toolbox
    });

    BlocklyTest.reset();
};

BlocklyTest.reset = function() {
    var startBlock = BlocklyTest.getStartBlock();
    if (startBlock) {
        var nextBlock = startBlock.nextConnection.targetBlock();
        if (nextBlock) {
            nextBlock.dispose();
        }
    } else {
        BlocklyTest.createBlock('start');
    }
};

BlocklyTest.removeWrong = function() {
    var current = Blockly.selected;
    if (current) {
        var previous = current.previousConnection.targetBlock();
        current.dispose();
        previous.select();
    }
};

window.addEventListener('load', BlocklyTest.init);

BlocklyTest.getStartBlock = function() {
    var startBlock = null;
    Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
        if (block.type === 'start') {
            startBlock = block;
        }
    });
    return startBlock;
};

BlocklyTest.populateProgram = function() {
	function createWhile(block) {
		return new While(
			counterCondition(block.inputList[0].fieldRow[1].text_), 
			getCommandsAtThisLevel(block.inputList[1].connection.targetBlock()),
			block);
	}
	
	function createIf(block) {
		var conditionalCommandSets = [];
    	
    	var i = 0;
    	while(i < block.inputList.length - block.elseCount_){
    		var input = block.inputList[i];
    		var condition;

    		if(input.name.indexOf('IF') === 0) {
    			var conditionBlock = input.connection.targetBlock();
    			if(conditionBlock.type === 'road_exists'){
    				var selection = conditionBlock.inputList[0].fieldRow[1].value_;
    				condition = roadCondition(selection);
    			} else if (conditionBlock.type === 'dead_end') {
                    condition = deadEndCondition();
                } else if (conditionBlock.type === 'at_destination') {
                    condition = atDestinationCondition();
                }
    		} else if(input.name.indexOf('DO') === 0){
    			var conditionalCommandSet = {};
    			conditionalCommandSet.condition = condition;
    			conditionalCommandSet.commands = getCommandsAtThisLevel(input.connection.targetBlock());
    			conditionalCommandSets.push(conditionalCommandSet);
    		}
    		
    		i++;
    	}
    	
    	if(block.elseCount_ === 1){
    		var elseCommands = getCommandsAtThisLevel(block.inputList[block.inputList.length - 1].connection.targetBlock());
    	}
    	
    	return new If(conditionalCommandSets, elseCommands, block);
	}
	
	function getCommandsAtThisLevel(block){
    	var commands = [];
    	
    	while(block){
    		if (block.type === 'move_van') {
    			commands.push(new ForwardCommand(block));
            } else if (block.type === 'turn_left') {
            	commands.push(new TurnLeftCommand(block));
            } else if (block.type === 'turn_right') {
                commands.push(new TurnRightCommand(block));
            } else if (block.type === 'turn_around') {
                commands.push(new TurnAroundCommand(block));
            } else if (block.type === 'controls_repeat') {
            	commands.push(createWhile(block));
            } else if (block.type === 'controls_if') {
            	commands.push(createIf(block));
            }
    		
    		block = block.nextConnection.targetBlock();
    	}
    	
    	return commands;
    }
	
    var program = new ocargo.Program();
    var startBlock = this.getStartBlock();
    program.startBlock = startBlock;
    program.stack.push(getCommandsAtThisLevel(startBlock));
    return program;
};
