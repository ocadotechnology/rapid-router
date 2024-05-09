"use strict";

var ocargo = ocargo || {};

ocargo.BlocklyControl = function () {
  this.blocklyCustomisations = new ocargo.BlocklyCustomisations();
  this.blocklyCustomisations.setupDoubleclick();
  this.blocklyCustomisations.setupLimitedBlocks();
  this.blocklyDiv = document.getElementById("blockly_holder");
  this.toolbox = document.getElementById("blockly_toolbox");

  Blockly.inject(this.blocklyDiv, {
    path: "/static/game/js/blockly/",
    toolbox: BLOCKLY_XML,
    trashcan: true,
    scrollbars: true,
    maxInstances: maxInstances,
  });

  // Stop the flyout from closing automatically
  Blockly.Flyout.autoClose = false;

  this.blocklyCustomisations.addLimitedBlockListeners(Blockly.mainWorkspace);
  this.blocklyCustomisations.addClickListenerToStartBlock();
};

ocargo.BlocklyControl.BLOCK_HEIGHT = 20;
ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH = 1;
ocargo.BlocklyControl.IMAGE_WIDTH = 20;
ocargo.BlocklyControl.COW_WIDTH = 30;
ocargo.BlocklyControl.BLOCK_CHARACTER_HEIGHT = 20;
ocargo.BlocklyControl.BLOCK_CHARACTER_WIDTH = 40;

ocargo.BlocklyControl.prototype.incorrectBlock = null;
ocargo.BlocklyControl.prototype.incorrectBlockColour = null;

ocargo.BlocklyControl.prototype.prepare = function (blocks) {
  try {
    return {
      success: true,
      program: blocks
        ? ocargo.blocklyCompiler.mobileCompile(blocks)
        : ocargo.blocklyCompiler.compile(),
    };
  } catch (error) {
    return {
      success: false,
      error:
        gettext("Your program doesn't look quite right...") +
        "<br><br>" +
        gettext(error),
    };
  }
};

ocargo.BlocklyControl.prototype.redrawBlockly = function () {
  Blockly.svgResize(Blockly.mainWorkspace);
};

ocargo.BlocklyControl.prototype.clearIncorrectBlock = function () {
  this.incorrectBlock = null;
};

function wasGameStarted(blocks) {
  let gameStarted = false;
  for (let block of blocks) {
    if (block.type == "start") gameStarted = true;
  }
  return gameStarted;
}

ocargo.BlocklyControl.prototype.reset = function () {
  let allBlocks = Blockly.mainWorkspace.getAllBlocks();

  for (let block of allBlocks) {
    if (block.type != "start") block.dispose(true);
  }

  // Each time a game starts the clear function is called.
  // Therefore a simple check is preformed to see if the level
  // has a start button, if not then create a start button
  if (!wasGameStarted(allBlocks)) {
    let startBlock = this.createBlock("start");
    // Generate the first block on the (100, 100) position
    startBlock.moveBy(100, 100);
  }

  this.clearIncorrectBlock();
};

ocargo.BlocklyControl.prototype.deserialize = function (text) {
  try {
    var oldXml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);

    var newXml = Blockly.Xml.textToDom(text);
    Blockly.mainWorkspace.clear();
    Blockly.Xml.domToWorkspace(newXml, Blockly.mainWorkspace);
    var legal = this.removeIllegalBlocks();

    if (!legal) {
      ocargo.Drawing.startPopup(
        gettext("Loading workspace"),
        "",
        gettext(
          "Sorry, this workspace has blocks in it that aren't allowed in this level!"
        ),
        true
      );
      Blockly.mainWorkspace.clear();
      Blockly.Xml.domToWorkspace(oldXml, Blockly.mainWorkspace);
    }
  } catch (e) {
    console.log(e);
    this.reset();
  }
};

ocargo.BlocklyControl.prototype.serialize = function () {
  var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
  return Blockly.Xml.domToText(xml);
};

ocargo.BlocklyControl.prototype.removeIllegalBlocks = function () {
  // Buggy blockly doesn't serialise properly on Safari.
  var isSafari =
    navigator.userAgent.indexOf("Safari") !== -1 &&
    navigator.userAgent.indexOf("Chrome") === -1;

  var blocks = Blockly.mainWorkspace.getAllBlocks();
  blocks.sort(function (a, b) {
    return a.id - b.id;
  });

  var startCount = 1;
  var clean = true;

  for (var i = 0; i < blocks.length; i++) {
    var block = blocks[i];

    if (block.type !== "start") {
      var found = false;
      for (var j = 0; j < BLOCKS.length; j++) {
        if (BLOCKS[j].type == block.type) {
          found = true;
          break;
        }
      }

      if (!found) {
        clean = false;
        block.dispose();
      }
    } else {
      startCount--;
      if (isSafari && startCount < 0) {
        block.dispose();
      }
    }
  }
  if (startCount > 0) {
    this.reset();
    return true;
  }
  return clean;
};

ocargo.BlocklyControl.prototype.setCodeChangesAllowed = function (
  changesAllowed
) {
  this.blocklyDiv.style.pointerEvents = changesAllowed ? "" : "none";
};

ocargo.BlocklyControl.prototype.loadPreviousAttempt = function () {
  function decodeHTML(text) {
    var e = document.createElement("div");
    e.innerHTML = text;
    return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
  }
  // Use the user's last attempt if available
  if (WORKSPACE) {
    this.deserialize(decodeHTML(WORKSPACE));
  }

  this.redrawBlockly();
};

ocargo.BlocklyControl.prototype.createBlock = function (blockType) {
  var block = Blockly.mainWorkspace.newBlock(blockType);
  // var block = Blockly.Block.obtain(Blockly.mainWorkspace, blockType);
  block.initSvg();
  block.render();
  return block;
};

ocargo.BlocklyControl.prototype.addBlockToEndOfProgram = function (blockType) {
  var blockToAdd = this.createBlock(blockType);

  var block = this.startBlock();
  while (block.nextConnection.targetBlock()) {
    block = block.nextConnection.targetBlock();
  }

  block.nextConnection.connect(blockToAdd.previousConnection);
};

ocargo.BlocklyControl.prototype.disconnectedStartBlock = function () {
  var emptyStart = this.startBlock().getChildren().length == 0;
  if (emptyStart) {
    if (this.totalBlocksCount() > 1) {
      return true;
    } else {
      return false;
    }
  } else {
    return false;
  }
};

ocargo.BlocklyControl.prototype.startBlock = function () {
  return Blockly.mainWorkspace.getTopBlocks().filter(function (block) {
    return block.type === "start";
  })[0];
};

ocargo.BlocklyControl.prototype.procedureBlocks = function () {
  return Blockly.mainWorkspace.getTopBlocks().filter(function (block) {
    return block.type === "declare_proc";
  });
};

ocargo.BlocklyControl.prototype.onEventDoBlocks = function () {
  // find and return all top blocks that are event handler blocks
  var startBlocks = [];
  Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
    if (block.type === "declare_event") {
      startBlocks.push(block);
    }
  });
  return startBlocks;
};

ocargo.BlocklyControl.prototype.totalBlocksCount = function () {
  return Blockly.mainWorkspace.getAllBlocks().length;
};

ocargo.BlocklyControl.prototype.activeBlocksCount = function () {
  var startBlock = this.startBlock();
  var procedureBlocks = this.procedureBlocks();
  var eventBlocks = this.onEventDoBlocks();
  var n = 0;
  var i;

  n += count(startBlock.nextConnection.targetBlock());

  // 1 includes the procedure declaration block
  for (i = 0; i < procedureBlocks.length; i++) {
    n += 1 + count(procedureBlocks[i].inputList[1].connection.targetBlock());
  }

  // 1 includes the on-event-do block
  for (i = 0; i < eventBlocks.length; i++) {
    n += 1 + count(eventBlocks[i].inputList[1].connection.targetBlock());
  }

  return n;

  function count(block) {
    if (!block) {
      return 0;
    }

    var n = 1;

    if (
      block.type === "controls_repeat_until" ||
      block.type === "controls_repeat_while" ||
      block.type === "controls_whileUntil"
    ) {
      var conditionBlock = block.inputList[0].connection.targetBlock();
      n += count(conditionBlock);
      var bodyBlock = block.inputList[1].connection.targetBlock();
      n += count(bodyBlock);
      var nextBlock = block.nextConnection.targetBlock();
      n += count(nextBlock);
    } else if (block.type === "controls_repeat") {
      var bodyBlock = block.inputList[1].connection.targetBlock();
      n += count(bodyBlock);
      var nextBlock = block.nextConnection.targetBlock();
      n += count(nextBlock);
    } else if (block.type === "controls_if") {
      var elseCount = block.elseCount_ || 0;

      for (var i = 0; i < block.inputList.length - elseCount; i++) {
        var input = block.inputList[i];
        if (input.name.indexOf("IF") === 0) {
          var conditionBlock = input.connection.targetBlock();
          n += count(conditionBlock);
        } else if (input.name.indexOf("DO") === 0) {
          var bodyBlock = input.connection.targetBlock();
          n += count(bodyBlock);
        }
      }

      if (elseCount === 1) {
        var elseBlock =
          block.inputList[block.inputList.length - 1].connection.targetBlock();
        n += count(elseBlock);
      }

      var nextBlock = block.nextConnection.targetBlock();
      n += count(nextBlock);
    } else if (
      block.type === "call_proc" ||
      block.type === "move_forwards" ||
      block.type === "turn_left" ||
      block.type === "turn_right" ||
      block.type === "turn_around" ||
      block.type === "wait" ||
      block.type === "deliver" ||
      block.type === "variables_numeric_set" ||
      block.type === "variables_increment"
    ) {
      var nextBlock = block.nextConnection.targetBlock();
      n += count(nextBlock);
    } else if (block.type === "logic_negate" || block.type === "logic_compare") {
      var conditionBlock = block.inputList[0].connection.targetBlock();
      n += count(conditionBlock);
    } else if (block.type === "variables_get" || block.type === "math_number") {
      n++
    }

    return n;
  }
};

/************************/
/** Block highlighting **/
/************************/

// Define custom select methods that select a block and its inputs
ocargo.BlocklyControl.prototype.setBlockSelected = function (block, selected) {
  if (!block instanceof Blockly.BlockSvg) {
    return;
  }

  block.inputList.forEach(
    function (input) {
      if (input.connection && input.type !== Blockly.NEXT_STATEMENT) {
        var targetBlock = input.connection.targetBlock();
        if (targetBlock) {
          this.setBlockSelected(targetBlock, selected);
        }
      }
    }.bind(this)
  );

  if (selected) {
    block.addSelect();
  } else {
    block.removeSelect();
  }
};

ocargo.BlocklyControl.prototype.clearAllSelections = function () {
  Blockly.mainWorkspace.getAllBlocks().forEach(
    function (block) {
      if (!block.keepHighlighting) {
        this.setBlockSelected(block, false);
      }
    }.bind(this)
  );
};

ocargo.BlocklyControl.prototype.highlightIncorrectBlock = function (
  incorrectBlock
) {
  var frequency = 300;
  var repeats = 3;

  this.incorrectBlock = incorrectBlock;
  this.incorrectBlockColour = incorrectBlock.getColour();

  this.incorrectBlock.setColour(0);
  for (var i = 0; i < repeats; i++) {
    window.setTimeout(
      function () {
        if (this.incorrectBlock) {
          this.setBlockSelected(incorrectBlock, true);
        }
      }.bind(this),
      2 * i * frequency
    );
    window.setTimeout(
      function () {
        if (this.incorrectBlock) {
          this.setBlockSelected(incorrectBlock, false);
        }
      }.bind(this),
      (2 * i + 1) * frequency
    );
  }
};

ocargo.BlocklyControl.tryCatchSilently = function (f) {
  return function () {
    try {
      f();
    } catch (e) {
      // Nothing
    }
  };
};

ocargo.BlocklyControl.prototype.resetIncorrectBlock = function () {
  if (this.incorrectBlock) {
    this.incorrectBlock.setColour(this.incorrectBlockColour);
  }
};

ocargo.BlockHandler = function (id) {
  this.id = id;
  this.selectedBlock = null;
};

ocargo.BlockHandler.prototype.selectBlock = function (block) {
  if (block) {
    this.deselectCurrent();
    this.setBlockSelected(block, true);
    this.selectedBlock = block;
  }
};

ocargo.BlockHandler.prototype.deselectCurrent = function () {
  if (this.selectedBlock) {
    this.setBlockSelected(this.selectedBlock, false);
    this.selectedBlock = null;
  }
};