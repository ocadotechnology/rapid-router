var ocargo = ocargo || {};

function createUi() {
    return new ocargo.SimpleUi();
}

function createDefaultLevel(nodeData, ui, maxFuel) {
	var nodes = createNodes(nodeData);
    
    var map = new ocargo.Map(nodes, nodes[nodes.length - 1], ui);
    var van = new ocargo.Van(nodes[0], nodes[1], maxFuel, ui);
    return new ocargo.Level(map, van, ui);
}

function createNodes(nodeData){
	var nodes = [];
	
	// Create nodes with coords
	for(var i = 0; i < nodeData.length; i++){
		 var coordinate = new ocargo.Coordinate(nodeData[i]['coordinate'][0], nodeData[i]['coordinate'][1]);
         nodes.push(new ocargo.Node(coordinate));
	}
	
	// Link nodes (must be done in second loop so that linked nodes have definitely been created)
	for(var i = 0; i < nodeData.length; i++){
		var node = nodes[i];
        var connectedNodes = nodeData[i]['connectedNodes'];
        for(var j = 0; j < connectedNodes.length; j++){
            node.addConnectedNode(nodes[connectedNodes[j]]);
    	}
	}
	
	return nodes;
}

function initialiseDefault() {
    'use strict';

    var title = LEVEL_ID > 15 ? "" : "Level " + LEVEL_ID;
    startPopup(title, "", LESSON); 

    ocargo.ui = createUi();
    ocargo.level = createDefaultLevel(PATH, ocargo.ui, MAX_FUEL);
    ocargo.level.levelId = JSON.parse(LEVEL_ID);
    ocargo.level.blockLimit = JSON.parse(BLOCK_LIMIT);
    enableDirectControl();
    if (ocargo.level.blockLimit)
        ocargo.level.blockLimit++;
    if ($.cookie("muted") === "true") {
        $('#mute').text("Unmute");
        ocargo.sound.mute();
    }
}

function enableDirectControl() {
    document.getElementById('moveForward').disabled = false;
    document.getElementById('turnLeft').disabled = false;
    document.getElementById('turnRight').disabled = false;
    document.getElementById('play').disabled = false;
    document.getElementById('controls').style.visibility='visible';
}

function disableDirectControl() {
    document.getElementById('controls').style.visibility='hidden';
    document.getElementById('moveForward').disabled = true;
    document.getElementById('turnLeft').disabled = true;
    document.getElementById('turnRight').disabled = true;
    document.getElementById('play').disabled = true;
}

function trackDevelopment() {
    $('#moveForward').click(function() {
        ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
        moveForward(function(){});
    });
    
    $('#turnLeft').click(function() {
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
        moveLeft(function(){});
    });

    $('#turnRight').click(function() {
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
        moveRight(function(){});
    });
    
    $('#play').click(function() {
        if (ocargo.blocklyControl.incorrect)
            ocargo.blocklyControl.incorrect.setColour(ocargo.blocklyControl.incorrectColour);
        disableDirectControl();
        var program = ocargo.blocklyControl.populateProgram();
        program.instructionHandler = new InstructionHandler(ocargo.level);
        var nodes = ocargo.level.map.nodes;
        ocargo.level.van = new ocargo.Van(nodes[0], nodes[1], ocargo.level.van.maxFuel, ocargo.ui);
        ocargo.ui.setVanToFront();
        ocargo.level.play(program);
        ocargo.level.correct = 0;
    });

    $('#clearIncorrect').click(function() {
        ocargo.blocklyControl.removeWrong();
        enableDirectControl();
    });

    $('#clear').click(function() {
        ocargo.blocklyControl.reset();
        enableDirectControl();
    });
    
    $('#slideBlockly').click(function() {
        var c = $('#programmingConsole');
        if (c.is(':visible')) {
            $('#paper').animate({width: '100%'});
            $('#sliderControls').animate({left: '0%'});
        } else {
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
    if (ocargo.sound.volume === 0) {
        $this.text('Mute');
        ocargo.sound.unmute();  
    } else {
        $this.text('Unmute');
        ocargo.sound.mute();
    }
});
