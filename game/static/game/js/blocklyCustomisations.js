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

ocargo.BlocklyCustomisations = function () {
    var limitedBlocks = false;
    var blockCount = {};

    for (var i = 0; i < BLOCKS.length; i++) {
        var block = BLOCKS[i];
        blockCount[block.type] = block.number;
        limitedBlocks = limitedBlocks || (block.number !== undefined);
    }

    //Make the flyout button more transparent so that it is clearer when blocks have been created.
    this.makeFlyoutButtonTransparent = function () {
        $("#flyoutButton").css("background", "rgba(255, 255, 255, 0.5)");
    };

    //Make the flyout more transparent so that it is clearer when blocks have been created.
    this.makeFlyoutTransparent = function () {
        $(".blocklyFlyoutBackground").css("fill-opacity", "0.5");
    };

    //Shift Blockly Div
    this.shiftBlockly = function () {
        $("#blockly_holder").css("marginLeft", "0px");
    };

    //Make it such that the workspace and game do not overlap
    this.shiftWorkspace = function () {
        $("#blockly_holder").css("width", "calc(100%)");
    };

    //Hide Blockly Toolbox to use our Flyout button instead
    this.hideBlocklyToolbox = function () {
        $(".blocklyToolboxDiv").css("display", "none");
    };



    var canAddNewBlock = function (blockType) {
        return blockCount[blockType] === undefined || blockCount[blockType] > 0;
    };

    this.widenFlyout = function () {
            //Override blockly flyout's position function to artificially widen it
            var oldPositionFunction = Blockly.Flyout.prototype.position;

            Blockly.Flyout.prototype.position = function () {
                this.width_ += 50;
                oldPositionFunction.call(this);
                this.width_ -= 50;
            }
    };

    Blockly.Flyout.prototype.autoClose = false;

    // Override Scrollbar::set to call constrainKnob, in case value is negative
    Blockly.Scrollbar.prototype.set = function (value) {
        // Move the scrollbar slider.
        this.svgKnob_.setAttribute(this.horizontal_ ? 'x' : 'y', this.constrainKnob_(value * this.ratio_));
        this.onScroll_();
    };

    /**
     * Sets up only having a limited number of blocks
     * Needs to be called BEFORE blockly is injected
     */
    this.setupLimitedBlocks = function () {
        var setQuantityText = function (element, blockType) {
            element.textContent = "×" + blockCount[blockType];
        };

        var selectAndSetQuantityText = function (blockType) {
            var element = $('.quantity_text[value="' + blockType + '"]')[0];
            if (element) {
                // Test needed for loading workspaces (when flyout doesn't exist apparently)
                setQuantityText(element, blockType);
            }
        };

        if (limitedBlocks) {
            this.widenFlyout();

            // Override blockly flyout's show function to add in the quantity text elements
            var oldShowFunction = Blockly.Flyout.prototype.show;
            var firstCall = true;
            Blockly.Flyout.prototype.show = function (xmlList) {
                if (firstCall) {
                    // The first time this is called the flyout doesn't yet exist.
                    // By calling show we give this.width_ a non-zero value.
                    oldShowFunction.call(this, xmlList);
                    firstCall = false;
                }

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
                        var attributes = {
                            'width': 30,
                            'height': 30,
                            'x': this.width_,
                            'y': cursorY + 22,
                            'class': 'quantity_text',
                            'value': block.type
                        };
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
            Blockly.Flyout.prototype.createBlockFunc_ = function (originBlock) {
                var func = oldCreateBlockFunction.call(this, originBlock);
                return function (e) {
                    if (canAddNewBlock(originBlock.type)) {
                        func(e);
                    }
                };
            };

            var changeBlockCount = function (blockType, workspace, delta) {
                if (blockType !== "start" && workspace === Blockly.mainWorkspace && blockCount[blockType] !== undefined) {
                    blockCount[blockType] += delta;
                    selectAndSetQuantityText(blockType);
                }
            };

            // Override the initialize method to track blocks entering the  workspace
            var oldInitialize = Blockly.Block.prototype.initialize;
            Blockly.Block.prototype.initialize = function (workspace, prototypeName) {
                oldInitialize.call(this, workspace, prototypeName);
                changeBlockCount(this.type, this.workspace, -1);
            };

            // Override block dispose method to keep track of blocks leaving the workspace
            var oldDispose = Blockly.Block.prototype.dispose;
            Blockly.Block.prototype.dispose = function (healStack, animate, opt_dontRemoveFromWorkspace) {
                changeBlockCount(this.type, this.workspace, 1);
                oldDispose.call(this, healStack, animate, opt_dontRemoveFromWorkspace);
            };
        }
    };

    /**
     * Sets up the ability to toggle the flyout
     * Needs to be called AFTER blockly is injected
     */
    this.setupFlyoutToggling = function (blocklyDiv) {
        var flyoutShown = false;
        var blocklyToggle = Blockly.getMainWorkspace().toolbox_.tree_.actualEventTarget_.firstChild_;

        var flyoutWidth = function() {
            return $('.blocklyFlyoutBackground')[0].getBoundingClientRect().width;
        };

        var flyoutRectangle = function() {
            var BIG_NUM = 10000000;
            return new goog.math.Rect(-BIG_NUM, -BIG_NUM, BIG_NUM + flyoutWidth(), 2 * BIG_NUM);
        };

        // So that the Delete area depends on whether the flyout is shown
        var oldRecordDeleteAreas = Blockly.getMainWorkspace().recordDeleteAreas;
        Blockly.WorkspaceSvg.prototype.recordDeleteAreas = function () {
            oldRecordDeleteAreas.call(Blockly.getMainWorkspace());

            if (flyoutShown) {
                this.deleteAreaToolbox_ = flyoutRectangle();
            }
        };

        var firstCall = true;
        var isSafari = Object.prototype.toString.call(window.HTMLElement).indexOf('Constructor') > 0;
        function getToggleSrc(image) {
            var originalSrc = ocargo.Drawing.imageDir + 'icons/' + image + '.svg';
            if (isSafari && !firstCall) {
                return originalSrc + '?SafariFix';
            } else {
                firstCall = false;
                return originalSrc;
            }
        }

        function image() {
            if (flyoutShown) {
                return 'hide';
            } else {
                return 'show';
            }
        }

        function buttonOffset() {
            if (flyoutShown) {
               return (flyoutWidth() - 1);
            } else {
               return 0;
            }
        }

        function moveButton() {
            var width = buttonOffset();
            $('#flyoutButton').css('left', width + 'px');
        }

        function changeButtonImage() {
            $('#flyoutButton img').attr("src", getToggleSrc(image()));
        }

        function clickButton() {
            blocklyToggle.onMouseDown(null);
        }

        this.bringStartBlockFromUnderFlyout = function () {
            var distanceFromToolboxDiv = 455;
            var distanceFromTopMargin = 15;
            Blockly.getMainWorkspace().scrollbar.hScroll.set(blocklyDiv.offsetWidth - distanceFromToolboxDiv);
            Blockly.getMainWorkspace().scrollbar.vScroll.set(blocklyDiv.offsetHeight - distanceFromTopMargin);
        };

        this.toggleFlyout = function () {
            flyoutShown = !flyoutShown;
            clickButton();
            changeButtonImage();
            moveButton();
        };
    };


    /**
     * Sets up big code mode (enlarges blockly)
     * Needs to be called BEFORE blockly is injected
     */
    this.setupBigCodeMode = function (blocks) {
        //so that image fields render properly when their size_ variable is broken above
        Blockly.FieldImage.prototype.render_ = function () {
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

        this.enableBigCodeMode = function () {
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
                ':' + '22pt !important' + '}',
                document.styleSheets[0].cssRules.length);
            document.styleSheets[0].insertRule(".blocklyIconMark, .beaconClass" + ' { font-size' +
                ':' + '18pt !important' + '}',
                document.styleSheets[0].cssRules.length);
            var blocks = Blockly.mainWorkspace.getAllBlocks();
            $(".blocklyDraggable > g > image").each(function (index, element) {
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

            Blockly.getMainWorkspace().toolbox_.flyout_.show(Blockly.languageTree.childNodes);

            $(".blocklyIconShield").attr("width", 32).attr("height", 32)
                .attr("rx", 8).attr("ry", 8);
            $(".blocklyIconMark").attr("x", 16).attr("y", 24);
            $(".blocklyEditableText > rect").attr("height", 32).attr("y", -24)
                .attr("x", -5).attr("width", 85);
        };

        this.disableBigCodeMode = function () {
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
                sheet.deleteRule(sheet.cssRules.length - 1);
            }

            var blocks = Blockly.mainWorkspace.getAllBlocks();

            $(".blocklyDraggable > g > image").each(function (index, element) {
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

            Blockly.getMainWorkspace().toolbox_.flyout_.show(Blockly.languageTree.childNodes);
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
    this.disableContextMenus = function (blocks) {
        Blockly.showContextMenu_ = function (e) {
        };
        Blockly.ContextMenu.show = function (e) {
        };
    };

    this.setupDoubleclick = function () {
        Blockly.Flyout.prototype.show = function (xmlList) {
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

                //Create an invisible rectangle under the block to act as a button.  Just
                //using the block as a button is poor, since blocks have holes in them.
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
                var isBlockAllowed = function (block) {
                    for (var i = 0; i < BLOCKS.length; i++) {
                        if (BLOCKS[i].type === block.type) {
                            return true;
                        }
                    }
                    return false;
                };
                var blockAddingListener = function (block) {
                    return function () {
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
                this.listeners_.push(Blockly.bindEvent_(root, 'mouseover', block,
                    block.addSelect));
                this.listeners_.push(Blockly.bindEvent_(root, 'mouseout', block,
                    block.removeSelect));
                this.listeners_.push(Blockly.bindEvent_(rect, 'mousedown', null,
                    this.createBlockFunc_(block)));
                this.listeners_.push(Blockly.bindEvent_(rect, 'mouseover', block,
                    block.addSelect));
                this.listeners_.push(Blockly.bindEvent_(rect, 'mouseout', block,
                    block.removeSelect));
                this.listeners_.push(rect.addEventListener('dblclick', blockAddingListener));
            }

            //IE 11 is an incompetant browser that fails to fire mouseout events.
            //When the mouse is over the background, deselect all blocks.
            var deselectAll = function (e) {
                var blocks = this.workspace_.getTopBlocks(false);
                for (var i = 0, block; block = blocks[i]; i++) {
                    block.removeSelect();
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
    };

    this.addClickListenerToStartBlock = function(startBlock){
        if(startBlock){
            var svgRoot = startBlock.getSvgRoot();
            if(svgRoot){
                if(!svgRoot.id || svgRoot.id == ""){
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
                            $('#play_radio').trigger('click');
                        }
                    },});
            }
        }
    };
};