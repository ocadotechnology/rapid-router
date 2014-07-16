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

Blockly.Blocks['wait'] = {
    // Block for not moving the van for a time
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('wait')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                ocargo.blocklyControl.EXTRA_BLOCK_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Keep the van stationary');
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

Blockly.Blocks['traffic_light'] = {
    init: function() {
        var BOOLEANS =
            [['traffic light red', ocargo.TrafficLight.RED],
             ['traffic light green', ocargo.TrafficLight.GREEN]];
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

Blockly.Blocks['call_proc'] = {
    // Block for calling a defined procedure
    init: function() {
        this.setColour(260);
        this.appendValueInput('Name:')
            .appendField('Call')
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Call');
    }
};

Blockly.Blocks['declare_proc'] = {
    // Block for declaring a procedure
    init: function() {
        this.setColour(260);
        this.appendValueInput('ID')
            .appendField('Define');
        this.appendStatementInput('DO')
            .appendField('Do');

        this.setTooltip('Declares the procedure');
    }
};

// Set text colour to red
var textBlock = Blockly.Blocks['text']
var originalTextInit = textBlock.init;
textBlock.init = function() {
    originalTextInit.call(this);
    this.setColour(260);
}

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

ocargo.BlocklyControl.prototype.createBlock = function(blockType) {
	var block = Blockly.Block.obtain(Blockly.mainWorkspace, blockType);
	block.initSvg();
	block.render();
    return block;
};

ocargo.BlocklyControl.prototype.addBlockToEndOfProgram = function(typeOfBlockToAdd) {
	var blockToAdd = this.createBlock(typeOfBlockToAdd);

	var block = this.getStartBlocks()[0];
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

    function decodeHTML(text) {
        var e = document.createElement('div');
        e.innerHTML = text;
        return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
    }

    // Use the user's last attempt if available, else use whatever's in local storage
    if (WORKSPACE && WORKSPACE != '') {
        ocargo.blocklyControl.deserialize(decodeHTML(WORKSPACE));
    }
    else {
        ocargo.blocklyControl.deserialize(localStorage.getItem('blocklyWorkspaceXml-' + LEVEL_ID));
    }
};

ocargo.BlocklyControl.prototype.teardown = function() {
    if (localStorage) {
        var text = ocargo.blocklyControl.serialize();
        try {
            localStorage.setItem('blocklyWorkspaceXml-' + LEVEL_ID, text);
        } catch (e) {
            // No point in even logging, as page is unloading
        }
    }
};

ocargo.BlocklyControl.prototype.deserialize = function(text) {
    try {
        var xml = Blockly.Xml.textToDom(text);
        Blockly.mainWorkspace.clear();
        Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, xml);
        ocargo.blocklyControl.removeUnavailableBlocks();
        ocargo.blocklyControl.addClickListenerToStartBlocks();
    } catch (e) {
        ocargo.blocklyControl.reset();
    }
};

ocargo.BlocklyControl.prototype.serialize = function() {
    var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
    var text = Blockly.Xml.domToText(xml);
    return text;
};

ocargo.BlocklyControl.prototype.reset = function() {
    Blockly.mainWorkspace.clear();

    for (var i = 0; i < THREADS; i++) {
        var startBlock = this.createBlock('start');
        startBlock.moveBy(30+(i%2)*200,30+Math.floor(i/2)*100);
    }
    this.addClickListenerToStartBlocks();
};

// Define custom select methods that select a block and its inputs
ocargo.BlocklyControl.prototype.setBlockSelected = function(block, selected) {
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

ocargo.BlocklyControl.prototype.makeBlockBlink = function(badBlock) {
    var blocklyControl = this;
    var frequency = 300;
    var repeats = 3;

    this.incorrect = badBlock;
    this.incorrectColour = badBlock.getColour();
    badBlock.setColour(0);
    for (var i = 0; i < repeats; i++) {
        window.setTimeout(function() { blocklyControl.setBlockSelected(badBlock, true); }, 2 * i * frequency);
        window.setTimeout(function() { blocklyControl.setBlockSelected(badBlock, false); }, (2 * i + 1) * frequency);
    }
};

window.addEventListener('load', ocargo.blocklyControl.init);
window.addEventListener('unload', ocargo.blocklyControl.teardown);

ocargo.BlocklyControl.prototype.getStartBlocks = function() {
    var startBlocks = [];
    Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
        if (block.type === 'start') {
            startBlocks.push(block);
        }
    });
    return startBlocks;
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
};

ocargo.BlocklyControl.prototype.resetWidthOnBlocks = function(blocks){
	for (var i = 0; i < blocks.length; i++) {
		var block = blocks[i];
		for( var j = 0; j < block.inputList.length; j++){
			var input = block.inputList[j];
			for(var k = 0; k < input.fieldRow.length; k++){
				input.fieldRow[k].size_.width = null;
			}
		}
	}
};

//so that image fields render properly when their size_ variable is broken above
Blockly.FieldImage.prototype.render_ = function(){
    this.size_ = {height: this.height_ + 10, width: this.width_};
};

ocargo.BlocklyControl.prototype.increaseBlockSize = function(){
	ocargo.blocklyControl.bigCodeMode = true;
    Blockly.BlockSvg.FIELD_HEIGHT *= 2; //30
    Blockly.BlockSvg.MIN_BLOCK_Y *= 2; // 25
    Blockly.BlockSvg.JAGGED_TEETH_HEIGHT *= 2; //20
    Blockly.BlockSvg.JAGGED_TEETH_WIDTH *= 2;
    Blockly.BlockSvg.SEP_SPACE_X *= 2;
    Blockly.BlockSvg.SEP_SPACE_Y *= 2;
    Blockly.BlockSvg.INLINE_PADDING_Y *= 2;
    Blockly.Icon.RADIUS *= 2;
    
    /*Blockly.BlockSvg.NOTCH_PATH_LEFT = 'l 12,8 6,0 12,-8';
    Blockly.BlockSvg.NOTCH_PATH_LEFT_HIGHLIGHT = 'l 13,4 4,0 13,-8';
    Blockly.BlockSvg.NOTCH_PATH_RIGHT = 'l -12,4 -6,0 -12,-8';
    Blockly.BlockSvg.TAB_HEIGHT *= 2;
    Blockly.BlockSvg.TAB_WIDTH *= 2;
    Blockly.BlockSvg.NOTCH_WIDTH *= 2;
    */
    
    ocargo.blocklyControl.IMAGE_WIDTH *= 2;
    ocargo.blocklyControl.BLOCK_HEIGHT *= 2;

	document.styleSheets[0].insertRule(".blocklyText, .beaconClass" + ' { font-size' + ':'+'22pt !important'+'}', document.styleSheets[0].cssRules.length);
	document.styleSheets[0].insertRule(".blocklyIconMark, .beaconClass" + ' { font-size' + ':'+'18pt !important'+'}', document.styleSheets[0].cssRules.length);
	var blocks = Blockly.mainWorkspace.getAllBlocks();
    ocargo.blocklyControl.resetWidthOnBlocks(blocks);
    Blockly.mainWorkspace.render();

	Blockly.mainWorkspace.flyout_.show(Blockly.languageTree.childNodes);
	
    $(".blocklyIconMark").attr("x", 16).attr("y", 24);
    $(".blocklyEditableText > rect").attr("height", 41).attr("y", -32);
};

ocargo.BlocklyControl.prototype.decreaseBlockSize = function(){
	ocargo.blocklyControl.bigCodeMode = false;
    Blockly.BlockSvg.FIELD_HEIGHT /= 2;
    Blockly.BlockSvg.MIN_BLOCK_Y /= 2;
    Blockly.BlockSvg.JAGGED_TEETH_HEIGHT /= 2;
    Blockly.BlockSvg.JAGGED_TEETH_WIDTH /= 2;
    Blockly.BlockSvg.SEP_SPACE_X /= 2;
    Blockly.BlockSvg.SEP_SPACE_Y /= 2;
    Blockly.BlockSvg.INLINE_PADDING_Y /= 2;
    Blockly.Icon.RADIUS /= 2;
    
    /*Blockly.BlockSvg.NOTCH_PATH_LEFT = 'l 12,8 6,0 12,-8';
    Blockly.BlockSvg.NOTCH_PATH_LEFT_HIGHLIGHT = 'l 13,4 4,0 13,-8';
    Blockly.BlockSvg.NOTCH_PATH_RIGHT = 'l -12,4 -6,0 -12,-8';
    Blockly.BlockSvg.TAB_HEIGHT /= 2;
    Blockly.BlockSvg.TAB_WIDTH /= 2;
    Blockly.BlockSvg.NOTCH_WIDTH /= 2;
    */
    
    ocargo.blocklyControl.IMAGE_WIDTH /= 2;
    ocargo.blocklyControl.BLOCK_HEIGHT /= 2;

    var sheet = document.styleSheets[0];
	for(var i = 0; i < 2; i++){
	    sheet.deleteRule(sheet.cssRules.length-1);
	}

	var blocks = Blockly.mainWorkspace.getAllBlocks();
    ocargo.blocklyControl.resetWidthOnBlocks(blocks);
    Blockly.mainWorkspace.render();

	Blockly.mainWorkspace.flyout_.show(Blockly.languageTree.childNodes);
};

ocargo.BlocklyControl.prototype.addClickListenerToStartBlocks = function() {
	var startBlocks = this.getStartBlocks();
    if (startBlocks) {
        for (var i = 0; i < startBlocks.length; i++) {
            var startBlock = startBlocks[i];
        	var svgRoot = startBlock.getSvgRoot();
        	if (svgRoot) {
        		if (!svgRoot.id || svgRoot.id === "") {
        			svgRoot.id = "startBlockSvg" + i;
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
};



ocargo.BlocklyControl.BlockHandler = function(id) {
    this.id = id;
    this.selectedBlock = null;
};

ocargo.BlocklyControl.BlockHandler.prototype.selectBlock = function(block) {
    if (block) {
        this.deselectCurrent();
        ocargo.blocklyControl.setBlockSelected(block, true);
        this.selectedBlock = block;
    }
};

ocargo.BlocklyControl.BlockHandler.prototype.deselectCurrent = function() {
    if (this.selectedBlock) {
        ocargo.blocklyControl.setBlockSelected(this.selectedBlock, false);
        this.selectedBlock = null;
    }
};



ocargo.BlocklyControl.prototype.populateProgram = function() {

    /** Instructions **/

    function createProcedures() {
        var newProcs = {};
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

                if (!(name in newProcs)) {
                    newProcs[name] = new Procedure(name, createSequence(bodyBlock),block)
                }
                else {
                    throw ocargo.messages.procDupNameError;
                }
            }
        }
        
        return newProcs;
    }

    function createProcCall(block) {
        var nameBlock = block.inputList[0].connection.targetBlock();
        if(nameBlock == null) {
            throw ocargo.messages.procMissingNameError;
        }
        var name = nameBlock.inputList[0].fieldRow[1].text_;
        if (name === "") {
            throw ocargo.messages.procCallNameError;
        }

        var procCall = new ProcedureCall(block);
        procedureBindings.push({call:procCall,name:name});
        return procCall;
    }

    function createWhile(block) {
        var bodyBlock = block.inputList[1].connection.targetBlock();
        if (bodyBlock === null) {
            throw ocargo.messages.whileBodyError;
        }
		return new While(
			counterCondition(block.inputList[0].fieldRow[1].text_),
			createSequence(bodyBlock),
			block);
	}

	function createWhileUntil(block) {
        var conditionBlock = block.inputList[0].connection.targetBlock();
        if (conditionBlock === null) {
            throw ocargo.messages.whileConditionError;
        }
		var condition = getCondition(conditionBlock);
		if (block.inputList[0].fieldRow[1].value_ == 'UNTIL') {
			condition = negateCondition(condition);
		}

        var bodyBlock = block.inputList[1].connection.targetBlock();
        if (bodyBlock === null) {
            throw ocargo.messages.whileBodyError;
        }
		return new While(condition,	createSequence(bodyBlock), block);
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
        } else if (conditionBlock.type === 'traffic_light') {
        	return trafficLightCondition(conditionBlock.inputList[0].fieldRow[1].value_);
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
                var conditionBlock = input.connection.targetBlock();
                if (conditionBlock === null) {
                    throw ocargo.messages.ifConditionError;
                }
    			condition = getCondition(conditionBlock);
    		} else if (input.name.indexOf('DO') === 0) {
    			var conditionalCommandSet = {};
    			conditionalCommandSet.condition = condition;
    			conditionalCommandSet.commands = createSequence(input.connection.targetBlock());
    			conditionalCommandSets.push(conditionalCommandSet);
    		}

    		i++;
    	}

    	if (elseCount === 1) {
    		var elseBody = createSequence(block.inputList[block.inputList.length - 1].connection.targetBlock());
    	}

    	return new If(conditionalCommandSets, elseBody, block);
	}

	function createSequence(block){
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
            	commands.push(createWhile(block));
            } else if (block.type === 'controls_whileUntil') {
            	commands.push(createWhileUntil(block));
            } else if (block.type === 'controls_if') {
            	commands.push(createIf(block));            
            } else if (block.type === 'call_proc') {
                commands.push(createProcCall(block));
            }

    		block = block.nextConnection.targetBlock();
    	}

        return commands;
    }

    function bindProcedureCalls(program) {
        program.procedures = procedures;
        for (var i = 0; i < procedureBindings.length; i++) {
            var name = procedureBindings[i].name;
            var call = procedureBindings[i].call;

            if (name in procedures) {
                call.bind(procedures[name]);
            } else {
                throw ocargo.messages.procCallNameError;
            }
        }
    }

    /** Conditions **/

    function trafficLightCondition(lightColour) {
        return function(level,threadID) {
            var van = level.vans[threadID];
            return level.isTrafficLightInState(van.previousNode, van.currentNode, lightColour);
        };
    }

    function roadCondition(selection) {
        return function(level,threadID) {
            var van = level.vans[threadID];
            if (selection === 'FORWARD') {
                return level.isActionValidForVan(van, ocargo.FORWARD_ACTION);
            } else if (selection === 'LEFT') {
                return level.isActionValidForVan(van, ocargo.TURN_LEFT_ACTION);
            } else if (selection === 'RIGHT') {
                return level.isActionValidForVan(van, ocargo.TURN_RIGHT_ACTION);
            }
        };
    }

    function counterCoundition(count) {
        return function() {
            if (count > 0) {
                count--;
                return true;
            }

            return false;
        };
    }

    function deadEndCondition() {
        return function(level,threadID) {
            return level.isVanAtDeadEnd(level.vans[threadID]);
        };
    }

    function negateCondition(otherCondition) {
        return function(level,threadID) {
            return !otherCondition(level,threadID);
        };
    }

    function atDestinationCondition() {
        return function(level,threadID) {
            return level.isVanAtDestination(level.vans[threadID]);
        };
    }

    var procedureBindings = [];
    var procedures = createProcedures();

    var program = new ocargo.Program();
    var startBlocks = this.getStartBlocks();
    for(var i = 0; i < THREADS; i++) {
        var thread = new ocargo.Thread(i);
        thread.startBlock = startBlocks[i];
        thread.stack.push(createSequence(thread.startBlock));
        program.threads.push(thread);
    }

    bindProcedureCalls(program);

    return program;
};
