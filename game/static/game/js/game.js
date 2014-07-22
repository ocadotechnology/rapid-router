var ocargo = ocargo || {};

'use strict';

function init() {
    ocargo.time = new ocargo.Time();
    ocargo.ui = new ocargo.SimpleUi();
    ocargo.blocklyControl = new ocargo.BlocklyControl();
    ocargo.blocklyCompiler = new ocargo.BlocklyCompiler();
    
    ocargo.level = createLevel(PATH, DESTINATION, DECOR, TRAFFIC_LIGHTS, MAX_FUEL, NEXT_LEVEL, NEXT_EPISODE);
    ocargo.level.levelId = JSON.parse(LEVEL_ID);

    setupSliderListeners();
    setupDirectDriveListeners();
    setupLoadSaveListeners();
    setupMenuListeners();

    window.addEventListener('unload', ocargo.blocklyControl.teardown);

    enableDirectControl();
    ocargo.blocklyControl.loadPreviousAttempt();
    startPopup("Level " + LEVEL_ID, "", LESSON + ocargo.messages.closebutton("Play"));

    if ($.cookie("muted") === "true") {
        $('#mute').text("Unmute");
        ocargo.sound.mute();
    }

    if(BLOCKLY_ENABLED) {
        $('#blockly').fadeIn();
    }
    else {
        $('#pythonCode').fadeIn();
    }
}

function createLevel(nodeData, destination, decor, trafficLightData, maxFuel, nextLevel, nextEpisode) {
    var nodes = createNodes(nodeData);
    var trafficLights = createAndAddTrafficLightsToNodes(nodes, trafficLightData);
    var destinationIndex = findByCoordinate(destination, nodes);
    var dest = destinationIndex > -1 ? nodes[destinationIndex] : nodes[nodes.length - 1];
    var map = new ocargo.Map(nodes, decor, trafficLights, dest);
    var vans = [];

    var previousNode = nodes[0];
    var startNode = nodes[0].connectedNodes[0];
    for (var i = 0; i < THREADS; i++) {
        vans.push(new ocargo.Van(i,previousNode, startNode, maxFuel));
    }

    ocargo.ui.renderMap(map);
    ocargo.ui.renderVans(vans);

    return new ocargo.Level(map, vans, nextLevel, nextEpisode);
}

function createNodes(nodeData) {
    var nodes = [];

    // Create nodes with coords
    for (var i = 0; i < nodeData.length; i++) {
         var coordinate = new ocargo.Coordinate(
            nodeData[i]['coordinate'][0], nodeData[i]['coordinate'][1]);
         nodes.push(new ocargo.Node(coordinate));
    }

    // Link nodes (must be done in second loop so that linked nodes have definitely been created)
    for (var i = 0; i < nodeData.length; i++) {
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
        var van = new ocargo.Van(i,previousNode, startNode, MAX_FUEL);
        ocargo.level.vans[i] = van;
        ocargo.ui.setVanToFront(previousNode, startNode, van);
    }
}

function levelWon(level) {
    console.debug('You win!');
    ocargo.sound.win();

    var scoreArray = level.pathFinder.getScore();
    sendAttempt(scoreArray[0]);
    
    var message = '';
    if (level.nextLevel != null) {
        message = ocargo.messages.nextLevelButton(level.nextLevel);
    } 
    else {
        if (level.nextEpisode != null && level.nextEpisode !== "") {
            message = ocargo.messages.nextEpisodeButton(level.nextEpisode);
        } else {
            message = ocargo.messages.lastLevel;
        }
    }

    startPopup("You win!", scoreArray[1], message);
};

function levelFailed(level, msg) {
    console.debug('You lose!');
    ocargo.sound.failure();

    sendAttempt(0);

    var title = 'Oh dear! :(';
    startPopup(title, '', msg + ocargo.messages.closebutton("Try again"));
    $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v3.svg)');
    
    level.fails++;
    if (level.fails >= FAILS_BEFORE_HINT) {
        var hintBtns = $("#hintPopupBtn");
        if (hintBtns.length === null || hintBtns.length === 0) {
            $("#myModal > .mainText").append('<p id="hintBtnPara">' +
                '<button id="hintPopupBtn">' + ocargo.messages.needHint + '</button>' + 
                '</p><p id="hintText">' + HINT + '</p>');
            if(level.hintOpened){
                $("#hintBtnPara").hide();
            } 
            else {
                $("#hintText" ).hide();
                $("#hintPopupBtn").click( function(){
                    $("#hintText").show(500);
                    $("#hintBtnPara").hide();
                    level.hintOpened = true;
                });
            }
        }
    }
};

function sendAttempt(score) {
    // Send out the submitted data.
    if (ocargo.level.levelId) {
        var attemptData = JSON.stringify(ocargo.level.attemptData);

        $.ajax({
            url : '/game/submit',
            type : 'POST',
            dataType: 'json',
            data : {
                attemptData : attemptData,
                csrfmiddlewaretoken :$( '#csrfmiddlewaretoken' ).val(),
                score : score,
                workspace : ocargo.blocklyControl.serialize()
            },
            success : function(json) {
            },
            error : function(xhr,errmsg,err) {
                console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    }
    return false;
}

function setupDirectDriveListeners() {
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
        ocargo.blocklyControl.resetIncorrectBlock();
        disableDirectControl();

        try {
            var program = ocargo.blocklyCompiler.compile();
        } catch (error) {
            enableDirectControl();
            levelFailed(ocargo.level, 'Your program crashed!<br>' + error);
            return;
        }

        clearVanData();
        ocargo.time.resetTime();
        ocargo.level.playProgram(program);
    });
}

function setupSliderListeners() {
    var getSliderRightLimit = function() {return $(window).width()/2};
    var getSliderLeftLimit = function() {return 46};
    var consoleSliderPosition = $(window).width()/2;
    var open = true;

    $('#slideConsole').click(function() {
        var pageWidth = $(window).width();
        var rightLimit = getSliderRightLimit();
        var leftLimit = getSliderLeftLimit();

        if (open) {
            $('#paper').animate({width: pageWidth + 'px'}, {queue: false});
            $('#paper').animate({left: leftLimit + 'px'}, {queue: false});
            $('#sliderControls').animate({left: leftLimit + 'px'}, {queue: false});
            $('#direct_drive').animate({left: leftLimit + 'px'}, {queue: false});
            $('#consoleSlider').animate({left: leftLimit + 'px'}, {queue: false});
            open = false;
        } else {
            $('#paper').animate({ width: (pageWidth - consoleSliderPosition) + 'px' }, {queue: false});
            $('#paper').animate({ left: consoleSliderPosition + 'px' }, {queue: false});
            $('#sliderControls').animate({ left: consoleSliderPosition + 'px' }, {queue: false})
            $('#direct_drive').animate({ left: consoleSliderPosition + 'px' }, {queue: false})
            $('#consoleSlider').animate({ left: consoleSliderPosition + 'px' }, {queue: false});
            open = true;
        }
    });

    $('#consoleSlider').on('mousedown', function(e){
        var slider = $(this);
        var p = slider.parent().offset();

        //disable drag when mouse leaves this or the parent
        slider.on('mouseup', function(e){
            slider.off('mousemove');
            slider.parent().off('mousemove');
            ocargo.blocklyControl.redrawBlockly();
        });
        slider.parent().on('mouseup', function(e) {
            slider.off('mousemove');
            slider.parent().off('mousemove');
            ocargo.blocklyControl.redrawBlockly();
        });

        slider.parent().on('mousemove', function(me){
            consoleSliderPosition = me.pageX;
            var pageWidth = $(window).width();
            var rightLimit = getSliderRightLimit();
            var leftLimit = getSliderLeftLimit();

            if (consoleSliderPosition > rightLimit) {
                consoleSliderPosition = rightLimit;
            }
            if (consoleSliderPosition < leftLimit) {
                consoleSliderPosition = leftLimit;
            }

            $('#consoleSlider').css({ left: consoleSliderPosition + 'px' });
            $('#paper').css({ width: (pageWidth - consoleSliderPosition) + 'px' });
            $('#paper').css({ left: consoleSliderPosition + 'px' });
            $('#programmingConsole').css({ width: consoleSliderPosition + 'px' });
            $('#sliderControls').css({ left: consoleSliderPosition + 'px' });
            $('#direct_drive').css({ left: consoleSliderPosition + 'px' });
            
            ocargo.blocklyControl.redrawBlockly();
        });
    });
}

function setupLoadSaveListeners() {

    var selectedWorkspace = null;

    var populateTable = function(tableName, workspaces) {
        var table = $('#'+tableName);

        // Remove click listeners to avoid memory leak and remove all rows
        $('#'+tableName+' td').off('click');
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
    }


    $('#load').click(function() {
        // Disable the button to stop users clicking it multiple times
        // whilst waiting for the table data to load
        $('#load').attr('disabled', 'disabled');
        retrieveAllWorkspaces(function(err, workspaces) {
            if (err != null) {
                console.debug(err);
                return;
            }

            populateTable("loadWorkspaceTable", workspaces);

            // Add click listeners to all rows
            $('#loadWorkspaceTable td').on('click', function(event) {
                $('#loadWorkspaceTable td').css('background-color', '#FFFFFF');
                $('#loadWorkspaceTable td').css('cursor', 'pointer');
                $(event.target).css('background-color', '#C0C0C0');
                selectedWorkspace = $(event.target).attr('value');
                $('#loadWorkspace').removeAttr('disabled');
                $('#lDeleteWorkspace').removeAttr('disabled');
            });

            // Finally show the modal dialog and reenable the button
            $('#loadModal').foundation('reveal', 'open');
            $('#load').removeAttr('disabled');

            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            $('#loadWorkspace').attr('disabled', 'disabled');
            $('#lDeleteWorkspace').attr('disabled', 'disabled');
        });
    });

    $('#save').click(function() {
        // Disable the button to stop users clicking it multiple times
        // whilst waiting for the table data to load
        $('#save').attr('disabled', 'disabled');

        retrieveAllWorkspaces(function(err, workspaces) {
            if (err != null) {
                console.debug(err);
                return;
            }

            populateTable("saveWorkspaceTable", workspaces);

            // Add click listeners to all rows
            $('#saveWorkspaceTable td').on('click', function(event) {
                $('#saveWorkspaceTable td').css('background-color', '#FFFFFF');
                $('#saveWorkspaceTable td').css('cursor', 'pointer');
                $(event.target).css('background-color', '#C0C0C0');
                selectedWorkspace = $(event.target).attr('value');
                var workspaceName = $(event.target)[0].innerHTML;
                document.getElementById("workspaceNameInput").value = workspaceName;
                $('#sDeleteWorkspace').removeAttr('disabled');
            });

            // Finally show the modal dialog and reenable the button
            $('#saveModal').foundation('reveal', 'open');
            $('#save').removeAttr('disabled');

            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            $('#overwriteWorkspace').attr('disabled', 'disabled');
            $('#sDeleteWorkspace').attr('disabled', 'disabled');
        });
    });
    
    $('#saveWorkspace').click(function() {
        var newName = $('#workspaceNameInput').val();
        if (newName && newName != "") {
            createNewWorkspace(newName, ocargo.blocklyControl.serialize(), function(err) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                $('#saveModal').foundation('reveal', 'close');
            });
        }
    });

    $('#loadWorkspace').click(function() {
        if (selectedWorkspace) {
            retrieveWorkspace(selectedWorkspace, function(err, workspace) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                ocargo.blocklyControl.deserialize(workspace);
                ocargo.blocklyControl.redrawBlockly();
                $('#loadModal').foundation('reveal', 'close');
            });
        }
    });

    $('#lDeleteWorkspace').click(function() {
        if (selectedWorkspace) {
            deleteWorkspace(selectedWorkspace, function(err) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                $('#loadWorkspaceTable td[value=' + selectedWorkspace + ']').remove();
                selectedWorkspace = null;
            });
        }
    });

    $('#sDeleteWorkspace').click(function() {
        if (selectedWorkspace) {
            deleteWorkspace(selectedWorkspace, function(err) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                $('#saveWorkspaceTable td[value=' + selectedWorkspace + ']').remove();
                selectedWorkspace = null;
            });
        }
    });

    // If the user pressed the enter key in the textbox, should be the same as clicking the button
    $('#newWorkspaceName').on('keypress', function(e) {
        if (e.which == 13) {
            $('#saveWorkspace').trigger('click');
        }
    });
}

function setupMenuListeners() {

    $('#play2').click(function() {
        ocargo.blocklyControl.resetIncorrectBlock();
        disableDirectControl();

        try {
            var program = ocargo.blocklyCompiler.compile();
        } catch (error) {
            enableDirectControl();
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
                ocargo.level.program = ocargo.blocklyCompiler.compile();
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
    });

    $('#stop').click(function() {
        ocargo.level.program.terminate();
    });

    $('#toggle_console').click(function() {
        if($('#blockly').css("display")=="none") {
            $('#pythonCode').css("display","none");
            $('#blockly').fadeIn();
        }
        else {
            $('#blockly').css("display","none");
            $('#pythonCode').fadeIn();
            ocargo.editor.setValue(Blockly.Python.workspaceToCode());
        }
    });

    $('#big_code_mode').click(function() {
        if(ocargo.blocklyControl.bigCodeMode){
            ocargo.blocklyControl.decreaseBlockSize()
        } else {
            ocargo.blocklyControl.increaseBlockSize();
        }
    });


    $('#quit').click(function() {
        window.location.href = "/game/";
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
    init();
});
