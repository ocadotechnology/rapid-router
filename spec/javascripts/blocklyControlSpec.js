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
describe("disconnectedStartBlock", function() {
  // XXX: This should probably be a fixture
  BLOCKS = [];
  BLOCKS.push({'type':"move_forwards"});
  BLOCKS.push({'type':"turn_left"});
  BLOCKS.push({'type':"turn_right"});
  BLOCKS.push({'type':"turn_around"});
  BLOCKS.push({'type':"controls_repeat"});
  BLOCKS.push({'type':"controls_repeat_until"});
  BLOCKS.push({'type':"controls_if"});
  BLOCKS.push({'type':"at_destination"});
  BLOCKS.push({'type':"road_exists"});
  BLOCKS.push({'type':"dead_end"});

  BLOCKLY_XML = '<xml id="blockly_toolbox" style="display: none"><category name="+">';
  for (var i = 0; i < BLOCKS.length; i++) {
    BLOCKLY_XML += '<block type="' + BLOCKS[i].type + '"></block>';
  }
  BLOCKLY_XML += '</category></xml>';
  CHARACTER_EN_FACE_URL = "characters/front_view/Phil.svg";

  beforeEach(function() {
    var blocklyHolder = document.createElement('div');
    blocklyHolder.id = 'blockly_holder';
    document.getElementsByTagName('body')[0].appendChild(blocklyHolder);
    initCustomBlocks();
    ocargo.blocklyControl = new ocargo.BlocklyControl();
  });

  afterEach(function() {
    var blocklyHolder = document.getElementById('blockly_holder');
    blocklyHolder.parentNode.removeChild(blocklyHolder);
  });

  it("works for start block", function() {
    var control = new ocargo.BlocklyControl();
    control.reset();
    disconnected = control.disconnectedStartBlock();
    expect(disconnected).toEqual(false);
  });


  it("works for start block and rogue block", function() {
    var control = new ocargo.BlocklyControl();
    control.reset();
    control.createBlock("turn_around");
    disconnected = control.disconnectedStartBlock();
    expect(disconnected).toEqual(true);
  });

  it("works for start block and connected block", function() {
    var control = new ocargo.BlocklyControl();
    control.reset();
    control.addBlockToEndOfProgram("turn_around");
    disconnected = control.disconnectedStartBlock();
    expect(disconnected).toEqual(false);
  });

  it("works for connected start block and rogue block", function() {
    var control = new ocargo.BlocklyControl();
    control.reset();
    control.createBlock("turn_around");
    control.addBlockToEndOfProgram("turn_around");
    disconnected = control.disconnectedStartBlock();
    expect(disconnected).toEqual(false);
  });
});
