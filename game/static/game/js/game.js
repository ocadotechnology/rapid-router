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
	var map = new ocargo.Map(nodes, nodes[nodes.length - 1], ui);
	var van = new ocargo.Van(nodes[0], nodes[1], ui);
	return new ocargo.Level(map, van, ui);
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

function loadDefaultProgram() {
    ocargo.blocklyTest.reset();

    ocargo.blocklyTest.addBlockToEndOfProgram('turn_left');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    ocargo.blocklyTest.addBlockToEndOfProgram('turn_right');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    ocargo.blocklyTest.addBlockToEndOfProgram('turn_left');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    ocargo.blocklyTest.addBlockToEndOfProgram('turn_right');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    ocargo.blocklyTest.addBlockToEndOfProgram('turn_right');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    ocargo.blocklyTest.addBlockToEndOfProgram('turn_left');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
}

function initialiseDefault() {
	'use strict';
	ocargo.ui = createUi();
	ocargo.level = createDefaultLevel(ocargo.ui);
}

function trackDevelopment() {
	$('#moveForward').click(function() {
		ocargo.blocklyTest.addBlockToEndOfProgram('move_van');
    });
	
    $('#turnLeft').click(function() {
		ocargo.blocklyTest.addBlockToEndOfProgram('turn_left');
    });

    $('#turnRight').click(function() {
		ocargo.blocklyTest.addBlockToEndOfProgram('turn_right');
	});
    
    $('#play').click(function() {
        var program = ocargo.blocklyTest.populateProgram();
        program.instructionHandler = new InstructionHandler(ocargo.level);
        var nodes = ocargo.level.map.nodes;
        ocargo.level.van = new ocargo.Van(nodes[0], nodes[1], ocargo.ui);
        ocargo.ui.setVanToFront();
    	ocargo.level.play(program);
        ocargo.level.correct = 0;
	});

    $('#loadDefaultProgram').click(function() {
        loadDefaultProgram();
    });

	$('#clearIncorrect').click(function() {
        ocargo.blocklyTest.removeWrong();
        var nodes = ocargo.level.map.nodes;
    });

    $('#clear').click(function() {
        ocargo.blocklyTest.reset();
    });
    
    $('#reset').click(function() {
        initialiseDefault();
        ocargo.blocklyTest.reset();
    });
}

$(function() {
   	initialiseDefault();
    trackDevelopment();
});

$('#mute').click(function() {
    var $this = $(this);
    if(ocargo.sound.volume == 0) {
        $this.text("Mute");
        ocargo.sound.unmute();  
    } else {
        $this.text("Unmute");
        ocargo.sound.mute();
    }
});

$('#randomRoad').click(function() {
	var points = generateRandomPathPoints([0,3], 0.5, 13);
	var nodes = generateNodes(points);  
	var van = new ocargo.Van(nodes[0], nodes[1], ocargo.ui);
	var map = new ocargo.Map(nodes, nodes[nodes.length - 1], ocargo.ui);
	ocargo.level = new ocargo.Level(map, van, ocargo.ui);
});
