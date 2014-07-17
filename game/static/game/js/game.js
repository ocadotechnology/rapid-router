var ocargo = ocargo || {};

function createUi() {
    return new ocargo.SimpleUi();
}

function createDefaultLevel(nodeData, destination, decor, trafficLightData, ui, maxFuel, nextLevel, nextEpisode) {
    var nodes = createNodes(nodeData);
    var trafficLights = createAndAddTrafficLightsToNodes(nodes, trafficLightData);
    var destinationIndex = findByCoordinate(destination, nodes);
    var dest = destinationIndex > -1 ? nodes[destinationIndex] : nodes[nodes.length - 1];
    var map = new ocargo.Map(nodes, decor, trafficLights, dest, ui);
    var vans = [];

    var previousNode = nodes[0];
    var startNode = nodes[0].connectedNodes[0];
    for (var i = 0; i < THREADS; i++) {
        vans.push(new ocargo.Van(i,previousNode, startNode, maxFuel, ui));
    }
    ocargo.ui.renderVans(vans);

    return new ocargo.Level(map, vans, ui, nextLevel, nextEpisode);
}

function createNodes(nodeData) {
    var nodes = [];

    var i;
    // Create nodes with coords
    for (i = 0; i < nodeData.length; i++) {
         var coordinate = new ocargo.Coordinate(
            nodeData[i]['coordinate'][0], nodeData[i]['coordinate'][1]);
         nodes.push(new ocargo.Node(coordinate));
    }

    // Link nodes (must be done in second loop so that linked nodes have definitely been created)
    for (i = 0; i < nodeData.length; i++) {
        var node = nodes[i];
        var connectedNodes = nodeData[i]['connectedNodes'];
        for (var j = 0; j < connectedNodes.length; j++) {
            node.addConnectedNode(nodes[connectedNodes[j]]);
        }
    }
    
    return nodes;
}

function createAndAddTrafficLightsToNodes(nodes, trafficLightData) {
	var trafficLights = [];
	for(i = 0; i < trafficLightData.length; i++){
    	var trafficLight = trafficLightData[i];
    	var controlledNodeId = trafficLight['node'];
    	var sourceNodeId = trafficLight['sourceNode'];
    	var redDuration = trafficLight['redDuration'];
    	var greenDuration = trafficLight['greenDuration'];
    	var startTime = trafficLight['startTime'];
    	var startingState = trafficLight['startingState'];
    	var controlledNode = nodes[controlledNodeId];
    	var sourceNode = nodes[sourceNodeId];
    	
        console.log(startingState);
    	var light = new ocargo.TrafficLight(i, startingState, startTime, redDuration, greenDuration, sourceNode, controlledNode);
    	trafficLights.push(light);
    	controlledNode.addTrafficLight(light);
    }
    return trafficLights;
}

function findByCoordinate(coordinate, nodes) {
    for (var i = 0; i < nodes.length; i++) {
        var coord = nodes[i].coordinate;
        if (coord.x === coordinate[0] && coord.y === coordinate[1]) {
            return i;
        }
    }
    return -1;
}

function initialiseDefault() {
    'use strict';

    var title = "Level " + LEVEL_ID;
    startPopup(title, "", LESSON + ocargo.messages.closebutton("Play"));

    ocargo.time = new ocargo.Time();
    ocargo.ui = createUi();
    ocargo.level = createDefaultLevel(PATH, DESTINATION, DECOR, TRAFFIC_LIGHTS, ocargo.ui, MAX_FUEL,
        NEXT_LEVEL, NEXT_EPISODE);
    ocargo.level.levelId = JSON.parse(LEVEL_ID);
    enableDirectControl();

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
    document.getElementById('direct_drive').style.visibility='visible';
    document.getElementById('stop').style.visibility='hidden';
    document.getElementById('step').disabled = false;
}

function disableDirectControl() {
    document.getElementById('controls').style.visibility='hidden';
    document.getElementById('direct_drive').style.visibility='hidden';
    document.getElementById('stop').style.visibility='visible';
    document.getElementById('moveForward').disabled = true;
    document.getElementById('turnLeft').disabled = true;
    document.getElementById('turnRight').disabled = true;
    document.getElementById('play').disabled = true;
    document.getElementById('step').disabled = true;
}

function clearVanData() {
    var nodes = ocargo.level.map.nodes;
    var previousNode = nodes[0];
    var startNode = nodes[0].connectedNodes[0];

    for (var i = 0; i < THREADS; i++) {
        var van = new ocargo.Van(i,previousNode, startNode, MAX_FUEL, ocargo.ui);
        ocargo.level.vans[i] = van;
        ocargo.ui.setVanToFront(previousNode, startNode, van);
    }
}

function redrawBlockly() {
    Blockly.fireUiEvent(window, 'resize');
}

function trackDevelopment() {

    $('#moveForward').click(function() {
        disableDirectControl();
        ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
        moveForward(ocargo.level.vans[0],enableDirectControl);
        ocargo.time.incrementTime();
    });

    $('#turnLeft').click(function() {
        disableDirectControl();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
        moveLeft(ocargo.level.vans[0],enableDirectControl);
        ocargo.time.incrementTime();
    });

    $('#turnRight').click(function() {
        disableDirectControl();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
        moveRight(ocargo.level.vans[0],enableDirectControl);
        ocargo.time.incrementTime();
    });

    $('#play').click(function() {
        if (ocargo.blocklyControl.incorrect) {
            ocargo.blocklyControl.incorrect.setColour(ocargo.blocklyControl.incorrectColour);
        }
        disableDirectControl();

        try {
            var program = ocargo.blocklyControl.populateProgram();
        } catch (error) {
            levelFailed(ocargo.level, 'Your program crashed!<br>' + error);
            return;
        }

        clearVanData();
        ocargo.time.resetTime();
        ocargo.level.playProgram(program);
    });

    $('#step').click(function() {
        if (ocargo.blocklyControl.incorrect) {
            ocargo.blocklyControl.incorrect.setColour(ocargo.blocklyControl.incorrectColour);
        }

        if (ocargo.level.program === undefined || ocargo.level.program.isFinished) {
            try {
                ocargo.level.program = ocargo.blocklyControl.populateProgram();
                ocargo.level.selectStartBlocks();
                clearVanData();
                ocargo.time.resetTime();
                Blockly.addChangeListener(terminate);
            } catch (error) {
                ocargo.level.fail('Your program crashed!');
                throw error;
            }
        }
        disableDirectControl();
        $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v3.svg)');
        ocargo.level.stepProgram(enableDirectControl);

        function terminate() {
            ocargo.level.program.isTerminated = true;
        }
    });
    
    $('#help').click(function() {
        startPopup('Help', HINT, ocargo.messages.closebutton("Close help"));
    });

    $('#clear').click(function() {
        ocargo.blocklyControl.reset();
        enableDirectControl();
        clearVanData();
        ocargo.time.resetTime();
        $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v2.svg)');
    });

    $('#stop').click(function() {
        ocargo.level.program.terminate();
    });

    var selectedWorkspace = null;

    $('#loadSave').click(function() {
        // Disable the button to stop users clicking it multiple times
        // whilst waiting for the table data to load
        $('#loadSave').attr('disabled', 'disabled');


        loadAllSavedWorkspaces(function(err, workspaces) {
            if (err != null) {
                console.debug(err);
                return;
            }

            var table = $('#workspaceTable');

            // Remove click listeners to avoid memory leak and remove all rows
            $('#workspaceTable td').off('click');
            table.empty();

            // Order them alphabetically
            workspaces.sort(function(a, b) {
                if (a.name < b.name) {
                    return -1;
                }
                else if (a.name > b.name) {
                    return 1;
                }
                return 0;
            });

            // Add a row to the table for each workspace saved in the database
            for (var i = 0, ii = workspaces.length; i < ii; i++) {
                var workspace = workspaces[i];
                table.append('<tr><td value=' + workspace.id + '>' + workspace.name + '</td></tr>');
            }

            // Add click listeners to all rows
            $('#workspaceTable td').on('click', function(event) {
                $('#workspaceTable td').css('background-color', '#FFFFFF');
                $(event.target).css('background-color', '#C0C0C0');
                selectedWorkspace = $(event.target).attr('value');
                $('#loadWorkspace').removeAttr('disabled');
                $('#overwriteWorkspace').removeAttr('disabled');
                $('#deleteWorkspace').removeAttr('disabled');
            });

            // Finally show the modal dialog and reenable the button
            $('#loadSaveModal').foundation('reveal', 'open');
            $('#loadSave').removeAttr('disabled');

            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            $('#loadWorkspace').attr('disabled', 'disabled');
            $('#overwriteWorkspace').attr('disabled', 'disabled');
            $('#deleteWorkspace').attr('disabled', 'disabled');
        });
    });

    $('#loadWorkspace').click(function() {
        if (selectedWorkspace) {
            loadWorkspace(selectedWorkspace, function(err, workspace) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                ocargo.blocklyControl.reset();
                ocargo.blocklyControl.deserialize(workspace);
                $('#loadSaveModal').foundation('reveal', 'close');
            });
        }
    });

    $('#overwriteWorkspace').click(function() {
        if (selectedWorkspace) {
            overwriteWorkspace(selectedWorkspace, ocargo.blocklyControl.serialize(), function(err) {
                if (err != null) {
                    console.debug(err);
                    return;
                }
                $('#loadSaveModal').foundation('reveal', 'close');
            });
        }
    });

    $('#deleteWorkspace').click(function() {
        if (selectedWorkspace) {
            deleteWorkspace(selectedWorkspace, function(err) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                $('#workspaceTable td[value=' + selectedWorkspace + ']').remove();
                selectedWorkspace = null;
            });
        }
    });

    $('#createNewWorkspace').click(function() {
        var newName = $('#newWorkspaceName').val();
        if (newName && newName != "") {
            createNewWorkspace(newName, ocargo.blocklyControl.serialize(), function(err) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                $('#loadSaveModal').foundation('reveal', 'close');
            });
        }
    });

    // If the user pressed the enter key in the textbox, should be the same as clicking the button
    $('#newWorkspaceName').on('keypress', function(e) {
        if (e.which == 13) {
            $('#createNewWorkspace').trigger('click');
        }
    });

    $('#bigCodeModeBtn').click(function() {
        if(ocargo.blocklyControl.bigCodeMode){
            ocargo.blocklyControl.decreaseBlockSize();
            $('#bigCodeModeBtn').text("Big Code Mode");
        } else {
            ocargo.blocklyControl.increaseBlockSize();
            $('#bigCodeModeBtn').html("<del>Big</del> Code Mode");
        }
    });

    var consoleSliderPosition = 50;
    
    $('#slideConsole').click(function() {
        if ($('#programmingConsole').width() != 0) {
            $('#paper').animate({width: '100%'}, {queue: false});
            $('#paper').animate({left: '0%'}, {queue: false});
            $('#programmingConsole').animate({width: '0%'}, {queue: false});
            $('#sliderControls').animate({left: '0%'}, {queue: false});
            $('#direct_drive').animate({left: '0%'}, {queue: false});
            $('#consoleSlider').animate({left: '0px'}, {queue: false, complete: function() { redrawBlockly(); }});
        } else {
            $('#paper').animate({ width: (100 - consoleSliderPosition) + '%' }, {queue: false});
            $('#paper').animate({ left: consoleSliderPosition + '%' }, {queue: false});
            $('#programmingConsole').animate({ width: consoleSliderPosition + '%' }, {queue: false});
            $('#sliderControls').animate({ left: consoleSliderPosition + '%' }, {queue: false})
            $('#direct_drive').animate({ left: consoleSliderPosition + '%' }, {queue: false})
            $('#consoleSlider').animate({ left: consoleSliderPosition + '%' }, {queue: false, complete: function() { redrawBlockly(); }});
        }
    });

    $('#toggleConsole').click(function() {
        if($('#blockly').css("display")=="none") {
            $('#pythonCode').fadeOut();
            $('#blockly').fadeIn();
            redrawBlockly();
        }
        else {
            $('#blockly').fadeOut();
            $('#pythonCode').fadeIn();
            ocargo.editor.setValue(Blockly.Python.workspaceToCode());
        }
    });

    $('#consoleSlider').on('mousedown', function(e){
        var slider = $(this);
        var p = slider.parent().offset();

        //disable drag when mouse leaves this or the parent
        slider.on('mouseup', function(e){
            slider.off('mousemove');
            slider.parent().off('mousemove');
            redrawBlockly();
        });
        slider.parent().on('mouseup', function(e) {
            slider.off('mousemove');
            slider.parent().off('mousemove');
            redrawBlockly();
        });

        slider.parent().on('mousemove', function(me){
            consoleSliderPosition = 100 * me.pageX / $( window ).width();
            if (consoleSliderPosition > 50) {
                consoleSliderPosition = 50;
            }

            $('#consoleSlider').css({ left: consoleSliderPosition + '%' });
            $('#paper').css({ width: (100 - consoleSliderPosition) + '%' });
            $('#paper').css({ left: consoleSliderPosition + '%' });
            $('#programmingConsole').css({ width: consoleSliderPosition + '%' });
            $('#sliderControls').css({ left: consoleSliderPosition + '%' });
            $('#direct_drive').css({ left: consoleSliderPosition + '%' });
            
            redrawBlockly();
        });
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

}

$(function() {
    initialiseDefault();
    trackDevelopment();
});
