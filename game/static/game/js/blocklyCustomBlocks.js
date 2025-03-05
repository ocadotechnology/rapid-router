"use strict";

var ocargo = ocargo || {};
var Blockly = Blockly || {};

function initCustomBlocks() {
  initCustomBlocksDescription();
  initCustomBlocksPython();
}

function initCustomBlocksDescription() {
  Blockly.Blocks["start"] = {
    // Beginning block - identifies the start of the program
    init: function () {
      ocargo.blocklyControl.numStartBlocks++;
      this.setColour(50);
      this.appendDummyInput()
        .appendField(Blockly.Msg.START_TITLE)
        .appendField(
          new Blockly.FieldImage(
            new Date().getMonth() === 11 && CHARACTER_NAME === "Van"
              ? ocargo.Drawing.imageDir + "characters/top_view/Sleigh.svg"
              : ocargo.Drawing.imageDir + CHARACTER_EN_FACE_URL,
            ocargo.BlocklyControl.BLOCK_CHARACTER_HEIGHT,
            ocargo.BlocklyControl.BLOCK_CHARACTER_WIDTH
          )
        );
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.START_TOOLTIP);
      this.setDeletable(false);
    },
  };

  /*****************/
  /* Action Blocks */
  /*****************/

  Blockly.Blocks["move_forwards"] = {
    // Block for moving forward
    init: function () {
      this.setColour(160);
      this.appendDummyInput()
        .appendField(Blockly.Msg.MOVE_FORWARDS_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "actions/forward.svg",
            ocargo.BlocklyControl.IMAGE_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.MOVE_FORWARDS_TOOLTIP);
    },
  };

  Blockly.Blocks["turn_left"] = {
    // Block for turning left
    init: function () {
      this.setColour(160);
      this.appendDummyInput()
        .appendField(Blockly.Msg.TURN_LEFT_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            38,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        )
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "actions/left.svg",
            ocargo.BlocklyControl.IMAGE_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.TURN_LEFT_TOOLTIP);
    },
  };

  Blockly.Blocks["turn_right"] = {
    // Block for turning right
    init: function () {
      this.setColour(160);
      this.appendDummyInput()
        .appendField(Blockly.Msg.TURN_RIGHT_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            29,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        )
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "actions/right.svg",
            ocargo.BlocklyControl.IMAGE_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.TURN_RIGHT_TOOLTIP);
    },
  };

  Blockly.Blocks["turn_around"] = {
    // Block for turning around
    init: function () {
      this.setColour(160);
      this.appendDummyInput()
        .appendField(Blockly.Msg.TURN_AROUND_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            12,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        )
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "actions/turn_around.svg",
            ocargo.BlocklyControl.IMAGE_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.TURN_AROUND_TOOLTIP);
    },
  };

  Blockly.Blocks["wait"] = {
    // Block for not moving the van for a time
    init: function () {
      this.setColour(160);
      this.appendDummyInput()
        .appendField(Blockly.Msg.WAIT_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            60,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        )
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "actions/wait.svg",
            ocargo.BlocklyControl.IMAGE_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.WAIT_TOOLTIP);
    },
  };

  Blockly.Blocks["deliver"] = {
    // Block for delivering (only on levels with multiple destinations)
    init: function () {
      this.setColour(160);
      this.appendDummyInput()
        .appendField(Blockly.Msg.DELIVER_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            43,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        )
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "actions/deliver.svg",
            ocargo.BlocklyControl.IMAGE_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.DELIVER_TOOLTIP);
    },
  };

  Blockly.Blocks["sound_horn"] = {
    init: function () {
      this.setColour(160);
      this.appendDummyInput()
        .appendField(Blockly.Msg.SOUND_HORN_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            43,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        )
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            ocargo.BlocklyControl.IMAGE_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.SOUND_HORN_TOOLTIP);
    },
  };

  /*****************/
  /*   Conditions  */
  /*****************/

  Blockly.Blocks["road_exists"] = {
    init: function () {
      var BOOLEANS = [
        [Blockly.Msg.ROAD_EXISTS_FORWARD_TITLE, "FORWARD"],
        [Blockly.Msg.ROAD_EXISTS_LEFT_TITLE, "LEFT"],
        [Blockly.Msg.ROAD_EXISTS_RIGHT_TITLE, "RIGHT"],
      ];
      this.setColour(210);
      this.setOutput(true, "Boolean");
      this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown(BOOLEANS), "CHOICE")
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
    },
  };

  Blockly.Blocks["traffic_light"] = {
    init: function () {
      var BOOLEANS = [
        [Blockly.Msg.TRAFFIC_LIGHT_RED_TITLE, ocargo.TrafficLight.RED],
        [Blockly.Msg.TRAFFIC_LIGHT_GREEN_TITLE, ocargo.TrafficLight.GREEN],
      ];
      this.setColour(210);
      this.setOutput(true, "Boolean");
      this.appendDummyInput()
        .appendField(new Blockly.FieldDropdown(BOOLEANS), "CHOICE")
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
    },
  };

  Blockly.Blocks["dead_end"] = {
    init: function () {
      this.setColour(210);
      this.setOutput(true, "Boolean");
      this.appendDummyInput()
        .appendField(Blockly.Msg.DEAD_END_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
    },
  };

  Blockly.Blocks["at_destination"] = {
    init: function () {
      this.setColour(210);
      this.setOutput(true, "Boolean");
      this.appendDummyInput()
        .appendField(Blockly.Msg.AT_DESTINATION_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        );
    },
  };

  Blockly.Blocks["cow_crossing"] = {
    init: function () {
      this.setColour(210);
      this.setOutput(true, "Boolean");
      let imageUrl =
        ocargo.Drawing.animalType == ocargo.Cow.PIGEON
          ? ocargo.Drawing.pigeonUrl
          : ocargo.Drawing.whiteCowUrl;
      this.appendDummyInput()
        .appendField(
          ocargo.Drawing.animalType == ocargo.Cow.PIGEON
            ? Blockly.Msg.PIGEON_CROSSING_TITLE
            : Blockly.Msg.COW_CROSSING_TITLE
        )
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + imageUrl,
            ocargo.BlocklyControl.COW_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          ),
          "IMAGE"
        );
    },
  };

  Blockly.Blocks["pigeon_crossing_IMAGE_ONLY"] = {
    init: function () {
      this.setColour(210);
      this.setOutput(true, "Boolean");
      this.appendDummyInput()
        .appendField("pigeons")
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + ocargo.Drawing.pigeonUrl,
            ocargo.BlocklyControl.COW_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          ),
          "IMAGE"
        );
    },
  };
  /****************/
  /*  Procedures  */
  /****************/

  Blockly.Blocks["call_proc"] = {
    // Block for calling a defined procedure
    init: function () {
      var name = "";
      this.setColour(260);
      this.appendDummyInput()
        .appendField(Blockly.Msg.CALL_PROC_TITLE)
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + "empty.svg",
            7,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          )
        )
        .appendField(new Blockly.FieldTextInput(name), "NAME");
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.CALL_PROC_TOOLTIP);
    },
  };

  Blockly.Blocks["declare_proc"] = {
    // Block for declaring a procedure
    init: function () {
      var name = "";
      this.setColour(260);
      this.appendDummyInput()
        .appendField(Blockly.Msg.DECLARE_PROC_TITLE)
        .appendField(new Blockly.FieldTextInput(name), "NAME");
      this.appendStatementInput("DO")
        .setCheck("Action")
        .appendField(Blockly.Msg.DECLARE_PROC_SUBTITLE);
      this.setTooltip(Blockly.Msg.DECLARE_PROC_TOOLTIP);
      this.statementConnection_ = null;
    },
  };

  /****************/
  /*    Events    */
  /****************/

  Blockly.Blocks["declare_event"] = {
    // Block for declaring an event handler
    init: function () {
      this.setColour(260);
      var dropdown = new Blockly.FieldDropdown(
        [
          [gettext("white"), ocargo.Cow.WHITE],
          [gettext("brown"), ocargo.Cow.BROWN],
        ],
        function (option) {
          var imageUrl =
            ocargo.Drawing.imageDir + ocargo.Drawing.cowUrl(option);
          this.sourceBlock_.getField("IMAGE").setValue(imageUrl);
        }
      );
      this.appendDummyInput("Event")
        .appendField(gettext("On "))
        .appendField(dropdown, "TYPE")
        .appendField(
          new Blockly.FieldImage(
            ocargo.Drawing.imageDir + ocargo.Drawing.whiteCowUrl,
            ocargo.BlocklyControl.COW_WIDTH,
            ocargo.BlocklyControl.BLOCK_HEIGHT
          ),
          "IMAGE"
        );
      this.getField("IMAGE").EDITABLE = true; //saves the image path as well in the XML
      this.appendStatementInput("DO")
        .setCheck("EventAction")
        .appendField(gettext("Do"));
      this.setTooltip(gettext("Declares the event handler"));
      this.statementConnection_ = null;
    },
  };

  /*******************/
  /*  Control Flows  */
  /*******************/

  Blockly.Blocks["controls_repeat_while"] = {
    // Block for repeat while
    init: function () {
      this.setColour(120);
      this.appendValueInput("condition")
        .setCheck("Boolean")
        .appendField(Blockly.Msg.CONTROLS_REPEAT_WHILE_TITLE);
      this.appendStatementInput("body")
        .setCheck("Action")
        .appendField(Blockly.Msg.CONTROLS_REPEAT_WHILE_SUBTITLE);
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.CONTROLS_REPEAT_WHILE_TOOLTIP);
    },
  };

  Blockly.Blocks["controls_repeat_until"] = {
    // Block for repeat until
    init: function () {
      this.setColour(120);
      this.appendValueInput("condition")
        .setCheck("Boolean")
        .appendField(Blockly.Msg.CONTROLS_REPEAT_UNTIL_TITLE);
      this.appendStatementInput("body")
        .setCheck("Action")
        .appendField(Blockly.Msg.CONTROLS_REPEAT_UNTIL_SUBTITLE);
      this.setPreviousStatement(true, "Action");
      this.setNextStatement(true, "Action");
      this.setTooltip(Blockly.Msg.CONTROLS_REPEAT_UNTIL_TOOLTIP);
    },
  };

  /*****************/
  /*   Variables   */
  /*****************/

  Blockly.Blocks["variables_get"] = {
    init: function () {
      this.appendDummyInput().appendField(
        new Blockly.FieldTextInput(""),
        "NAME"
      );
      this.setOutput(true, null);
      this.setColour(330);
      this.setTooltip(Blockly.Msg.VARIABLES_GET_TOOLTIP);
    },
  };

  Blockly.Blocks["variables_set"] = {
    init: function () {
      this.appendValueInput("VALUE")
        .setCheck(null)
        .appendField(Blockly.Msg.VARIABLES_SET_TITLE)
        .appendField(new Blockly.FieldTextInput(""), "VAR")
        .appendField(Blockly.Msg.VARIABLES_SET_SUBTITLE);
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(330);
      this.setTooltip(Blockly.Msg.VARIABLES_SET_TOOLTIP);
    },
  };

  Blockly.Blocks["variables_numeric_set"] = {
    init: function () {
      this.appendDummyInput()
        .appendField(Blockly.Msg.VARIABLES_SET_TITLE)
        .appendField(new Blockly.FieldTextInput(""), "NAME")
        .appendField(Blockly.Msg.VARIABLES_SET_SUBTITLE)
        .appendField(new Blockly.FieldNumber(0), "VALUE");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(330);
      this.setTooltip(Blockly.Msg.VARIABLES_NUMERIC_SET_TOOLTIP);
    },
  };

  Blockly.Blocks["variables_increment"] = {
    init: function () {
      this.appendDummyInput()
        .appendField(Blockly.Msg.VARIABLES_INCREMENT_TITLE)
        .appendField(new Blockly.FieldTextInput(""), "NAME")
        .appendField(Blockly.Msg.VARIABLES_INCREMENT_SUBTITLE)
        .appendField(new Blockly.FieldNumber(0), "VALUE");
      this.setPreviousStatement(true, null);
      this.setNextStatement(true, null);
      this.setColour(330);
      this.setTooltip(Blockly.Msg.VARIABLES_INCREMENT_TOOLTIP);
    },
  };

  /***************/
  /*   Numbers   */
  /***************/

  Blockly.Blocks["math_number"] = {
    init: function () {
      this.appendDummyInput()
        .appendField(Blockly.Msg.NUMBER_TITLE)
        .appendField(new Blockly.FieldNumber(0), "NUM");
      this.setOutput(true, null);
      this.setColour(230);
      this.setTooltip(Blockly.Msg.NUMBER_TOOLTIP);
    },
  };

  // Set text colour to red
  var textBlock = Blockly.Blocks["text"];
  var originalTextInit = textBlock.init;
  textBlock.init = function () {
    originalTextInit.call(this);
    this.setColour(260);
  };

  //Customise controls_repeat block to not allow more than a sensible number of repetitions
  var controlsRepeatBlock = Blockly.Blocks["controls_repeat"];
  var originalInit = controlsRepeatBlock.init;
  controlsRepeatBlock.init = function () {
    originalInit.call(this);

    this.setPreviousStatement(!0, "Action");
    this.setNextStatement(!0, "Action");
    this.inputList[1].setCheck("Action"); //Disallow event action blocks to be in body

    var input = this.inputList[0];
    var field = input.fieldRow[1];
    field.changeHandler_ = function (text) {
      var n = Blockly.FieldTextInput.numberValidator(text);
      if (n) {
        n = String(Math.min(Math.max(0, Math.floor(n)), 20));
      }
      return n;
    };
  };

  // Make 'not' taller
  var notBlock = Blockly.Blocks["logic_negate"];
  var originalNotInit = notBlock.init;
  notBlock.init = function () {
    originalNotInit.call(this);
    this.inputList[0].appendField(
      new Blockly.FieldImage(
        ocargo.Drawing.imageDir + "empty.svg",
        ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH,
        ocargo.BlocklyControl.BLOCK_HEIGHT
      )
    );
  };
}

function initCustomBlocksPython() {
  Blockly.Python["start"] = function (block) {
    return "";
  };

  Blockly.Python["move_forwards"] = function (block) {
    return "my_van.move_forwards()\n";
  };

  Blockly.Python["turn_left"] = function (block) {
    return "my_van.turn_left()\n";
  };

  Blockly.Python["turn_right"] = function (block) {
    return "my_van.turn_right()\n";
  };

  Blockly.Python["turn_around"] = function (block) {
    return "my_van.turn_around()\n";
  };

  Blockly.Python["wait"] = function (block) {
    return "my_van.wait()\n";
  };

  Blockly.Python["deliver"] = function (block) {
    return "my_van.deliver()\n";
  };

  Blockly.Python["sound_horn"] = function (block) {
    return "my_van.sound_horn()\n";
  };

  Blockly.Python["road_exists"] = function (block) {
    if (block.inputList[0].fieldRow[1].value_ === "FORWARD") {
      var python = "my_van.is_road_forward()";
    } else if (block.inputList[0].fieldRow[1].value_ === "LEFT") {
      var python = "my_van.is_road_left()";
    } else {
      var python = "my_van.is_road_right()";
    }

    return [python, Blockly.Python.ORDER_NONE];
    // TODO: figure out what this ordering relates to
  };

  Blockly.Python["traffic_light"] = function (block) {
    var python;
    if (block.inputList[0].fieldRow[1].value_ === ocargo.TrafficLight.RED) {
      python = "my_van.is_red_traffic_light()";
    } else {
      python = "my_van.is_green_traffic_light()";
    }

    return [python, Blockly.Python.ORDER_NONE]; //TODO: figure out what this ordering relates to
  };

  Blockly.Python["dead_end"] = function (block) {
    return ["my_van.at_dead_end()", Blockly.Python.ORDER_NONE];
    // TODO: figure out what this ordering relates to
  };

  Blockly.Python["cow_crossing"] = function (block) {
    return ["my_van.is_animal_crossing()", Blockly.Python.ORDER_NONE];
    // TODO: figure out what this ordering relates to
  };

  Blockly.Python["at_destination"] = function (block) {
    return ["my_van.at_destination()", Blockly.Python.ORDER_NONE];
    // TODO: figure out what this ordering relates to;
  };

  Blockly.Python["call_proc"] = function (block) {
    return block.inputList[0].fieldRow[2].text_ + "()\n";
  };

  Blockly.Python["declare_proc"] = function (block) {
    var branch = Blockly.Python.statementToCode(block, "DO");
    return "def " + block.inputList[0].fieldRow[1].text_ + "():\n" + branch;
    // TODO: get code out of sub-blocks (there's a Blockly function for it)
  };

  Blockly.Python["declare_event"] = function (block) {
    // TODO support events in python
    throw "events not supported in python";
  };

  Blockly.Python["controls_repeat_while"] = function (block) {
    var condition = Blockly.Python.valueToCode(
      block,
      "condition",
      Blockly.Python.ORDER_ATOMIC
    );

    condition = condition.replace(/\((.*)\)/, "$1");

    var subBlock = Blockly.Python.statementToCode(block, "body");
    var code = "while " + condition + ":\n" + subBlock;
    return code;
  };

  Blockly.Python["controls_repeat_until"] = function (block) {
    var condition = Blockly.Python.valueToCode(
      block,
      "condition",
      Blockly.Python.ORDER_ATOMIC
    );
    var subBlock = Blockly.Python.statementToCode(block, "body");
    var code = "while not " + condition + ":\n" + subBlock;
    return code;
  };

  Blockly.Python["variables_get"] = function (block) {
    var variableName = block.getFieldValue("NAME");
    return [variableName, Blockly.Python.ORDER_ATOMIC];
  };

  Blockly.Python["variables_set"] = function (block) {
    var variableName = block.getFieldValue("VAR");
    var value = Blockly.Python.valueToCode(
      block,
      "VALUE",
      Blockly.Python.ORDER_NONE
    );
    var code = `${variableName} = ${value}\n`;
    return code;
  };

  Blockly.Python["variables_numeric_set"] = function (block) {
    var variableName = block.getFieldValue("NAME");
    var numberValue = block.getFieldValue("VALUE");
    var code = `${variableName} = ${numberValue}\n`;
    return code;
  };

  Blockly.Python["variables_increment"] = function (block) {
    var variableName = block.getFieldValue("NAME");
    var numberValue = block.getFieldValue("VALUE");
    var code = `${variableName} = ${variableName} + ${numberValue}\n`;
    return code;
  };
}
