var ocargo = ocargo || {};

function createUi() {
    return new ocargo.SimpleUi();
}

function createDefaultLevel(path, ui) {
	var nodes = generateNodes(path);
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
    ocargo.blocklyControl.reset();

    ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
}

function initialiseDefault() {
	'use strict';
    var path = JSON.parse(PATH);
	ocargo.ui = createUi();
	ocargo.level = createDefaultLevel(path, ocargo.ui);
        if ($.cookie("muted") == "true") {
            $('#mute').text("Unmute");
            ocargo.sound.mute();
        }
}

function trackDevelopment() {
	$('#moveForward').click(function() {
		ocargo.blocklyControl.addBlockToEndOfProgram('move_van');
    });
	
    $('#turnLeft').click(function() {
		ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
    });

    $('#turnRight').click(function() {
		ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
	});
    
    $('#quit').click(function(){
    	window.location.replace('/game/');
    });
    
    $('#play').click(function() {
        var program = ocargo.blocklyControl.populateProgram();
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
        ocargo.blocklyControl.removeWrong();
    });

    $('#clear').click(function() {
        ocargo.blocklyControl.reset();
    });
    
    $('#reset').click(function() {
        initialiseDefault();
        ocargo.blocklyControl.reset();
    });
    
    $('#slideBlockly').click(function() {
    	var c = $('#programmingConsole');
    	if(c.is(':visible')){
    		$('#paper').animate({width: '100%'});
    		$('#sliderControls').animate({left: '0%'});
    	}else{
    		$('#paper').animate({width: '50%'});
    		$('#sliderControls').animate({left: '50%'});
    	}
    	c.animate({width: 'toggle'});
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
