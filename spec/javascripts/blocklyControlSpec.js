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
