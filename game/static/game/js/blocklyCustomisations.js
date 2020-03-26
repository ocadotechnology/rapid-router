/*
Code for Life

Copyright (C) 2019, Ocado Innovation Limited

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

    const TOOLBOX_REMAINING_CAPACITY_TEXT_COLUMN_WIDTH = 50;

    var limitedBlocks = false;
    var blockCount = {};

    for (var i = 0; i < BLOCKS.length; i++) {
        var block = BLOCKS[i];
        blockCount[block.type] = block.number;
        limitedBlocks = limitedBlocks || (block.number !== undefined);
    }

    var canAddNewBlock = function (blockType) {
        return maxInstances[blockType] === undefined 
            || Blockly.mainWorkspace.remainingCapacityOfType(blockType) > 0;
    };

    var setQuantityText = function (element, blockType) {

        /**
         * This function is copied from the blockly library
         * https://github.com/google/blockly/blob/1.20190419.0/core/workspace.js#L533
         */ 
        var getCapacityOfBlockType = function (blockType) {
            var realBlocks = Blockly.mainWorkspace.getBlocksByType(blockType).filter(function (block) {
                return !block.isInsertionMarker();
            });
            return maxInstances[blockType] - realBlocks.length;
        };

        var capacity = getCapacityOfBlockType(blockType);
        element.textContent = "×" + capacity;
    };

    /**
     * Adds the Blockly event listeners to update remaining quantities
     * when a block enters/leaves the workspace
     * Needs to be called AFTER Blockly is injected
     */
    this.addLimitedBlockListeners = function (workspace) {
        if (!limitedBlocks) {
            return;
        }

        var selectAndSetQuantityText = function (blockType) {
            var element = $('.quantity_text[value="' + blockType + '"]')[0];
            if (element) {
                setQuantityText(element, blockType);
            }
        };

        var updateRemainingCapacities = function () {
            for (let blockType in maxInstances) {
                selectAndSetQuantityText(blockType);
            }
        };

        var listenForBlockWorkspaceChanges = function (event) {
            if (event.type == Blockly.Events.BLOCK_CREATE 
                || event.type == Blockly.Events.BLOCK_DELETE) {
                updateRemainingCapacities();
            }
        }

        workspace.addChangeListener(listenForBlockWorkspaceChanges);
    }

    /**
     * Override blockly flyout's reflowInternal_ function to artificially widen it
     */
    this.widenFlyout = function () {
        var oldCaclulateWidthFunction = Blockly.VerticalFlyout.prototype.reflowInternal_;

        Blockly.VerticalFlyout.prototype.reflowInternal_ = function() {
            this.workspace_.scale = this.targetWorkspace_.scale;
            var flyoutWidth = 0;
            var blocks = this.workspace_.getTopBlocks(false);
            for (var i = 0, block; block = blocks[i]; i++) {
                var width = block.getHeightWidth().width;
                if (block.outputConnection) {
                    width -= Blockly.BlockSvg.TAB_WIDTH;
                }
                flyoutWidth = Math.max(flyoutWidth, width);
            }
            for (var i = 0, button; button = this.buttons_[i]; i++) {
                flyoutWidth = Math.max(flyoutWidth, button.width);
            }
            flyoutWidth += this.MARGIN * 1.5 + Blockly.BlockSvg.TAB_WIDTH;
            flyoutWidth *= this.workspace_.scale;
            flyoutWidth += Blockly.Scrollbar.scrollbarThickness;
            flyoutWidth += TOOLBOX_REMAINING_CAPACITY_TEXT_COLUMN_WIDTH;

            if (this.width_ != flyoutWidth) {
                for (var i = 0, block; block = blocks[i]; i++) {
                    if (this.RTL) {
                        // With the flyoutWidth known, right-align the blocks.
                        var oldX = block.getRelativeToSurfaceXY().x;
                        var newX = flyoutWidth / this.workspace_.scale - this.MARGIN -
                            Blockly.BlockSvg.TAB_WIDTH;
                        block.moveBy(newX - oldX, 0);
                    }
                    if (block.flyoutRect_) {
                        this.moveRectToBlock_(block.flyoutRect_, block);
                    }
                }
                if (this.RTL) {
                // With the flyoutWidth known, right-align the buttons.
                    for (var i = 0, button; button = this.buttons_[i]; i++) {
                        var y = button.getPosition().y;
                        var x = flyoutWidth / this.workspace_.scale - button.width -
                            this.MARGIN - Blockly.BlockSvg.TAB_WIDTH;
                        button.moveTo(x, y);
                    }
                }
                // Record the width for .getMetrics_ and .position.
                this.width_ = flyoutWidth;
                this.position();
            };
        };
    };

    /**
     * Sets up only having a limited number of blocks
     * Needs to be called BEFORE blockly is injected
     */
    this.setupLimitedBlocks = function () {     
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
                        blocks.push(Blockly.Xml.domToBlock(xml, this.workspace_));
                        gaps.push(margin * 3);
                    }
                }

                // Lay out the quantaties vertically.
                var cursorY = margin;
                for (var i = 0; i < blocks.length; i++) {
                    var block = blocks[i];
                    var blockHW = block.getHeightWidth();

                    if (maxInstances[block.type] !== undefined) {
                        var attributes = {
                            'width': 30,
                            'height': 30,
                            'x': this.width_ - TOOLBOX_REMAINING_CAPACITY_TEXT_COLUMN_WIDTH,
                            'y': cursorY + 22,
                            'class': 'quantity_text',
                            'value': block.type
                        };
                        var element = Blockly.utils.createSvgElement('text', attributes, null);
                        setQuantityText(element, block.type);
                        this.blockQuantities_.push(element);

                        this.workspace_.getCanvas().insertBefore(element, block.getSvgRoot());
                    }

                    cursorY += blockHW.height + gaps[i];
                }

                oldShowFunction.call(this, xmlList);
            };
        }
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
        
        Blockly.Flyout.prototype.addBlockListeners_ = function(root, block, rect) {
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

            this.listeners_.push(Blockly.bindEventWithChecks_(root, 'mousedown', null,
                this.blockMouseDown_(block)));
            this.listeners_.push(Blockly.bindEventWithChecks_(rect, 'mousedown', null,
                this.blockMouseDown_(block)));
            this.listeners_.push(Blockly.bindEvent_(root, 'mouseover', block,
                block.addSelect));
            this.listeners_.push(Blockly.bindEvent_(root, 'mouseout', block,
                block.removeSelect));
            this.listeners_.push(Blockly.bindEvent_(rect, 'mouseover', block,
                block.addSelect));
            this.listeners_.push(Blockly.bindEvent_(rect, 'mouseout', block,
                block.removeSelect));
            this.listeners_.push(Blockly.bindEvent_(root, 'dblclick', block, blockAddingListener));
        };
    };

    this.addClickListenerToStartBlock = function() {
        const play_button = $('#play_radio');
        Blockly.mainWorkspace.addChangeListener(function(event) {
            const startBlockID = Blockly.mainWorkspace.getBlocksByType('start')[0]['id'];

            if (event.type == Blockly.Events.UI && event.element == 'click' && event.blockId == startBlockID) {
                play_button.trigger('click');
            }
        });
    };
};
