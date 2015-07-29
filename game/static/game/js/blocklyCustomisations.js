'use strict';

var ocargo = ocargo || {};

ocargo.BlocklyCustomisations = function() {
    var limitedBlocks = false;
    var blockCount = {};

    for (var i = 0; i < BLOCKS.length; i++) {
        var block = BLOCKS[i];
        blockCount[block.type] = block.number;
        limitedBlocks = limitedBlocks || (block.number !== undefined);
    }

    var canAddNewBlock = function(blockType) {
        return blockCount[blockType] === undefined || blockCount[blockType] > 0;
    };

	this.widenFlyout = function() {
	    if (limitedBlocks) {
		    // Override blockly flyout's position function to artificially widen it
		    var oldPositionFunction = Blockly.Flyout.prototype.position_;
		    Blockly.Flyout.prototype.position_ = function() {
		        this.width_ += 50;
		        oldPositionFunction.call(this);
		        this.width_ -= 50;
		    };
		}
	};

    // Override Scrollbar::set to call constrainKnob, in case value is negative
    Blockly.Scrollbar.prototype.set = function(value) {
        // Move the scrollbar slider.
        this.svgKnob_.setAttribute(this.horizontal_ ? 'x' : 'y', this.constrainKnob_(value * this.ratio_));
        this.onScroll_();
    };

	/**
	 * Sets up only having a limited number of blocks
	 * Needs to be called BEFORE blockly is injected
	 */
	this.setupLimitedBlocks = function() {
        var setQuantityText = function(element, blockType) {
            element.textContent = "×" + blockCount[blockType];
        };

        var selectAndSetQuantityText = function(blockType) {
            var element = $('.quantity_text[value="' + blockType + '"]')[0];
            if (element) {
                // Test needed for loading workspaces (when flyout doesn't exist apparently)
                setQuantityText(element, blockType);
            }
        };

	    if (limitedBlocks) {
		    // Override blockly flyout's position function to artificially widen it
		    var oldPositionFunction = Blockly.Flyout.prototype.position_;
		    Blockly.Flyout.prototype.position_ = function() {
		        this.width_ += 50;
		        oldPositionFunction.call(this);
		        this.width_ -= 50;
		    };

		    // Override blockly flyout's show function to add in the quantity text elements
		    var oldShowFunction = Blockly.Flyout.prototype.show;
		    Blockly.Flyout.prototype.show = function(xmlList) {
		        var margin = this.CORNER_RADIUS;

                this.blockQuantities_ = this.blockQuantities_ || [];

		        // Remove current quantity elements
		        for (var i = this.blockQuantities_.length - 1; i >= 0; i--) {
		            goog.dom.removeNode(this.blockQuantities_[i]);
		        }

                this.blockQuantities_ = [];

		        // Creates the blocks that are shown (to calculate correct heights).
		        var blocks = [];
		        var gaps = [];
		        for (var i = 0, xml; xml = xmlList[i]; i++) {
		            if (xml.tagName && xml.tagName.toUpperCase() == 'BLOCK') {
		                blocks.push(Blockly.Xml.domToBlock(this.workspace_, xml));
		                gaps.push(margin * 3);
		            }
		        }

		        // Lay out the quantaties vertically.
		        var cursorY = margin;
		        for (var i = 0; i < blocks.length; i++) {
		            var block = blocks[i];
		            var blockHW = block.getHeightWidth();

		            if (blockCount[block.type] !== undefined) {
		                var attributes = {'width': 30,
			                              'height': 30,
			                              'x': this.width_,
			                              'y': cursorY + 22,
			                              'class': 'quantity_text',
			                              'value': block.type};

		                var element = Blockly.createSvgElement('text', attributes, null);
		                setQuantityText(element, block.type);
                        this.blockQuantities_.push(element);

		                this.workspace_.getCanvas().insertBefore(element, block.getSvgRoot());
		            }

		            cursorY += blockHW.height + gaps[i];
		        }

		        oldShowFunction.call(this, xmlList);
		    };

		    // Override the blockly flyout's createBlockFunction to control block creation
		    var oldCreateBlockFunction = Blockly.Flyout.prototype.createBlockFunc_;
		    Blockly.Flyout.prototype.createBlockFunc_ = function(originBlock) {
		        var func = oldCreateBlockFunction.call(this, originBlock);
		        return function(e) {
		            if (canAddNewBlock(originBlock.type)) {
		                func(e);
		            }
		        };
		    };

            var changeBlockCount = function(blockType, workspace, delta) {
                if (blockType !== "start"  && workspace === Blockly.mainWorkspace && blockCount[blockType] !== undefined) {
                    blockCount[blockType] += delta;
                    selectAndSetQuantityText(blockType);
                }
            };

		    // Override the initialize method to track blocks entering the  workspace
		    var oldInitialize = Blockly.Block.prototype.initialize;
		    Blockly.Block.prototype.initialize = function(workspace, prototypeName) {
		        oldInitialize.call(this, workspace, prototypeName);
                changeBlockCount(this.type, this.workspace, -1);
		    };

		    // Override block dispose method to keep track of blocks leaving the workspace
		    var oldDispose = Blockly.Block.prototype.dispose;
		    Blockly.Block.prototype.dispose = function(healStack, animate, opt_dontRemoveFromWorkspace) {
                changeBlockCount(this.type, this.workspace, 1);
                oldDispose.call(this, healStack, animate, opt_dontRemoveFromWorkspace);
            };
	    }
	};

	/**
	 * Sets up the ability to toggle the flyout
	 * Needs to be called AFTER blockly is injected
	 */
	this.setupFlyoutToggling = function(blocklyDiv) {
		var flyoutOut = false;

		// Needed so that the size of the flyout is available
	    // for when toggle flyout is first called
	    Blockly.Toolbox.tree_.firstChild_.onMouseDown();
	    this.flyoutWidth = $('.blocklyFlyoutBackground')[0].getBoundingClientRect().width;
	    Blockly.Toolbox.tree_.firstChild_.onMouseDown();

		this.toggleFlyout = function() {
		    Blockly.Toolbox.tree_.firstChild_.onMouseDown();
		    this.flyoutOut = !this.flyoutOut;

		    var image;
		    if (this.flyoutOut) {
		        image = 'hide';
		        $('#flyoutButton').css('left', (this.flyoutWidth - 4 ) +  'px');
		    }
		    else {
		        image = 'show';
		        $('#flyoutButton').css('left', '0px');
		    }

		    $('#flyoutButton img').attr('src', ocargo.Drawing.imageDir + 'icons/' + image + '.svg');
		};

		this.bringStartBlockFromUnderFlyout = function() {
		    Blockly.mainWorkspace.scrollbar.hScroll.set(blocklyDiv.offsetWidth - 455);
		    Blockly.mainWorkspace.scrollbar.vScroll.set(blocklyDiv.offsetHeight - 15);
		};
	};

	/**
	 * Sets up big code mode (enlarges blockly)
	 * Needs to be called BEFORE blockly is injected
	 */
	this.setupBigCodeMode =  function(blocks) {

		//so that image fields render properly when their size_ variable is broken above
		Blockly.FieldImage.prototype.render_ = function() {
		    this.size_ = {height: this.height_ + 10, width: this.width_};
		};

		function resetWidthOnBlocks(blocks) {
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
		}

		this.enableBigCodeMode = function() {
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

			document.styleSheets[0].insertRule(".blocklyText, .beaconClass" + ' { font-size' +
											   ':'+'22pt !important'+'}',
											   document.styleSheets[0].cssRules.length);
			document.styleSheets[0].insertRule(".blocklyIconMark, .beaconClass" + ' { font-size' +
											   ':'+'18pt !important'+'}',
											   document.styleSheets[0].cssRules.length);
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

		    resetWidthOnBlocks(blocks);
		    Blockly.mainWorkspace.render();

			Blockly.Toolbox.flyout_.show(Blockly.languageTree.childNodes);

		    $(".blocklyIconShield").attr("width", 32).attr("height", 32)
		    	.attr("rx", 8).attr("ry", 8);
		    $(".blocklyIconMark").attr("x", 16).attr("y", 24);
		    $(".blocklyEditableText > rect").attr("height", 32).attr("y", -24)
		    	.attr("x", -5).attr("width", 85);
		};

		this.disableBigCodeMode = function() {
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

		    resetWidthOnBlocks(blocks);
		    Blockly.mainWorkspace.render();

			Blockly.Toolbox.flyout_.show(Blockly.languageTree.childNodes);
		    $(".blocklyIconShield").attr("width", 16).attr("height", 16)
		    	.attr("rx", 4).attr("ry", 4);
		    $(".blocklyIconMark").attr("x", 8).attr("y", 12);
		    $(".blocklyEditableText > rect").attr("height", 16).attr("y", -12)
		    	.attr("x", -5).attr("width", 43);
		};
	};

	/**
	 * Disable the right-click context menus
	 */
	this.disableContextMenus = function(blocks) {
	    Blockly.showContextMenu_ = function(e) {};
    	Blockly.Block.prototype.showContextMenu_ = function(e) {};
	};

    this.setupDoubleclick = function() {
        Blockly.Flyout.prototype.show = function(xmlList) {
            this.hide();
            // Delete any blocks from a previous showing.
            var blocks = this.workspace_.getTopBlocks(false);
            for (var x = 0, block; block = blocks[x]; x++) {
                if (block.workspace == this.workspace_) {
                    block.dispose(false, false);
                }
            }
            // Delete any background buttons from a previous showing.
            for (var x = 0, rect; rect = this.buttons_[x]; x++) {
                goog.dom.removeNode(rect);
            }
            this.buttons_.length = 0;

            var margin = this.CORNER_RADIUS;
            this.svgGroup_.style.display = 'block';

            // Create the blocks to be shown in this flyout.
            blocks = [];
            var gaps = [];
            if (xmlList == Blockly.Variables.NAME_TYPE) {
                // Special category for variables.
                Blockly.Variables.flyoutCategory(blocks, gaps, margin,
                    /** @type {!Blockly.Workspace} */ (this.workspace_));
            } else if (xmlList == Blockly.Procedures.NAME_TYPE) {
                // Special category for procedures.
                Blockly.Procedures.flyoutCategory(blocks, gaps, margin,
                    /** @type {!Blockly.Workspace} */ (this.workspace_));
            } else {
                for (var i = 0, xml; xml = xmlList[i]; i++) {
                    if (xml.tagName && xml.tagName.toUpperCase() == 'BLOCK') {
                        var block = Blockly.Xml.domToBlock(
                            /** @type {!Blockly.Workspace} */ (this.workspace_), xml);
                        blocks.push(block);
                        gaps.push(margin * 3);
                    }
                }
            }

            // Lay out the blocks vertically.
            var cursorY = margin;
            for (var i = 0, block; block = blocks[i]; i++) {
                var allBlocks = block.getDescendants();
                for (var j = 0, child; child = allBlocks[j]; j++) {
                    // Mark blocks as being inside a flyout.  This is used to detect and
                    // prevent the closure of the flyout if the user right-clicks on such a
                    // block.
                    child.isInFlyout = true;
                    // There is no good way to handle comment bubbles inside the flyout.
                    // Blocks shouldn't come with predefined comments, but someone will
                    // try this, I'm sure.  Kill the comment.
                    child.setCommentText(null);
                }
                block.render();
                var root = block.getSvgRoot();
                var blockHW = block.getHeightWidth();
                var x = Blockly.RTL ? 0 : margin + Blockly.BlockSvg.TAB_WIDTH;
                block.moveBy(x, cursorY);
                cursorY += blockHW.height + gaps[i];

                // Create an invisible rectangle under the block to act as a button.  Just
                // using the block as a button is poor, since blocks have holes in them.
                var rect = Blockly.createSvgElement('rect', {'fill-opacity': 0}, null);
                // Add the rectangles under the blocks, so that the blocks' tooltips work.
                this.workspace_.getCanvas().insertBefore(rect, block.getSvgRoot());
                block.flyoutRect_ = rect;
                this.buttons_[i] = rect;

                if (this.autoClose) {
                    this.listeners_.push(Blockly.bindEvent_(root, 'mousedown', null,
                        this.createBlockFunc_(block)));
                } else {
                    this.listeners_.push(Blockly.bindEvent_(root, 'mousedown', null,
                        this.blockMouseDown_(block)));
                }
                var block2 = block;
                var isBlockAllowed = function(block) {
                    for (var i = 0; i < BLOCKS.length; i++) {
                        if (BLOCKS[i].type === block.type) {
                            return true;
                        }
                    }
                    return false;
                };
                var blockAddingListener = function(block) {
                    return function() {
                        if (canAddNewBlock(block.type) && isBlockAllowed(block)) {
                            if (block.previousConnection) {
                                ocargo.blocklyControl.addBlockToEndOfProgram(block.type);
                            } else {
                                ocargo.blocklyControl.createBlock(block.type);
                            }
                        }
                    };
                }(block2);
                this.listeners_.push(root.addEventListener('dblclick', blockAddingListener));
                this.listeners_.push(Blockly.bindEvent_(root, 'mouseover', block.svg_,
                    block.svg_.addSelect));
                this.listeners_.push(Blockly.bindEvent_(root, 'mouseout', block.svg_,
                    block.svg_.removeSelect));
                this.listeners_.push(Blockly.bindEvent_(rect, 'mousedown', null,
                    this.createBlockFunc_(block)));
                this.listeners_.push(Blockly.bindEvent_(rect, 'mouseover', block.svg_,
                    block.svg_.addSelect));
                this.listeners_.push(Blockly.bindEvent_(rect, 'mouseout', block.svg_,
                    block.svg_.removeSelect));
                this.listeners_.push(rect.addEventListener('dblclick', blockAddingListener));
            }

            // IE 11 is an incompetant browser that fails to fire mouseout events.
            // When the mouse is over the background, deselect all blocks.
            var deselectAll = function(e) {
                var blocks = this.workspace_.getTopBlocks(false);
                for (var i = 0, block; block = blocks[i]; i++) {
                    block.svg_.removeSelect();
                }
            };
            this.listeners_.push(Blockly.bindEvent_(this.svgBackground_, 'mouseover',
                this, deselectAll));

            this.width_ = 0;
            this.reflow();

            this.filterForCapacity_();

            // Fire a resize event to update the flyout's scrollbar.
            Blockly.fireUiEventNow(window, 'resize');
            this.reflowWrapper_ = Blockly.bindEvent_(this.workspace_.getCanvas(),
                'blocklyWorkspaceChange', this, this.reflow);
            this.workspace_.fireChangeEvent();
        };
    }
};
