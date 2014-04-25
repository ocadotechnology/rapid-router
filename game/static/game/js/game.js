var ocargo = ocargo || {};

function createUi() {
    return new ocargo.SimpleUi();
}

function createDefaultLevel(ui) {
    var points = [
        [0, 3],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 5],
        [3, 5],
        [3, 6],
        [3, 7],
        [4, 7],
        [5, 7],
        [5, 6],
        [5, 5],
        [6, 5],
        [7, 5],
        [8, 5],
        [9, 5]
    ];

	var nodes = generateNodes(points);  
	var map = new ocargo.Map(nodes, ui);
	var van = new ocargo.Van(nodes[0], nodes[1], ui);
	return new ocargo.Level(map, van, nodes[nodes.length - 1], ui);
}

function generateNodes(points){
	var previousNode = null;
	var nodes = [];
	for (var i = 0; i < points.length; i++) {
	      var p = points[i];
	      var coordinate = new ocargo.Coordinate(p[0], p[1]);
	      var node = new ocargo.Node(coordinate);
	      if (previousNode) {
	          node.addConnectedNodeWithBacklink(previousNode);
	      }
	      previousNode = node;
	      nodes.push(node);
	}
	return nodes;
}

function defaultProgram(level) {
	var program = new ocargo.Program(new InstructionHandler(level));
	
	program.addNewStackLevel(
	          [TURN_LEFT_COMMAND,
	              FORWARD_COMMAND,
	              TURN_RIGHT_COMMAND,
	              FORWARD_COMMAND,
	              TURN_LEFT_COMMAND,
	              FORWARD_COMMAND,
	              TURN_RIGHT_COMMAND,
	              FORWARD_COMMAND,
	              TURN_RIGHT_COMMAND,
	              FORWARD_COMMAND,
	              TURN_LEFT_COMMAND,
	              FORWARD_COMMAND,
	              FORWARD_COMMAND,
	              FORWARD_COMMAND
	          ]);
	
	level.play(program);
}

function initialiseDefault() {
	'use strict';
	ocargo.ui = createUi();
	ocargo.level = createDefaultLevel(ocargo.ui);
	$('#runDefaultProgram').click(function() {
		defaultProgram(ocargo.level);
	});
}

function trackDevelopment() {
	$('#moveForward').click(function() {
		BlocklyTest.addBlockToEndOfProgram('move_van');
    });
	
    $('#turnLeft').click(function() {
		BlocklyTest.addBlockToEndOfProgram('turn_left');
    });

    $('#turnRight').click(function() {
		BlocklyTest.addBlockToEndOfProgram('turn_right');
	});
    
    $('#play').click(function() {
        var program = BlocklyTest.populateProgram();
        program.instructionHandler = new InstructionHandler(ocargo.level);
    	ocargo.level.play(program);
	});
	
	$('#reset').click(function() {
		initialiseDefault();	
	});
}

$(function() {
   	initialiseDefault();
    trackDevelopment();
});

$('#randomRoad').click(function() {
	var points = generateRandomPathPoints([0,3], 0.5, 13);
	var nodes = generateNodes(points);  
	var van = new ocargo.Van(nodes[0], nodes[1], ocargo.ui);
	var map = new ocargo.Map(nodes, ocargo.ui);
	ocargo.level = new ocargo.Level(map, van, nodes[nodes.length - 1], ocargo.ui);
});
