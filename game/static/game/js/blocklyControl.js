/*
Code for Life

Copyright (C) 2016, Ocado Innovation Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
'use strict';

var ocargo = ocargo || {};

ocargo.BlocklyControl = function () {
    this.blocklyCustomisations = new ocargo.BlocklyCustomisations();
    this.blocklyCustomisations.setupBigCodeMode();

    this.blocklyDiv = document.getElementById('blockly_holder');
    this.toolbox = document.getElementById('blockly_toolbox');
    Blockly.inject(this.blocklyDiv, {
        path: '/static/game/js/blockly/',
        toolbox: BLOCKLY_XML,
        trashcan: true,
        scrollbars: true
    });

    this.blocklyCustomisations.setupFlyoutToggling(this.blocklyDiv);
    this.blocklyCustomisations.disableContextMenus();

    // Stop the flyout from closing automatically
    Blockly.Flyout.autoClose = false;

    this.blocklyCustomisations.makeFlyoutTransparent();
    this.blocklyCustomisations.shiftBlockly();
    this.blocklyCustomisations.shiftWorkspace();
    this.blocklyCustomisations.hideBlocklyToolbox();
    this.blocklyCustomisations.makeFlyoutButtonTransparent();
};

ocargo.BlocklyControl.BLOCK_HEIGHT = 20;
ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH = 1;
ocargo.BlocklyControl.IMAGE_WIDTH = 20;
ocargo.BlocklyControl.COW_WIDTH = 30;
ocargo.BlocklyControl.BLOCK_CHARACTER_HEIGHT = 20;
ocargo.BlocklyControl.BLOCK_CHARACTER_WIDTH = 40;

ocargo.BlocklyControl.prototype.incorrectBlock = null;
ocargo.BlocklyControl.prototype.incorrectBlockColour = null;

ocargo.BlocklyControl.prototype.prepare = function(blocks) {
    try {
        return {
            success:true,
            program: blocks? ocargo.blocklyCompiler.mobileCompile(blocks) : ocargo.blocklyCompiler.compile()
        };
    } catch (error) {
        return {
            success:false,
            error: gettext('Your program doesn\'t look quite right...') + "<br><br>" + gettext(error)
        };
    }
};

ocargo.BlocklyControl.prototype.redrawBlockly = function() {
    Blockly.fireUiEvent(window, 'resize');
};

ocargo.BlocklyControl.prototype.clearIncorrectBlock = function () {
    this.incorrectBlock = null;
}

ocargo.BlocklyControl.prototype.reset = function() {
    Blockly.mainWorkspace.clear();

    var startBlock = this.createBlock('start');
    startBlock.moveBy(30+(i%2)*200,30+Math.floor(i/2)*100);
    this.blocklyCustomisations.addClickListenerToStartBlock(startBlock);

    this.clearIncorrectBlock();
};

ocargo.BlocklyControl.prototype.toggleFlyout = function() {
    this.blocklyCustomisations.toggleFlyout();
};

ocargo.BlocklyControl.prototype.bringStartBlockFromUnderFlyout = function() {
    this.blocklyCustomisations.bringStartBlockFromUnderFlyout();
};

ocargo.BlocklyControl.prototype.enableBigCodeMode = function() {
    this.bigCodeMode = true;
    this.blocklyCustomisations.enableBigCodeMode();
};

ocargo.BlocklyControl.prototype.disableBigCodeMode =  function() {
    this.bigCodeMode = false;
    this.blocklyCustomisations.disableBigCodeMode();
};


ocargo.BlocklyControl.prototype.teardown = function() {
    if (localStorage && !ANONYMOUS) {
        var text = this.serialize();
        try {
            if (NIGHT_MODE) {
                localStorage.setItem('blocklyNightModeWorkspaceXml-' + LEVEL_ID, text);
            } else {
                localStorage.setItem('blocklyWorkspaceXml-' + LEVEL_ID, text);
            }
        } catch (e) {
            // No point in even logging, as page is unloading
        }
    }
};

ocargo.BlocklyControl.prototype.deserialize = function(text) {
    try {
        var oldXml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);

        var newXml = Blockly.Xml.textToDom(text);
        Blockly.mainWorkspace.clear();
        Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, newXml);
        var legal = this.removeIllegalBlocks();

        if (!legal) {
            ocargo.Drawing.startPopup(
                gettext('Loading workspace'),
                "",
                gettext('Sorry, this workspace has blocks in it that aren\'t allowed in this level!'),
                true
            );
            Blockly.mainWorkspace.clear();
            Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, oldXml);
        }
        this.blocklyCustomisations.addClickListenerToStartBlock(this.startBlock());
    } catch (e) {
        console.log(e);
        this.reset();
    }
};

ocargo.BlocklyControl.prototype.serialize = function() {
    var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
    return Blockly.Xml.domToText(xml);
};

ocargo.BlocklyControl.prototype.removeIllegalBlocks = function() {
    // Buggy blockly doesn't serialise properly on Safari.
    var isSafari = navigator.userAgent.indexOf('Safari') !== -1 &&
                    navigator.userAgent.indexOf('Chrome') === -1;

    var blocks = Blockly.mainWorkspace.getAllBlocks();
    blocks.sort(function(a, b) {
        return a.id - b.id;
    });

    var startCount = 1;
    var clean = true;

    for (var i = 0; i < blocks.length; i++) {
        var block = blocks[i];

        if (block.type !== 'start') {
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

ocargo.BlocklyControl.prototype.setCodeChangesAllowed = function(changesAllowed) {
    this.blocklyDiv.style.pointerEvents = changesAllowed ? "" : "none";
};

ocargo.BlocklyControl.prototype.loadPreviousAttempt = function() {
    function decodeHTML(text) {
        var e = document.createElement('div');
        e.innerHTML = text;
        return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
    }
    // Use the user's last attempt if available, else use whatever's in local storage
    if (WORKSPACE) {
        this.deserialize(decodeHTML(WORKSPACE));
    } else {
        if (NIGHT_MODE) {
            this.deserialize(localStorage.getItem('blocklyNightModeWorkspaceXml-' + LEVEL_ID));
        } else {
            this.deserialize(localStorage.getItem('blocklyWorkspaceXml-' + LEVEL_ID));
        }
    }

    this.redrawBlockly();
};

ocargo.BlocklyControl.prototype.createBlock = function(blockType) {
    var block = Blockly.Block.obtain(Blockly.mainWorkspace, blockType);
    block.initSvg();
    block.render();
    return block;
};

ocargo.BlocklyControl.prototype.addBlockToEndOfProgram = function(blockType) {
    var blockToAdd = this.createBlock(blockType);

    var block = this.startBlock();
    while (block.nextConnection.targetBlock()) {
        block = block.nextConnection.targetBlock();
    }

    block.nextConnection.connect(blockToAdd.previousConnection);
};

ocargo.BlocklyControl.prototype.disconnectedStartBlock = function() {
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

ocargo.BlocklyControl.prototype.startBlock = function() {
    return Blockly.mainWorkspace.getTopBlocks().filter(function (block) {
        return block.type === 'start';
    })[0];
};

ocargo.BlocklyControl.prototype.procedureBlocks = function() {
    return Blockly.mainWorkspace.getTopBlocks().filter(function (block) {
        return block.type === 'declare_proc';
    });
};

ocargo.BlocklyControl.prototype.onEventDoBlocks = function() {
    // find and return all top blocks that are event handler blocks
    var startBlocks = [];
    Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
        if (block.type === 'declare_event') {
            startBlocks.push(block);
        }
    });
    return startBlocks;
};

ocargo.BlocklyControl.prototype.totalBlocksCount = function() {
    return Blockly.mainWorkspace.getAllBlocks().length;
};

ocargo.BlocklyControl.prototype.activeBlocksCount = function() {
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

        if (block.type === 'controls_repeat_until' || block.type === 'controls_repeat_while' ||
            block.type === 'controls_whileUntil') {
            var conditionBlock = block.inputList[0].connection.targetBlock();
            n += count(conditionBlock);
            var bodyBlock = block.inputList[1].connection.targetBlock();
            n += count(bodyBlock);
            var nextBlock = block.nextConnection.targetBlock();
            n += count(nextBlock);
        } else if (block.type === 'controls_repeat') {
            var bodyBlock = block.inputList[1].connection.targetBlock();
            n += count(bodyBlock);
            var nextBlock = block.nextConnection.targetBlock();
            n += count(nextBlock);
        } else if (block.type === 'controls_if') {
            var elseCount = block.elseCount_ || 0;

            for (var i = 0; i < block.inputList.length - elseCount; i++) {
                var input = block.inputList[i];
                if (input.name.indexOf('IF') === 0) {
                    var conditionBlock = input.connection.targetBlock();
                    n += count(conditionBlock);
                } else if (input.name.indexOf('DO') === 0) {
                    var bodyBlock = input.connection.targetBlock();
                    n += count(bodyBlock);
                }
            }

            if (elseCount === 1) {
                var elseBlock = block.inputList[block.inputList.length - 1]
                                     .connection.targetBlock();
                n += count(elseBlock);
            }

            var nextBlock = block.nextConnection.targetBlock();
            n += count(nextBlock);
        } else if (block.type === 'call_proc' || block.type === 'move_forwards' ||
                 block.type === 'turn_left' || block.type === 'turn_right' ||
                 block.type === 'turn_around' || block.type === 'wait' ||
                 block.type === 'deliver') {
            var nextBlock = block.nextConnection.targetBlock();
            n += count(nextBlock);
        } else if (block.type === 'logic_negate') {
            var conditionBlock = block.inputList[0].connection.targetBlock();
            n += count(conditionBlock);
        }

        return n;
    }
};

/************************/
/** Block highlighting **/
/************************/

// Define custom select methods that select a block and its inputs
ocargo.BlocklyControl.prototype.setBlockSelected = function(block, selected) {
    if (!block instanceof Blockly.BlockSvg) {
        return;
    }

    block.inputList.forEach(function(input) {
        if (input.connection && input.type !== Blockly.NEXT_STATEMENT) {
            var targetBlock = input.connection.targetBlock();
            if (targetBlock) {
                this.setBlockSelected(targetBlock, selected);
            }
        }
    }.bind(this));

    if (selected) {
        block.addSelect();
    } else {
        block.removeSelect();
    }
};

ocargo.BlocklyControl.prototype.clearAllSelections = function() {
    Blockly.mainWorkspace.getAllBlocks().forEach(function (block) {
            if(!block.keepHighlighting){
                this.setBlockSelected(block, false);
            }
        }.bind(this));
};

ocargo.BlocklyControl.prototype.highlightIncorrectBlock = function(incorrectBlock) {
    var frequency = 300;
    var repeats = 3;

    this.incorrectBlock = incorrectBlock;
    this.incorrectBlockColour = incorrectBlock.getColour();

    this.incorrectBlock.setColour(0);
    for (var i = 0; i < repeats; i++) {
        window.setTimeout(function () {
            if (this.incorrectBlock) {
                this.setBlockSelected(incorrectBlock, true);
            }
        }.bind(this), 2 * i * frequency);
        window.setTimeout(function () {
            if (this.incorrectBlock) {
                this.setBlockSelected(incorrectBlock, false);
            }
        }.bind(this), (2 * i + 1) * frequency);
    }
};

ocargo.BlocklyControl.tryCatchSilently = function (f) {
    return function() {
        try {
            f();
        } catch (e) {
            // Nothing
        }
    };
};

ocargo.BlocklyControl.prototype.resetIncorrectBlock = function() {
    if (this.incorrectBlock) {
        this.incorrectBlock.setColour(this.incorrectBlockColour);
    }
};


ocargo.BlockHandler = function(id) {
    this.id = id;
    this.selectedBlock = null;
};

ocargo.BlockHandler.prototype.selectBlock = function(block) {
    if (block) {
        this.deselectCurrent();
        this.setBlockSelected(block, true);
        this.selectedBlock = block;
    }
};

ocargo.BlockHandler.prototype.deselectCurrent = function() {
    if (this.selectedBlock) {
        this.setBlockSelected(this.selectedBlock, false);
        this.selectedBlock = null;
    }
};
