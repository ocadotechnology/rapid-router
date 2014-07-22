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
    setupListeners();
    enableDirectControl();

    // startPopup("Level " + LEVEL_ID, "", LESSON + ocargo.messages.closebutton("Play"));

    if ($.cookie("muted") === "true") {
        $('#mute').text("Unmute");
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
        // $.ajax({
        //     url : '/game/submit',
        //     type : 'POST',
        //     data : {
        //         attemptData : attemptData,
        //         csrfmiddlewaretoken :$( '#csrfmiddlewaretoken' ).val(),
        //         score : score,
        //         workspace : ocargo.blocklyControl.serialize()
        //     },
        //     error : function(xhr,errmsg,err) {
        //         console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        //     }
        // });
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
    //document.getElementById('controls').style.visibility='hidden';
    document.getElementById('direct_drive').style.visibility='hidden';
    document.getElementById('stop').style.visibility='visible';
    document.getElementById('moveForward').disabled = true;
    document.getElementById('turnLeft').disabled = true;
    document.getElementById('turnRight').disabled = true;
    document.getElementById('play').disabled = true;
    //document.getElementById('step').disabled = true;
}

function runProgramAndPrepareAnimation() {
    // clear animations
    ocargo.animation.resetAnimation();
    // try to compile and run program
    try {
        var program = ocargo.blocklyCompiler.compile();
        program.run(ocargo.model);
    }
    catch (error) {
        // print error for now
        console.info("compilation error " + error);
        return false;
    }
    return true;
}

function setupListeners() {
    // Direct Control Listeners
    $('#moveForward').click(function() {
        disableDirectControl();
        ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
        moveForward(0, enableDirectControl);
    });

    $('#turnLeft').click(function() {
        disableDirectControl();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
        moveLeft(0, enableDirectControl);
    });

    $('#turnRight').click(function() {
        disableDirectControl();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
        moveRight(0, enableDirectControl);
    });

    // Normal Control Listeners
    $('#play').click(function() {
        ocargo.blocklyControl.resetIncorrectBlock();
        disableDirectControl();
        if (runProgramAndPrepareAnimation()) {
            // append function call to ~~enable direct control~~ TODO: sort all buttons out at end of a full run of playing?
            var timestamp = ocargo.animation.getLastTimestamp();
            ocargo.animation.queueAnimation({
                timestamp: timestamp,
                type: 'callable',
                functionCall: enableDirectControl,
            });
            ocargo.animation.playAnimation();
        } else {
            enableDirectControl();
        }
    });

    $('#pause').click(function() {
        ocargo.animation.pauseAnimation();
    });

    $('#resume').click(function() {
        ocargo.animation.playAnimation();
    });

    $('#step').click(function() {
        if (!ocargo.animation.isFinished()) {  // NB Should NOT be *visible* at the end of execution - should wait for a reset!
            ocargo.animation.stepAnimation();
        } else {
            runProgramAndPrepareAnimation();
            ocargo.animation.stepAnimation();
        }
        // show start over button
        $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v3.svg)');
    });

    $('#stop').click(function() {
        ocargo.animation.resetAnimation();
    });

    $('#reset').click(function() {
        ocargo.animation.resetAnimation();
        // show go button
        $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v2.svg)');
    });
    
    $('#help').click(function() {
        startPopup('Help', HINT, ocargo.messages.closebutton("Close help"));
    });

    $('#clear').click(function() {
        ocargo.blocklyControl.reset();
        enableDirectControl();
        ocargo.animation.resetAnimation();
        // show go button
        $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v2.svg)');
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
            $('#consoleSlider').animate({left: '0px'}, {queue: false, complete: function() { ocargo.blocklyControl.redrawBlockly(); }});
        } else {
            $('#paper').animate({ width: (100 - consoleSliderPosition) + '%' }, {queue: false});
            $('#paper').animate({ left: consoleSliderPosition + '%' }, {queue: false});
            $('#programmingConsole').animate({ width: consoleSliderPosition + '%' }, {queue: false});
            $('#sliderControls').animate({ left: consoleSliderPosition + '%' }, {queue: false})
            $('#direct_drive').animate({ left: consoleSliderPosition + '%' }, {queue: false})
            $('#consoleSlider').animate({ left: consoleSliderPosition + '%' }, {queue: false, complete: function() { ocargo.blocklyControl.redrawBlockly(); }});
        }
    });

    $('#toggleConsole').click(function() {
        if($('#blockly').css("display")=="none") {
            $('#pythonCode').fadeOut();
            $('#blockly').fadeIn();
            ocargo.blocklyControl.redrawBlockly();
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
            ocargo.blocklyControl.redrawBlockly();
        });
        slider.parent().on('mouseup', function(e) {
            slider.off('mousemove');
            slider.parent().off('mousemove');
            ocargo.blocklyControl.redrawBlockly();
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
            
            ocargo.blocklyControl.redrawBlockly();
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
    init();
});
