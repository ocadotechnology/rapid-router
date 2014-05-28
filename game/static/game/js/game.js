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

function initialiseDefault() {
    'use strict';

    var title = LEVEL_ID > 15 ? "" : "Lesson " + LEVEL_ID;
    startPopup(title, "", LESSON); 

    var path = JSON.parse(PATH);
    ocargo.ui = createUi();
    ocargo.level = createDefaultLevel(path, ocargo.ui);
    ocargo.level.levelId = JSON.parse(LEVEL_ID);
    ocargo.level.blockLimit = JSON.parse(BLOCK_LIMIT);
    setDirectControl(moveForward(function(){}, moveLeft(function(){}), moveRight(function(){})));
    if (ocargo.level.blockLimit)
        ocargo.level.blockLimit++;
    if ($.cookie("muted") == "true") {
        $('#mute').text("Unmute");
        ocargo.sound.mute();
    }
}

function setDirectControl(forward, left, right) {
    ocargo.moveForward = forward;
    ocargo.moveLeft = left;
    ocargo.moveRigt = right;
}

function trackDevelopment() {
    $('#moveForward').click(function() {
        ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
        ocargo.moveForward();
    });
    
    $('#turnLeft').click(function() {
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
        ocargo.moveLeft();
    });

    $('#turnRight').click(function() {
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
        ocargo.moveRight();
    });
    
    $('#play').click(function() {
        if (ocargo.blocklyControl.incorrect)
            ocargo.blocklyControl.incorrect.setColour(ocargo.blocklyControl.incorrectColour);
        var program = ocargo.blocklyControl.populateProgram();
        program.instructionHandler = new InstructionHandler(ocargo.level);
        var nodes = ocargo.level.map.nodes;
        ocargo.level.van = new ocargo.Van(nodes[0], nodes[1], ocargo.ui);
        ocargo.ui.setVanToFront();
        ocargo.level.play(program);
        ocargo.level.correct = 0;
    });

    $('#clearIncorrect').click(function() {
        ocargo.blocklyControl.removeWrong();
        setDirectControl(moveForward(function(){}, moveLeft(function(){}), moveRight(function(){})));
    });

    $('#clear').click(function() {
        ocargo.blocklyControl.reset();
        setDirectControl(moveForward(function(){}, moveLeft(function(){}), moveRight(function(){})));
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

$('#randomRoad').click(function() {
    var points = generateRandomPathPoints([0,3], 0.5, 13);
    var nodes = generateNodes(points);  
    var van = new ocargo.Van(nodes[0], nodes[1], ocargo.ui);
    var map = new ocargo.Map(nodes, nodes[nodes.length - 1], ocargo.ui);
    ocargo.level = new ocargo.Level(map, van, ocargo.ui);
});
