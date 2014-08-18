'use strict';

var ocargo = ocargo || {};

ocargo.Game = function() {

    this.tabs = [];
    this.failures = 0;
    this.hasFailedThisTry = false;
    this.currentTabSelected;

};

ocargo.Game.prototype.setup = function() {

    initCustomBlocks();
    ocargo.blocklyControl = new ocargo.BlocklyControl();
    ocargo.blocklyCompiler = new ocargo.BlocklyCompiler();
    ocargo.drawing = new ocargo.Drawing();
    ocargo.model = new ocargo.Model(PATH, DESTINATIONS, TRAFFIC_LIGHTS, MAX_FUEL);
    ocargo.animation = new ocargo.Animation(ocargo.model, DECOR, THREADS);
    ocargo.saving = new ocargo.Saving();
    ocargo.blocklyControl.loadPreviousAttempt();

    // Setup the ui
    this.setupSliderListeners();
    this.setupDirectDriveListeners();
    this.setupFuelGauge(ocargo.model.map.nodes, BLOCKS);
    this.setupTabs();

    this.onStopControls();

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
    ocargo.Drawing.startPopup("Level " + LEVEL_ID, "", LESSON + ocargo.messages.closebutton("Play"), true);
};

ocargo.Game.prototype.runProgramAndPrepareAnimation = function() {
    var result = ocargo.controller.prepare();
    if(!result.success) {
        ocargo.Drawing.startPopup(ocargo.messages.failTitle, "", result.error, false);
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
        functionCall: function() {ocargo.game.onStopControls();},
        description: 'onStopControls',
    });

    return true;
};

ocargo.Game.prototype.sendAttempt = function(score) {
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
};

ocargo.Game.prototype.registerFailure = function() {
    if (!this.hasFailedThisTry) {
        this.failures += 1;
        this.hasFailedThisTry = true;
    }
    return (this.failures >= 3);
};

// function to enable or disable pointerEvents on running python or blockly code
ocargo.Game.prototype.allowCodeChanges = function(changesAllowed) {
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
};

ocargo.Game.prototype.setupFuelGauge = function(nodes, blocks) {
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
};

ocargo.Game.prototype.setupDirectDriveListeners = function() {
    $('#moveForward').click(function() {
        ocargo.game.onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
        ocargo.drawing.moveForward(0, ANIMATION_LENGTH, function() {ocargo.game.onStopControls();});
    });
    $('#turnLeft').click(function() {
        ocargo.game.onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
        ocargo.drawing.moveLeft(0, ANIMATION_LENGTH, function() {ocargo.game.onStopControls();});
    });
    $('#turnRight').click(function() {
        ocargo.game.onPlayControls();
        ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
        ocargo.drawing.moveRight(0, ANIMATION_LENGTH, function() {ocargo.game.onStopControls();});
    });
    $('#go').click(function() {
        $('#play_radio').trigger('click');
    });
};


ocargo.Game.prototype.setupSliderListeners = function() {
    var getSliderRightLimit = function(pageWidth) {return pageWidth/2;};
    var getSliderLeftLimit = function() {return 46;};
    var consoleSliderPosition = $(window).width()/2;
};

ocargo.Game.prototype.setupTabs = function() {
    setupTabListeners();
    setupBlocklyPane();
    setupPythonPane();
    setupLoadPane();
    setupSavePane();
    setupHelpPane();

    function setupTabListeners() {
        function onBlockly() {
            var tab = ocargo.game.tabs['blockly'];
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            ocargo.blocklyControl.redrawBlockly();
            Blockly.mainWorkspace.render();
            // reset blockly to python converter
            Blockly.Python.init();
            ocargo.controller = ocargo.blocklyControl;
            ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
        }

        function onPython() {
            var tab = ocargo.game.tabs['python'];
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            ocargo.editor.setValue(ocargo.blocklyCompiler.workspaceToPython());
            ocargo.controller = ocargo.editor;
        }

        function onPlay() {
            var existingHtml = ocargo.game.tabs['play'].getText();

            if(existingHtml == "Play") {
                if(ocargo.game.runProgramAndPrepareAnimation()) {
                    ocargo.game.onPlayControls();
                    ocargo.animation.playAnimation();
                }
                
            }
            else if(existingHtml == 'Pause') {
                ocargo.game.onPauseControls();
                ocargo.animation.pauseAnimation();
            }
            else if(existingHtml == 'Resume') {
                // Important ordering
                ocargo.game.onResumeControls();
                ocargo.animation.playAnimation();
            }

            ocargo.game.currentTabSelected.select();
        }

        function onStop() {
            ocargo.animation.resetAnimation();
            ocargo.game.onStopControls();

            ocargo.game.currentTabSelected.select();
        }

        function onStep() {
            if (ocargo.animation.isFinished()) {
                var successfullyCompiled = ocargo.game.runProgramAndPrepareAnimation();
                if(!successfullyCompiled) {
                    return;
                }
            }

            ocargo.animation.stepAnimation(function() {
                if (ocargo.animation.isFinished()) {
                    ocargo.game.onStopControls();
                }
                else {
                    ocargo.game.onPauseControls();
                }
            });
            ocargo.game.onStepControls();

            ocargo.game.currentTabSelected.select();
        }

        
        function onLoad() {
            var tab = ocargo.game.tabs['load'];
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            onLoadTrigger();
        }

        function onSave() {
            var tab = ocargo.game.tabs['save'];
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            onSaveTrigger();
        }

        function onClearProgram() {
            ocargo.blocklyControl.reset();
            ocargo.editor.reset();

            ocargo.game.currentTabSelected.select();
        }

        function onBigCodeMode() {
            ocargo.game.tabs['blockly'].select();

            if(ocargo.blocklyControl.bigCodeMode){
                ocargo.game.tabs['big_code_mode'].setContents('/static/game/image/icons/big_code_mode.svg', "Enlarge");
                ocargo.blocklyControl.decreaseBlockSize();
            } else {
                ocargo.game.tabs['big_code_mode'].setContents('/static/game/image/icons/big_code_mode.svg', "Shrink");
                ocargo.blocklyControl.increaseBlockSize();
            }
            ocargo.blocklyControl.showFlyout();
            ocargo.blocklyControl.showFlyout();

            ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
        }

        function onPrint() {
            ocargo.game.currentTabSelected.select();
        }

        function onMute() {
            if (ocargo.game.tabs['mute'].getContents() === 'Unmute') {
                ocargo.sound.unmute();
                ocargo.game.tabs['mute'].setContents('/static/game/image/icons/muted.svg', 'Mute');
            } else {
                ocargo.sound.mute();
                ocargo.game.tabs['mute'].setContents('/static/game/image/icons/unmuted.svg', 'Unmute');
            }
            ocargo.game.currentTabSelected.select();
        }

        function onHelp() {
            var tab = ocargo.game.tabs['help'];
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;
        }

        function onQuit() {
            window.location.href = "/game/";
        }

        ocargo.game.tabs['blockly'] = new ocargo.Tab($('#blockly_radio'), $('#blockly_radio + label'), onBlockly, $('#blockly_pane'));
        ocargo.game.tabs['python'] = new ocargo.Tab($('#python_radio'), $('#python_radio + label'), onPython, $('#python_pane'));

        ocargo.game.tabs['play'] = new ocargo.Tab($('#play_radio'), $('#play_radio + label'), onPlay);
        ocargo.game.tabs['stop'] = new ocargo.Tab($('#stop_radio'), $('#stop_radio + label'), onStop);
        ocargo.game.tabs['step'] = new ocargo.Tab($('#step_radio'), $('#step_radio + label'), onStep);

        ocargo.game.tabs['load'] = new ocargo.Tab($('#load_radio'), $('#load_radio + label'), onLoad, $('#load_pane'));
        ocargo.game.tabs['save'] = new ocargo.Tab($('#save_radio'), $('#save_radio + label'), onSave, $('#save_pane'));
        ocargo.game.tabs['clear_program'] = new ocargo.Tab($('#clear_program_radio'), $('#clear_program_radio + label'), onClearProgram);

        ocargo.game.tabs['big_code_mode'] = new ocargo.Tab($('#big_code_mode_radio'), $('#big_code_mode_radio + label'), onBigCodeMode);
        ocargo.game.tabs['print'] = new ocargo.Tab($('#print_radio'), $('#print_radio + label'), onPrint);
        ocargo.game.tabs['help'] = new ocargo.Tab($('#help_radio'), $('#help_radio + label'), onHelp, $('#help_pane'));
        ocargo.game.tabs['quit'] = new ocargo.Tab($('#quit_radio'), $('#quit_radio + label'), onQuit);

        ocargo.game.tabs['mute'] = new ocargo.Tab($('#mute_radio'), $('#mute_radio + label'), onMute);

        if ($.cookie("muted") === "true") {
            ocargo.sound.mute();
            ocargo.game.tabs['mute'].setContents('/static/game/image/icons/unmuted.svg', 'Unmute');
        }


        //  Trigger the initial tabs
        ocargo.game.tabs['blockly'].select();
        ocargo.game.currentTabSelected = ocargo.game.tabs['blockly'];
  
        // Enable all the permanently enabled tabs
        ocargo.game.tabs['blockly'].setEnabled(true);
        ocargo.game.tabs['python'].setEnabled(true);
        ocargo.game.tabs['play'].setEnabled(true);
        ocargo.game.tabs['mute'].setEnabled(true);
        ocargo.game.tabs['quit'].setEnabled(true);

        // Remove the panes of all the initially disabled tabs
        ocargo.game.tabs['python'].setPaneEnabled(false);
        ocargo.game.tabs['load'].setPaneEnabled(false);
        ocargo.game.tabs['save'].setPaneEnabled(false);
        ocargo.game.tabs['help'].setPaneEnabled(false);
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

            ocargo.game.tabs['blockly'].select();
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

            ocargo.game.tabs['blockly'].select();
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
    }
};

ocargo.Game.prototype.onPlayControls = function() {
    this.allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';
    
    ocargo.game.tabs['play'].setContents('/static/game/image/icons/pause.svg', 'Pause');
    ocargo.game.tabs['stop'].setEnabled(true);
    ocargo.game.tabs['step'].setEnabled(false);

    ocargo.game.tabs['load'].setEnabled(false);
    ocargo.game.tabs['save'].setEnabled(false);
    ocargo.game.tabs['clear_program'].setEnabled(false);
    ocargo.game.tabs['big_code_mode'].setEnabled(false);
    ocargo.game.tabs['print'].setEnabled(false);
    ocargo.game.tabs['help'].setEnabled(false);
};

ocargo.Game.prototype.onStepControls = function() {
    this.allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';

    ocargo.game.tabs['play'].setContents('/static/game/image/icons/play.svg', 'Resume');
    ocargo.game.tabs['stop'].setEnabled(true);
    ocargo.game.tabs['step'].setEnabled(false);

    ocargo.game.tabs['load'].setEnabled(false);
    ocargo.game.tabs['save'].setEnabled(false);
    ocargo.game.tabs['clear_program'].setEnabled(false);
    ocargo.game.tabs['big_code_mode'].setEnabled(false);
    ocargo.game.tabs['print'].setEnabled(false);
    ocargo.game.tabs['help'].setEnabled(false);
};

ocargo.Game.prototype.onStopControls = function() {
    this.allowCodeChanges(true);

    // TODO make this hidden unless blocks are clear or something... 
    document.getElementById('direct_drive').style.visibility='visible';
    
    ocargo.game.tabs['play'].setContents('/static/game/image/icons/play.svg', 'Play');
    ocargo.game.tabs['stop'].setEnabled(false);
    ocargo.game.tabs['step'].setEnabled(true);

    ocargo.game.tabs['load'].setEnabled(true);
    ocargo.game.tabs['save'].setEnabled(true);
    ocargo.game.tabs['clear_program'].setEnabled(true);
    ocargo.game.tabs['big_code_mode'].setEnabled(true);
    ocargo.game.tabs['print'].setEnabled(true);
    ocargo.game.tabs['help'].setEnabled(true);
};

ocargo.Game.prototype.onPauseControls = function() {
    ocargo.game.tabs['play'].setContents('/static/game/image/icons/play.svg', 'Resume');
    ocargo.game.tabs['stop'].setEnabled(true);
    ocargo.game.tabs['step'].setEnabled(true);
};

ocargo.Game.prototype.onResumeControls = function() {
    ocargo.game.tabs['play'].setContents('/static/game/image/icons/pause.svg', 'Pause');
    ocargo.game.tabs['stop'].setEnabled(true);
    ocargo.game.tabs['step'].setEnabled(false);
};

$(document).ready(function() {
    ocargo.game = new ocargo.Game();
    ocargo.game.setup();
});

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

