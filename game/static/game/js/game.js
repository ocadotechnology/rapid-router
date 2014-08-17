'use strict';

var ocargo = ocargo || {};

var tabs = [];

initCustomBlocks();
ocargo.blocklyControl = new ocargo.BlocklyControl();
ocargo.blocklyCompiler = new ocargo.BlocklyCompiler();
ocargo.drawing = new ocargo.Drawing();
ocargo.model = new ocargo.Model(PATH, DESTINATIONS, TRAFFIC_LIGHTS, MAX_FUEL);
ocargo.animation = new ocargo.Animation(ocargo.model, DECOR, THREADS);
ocargo.saving = new ocargo.Saving();
ocargo.blocklyControl.loadPreviousAttempt();

// Setup the ui
setupSliderListeners();
setupDirectDriveListeners();
setupFuelGauge(ocargo.model.map.nodes, BLOCKS);
setupTabs();

onStopControls();

// default controller
if(BLOCKLY_ENABLED) {
    ocargo.controller = ocargo.blocklyControl;
}
else {
    ocargo.controller = ocargo.editor;
}

// Setup blockly to python
Blockly.Python.init();
window.addEventListener('unload', ocargo.blocklyControl.teardown);

// Start the popup
ocargo.Drawing.startPopup("Level " + LEVEL_ID, "", LESSON + ocargo.messages.closebutton("Play"));




function runProgramAndPrepareAnimation() {
    var result = ocargo.controller.prepare();
    if(!result.success) {
        ocargo.Drawing.startPopup(ocargo.messages.failTitle, "", result.error);
        return false;
    }
    var program = result.program;

    ocargo.blocklyControl.resetIncorrectBlock();

    // clear animations
    ocargo.animation.resetAnimation();

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
        functionCall: function() {onStopControls();},
        description: 'onStopControls',
    });

    return true;
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

var failures = 0;
var hasFailedThisTry = false;
function registerFailure() {
    if (!hasFailedThisTry) {
        failures += 1;
        hasFailedThisTry = true;
    }
    return (failures >= 3);
}

// function to enable or disable pointerEvents on running python or blockly code
function allowCodeChanges(changesAllowed) {
    ocargo.blocklyControl.setCodeChangesAllowed(changesAllowed);

    var setting = "";
    if (!changesAllowed) {
        setting = "none";
    }

    var codeMirrors = document.getElementsByClassName('CodeMirror');
    var i;
    for (i = 0; i < codeMirrors.length; i++) {
        codeMirrors[i].style.pointerEvents = setting;
    }
}

function setupFuelGauge(nodes, blocks) {
    if (FUEL_GAUGE) {
        document.getElementById('fuelGauge').style.visibility='visible';
            if (blocks.indexOf("turn_around") !== -1 || blocks.indexOf("wait") !== -1) {
            return;
        }

        for(var i = 0; i < nodes.length; i++) {
            if(nodes[i].connectedNodes.length > 2) {
                return;
            }
        }
    }
}

function setupDirectDriveListeners() {
    $('#moveForward').click(function() {
        onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
        ocargo.drawing.moveForward(0, ANIMATION_LENGTH, function() {onStopControls();});
    });
    $('#turnLeft').click(function() {
        onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
        ocargo.drawing.moveLeft(0, ANIMATION_LENGTH, function() {onStopControls();});
    });
    $('#turnRight').click(function() {
        onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
        ocargo.drawing.moveRight(0, ANIMATION_LENGTH, function() {onStopControls();});
    });
    $('#go').click(function() {
        $('#play_radio').trigger('click');
    });
}


function setupSliderListeners() {
    var getSliderRightLimit = function(pageWidth) {return pageWidth/2;};
    var getSliderLeftLimit = function() {return 46;};
    var consoleSliderPosition = $(window).width()/2;

    /**
    $('#hide').click(function() {
        var pageWidth = $(window).width();
        var leftLimit = getSliderLeftLimit();

        $('#paper').animate({width: pageWidth + 'px'}, {queue: false});
        $('#paper').animate({left: leftLimit + 'px'}, {queue: false});
        $('#hide').animate({left: leftLimit + 'px'}, {queue: false});
        $('#show').animate({left: leftLimit + 'px'}, {queue: false});
        $('#direct_drive').animate({left: leftLimit + 'px'}, {queue: false});
        $('#consoleSlider').css('left', leftLimit + 'px');

        $('#hide').css('display','none');
        $('#show').css('display','block');
        $('#consoleSlider').css('display','none');
    });

    $('#show').click(function() {
        var pageWidth = $(window).width();

        $('#paper').animate({ width: (pageWidth - consoleSliderPosition) + 'px' }, {queue: false});
        $('#paper').animate({ left: consoleSliderPosition + 'px' }, {queue: false});
        $('#hide').animate({ left: consoleSliderPosition + 'px' }, {queue: false});
        $('#show').animate({ left: consoleSliderPosition + 'px' }, {queue: false});
        $('#direct_drive').animate({ left: consoleSliderPosition + 'px' }, {queue: false});
        $('#consoleSlider').animate({ left: consoleSliderPosition + 'px' }, {queue: false});

        $('#hide').css('display','block');
        $('#show').css('display','none');
        $('#consoleSlider').css('display','block');
    });

    $('#consoleSlider').on('mousedown', function(e){
        var slider = $(this);

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
            var rightLimit = getSliderRightLimit(pageWidth);
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
            $('#hide').css({ left: consoleSliderPosition + 'px' });
            $('#show').css({ left: consoleSliderPosition + 'px' });
            $('#direct_drive').css({ left: consoleSliderPosition + 'px' });
            
            ocargo.blocklyControl.redrawBlockly();
        });
    });
**/
}

function setupTabs() {
    setupTabListeners();
    setupBlocklyPane();
    setupPythonPane();
    setupLoadPane();
    setupSavePane();
    setupHelpPane();

    function setupTabListeners() {
        function onBlockly() {
            var tab = tabs['blockly'];
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            ocargo.blocklyControl.redrawBlockly();
            Blockly.mainWorkspace.render();
            // reset blockly to python converter
            Blockly.Python.init();
            ocargo.controller = ocargo.blocklyControl;
            ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
        }

        function onPython() {
            var tab = tabs['python'];
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            ocargo.editor.setValue(ocargo.blocklyCompiler.workspaceToPython());
            ocargo.controller = ocargo.editor;
        }

        function onPlay() {
            var existingHtml = tabs['play'].getText();

            if(existingHtml == "Play") {
                if(runProgramAndPrepareAnimation()) {
                    onPlayControls();
                    ocargo.animation.playAnimation();
                }
                
            }
            else if(existingHtml == 'Pause') {
                onPauseControls();
                ocargo.animation.pauseAnimation();
            }
            else if(existingHtml == 'Resume') {
                // Important ordering
                onResumeControls();
                ocargo.animation.playAnimation();
            }

            currentTabSelected.select();
        }

        function onStop() {
            ocargo.animation.resetAnimation();
            onStopControls();

            currentTabSelected.select();
        }

        function onStep() {
            if (ocargo.animation.isFinished()) {
                var successfullyCompiled = runProgramAndPrepareAnimation();
                if(!successfullyCompiled) {
                    return;
                }
            }

            ocargo.animation.stepAnimation(function() {
                if (ocargo.animation.isFinished()) {
                    onStopControls();
                }
                else {
                    onPauseControls();
                }
            });
            onStepControls();

            currentTabSelected.select();
        }

        
        function onLoad() {
            var tab = tabs['load'];
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            onLoadTrigger();
        }

        function onSave() {
            var tab = tabs['save'];
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            onSaveTrigger();
        }

        function onClearProgram() {
            ocargo.blocklyControl.reset();
            ocargo.editor.reset();

            currentTabSelected.select();
        }

        function onBigCodeMode() {
            tabs['blockly'].select();

            if(ocargo.blocklyControl.bigCodeMode){
                tabs['big_code_mode'].setContents('/static/game/image/icons/big_code_mode.svg', "Enlarge");
                ocargo.blocklyControl.decreaseBlockSize();
            } else {
                tabs['big_code_mode'].setContents('/static/game/image/icons/big_code_mode.svg', "Shrink");
                ocargo.blocklyControl.increaseBlockSize();
            }
            ocargo.blocklyControl.showFlyout();
            ocargo.blocklyControl.showFlyout();

            ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
        }

        function onPrint() {
            currentTabSelected.select();
        }

        function onMute() {
            if (tabs['mute'].getContents() === 'Unmute') {
                ocargo.sound.unmute();
                tabs['mute'].setContents('/static/game/image/icons/muted.svg', 'Mute');
            } else {
                ocargo.sound.mute();
                tabs['mute'].setContents('/static/game/image/icons/unmuted.svg', 'Unmute');
            }
            currentTabSelected.select();
        }

        function onHelp() {
            var tab = tabs['help'];
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;
        }

        function onQuit() {
            window.location.href = "/game/";
        }

        tabs['blockly'] = new ocargo.Tab($('#blockly_radio'), $('#blockly_radio + label'), onBlockly, $('#blockly_pane'));
        tabs['python'] = new ocargo.Tab($('#python_radio'), $('#python_radio + label'), onPython, $('#python_pane'));

        tabs['play'] = new ocargo.Tab($('#play_radio'), $('#play_radio + label'), onPlay);
        tabs['stop'] = new ocargo.Tab($('#stop_radio'), $('#stop_radio + label'), onStop);
        tabs['step'] = new ocargo.Tab($('#step_radio'), $('#step_radio + label'), onStep);

        tabs['load'] = new ocargo.Tab($('#load_radio'), $('#load_radio + label'), onLoad, $('#load_pane'));
        tabs['save'] = new ocargo.Tab($('#save_radio'), $('#save_radio + label'), onSave, $('#save_pane'));
        tabs['clear_program'] = new ocargo.Tab($('#clear_program_radio'), $('#clear_program_radio + label'), onClearProgram);

        tabs['big_code_mode'] = new ocargo.Tab($('#big_code_mode_radio'), $('#big_code_mode_radio + label'), onBigCodeMode);
        tabs['print'] = new ocargo.Tab($('#print_radio'), $('#print_radio + label'), onPrint);
        tabs['help'] = new ocargo.Tab($('#help_radio'), $('#help_radio + label'), onHelp, $('#help_pane'));
        tabs['quit'] = new ocargo.Tab($('#quit_radio'), $('#quit_radio + label'), onQuit);

        tabs['mute'] = new ocargo.Tab($('#mute_radio'), $('#mute_radio + label'), onMute);

        if ($.cookie("muted") === "true") {
            ocargo.sound.mute();
            tabs['mute'].setContents('/static/game/image/icons/unmuted.svg', 'Unmute');
        }


        //  Trigger the initial tabs
        tabs['blockly'].select();
        var currentTabSelected = tabs['blockly'];
  
        // Enable all the permanently enabled tabs
        tabs['blockly'].setEnabled(true);
        tabs['python'].setEnabled(true);
        tabs['play'].setEnabled(true);
        tabs['mute'].setEnabled(true);
        tabs['quit'].setEnabled(true);

        // Remove the panes of all the initially disabled tabs
        tabs['python'].setPaneEnabled(false);
        tabs['load'].setPaneEnabled(false);
        tabs['save'].setPaneEnabled(false);
        tabs['help'].setPaneEnabled(false);
    }

    function setupBlocklyPane() {
        ocargo.blocklyControl.showFlyout();
        ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
    }

    function setupPythonPane() {
        $('#clear_console').click(function (e) {
            $('#consoleOutput').text('');
        });
    }

    var selectedWorkspace = null;

    function setupLoadPane() {
        $('#loadWorkspace').click(function() {
            if (selectedWorkspace) {
                ocargo.saving.retrieveWorkspace(selectedWorkspace, function(err, workspace) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }

                    ocargo.blocklyControl.deserialize(workspace);
                    ocargo.blocklyControl.redrawBlockly();
                    $('#loadModal').foundation('reveal', 'close');
                });
            }

            tabs['blockly'].select();
        });

        $('#deleteWorkspace').click(function() {
            if (selectedWorkspace) {
                ocargo.saving.deleteWorkspace(selectedWorkspace, function(err) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }
                    $('#loadWorkspaceTable td[value=' + selectedWorkspace + ']').remove();
                    selectedWorkspace = null;
                });
            }
        });
    }

    function setupSavePane() {
        $('#saveWorkspace').click(function() {
            var newName = $('#workspaceNameInput').val();
            if (newName && newName != "") {
                var table = $("#saveWorkspaceTable");
                for (var i = 0; i < table[0].rows.length; i++) {
                     var cell = table[0].rows[i].cells[0];
                     var wName = cell.innerHTML;
                     if (wName == newName) {
                        ocargo.saving.deleteWorkspace(cell.attributes[0].value, 
                                        function(err, workspace) {
                                            if (err != null) {
                                                console.debug(err);
                                                return;
                                            }
                                        });
                     }
                }

                ocargo.saving.createNewWorkspace(newName, ocargo.blocklyControl.serialize(), function(err) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }
                    $('#saveModal').foundation('reveal', 'close');
                });
            }

            tabs['blockly'].select();
        });

        // If the user pressed the enter key in the textbox, should be the same as clicking the button
        $('#newWorkspaceName').on('keypress', function(e) {
            if (e.which == 13) {
                $('#saveWorkspace').trigger('click');
            }
        });
    }

    function setupHelpPane() {
        $('#help_pane').html(HINT)
    }

    // Helper methods for loading and saving tabs
    function onLoadTrigger() {
        selectedWorkspace = null;

        // TODO Disable the tab to stop users clicking it multiple times
        // whilst waiting for the table data to load
        // JQuery currently throwing errors :(

        ocargo.saving.retrieveListOfWorkspaces(function(err, workspaces) {
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

            
            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            $('#loadWorkspace').attr('disabled', 'disabled');
            $('#deleteWorkspace').attr('disabled', 'disabled');
        });
    }

    function onSaveTrigger() {
        selectedWorkspace = null;

        // TODO Disable the tab to stop users clicking it multiple times
        // whilst waiting for the table data to load
        // JQuery currently throwing errors :()
        
        ocargo.saving.retrieveListOfWorkspaces(function(err, workspaces) {
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

            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            
        });
    }
    
    function populateTable (tableName, workspaces) {
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
    };
}

function onPlayControls() {
    allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';
    
    tabs['play'].setContents('/static/game/image/icons/pause.svg', 'Pause');
    tabs['stop'].setEnabled(true);
    tabs['step'].setEnabled(false);

    tabs['load'].setEnabled(false);
    tabs['save'].setEnabled(false);
    tabs['clear_program'].setEnabled(false);
    tabs['big_code_mode'].setEnabled(false);
    tabs['print'].setEnabled(false);
    tabs['help'].setEnabled(false);
}

function onStepControls() {
    allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';

    tabs['play'].setContents('/static/game/image/icons/play.svg', 'Resume');
    tabs['stop'].setEnabled(true);
    tabs['step'].setEnabled(false);

    tabs['load'].setEnabled(false);
    tabs['save'].setEnabled(false);
    tabs['clear_program'].setEnabled(false);
    tabs['big_code_mode'].setEnabled(false);
    tabs['print'].setEnabled(false);
    tabs['help'].setEnabled(false);
}

function onStopControls() {
    allowCodeChanges(true);

    // TODO make this hidden unless blocks are clear or something... 
    document.getElementById('direct_drive').style.visibility='visible';
    
    tabs['play'].setContents('/static/game/image/icons/play.svg', 'Play');
    tabs['stop'].setEnabled(false);
    tabs['step'].setEnabled(true);

    tabs['load'].setEnabled(true);
    tabs['save'].setEnabled(true);
    tabs['clear_program'].setEnabled(true);
    tabs['big_code_mode'].setEnabled(true);
    tabs['print'].setEnabled(true);
    tabs['help'].setEnabled(true);
}

function onPauseControls() {
    tabs['play'].setContents('/static/game/image/icons/play.svg', 'Resume');
    tabs['stop'].setEnabled(true);
    tabs['step'].setEnabled(true);
}

function onResumeControls() {
    tabs['play'].setContents('/static/game/image/icons/pause.svg', 'Pause');
    tabs['stop'].setEnabled(true);
    tabs['step'].setEnabled(false);
}
