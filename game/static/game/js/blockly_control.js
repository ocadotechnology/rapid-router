'use strict';

var ocargo = ocargo || {};

ocargo.BlocklyControl = function(){
    this.incorrect = null;
    this.incorrectColour = null;
};

ocargo.blocklyControl = new ocargo.BlocklyControl();

ocargo.blocklyControl.BLOCK_HEIGHT = 30;
ocargo.blocklyControl.EXTRA_BLOCK_WIDTH = 1;
ocargo.blocklyControl.IMAGE_WIDTH = 30;

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

Blockly.Blocks['move_forwards'] = {
    // Block for moving forward
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('move forwards')
            .appendField(new Blockly.FieldImage('/static/game/image/arrow_forward.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
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
            .appendField('turn left')
            .appendField(new Blockly.FieldImage('/static/game/image/arrow_left.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
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
            .appendField('turn right')
            .appendField(new Blockly.FieldImage('/static/game/image/arrow_right.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
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
            .appendField('turn around')
            .appendField(new Blockly.FieldImage('/static/game/image/arrow_u.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
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
            .appendField(new Blockly.FieldDropdown(BOOLEANS), 'CHOICE')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                ocargo.blocklyControl.EXTRA_BLOCK_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
    }
};

Blockly.Blocks['dead_end'] = {
    init: function() {
        this.setColour(210);
        this.setOutput(true, 'Boolean');
        this.appendDummyInput()
            .appendField('is dead end')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                ocargo.blocklyControl.EXTRA_BLOCK_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
    }
};

Blockly.Blocks['at_destination'] = {
    init: function() {
        this.setColour(210);
        this.setOutput(true, 'Boolean');
        this.appendDummyInput()
            .appendField('at destination')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                ocargo.blocklyControl.EXTRA_BLOCK_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
    }
};

//Customise controls_repeat block to not allow more than a sensible number of repetitions
var controlsRepeatBlock = Blockly.Blocks['controls_repeat'];
var originalInit = controlsRepeatBlock.init;
controlsRepeatBlock.init = function () {
    originalInit.call(this);

    var input = this.inputList[0];
    var field = input.fieldRow[1];
    field.changeHandler_ = function(text) {
        var n = Blockly.FieldTextInput.numberValidator(text);
        if (n) {
            n = String(Math.min(Math.max(0, Math.floor(n)), 20));
        }
        return n;
    };
};

// Make 'not' taller
var notBlock = Blockly.Blocks['logic_negate'];
var originalNotInit = notBlock.init;
notBlock.init = function () {
	originalNotInit.call(this);
	this.inputList[0].appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                         ocargo.blocklyControl.EXTRA_BLOCK_WIDTH,
                                                         ocargo.blocklyControl.BLOCK_HEIGHT));
};

// Disable the right-click context menus
Blockly.showContextMenu_ = function(e) {};
Blockly.Block.prototype.showContextMenu_ = function(e) {};

// Define custom select methods that select a block and its connected blocks
function setBlockAndConnectedBlocksSelected(block, selected) {
    if (!block.svg_) {
        return;
    }

    block.inputList.forEach(function(input) {
        if (input.connection && input.type !== Blockly.NEXT_STATEMENT) {
            var targetBlock = input.connection.targetBlock();
            if (targetBlock) {
                setBlockAndConnectedBlocksSelected(targetBlock, selected);
            }
        }
    });

    if (selected) {
        block.svg_.addSelect();
    } else {
        block.svg_.removeSelect();
    }
}

var selectedWithConnected;

Blockly.Block.prototype.selectWithConnected = function() {
    // Unselect any previously selected blocks
    if (Blockly.selected) {
        Blockly.selected.unselect();
    }
    if (selectedWithConnected) {
        selectedWithConnected.unselectWithConnected();
    }

    selectedWithConnected = this;
    setBlockAndConnectedBlocksSelected(this, true);
};

Blockly.Block.prototype.unselectWithConnected = function() {
    selectedWithConnected = null;
    setBlockAndConnectedBlocksSelected(this, false);
};

ocargo.BlocklyControl.prototype.createBlock = function(blockType) {
	var block = Blockly.Block.obtain(Blockly.mainWorkspace, blockType);
	block.initSvg();
	block.render();
    return block;
};

ocargo.BlocklyControl.prototype.addBlockToEndOfProgram = function(typeOfBlockToAdd) {
	var blockToAdd = this.createBlock(typeOfBlockToAdd);

	var block = this.getStartBlock();
	while (block.nextConnection.targetBlock()) {
		block = block.nextConnection.targetBlock();
	}

	block.nextConnection.connect(blockToAdd.previousConnection);
};

ocargo.BlocklyControl.prototype.init = function() {
    var blockly = document.getElementById('blockly');
    var toolbox = document.getElementById('toolbox');
    Blockly.inject(blockly, {
        path: '/static/game/js/blockly/',
        toolbox: toolbox,
        trashcan: true
    });

    try {
        var text = localStorage.getItem('blocklyWorkspaceXml');
        var xml = Blockly.Xml.textToDom(text);
        Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, xml);
        ocargo.blocklyControl.removeUnavailableBlocks();
        ocargo.blocklyControl.addClickListenerToStartBlock();
    } catch (e) {
        ocargo.blocklyControl.reset();
    }
    

};

ocargo.BlocklyControl.prototype.teardown = function() {
    if (localStorage) {
        var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
        var text = Blockly.Xml.domToText(xml);
        localStorage.setItem('blocklyWorkspaceXml', text);
    }
};

ocargo.BlocklyControl.prototype.reset = function() {
    Blockly.mainWorkspace.clear();
    this.createBlock('start');
    this.addClickListenerToStartBlock();
};

ocargo.BlocklyControl.prototype.removeWrong = function() {
    if (this.incorrect) {
        var previous = this.incorrect.previousConnection.targetBlock();
        this.incorrect.dispose();
        this.incorrect = null;
        previous.selectWithConnected();
    }
};

ocargo.BlocklyControl.prototype.blink = function() {
    var badBlock = selectedWithConnected;
    this.incorrect = badBlock;
    this.incorrectColour = badBlock.getColour();
    badBlock.setColour(0);
    for (var i = 0; i < 3; i++) {
        window.setTimeout(function() { badBlock.selectWithConnected(); }, i * 600 - 300);
        window.setTimeout(function() { badBlock.unselectWithConnected(); }, i * 600);
    }
    window.setTimeout(function() { badBlock.selectWithConnected(); }, 1500);
};

window.addEventListener('load', ocargo.blocklyControl.init);
window.addEventListener('unload', ocargo.blocklyControl.teardown);

ocargo.BlocklyControl.prototype.getStartBlock = function() {
    var startBlock = null;
    Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
        if (block.type === 'start') {
            startBlock = block;
        }
    });
    return startBlock;
};

ocargo.BlocklyControl.prototype.getBlocksCount = function() {
    return Blockly.mainWorkspace.getAllBlocks().length;
};

ocargo.BlocklyControl.prototype.removeUnavailableBlocks = function() {
    var blocks = Blockly.mainWorkspace.getAllBlocks();
    var block;
    for (var i = 0; i < blocks.length; i++) {
        block = blocks[i];
        if (BLOCKS.indexOf(block.type) === -1 && block.type !== 'start') {
            block.dispose();
        }
    }
}

ocargo.BlocklyControl.prototype.addClickListenerToStartBlock = function() {
	var startBlock = this.getStartBlock();
	if (startBlock) {
		var svgRoot = startBlock.getSvgRoot();
		if (svgRoot) {
			if (!svgRoot.id || svgRoot.id === "") {
				svgRoot.id = "startBlockSvg"
			}
			var downX = 0;
			var downY = 0;
			var maxMove = 5;
			$('#' + svgRoot.id).on({
				mousedown: function(e) {
					downX  = e.pageX;
					downY   = e.pageY;
				},
				mouseup: function(e) {
					if ( Math.abs(downX - e.pageX) < maxMove && Math.abs(downY - e.pageY) < maxMove) {
						var playEls = $('#play');
						if(playEls && playEls.length && playEls.length > 0){
							playEls[0].click();
						}
					}
				}
			});
		}
    } 
}

ocargo.BlocklyControl.prototype.populateProgram = function() {
	function createWhile(block) {
		return new While(
			counterCondition(block.inputList[0].fieldRow[1].text_),
			getCommandsAtThisLevel(block.inputList[1].connection.targetBlock()),
			block);
	}

	function createWhileUntil(block) {
		var condition = getCondition(block.inputList[0].connection.targetBlock());
		if (block.inputList[0].fieldRow[1].value_ == 'UNTIL') {
			condition = negateCondition(condition);
		}

		return new While(
			condition,
			getCommandsAtThisLevel(block.inputList[1].connection.targetBlock()),
			block);
	}

	function getCondition(conditionBlock) {
		if (conditionBlock.type === 'road_exists') {
			var selection = conditionBlock.inputList[0].fieldRow[1].value_;
			return roadCondition(selection);
		} else if (conditionBlock.type === 'dead_end') {
			return deadEndCondition();
        } else if (conditionBlock.type === 'at_destination') {
        	return atDestinationCondition();
        } else if (conditionBlock.type === 'logic_negate') {
        	return negateCondition(getCondition(conditionBlock.inputList[0].connection.targetBlock()));
        }
	}

	function createIf(block) {
		var conditionalCommandSets = [];

        var elseCount = block.elseCount_ || 0;
    	var i = 0;
    	while (i < block.inputList.length - elseCount) {
    		var input = block.inputList[i];
    		var condition;

    		if (input.name.indexOf('IF') === 0) {
    			condition = getCondition(input.connection.targetBlock());
    		} else if (input.name.indexOf('DO') === 0) {
    			var conditionalCommandSet = {};
    			conditionalCommandSet.condition = condition;
    			conditionalCommandSet.commands = getCommandsAtThisLevel(input.connection.targetBlock());
    			conditionalCommandSets.push(conditionalCommandSet);
    		}

    		i++;
    	}

    	if (elseCount === 1) {
    		var elseCommands = getCommandsAtThisLevel(block.inputList[block.inputList.length - 1]
                                                                    .connection.targetBlock());
    	}

    	return new If(conditionalCommandSets, elseCommands, block);
	}

	function getCommandsAtThisLevel(block){
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
            } else if (block.type === 'controls_repeat') {
            	commands.push(createWhile(block));
            } else if (block.type === 'controls_whileUntil') {
            	commands.push(createWhileUntil(block));
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
