'use strict';

var ocargo = ocargo || {};

function init() {
    // Setup blockly
    ocargo.blocklyControl = new ocargo.BlocklyControl();
    ocargo.blocklyCompiler = new ocargo.BlocklyCompiler();
    ocargo.blocklyControl.loadPreviousAttempt();
    window.addEventListener('unload', ocargo.blocklyControl.teardown);
    
    // Create the model
    ocargo.model = new ocargo.Model(PATH, DESTINATION, TRAFFIC_LIGHTS, MAX_FUEL);

    // Setup animation
    ocargo.animation = new ocargo.Animation(ocargo.model, DECOR, THREADS);

    // Setup the ui
    setupSliderListeners();
    setupDirectDriveListeners();
    setupLoadSaveListeners();
    setupMenuListeners();

    onStopOrResetControls();

    // default controller
    if(BLOCKLY_ENABLED) {
        $('#blockly').fadeIn();
        ocargo.controller = ocargo.blocklyControl;
    }
    else {
        $('#pythonCode').fadeIn();
        ocargo.controller = ocargo.editor;
    }

    startPopup("Level " + LEVEL_ID, "", LESSON + ocargo.messages.closebutton("Play"));

    setupFuelGauge(ocargo.model.map.nodes, BLOCKS);

    if ($.cookie("muted") === "true") {
        $('#muted').css('display','block');
        $('#unmuted').css('display','none');
        ocargo.sound.mute();
    }
}

var failures = 0;
var hasFailedThisTry = false;
function registerFailure() {
    if (!hasFailedThisTry) {
        failures += 1;
        hasFailedThisTry = true;
    }
    return (failures >= 3);
}

function sendAttempt(score) {
    // Send out the submitted data.
    if (LEVEL_ID) {
        $.ajax({
            url : '/game/submit',
            type : 'POST',
            data : {
                csrfmiddlewaretoken : $( '#csrfmiddlewaretoken' ).val(),
                level : LEVEL_ID,
                score : score,
                workspace : ocargo.blocklyControl.serialize(),
            },
            error : function(xhr,errmsg,err) {
                console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    }
}

// function to enable or disable pointerEvents on running python or blockly code
function allowCodeChanges(changesAllowed) {
    var setting = "";
    if (!changesAllowed) {
        setting = "none";
    }
    document.getElementById('blockly').style.pointerEvents = setting;
    var codeMirrors = document.getElementsByClassName('CodeMirror');
    var i;
    for (i = 0; i < codeMirrors.length; i++) {
        codeMirrors[i].style.pointerEvents = setting;
    }
}

function onPlayControls() {
    allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';

    document.getElementById('play').style.visibility='hidden';
    document.getElementById('pause').style.visibility='visible';
    document.getElementById('resume').style.visibility='hidden';
    document.getElementById('stop').style.visibility='visible';
    document.getElementById('reset').style.visibility='hidden';
    document.getElementById('step').style.visibility='hidden';

    document.getElementById('load').disabled = true;
    document.getElementById('save').disabled = true;
    document.getElementById('clear').disabled = true;
    document.getElementById('big_code_mode').disabled = true;
    document.getElementById('toggle_console').disabled = true;
    document.getElementById('help').disabled = true;
}

function onStepControls() {
    allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';

    document.getElementById('play').style.visibility='hidden';
    document.getElementById('pause').style.visibility='hidden';
    document.getElementById('resume').style.visibility='visible';
    document.getElementById('stop').style.visibility='visible';
    document.getElementById('reset').style.visibility='hidden';
    document.getElementById('step').style.visibility='hidden';

    document.getElementById('load').disabled = true;
    document.getElementById('save').disabled = true;
    document.getElementById('clear').disabled = true;
    document.getElementById('big_code_mode').disabled = true;
    document.getElementById('toggle_console').disabled = true;
    document.getElementById('help').disabled = true;
}

function onStopOrResetControls() {
    allowCodeChanges(true);

    document.getElementById('direct_drive').style.visibility='visible';  // TODO make this hidden unless blocks are clear or something...

    document.getElementById('play').style.visibility='visible';
    document.getElementById('pause').style.visibility='hidden';
    document.getElementById('resume').style.visibility='hidden';
    document.getElementById('stop').style.visibility='hidden';
    document.getElementById('reset').style.visibility='hidden';
    document.getElementById('step').style.visibility='visible';

    document.getElementById('load').disabled = false;
    document.getElementById('save').disabled = false;
    document.getElementById('clear').disabled = false;
    document.getElementById('big_code_mode').disabled = false;
    document.getElementById('toggle_console').disabled = false;
    document.getElementById('help').disabled = false;
}

function onEndControls() {
    allowCodeChanges(true);

    document.getElementById('direct_drive').style.visibility='visible';

    document.getElementById('play').style.visibility='hidden';
    document.getElementById('pause').style.visibility='hidden';
    document.getElementById('resume').style.visibility='hidden';
    document.getElementById('stop').style.visibility='hidden';
    document.getElementById('reset').style.visibility='visible';
    document.getElementById('step').style.visibility='hidden';

    document.getElementById('load').disabled = false;
    document.getElementById('save').disabled = false;
    document.getElementById('clear').disabled = false;
    document.getElementById('big_code_mode').disabled = false;
    document.getElementById('toggle_console').disabled = false;
    document.getElementById('help').disabled = false;
}

function onPauseControls() {
    allowCodeChanges(false);

    document.getElementById('play').style.visibility='hidden';
    document.getElementById('pause').style.visibility='hidden';
    document.getElementById('resume').style.visibility='visible';
    document.getElementById('stop').style.visibility='visible';
    document.getElementById('reset').style.visibility='hidden';
    document.getElementById('step').style.visibility='visible';
}

function onResumeControls() {
    allowCodeChanges(false);

    document.getElementById('play').style.visibility='hidden';
    document.getElementById('pause').style.visibility='visible';
    document.getElementById('resume').style.visibility='hidden';
    document.getElementById('stop').style.visibility='visible';
    document.getElementById('reset').style.visibility='hidden';
    document.getElementById('step').style.visibility='hidden';
}

function setupFuelGauge(nodes, blocks) {
    if(blocks.indexOf("turn_around") != -1 || blocks.indexOf("wait") != -1)
    {
        return;
    }

    for(var i = 0; i < nodes.length; i++) {
        if(nodes[i].connectedNodes.length > 2) {
            return;
        }
    }

    $('#fuelGuage').css("display","none");
}

function runProgramAndPrepareAnimation() {
    // clear animations
    ocargo.animation.resetAnimation();

    var program = ocargo.controller.prepare();

    // Starting sound
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: ocargo.sound.starting,
        description: 'starting sound',
    });

    program.run(ocargo.model);

    // Set controls ready for user to reset
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: onEndControls,
        description: 'onEndControls',
    });

    return true;
}

function setupDirectDriveListeners() {
    $('#moveForward').click(function() {
        onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
        moveForward(0, ANIMATION_LENGTH, onEndControls);
    });

    $('#turnLeft').click(function() {
        onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
        moveLeft(0, ANIMATION_LENGTH, onEndControls);
    });

    $('#turnRight').click(function() {
        onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
        moveRight(0, ANIMATION_LENGTH, onEndControls);
    });
    $('#go').click(function() {
        $('#play')[0].click();
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
                $(event.target).css('background-color', '#C0C0C0');
                selectedWorkspace = $(event.target).attr('value');
                $('#loadWorkspace').removeAttr('disabled');
                $('#deleteWorkspace').removeAttr('disabled');
            });

            // Finally show the modal dialog and reenable the button
            $('#loadModal').foundation('reveal', 'open');
            $('#load').removeAttr('disabled');

            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            $('#loadWorkspace').attr('disabled', 'disabled');
            $('#deleteWorkspace').attr('disabled', 'disabled');
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
                $(event.target).css('background-color', '#C0C0C0');
                selectedWorkspace = $(event.target).attr('value');
                var workspaceName = $(event.target)[0].innerHTML;
                document.getElementById("workspaceNameInput").value = workspaceName;
            });

            // Finally show the modal dialog and reenable the button
            $('#saveModal').foundation('reveal', 'open');
            $('#save').removeAttr('disabled');

            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            $('#overwriteWorkspace').attr('disabled', 'disabled');
        });
    });
    
    $('#saveWorkspace').click(function() {
        var newName = $('#workspaceNameInput').val();
        if (newName && newName != "") {
            var table = $("#saveWorkspaceTable");
            for (var i = 0; i < table[0].rows.length; i++) {
                 var cell = table[0].rows[i].cells[0];
                 var wName = cell.innerHTML;
                 if(wName == newName) {
                    deleteWorkspace(cell.attributes[0].value, 
                                    function(err, workspace) {
                                        if (err != null) {
                                            console.debug(err);
                                            return;
                                        }
                                    });
                 }
            }

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

    $('#deleteWorkspace').click(function() {
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

    // If the user pressed the enter key in the textbox, should be the same as clicking the button
    $('#newWorkspaceName').on('keypress', function(e) {
        if (e.which == 13) {
            $('#saveWorkspace').trigger('click');
        }
    });
}

function setupMenuListeners() {

    $('#play').click(function() {
        ocargo.blocklyControl.resetIncorrectBlock();
        onPlayControls();

        if (runProgramAndPrepareAnimation()) {
            ocargo.animation.playAnimation();
        }
        else {
            onStopOrResetControls();
        }
    });

    $('#pause').click(function() {
        ocargo.animation.pauseAnimation();
        onPauseControls();
    });

    $('#resume').click(function() {
        ocargo.animation.playAnimation();
        onResumeControls();
    });

    $('#stop').click(function() {
        ocargo.animation.resetAnimation();
        onStopOrResetControls();
    });

    $('#reset').click(function() {
        ocargo.animation.resetAnimation();
        onStopOrResetControls();
    });

    $('#step').click(function() {
        if (ocargo.animation.wasJustReset()) {
            runProgramAndPrepareAnimation();
        }
        ocargo.animation.stepAnimation(function() {
            if (ocargo.animation.isFinished()) {
                onEndControls();
            }
            else {
                onPauseControls();
            }
        });
        onStepControls();
    });

    $('#clear').click(function() {
        ocargo.blocklyControl.reset();
        onStopOrResetControls();
        ocargo.animation.resetAnimation();
    });

    var blockly = true;
    $('#toggle_console').click(function() {
        $('#blockly').css("display","none");
        $('#pythonCode').css("display","none");
        if(blockly) {
            $('#pythonCode').fadeIn();
            ocargo.editor.setValue(ocargo.blocklyCompiler.workspaceToPython());
            ocargo.controller = ocargo.editor;
            blockly = false;
        }
        else {
            $('#blockly').fadeIn();
            ocargo.blocklyControl.redrawBlockly();
            Blockly.mainWorkspace.render();
            ocargo.controller = ocargo.blocklyControl;
            blockly = true;
        }
    });

    $('#big_code_mode').click(function() {
        if(ocargo.blocklyControl.bigCodeMode){
            ocargo.blocklyControl.decreaseBlockSize()
        } else {
            ocargo.blocklyControl.increaseBlockSize();
        }
    });

    $('#help').click(function() {
        startPopup('Help', HINT, ocargo.messages.closebutton("Close help"));
    });

    $('#muted').click(function() {
        $('#muted').css('display','none');
        $('#unmuted').css('display','block');
        ocargo.sound.mute();
    });

    $('#unmuted').click(function() {
        $('#muted').css('display','block');
        $('#unmuted').css('display','none');
        ocargo.sound.mute();
    });

    $('#quit').click(function() {
        window.location.href = "/game/"
    });
}

$(function() {
    init();
});
