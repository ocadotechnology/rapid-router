'use strict';

var ocargo = ocargo || {};
var Blockly = Blockly || {};

function initCustomBlocks() {
    initCustomBlocksDescription();
    initCustomBlocksPython();
}

function initCustomBlocksDescription() {

    Blockly.Blocks['start'] = {
        // Beginning block - identifies the start of the program
        init: function() {
            ocargo.blocklyControl.numStartBlocks++;
            this.setColour(50);
            this.appendDummyInput()
                .appendField(gettext('Start'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + CHARACTER_EN_FACE_URL,
                    ocargo.BlocklyControl.BLOCK_CHARACTER_HEIGHT,
                    ocargo.BlocklyControl.BLOCK_CHARACTER_WIDTH));
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('The beginning of the program'));
            this.setDeletable(false);
        }
    };

    /*****************/
    /* Action Blocks */
    /*****************/

    Blockly.Blocks['move_forwards'] = {
        // Block for moving forward
        init: function() {
            this.setColour(160);
            this.appendDummyInput()
                .appendField(gettext('move forwards'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'actions/forward.svg',
                                                    ocargo.BlocklyControl.IMAGE_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Move the van forwards'));
        }
    };

    Blockly.Blocks['turn_left'] = {
        // Block for turning left
        init: function() {
            this.setColour(160);
            this.appendDummyInput()
                .appendField(gettext('turn left'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    38,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'actions/left.svg',
                                                    ocargo.BlocklyControl.IMAGE_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Turn the van left'));
        }
    };

    Blockly.Blocks['turn_right'] = {
        // Block for turning right
        init: function() {
            this.setColour(160);
            this.appendDummyInput()
                .appendField(gettext('turn right'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    29,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'actions/right.svg',
                                                    ocargo.BlocklyControl.IMAGE_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Turn the van right'));
        }
    };

    Blockly.Blocks['turn_around'] = {
        // Block for turning around
        init: function() {
            this.setColour(160);
            this.appendDummyInput()
                .appendField(gettext('turn around'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    12,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir +
                                                    'actions/turn_around.svg',
                                                    ocargo.BlocklyControl.IMAGE_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Turn the van around'));
        }
    };

    Blockly.Blocks['wait'] = {
        // Block for not moving the van for a time
        init: function() {
            this.setColour(160);
            this.appendDummyInput()
                .appendField(gettext('wait'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    60,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'actions/wait.svg',
                                                    ocargo.BlocklyControl.IMAGE_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Keep the van stationary'));
        }
    };

    Blockly.Blocks['deliver'] = {
        // Block for delivering (only on levels with multiple destinations)
        init: function() {
            this.setColour(160);
            this.appendDummyInput()
                .appendField(gettext('deliver'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    43,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'actions/deliver.svg',
                                                    ocargo.BlocklyControl.IMAGE_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Deliver the goods from the van'));
        }
    };

    Blockly.Blocks['sound_horn'] = {
        init: function() {
            this.setColour(160);
            this.appendDummyInput()
                .appendField(gettext('sound horn'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                    43,
                    ocargo.BlocklyControl.BLOCK_HEIGHT))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                    ocargo.BlocklyControl.IMAGE_WIDTH,
                    ocargo.BlocklyControl.BLOCK_HEIGHT));
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Sound the horn to scare away the cows'));
        }
    };

    /*****************/
    /*   Conditions  */
    /*****************/

    Blockly.Blocks['road_exists'] = {
        init: function() {
            var BOOLEANS =
                [[gettext('road exists forward'), 'FORWARD'],
                 [gettext('road exists left'), 'LEFT'],
                 [gettext('road exists right'), 'RIGHT']];
            this.setColour(210);
            this.setOutput(true, 'Boolean');
            this.appendDummyInput()
                .appendField(new Blockly.FieldDropdown(BOOLEANS), 'CHOICE')
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
        }
    };

    Blockly.Blocks['traffic_light'] = {
        init: function() {
            var BOOLEANS =
                [[gettext('traffic light red'), ocargo.TrafficLight.RED],
                 [gettext('traffic light green'), ocargo.TrafficLight.GREEN]];
            this.setColour(210);
            this.setOutput(true, 'Boolean');
            this.appendDummyInput()
                .appendField(new Blockly.FieldDropdown(BOOLEANS), 'CHOICE')
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
        }
    };

    Blockly.Blocks['dead_end'] = {
        init: function() {
            this.setColour(210);
            this.setOutput(true, 'Boolean');
            this.appendDummyInput()
                .appendField(gettext('is dead end'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
        }
    };

    Blockly.Blocks['at_destination'] = {
        init: function() {
            this.setColour(210);
            this.setOutput(true, 'Boolean');
            this.appendDummyInput()
                .appendField(gettext('at destination'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                    ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT));
        }
    };

    Blockly.Blocks['cow_crossing'] = {
        init: function() {
            this.setColour(210);
            this.setOutput(true, 'Boolean');
            this.appendDummyInput()
                .appendField(gettext('cows'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + ocargo.Drawing.whiteCowUrl,
                    ocargo.BlocklyControl.COW_WIDTH,
                    ocargo.BlocklyControl.BLOCK_HEIGHT), 'IMAGE');
        }
    };
    /****************/
    /*  Procedures  */
    /****************/

    Blockly.Blocks['call_proc'] = {
        // Block for calling a defined procedure
        init: function() {
            var name = '';
            this.setColour(260);
            this.appendDummyInput()
                .appendField(gettext('Call'))
                .appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg', 7,
                                                    ocargo.BlocklyControl.BLOCK_HEIGHT))
                .appendField(new Blockly.FieldTextInput(name),'NAME');
            this.setPreviousStatement(true, 'Action');
            this.setNextStatement(true, 'Action');
            this.setTooltip(gettext('Call'));
        }

    };

    Blockly.Blocks['declare_proc'] = {
        // Block for declaring a procedure
        init: function() {
            var name = '';
            this.setColour(260);
            this.appendDummyInput()
                .appendField(gettext('Define'))
                .appendField(new Blockly.FieldTextInput(name),'NAME');
            this.appendStatementInput('DO')
                .setCheck('Action')
                .appendField(gettext('Do'));
            this.setTooltip(gettext('Declares the procedure'));
            this.statementConnection_ = null;
        }
    };

    /*******************/
    /*  Control Flows  */
    /*******************/

    Blockly.Blocks['controls_repeat_while'] = {
        // Block for repeat while
        init: function() {
          this.setColour(120);
          this.appendValueInput("condition")
              .setCheck("Boolean")
              .appendField(gettext('repeat while'));
          this.appendStatementInput("body")
              .setCheck("Action")
              .appendField(gettext('do'));
          this.setPreviousStatement(true, 'Action');
          this.setNextStatement(true, 'Action');
          this.setTooltip(gettext('While a value is true, do some statements'));
        }
    };

    Blockly.Blocks['controls_repeat_until'] = {
        // Block for repeat until
        init: function() {
          this.setColour(120);
          this.appendValueInput("condition")
              .setCheck("Boolean")
              .appendField(gettext('repeat until'));
          this.appendStatementInput("body")
              .setCheck("Action")
              .appendField(gettext('do'));
          this.setPreviousStatement(true, 'Action');
          this.setNextStatement(true, 'Action');
          this.setTooltip(gettext('Until a value is true, do some statements'));
        }
    };

    // Set text colour to red
    var textBlock = Blockly.Blocks['text'];
    var originalTextInit = textBlock.init;
    textBlock.init = function() {
        originalTextInit.call(this);
        this.setColour(260);
    };

    //Customise controls_repeat block to not allow more than a sensible number of repetitions
    var controlsRepeatBlock = Blockly.Blocks['controls_repeat'];
    var originalInit = controlsRepeatBlock.init;
    controlsRepeatBlock.init = function () {
        originalInit.call(this);

        this.setPreviousStatement(!0, 'Action');
        this.setNextStatement(!0, 'Action');
        this.inputList[1].setCheck('Action'); //Disallow event action blocks to be in body

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
        this.inputList[0].appendField(new Blockly.FieldImage(ocargo.Drawing.imageDir + 'empty.svg',
                                                             ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
                                                             ocargo.BlocklyControl.BLOCK_HEIGHT));
    };
}

function initCustomBlocksPython() {
    Blockly.Python['start'] = function(block) {
        return '';
    };

    Blockly.Python['move_forwards'] = function(block) {
        return 'my_van.move_forwards()\n';
    };

    Blockly.Python['turn_left'] = function(block) {
        return 'my_van.turn_left()\n';
    };

    Blockly.Python['turn_right'] = function(block) {
        return 'my_van.turn_right()\n';
    };

    Blockly.Python['turn_around'] = function(block) {
        return 'my_van.turn_around()\n';
    };

    Blockly.Python['wait'] = function(block) {
        return 'my_van.wait()\n';
    };

    Blockly.Python['deliver'] = function(block) {
        return 'my_van.deliver()\n';
    };

    Blockly.Python['sound_horn'] = function(block) {
        return 'my_van.sound_horn()\n';
    };


    Blockly.Python['road_exists'] = function(block) {
        if(block.inputList[0].fieldRow[1].value_ === 'FORWARD'){
            var python = "my_van.is_road('FORWARD')";
        }else if(block.inputList[0].fieldRow[1].value_ === 'LEFT'){
            var python = "my_van.is_road('LEFT')";
        }else{
            var python = "my_van.is_road('RIGHT')";
        }

        return [python, Blockly.Python.ORDER_NONE];
        // TODO: figure out what this ordering relates to
    };

    Blockly.Python['traffic_light'] = function(block) {
        var python;
        if(block.inputList[0].fieldRow[1].value_ === ocargo.TrafficLight.RED){
            python = "my_van.at_traffic_light('RED')";
        }else{
            python = "my_van.at_traffic_light('GREEN')";
        }

        return [python, Blockly.Python.ORDER_NONE]; //TODO: figure out what this ordering relates to
    };

    Blockly.Python['dead_end'] = function(block) {
        return ['my_van.at_dead_end()', Blockly.Python.ORDER_NONE];
        // TODO: figure out what this ordering relates to
    };

    Blockly.Python['cow_crossing'] = function(block) {
        return ['my_van.cow_crossing()', Blockly.Python.ORDER_NONE];
        // TODO: figure out what this ordering relates to
    };

    Blockly.Python['at_destination'] = function(block) {
        return ['my_van.at_destination()', Blockly.Python.ORDER_NONE];
        // TODO: figure out what this ordering relates to;
    };

    Blockly.Python['call_proc'] = function(block) {
        return block.inputList[0].fieldRow[2].text_ + '()\n';
    };

    Blockly.Python['declare_proc'] = function(block) {
        var branch = Blockly.Python.statementToCode(block, 'DO');
        return 'def ' + block.inputList[0].fieldRow[1].text_ + '():\n' + branch;
        // TODO: get code out of sub-blocks (there's a Blockly function for it)
    };

    Blockly.Python['controls_repeat_while'] = function(block) {
      var condition = Blockly.Python.valueToCode(block, 'condition', Blockly.Python.ORDER_ATOMIC);
      var subBlock = Blockly.Python.statementToCode(block, 'body');
      var code = 'while ' + condition + ':\n' + subBlock;
      return code;
    };

    Blockly.Python['controls_repeat_until'] = function(block) {
      var condition = Blockly.Python.valueToCode(block, 'condition', Blockly.Python.ORDER_ATOMIC);
      var subBlock = Blockly.Python.statementToCode(block, 'body');
      var code = 'while not ' + condition + ':\n' + subBlock;
      return code;
    };
}
