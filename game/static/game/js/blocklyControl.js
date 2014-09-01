'use strict';

var ocargo = ocargo || {};

ocargo.BlocklyControl = function () {
    this.blocklyDiv = document.getElementById('blockly_holder');
    this.toolbox = document.getElementById('blockly_toolbox');


    Blockly.inject(this.blocklyDiv, {
        path: '/static/game/js/blockly/',
        toolbox: BLOCKLY_XML,
        trashcan: true
    });

    // Disable the right-click context menus
    Blockly.showContextMenu_ = function(e) {};
    Blockly.Block.prototype.showContextMenu_ = function(e) {};

    this.numberOfStartBlocks = THREADS;
    
    // Needed so that the size of the flyout is available
    // for when toggle flyout is first called
    Blockly.Toolbox.tree_.firstChild_.onMouseDown();
    this.flyoutWidth = $('.blocklyFlyoutBackground')[0].getBoundingClientRect().width;
    Blockly.Toolbox.tree_.firstChild_.onMouseDown();
    this.flyoutOut = false;
    Blockly.Flyout.autoClose = false;
};

ocargo.BlocklyControl.BLOCK_HEIGHT = 20;
ocargo.BlocklyControl.EXTRA_BLOCK_WIDTH = 1;
ocargo.BlocklyControl.IMAGE_WIDTH = 20; 
ocargo.BlocklyControl.BLOCK_CHARACTER_HEIGHT = CHARACTER_HEIGHT;
ocargo.BlocklyControl.BLOCK_CHARACTER_WIDTH = CHARACTER_WIDTH;

ocargo.BlocklyControl.prototype.incorrectBlock = null;
ocargo.BlocklyControl.prototype.incorrectBlockColour = null;

ocargo.BlocklyControl.prototype.prepare = function() {
    try {
        return {success:true, program: ocargo.blocklyCompiler.compile()};
    }
    catch (error) {
        return {success:false, error: ocargo.messages.compilationError + "<br><br>" + error};
    }
};

ocargo.BlocklyControl.prototype.redrawBlockly = function() {
    Blockly.fireUiEvent(window, 'resize');
};

ocargo.BlocklyControl.prototype.reset = function() {
    Blockly.mainWorkspace.clear();

    this.numberOfStartBlocks = THREADS;

    for (var i = 0; i < THREADS; i++) {
        var startBlock = this.createBlock('start');
        startBlock.moveBy(30+(i%2)*200,30+Math.floor(i/2)*100);
    }
};

ocargo.BlocklyControl.prototype.toggleFlyout = function() {
    Blockly.Toolbox.tree_.firstChild_.onMouseDown();
    this.flyoutOut = !this.flyoutOut;
    $('#flyoutButton').attr('src', imgSrc);
    $('#flyoutButton').css('left', (this.flyoutOut ? (this.flyoutWidth-4)  : 0) +  'px');
    var imgSrc = ocargo.Drawing.imageDir + 'icons/' + (this.flyoutOut ? 'hide' : 'show') + '.svg';
    $('#flyoutButton img').attr('src', imgSrc);
}

ocargo.BlocklyControl.prototype.bringStartBlockFromUnderFlyout = function() {
    Blockly.mainWorkspace.scrollbar.hScroll.set(this.blocklyDiv.offsetWidth - 455);
    Blockly.mainWorkspace.scrollbar.vScroll.set(this.blocklyDiv.offsetWidth - 15);
}

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
        var oldXml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);

        var newXml = Blockly.Xml.textToDom(text);
        Blockly.mainWorkspace.clear();
        Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, newXml);
        var legal = ocargo.blocklyControl.removeIllegalBlocks();

        if(!legal) {
            ocargo.Drawing.startPopup("Loading workspace", "", ocargo.messages.illegalBlocks + ocargo.jsElements.closebutton("Close"), true);
            Blockly.mainWorkspace.clear();
            Blockly.Xml.domToWorkspace(Blockly.mainWorkspace, oldXml);
        }
    } 
    catch (e) {
        ocargo.blocklyControl.reset();
    }
};

ocargo.BlocklyControl.prototype.serialize = function() {
    var xml = Blockly.Xml.workspaceToDom(Blockly.mainWorkspace);
    var text = Blockly.Xml.domToText(xml);
    return text;

};

ocargo.BlocklyControl.prototype.removeIllegalBlocks = function() {

    // Buggy blockly doesn't serialise properly on Safari.
    var isSafari = navigator.userAgent.indexOf('Safari') !== -1 &&
                    navigator.userAgent.indexOf('Chrome') === -1;

    var blocks = Blockly.mainWorkspace.getAllBlocks();
    blocks.sort(function(a, b) {
        return a.id - b.id;
    });
    var startCount = this.numberOfStartBlocks;
    var block;
    for (var i = 0; i < blocks.length; i++) {
        block = blocks[i];
        if (BLOCKS.indexOf(block.type) === -1 && block.type !== 'start') {
            block.dispose();
            return false;
        }
        if(isSafari && block.type === 'start') {
            if (startCount > 0) {
                startCount--;
            } else {
                block.dispose();
            }
        }
    }
    return true;
};

ocargo.BlocklyControl.prototype.setCodeChangesAllowed = function(changesAllowed) {
    var setting = "";
    if (!changesAllowed) {
        setting = "none";
    }
    this.blocklyDiv.style.pointerEvents = setting;
}

ocargo.BlocklyControl.prototype.loadPreviousAttempt = function() {
    function decodeHTML(text) {
        var e = document.createElement('div');
        e.innerHTML = text;
        return e.childNodes.length === 0 ? "" : e.childNodes[0].nodeValue;
    }

    // Use the user's last attempt if available, else use whatever's in local storage
    if (WORKSPACE) {
        ocargo.blocklyControl.deserialize(decodeHTML(WORKSPACE));
    }
    else {
        ocargo.blocklyControl.deserialize(localStorage.getItem('blocklyWorkspaceXml-' + LEVEL_ID));
    }

    ocargo.blocklyControl.redrawBlockly();
};

ocargo.BlocklyControl.prototype.createBlock = function(blockType) {
    var block = Blockly.Block.obtain(Blockly.mainWorkspace, blockType);
    block.initSvg();
    block.render();
    return block;
};

ocargo.BlocklyControl.prototype.addBlockToEndOfProgram = function(blockType) {
    var blockToAdd = this.createBlock(blockType);

    var block = this.getStartBlocks()[0];
    while (block.nextConnection.targetBlock()) {
        block = block.nextConnection.targetBlock();
    }

    block.nextConnection.connect(blockToAdd.previousConnection);
};

ocargo.BlocklyControl.prototype.getStartBlocks = function() {
    var startBlocks = [];
    Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
        if (block.type === 'start') {
            startBlocks.push(block);
        }
    });
    return startBlocks;
};

ocargo.BlocklyControl.prototype.getProcedureBlocks = function() {
    var startBlocks = [];
    Blockly.mainWorkspace.getTopBlocks().forEach(function (block) {
        if (block.type === 'declare_proc') {
            startBlocks.push(block);
        }
    });
    return startBlocks;
};

ocargo.BlocklyControl.prototype.getTotalBlocksCount = function() {
    return Blockly.mainWorkspace.getAllBlocks().length;
};

ocargo.BlocklyControl.prototype.getActiveBlocksCount = function() {
    var startBlocks = this.getStartBlocks();
    var procedureBlocks = this.getProcedureBlocks();
    var n = 0;
    var i;

    for(i = 0; i < startBlocks.length; i++) {
        n += count(startBlocks[i].nextConnection.targetBlock());
    }

    for(i = 0; i < procedureBlocks.length; i++) {
        n += 1 + count(procedureBlocks[i].inputList[1].connection.targetBlock());
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
        } 
        else if (block.type === 'controls_repeat') {
            var bodyBlock = block.inputList[1].connection.targetBlock();
            n += count(bodyBlock);
            var nextBlock = block.nextConnection.targetBlock();
            n += count(nextBlock);
        } 
        else if (block.type === 'controls_if') {
            for (var i = 0; i < block.inputList.length - block.elseCount_; i++) {
                var input = block.inputList[i];
                if (input.name.indexOf('IF') === 0) {
                    var conditionBlock = input.connection.targetBlock();
                    n += count(conditionBlock);
                } else if (input.name.indexOf('DO') === 0) {
                    var bodyBlock = input.connection.targetBlock();
                    n += count(bodyBlock);
                }
            }

            if (block.elseCount_ === 1) {
                var elseBlock = block.inputList[block.inputList.length - 1].connection.targetBlock();
                n += count(elseBlock);
            }

            var nextBlock = block.nextConnection.targetBlock();
            n += count(nextBlock);
        } 
        else if (block.type === 'call_proc' || block.type === 'move_forwards' ||
                 block.type === 'turn_left' || block.type === 'turn_right' ||
                 block.type === 'turn_around' || block.type === 'wait' ||
                 block.type === 'deliver') {
            var nextBlock = block.nextConnection.targetBlock();
            n += count(nextBlock);
        } 
        else if (block.type === 'logic_negate') {
            var conditionBlock = block.inputList[0].connection.targetBlock();
            n += count(conditionBlock);
        }
        
        return n;
    }
};


/*******************/
/** Big Code Mode **/
/*******************/

ocargo.BlocklyControl.prototype.resetWidthOnBlocks = function(blocks) {
	for (var i = 0; i < blocks.length; i++) {
		var block = blocks[i];
		for (var j = 0; j < block.inputList.length; j++) {
			var input = block.inputList[j];
			for (var k = 0; k < input.fieldRow.length; k++) {
			    var field = input.fieldRow[k];
				field.size_.width = null;
				if (field.imageElement_) {
			        field.height_ = field.imageElement_.height.baseVal.value;
			        field.width_ = field.imageElement_.width.baseVal.value;
				}
			}
		}
	}
};

//so that image fields render properly when their size_ variable is broken above
Blockly.FieldImage.prototype.render_ = function() {
    this.size_ = {height: this.height_ + 10, width: this.width_};
};

ocargo.BlocklyControl.prototype.increaseBlockSize = function() {
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
    ocargo.blocklyControl.BLOCK_CHARACTER_HEIGHT *= 2;
    ocargo.blocklyControl.BLOCK_CHARACTER_WIDTH *= 2;    
    ocargo.blocklyControl.BLOCK_HEIGHT *= 2;

	document.styleSheets[0].insertRule(".blocklyText, .beaconClass" + ' { font-size' + ':'+'22pt !important'+'}', document.styleSheets[0].cssRules.length);
	document.styleSheets[0].insertRule(".blocklyIconMark, .beaconClass" + ' { font-size' + ':'+'18pt !important'+'}', document.styleSheets[0].cssRules.length);
	var blocks = Blockly.mainWorkspace.getAllBlocks();
    $(".blocklyDraggable > g > image").each( function(index, element) {
    	var jQueryElement = $(element);
    	var heightStr = jQueryElement.attr("height");
    	var heightNumber = parseInt(heightStr.substring(0, heightStr.length - 2));
    	var widthStr = jQueryElement.attr("width");
    	var widthNumber = parseInt(widthStr.substring(0, widthStr.length - 2));
    	jQueryElement.attr("height", heightNumber * 2 + "px");
    	jQueryElement.attr("width", widthNumber * 2 + "px");
    	jQueryElement.attr("y", -32);
    });
    ocargo.blocklyControl.resetWidthOnBlocks(blocks);
    Blockly.mainWorkspace.render();

	Blockly.Toolbox.flyout_.show(Blockly.languageTree.childNodes);
	
    $(".blocklyIconShield").attr("width", 32).attr("height", 32).attr("rx", 8).attr("ry", 8);
    $(".blocklyIconMark").attr("x", 16).attr("y", 24);
    $(".blocklyEditableText > rect").attr("height", 32).attr("y", -24).attr("x", -5).attr("width", 85);  
};

ocargo.BlocklyControl.prototype.decreaseBlockSize = function() {
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
    ocargo.blocklyControl.BLOCK_CHARACTER_HEIGHT /= 2;
    ocargo.blocklyControl.BLOCK_CHARACTER_WIDTH /= 2;  
    ocargo.blocklyControl.BLOCK_HEIGHT /= 2;

    var sheet = document.styleSheets[0];
	for (var i = 0; i < 2; i++) {
	    sheet.deleteRule(sheet.cssRules.length-1);
	}

	var blocks = Blockly.mainWorkspace.getAllBlocks();
    
    $(".blocklyDraggable > g > image").each( function(index, element) {
    	var jQueryElement = $(element);
    	var heightStr = jQueryElement.attr("height");
    	var heightNumber = parseInt(heightStr.substring(0, heightStr.length - 2));
    	var widthStr = jQueryElement.attr("width");
    	var widthNumber = parseInt(widthStr.substring(0, widthStr.length - 2));
    	jQueryElement.attr("height", heightNumber / 2 + "px");
    	jQueryElement.attr("width", widthNumber / 2 + "px");
    	jQueryElement.attr("y", -12);
    });
    ocargo.blocklyControl.resetWidthOnBlocks(blocks);
    Blockly.mainWorkspace.render();

	Blockly.Toolbox.flyout_.show(Blockly.languageTree.childNodes);
    $(".blocklyIconShield").attr("width", 16).attr("height", 16).attr("rx", 4).attr("ry", 4);
    $(".blocklyIconMark").attr("x", 8).attr("y", 12);
    $(".blocklyEditableText > rect").attr("height", 16).attr("y", -12).attr("x", -5).attr("width", 43);
};

/************************/
/** Block highlighting **/
/************************/

// Define custom select methods that select a block and its inputs
ocargo.BlocklyControl.prototype.setBlockSelected = function(block, selected) {
    if (!block.svg_) {
        return;
    }

    block.inputList.forEach(function(input) {
        if (input.connection && input.type !== Blockly.NEXT_STATEMENT) {
            var targetBlock = input.connection.targetBlock();
            if (targetBlock) {
                ocargo.blocklyControl.setBlockSelected(targetBlock, selected);
            }
        }
    });

    if (selected) {
        block.svg_.addSelect();
    } else {
        block.svg_.removeSelect();
    }
};

ocargo.BlocklyControl.prototype.clearAllSelections = function() {
    Blockly.mainWorkspace.getAllBlocks().forEach(
        function (block) {
            ocargo.blocklyControl.setBlockSelected(block, false);
        }
    );
};

ocargo.BlocklyControl.prototype.highlightIncorrectBlock = function(incorrectBlock) {
    var blocklyControl = this;
    var frequency = 300;
    var repeats = 3;

    this.incorrectBlock = incorrectBlock;
    this.incorrectBlockColour = incorrectBlock.getColour();

    incorrectBlock.setColour(0);
    for (var i = 0; i < repeats; i++) {
        window.setTimeout(function() { blocklyControl.setBlockSelected(incorrectBlock, true); }, 2 * i * frequency);
        window.setTimeout(function() { blocklyControl.setBlockSelected(incorrectBlock, false); }, (2 * i + 1) * frequency);
    }
};

ocargo.BlocklyControl.prototype.resetIncorrectBlock = function() {
    if (this.incorrectBlock) {
        this.incorrectBlock.setColour(ocargo.blocklyControl.incorrectBlockColour);
    }
};


ocargo.BlockHandler = function(id) {
    this.id = id;
    this.selectedBlock = null;
};

ocargo.BlockHandler.prototype.selectBlock = function(block) {
    if (block) {
        this.deselectCurrent();
        ocargo.blocklyControl.setBlockSelected(block, true);
        this.selectedBlock = block;
    }
};

ocargo.BlockHandler.prototype.deselectCurrent = function() {
    if (this.selectedBlock) {
        ocargo.blocklyControl.setBlockSelected(this.selectedBlock, false);
        this.selectedBlock = null;
    }
};
