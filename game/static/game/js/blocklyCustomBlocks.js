'use strict';

var ocargo = ocargo || {};

Blockly.Blocks['start'] = {
    // Beginning block - identifies the start of the program
    init: function() {
        var imageStr = (ocargo.blocklyControl.numStartBlocks%2 == 0) ? '/static/game/image/van_small.svg' : '/static/game/image/van_small2.svg';
        ocargo.blocklyControl.numStartBlocks++;
        
        this.setColour(50);
        this.appendDummyInput()
            .appendField('Start')
            .appendField(new Blockly.FieldImage(imageStr, ocargo.blocklyControl.BLOCK_VAN_HEIGHT, ocargo.blocklyControl.BLOCK_VAN_WIDTH));
        this.setNextStatement(true);
        this.setTooltip('The beginning of the program');
        this.setDeletable(false);
    }
};

Blockly.Python['start'] = function(block) {
	return '';
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

Blockly.Python['move_forwards'] = function(block) {
	return 'v.move_forwards()\n';
};

Blockly.Blocks['turn_left'] = {
    // Block for turning left
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('turn left')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                40,
                                                ocargo.blocklyControl.BLOCK_HEIGHT))
            .appendField(new Blockly.FieldImage('/static/game/image/arrow_left.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Turn the van left');
    }
};

Blockly.Python['turn_left'] = function(block) {
	return 'v.turn_left()\n';
};

Blockly.Blocks['turn_right'] = {
    // Block for turning right
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('turn right')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                31,
                                                ocargo.blocklyControl.BLOCK_HEIGHT))
            .appendField(new Blockly.FieldImage('/static/game/image/arrow_right.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Turn the van right');
    }
};

Blockly.Python['turn_right'] = function(block) {
	return 'v.turn_right()\n';
};

Blockly.Blocks['turn_around'] = {
    // Block for turning around
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('turn around')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                14,
                                                ocargo.blocklyControl.BLOCK_HEIGHT))
            .appendField(new Blockly.FieldImage('/static/game/image/arrow_u.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Turn the van around');
    }
};

Blockly.Python['turn_around'] = function(block) {
	return 'v.turn_around()\n';
};

Blockly.Blocks['wait'] = {
    // Block for not moving the van for a time
    init: function() {
        this.setColour(160);
        this.appendDummyInput()
            .appendField('wait')
            .appendField(new Blockly.FieldImage('/static/game/image/empty.svg',
                                                62,
                                                ocargo.blocklyControl.BLOCK_HEIGHT))
            .appendField(new Blockly.FieldImage('/static/game/image/wait.svg',
                                                ocargo.blocklyControl.IMAGE_WIDTH,
                                                ocargo.blocklyControl.BLOCK_HEIGHT));
        this.setPreviousStatement(true);
        this.setNextStatement(true);
        this.setTooltip('Keep the van stationary');
    }
};

Blockly.Python['wait'] = function(block) {
	return 'v.wait()\n';
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

Blockly.Python['road_exists'] = function(block) {
	if(block.inputList[0].fieldRow[1].value_ === 'FORWARD'){
		var python = "v.is_road('FORWARD')";
	}else if(block.inputList[0].fieldRow[1].value_ === 'LEFT'){
		var python = "v.is_road('LEFT')";
	}else{
		var python = "v.is_road('RIGHT')";
	}
	
	return [python, Blockly.Python.ORDER_NONE]; //TODO: figure out what this ordering relates to
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

Blockly.Python['traffic_light'] = function(block) {
	if(block.inputList[0].fieldRow[1].value_ === ocargo.TrafficLight.RED){
		var python = "v.at_traffic_light('RED')";
	}else{
		var python = "v.at_traffic_light('GREEN')";
	}
	
	return [python, Blockly.Python.ORDER_NONE]; //TODO: figure out what this ordering relates to
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

Blockly.Python['dead_end'] = function(block) {
	return ['v.at_dead_end()', Blockly.Python.ORDER_NONE]; //TODO: figure out what this ordering relates to
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

Blockly.Python['at_destination'] = function(block) {
	return ['v.at_destination()', Blockly.Python.ORDER_NONE]; //TODO: figure out what this ordering relates to;
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

Blockly.Python['call_proc'] = function(block) {
	return block.inputList[0].connection.targetBlock().inputList[0].fieldRow[1].text_ + '()\n';
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

Blockly.Python['declare_proc'] = function(block) {
	var branch = Blockly.Python.statementToCode(block, 'DO');
	return 'def ' + block.inputList[0].connection.targetBlock().inputList[0].fieldRow[1].text_ + '():\n'
		+ branch;//TODO: get code out of sub-blocks (there's a Blockly function for it)
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
