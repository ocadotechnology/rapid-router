'use strict';

var ocargo = ocargo || {};

ocargo.Game = function() {
    this.tabs = [];
    this.failures = 0;
    this.hasFailedThisTry = false;
};

ocargo.Game.prototype.setup = function() {
    initCustomBlocks();
    ocargo.blocklyControl = new ocargo.BlocklyControl();
    ocargo.blocklyCompiler = new ocargo.BlocklyCompiler();
    ocargo.drawing = new ocargo.Drawing();
    ocargo.drawing.preloadRoadTiles();
    ocargo.model = new ocargo.Model(PATH, ORIGIN, DESTINATIONS, TRAFFIC_LIGHTS, MAX_FUEL);
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
    if (BLOCKLY_ENABLED) {
        ocargo.controller = ocargo.blocklyControl;
    }
    else {
        ocargo.controller = ocargo.editor;
    }

    // Setup blockly to python
    Blockly.Python.init();
    window.addEventListener('unload', ocargo.blocklyControl.teardown);

    var loggedOutWarning = '';
    // Check if logged on
    if (USER_STATUS == 'UNTRACKED') {
        loggedOutWarning = '<br>' + ocargo.messages.loggedOutWarning;
    }
    // Start the popup
    var title = "Custom Level";
    if (LEVEL_ID) {
        title = "Level " + LEVEL_ID; 
    }
    ocargo.Drawing.startPopup(title, "",
        LESSON + ocargo.jsElements.closebutton("Play") + loggedOutWarning, true);
};

ocargo.Game.prototype.reset = function() {
    ocargo.blocklyControl.clearAllSelections();

    // Needed so animation can reset with the right information
    ocargo.model.reset(0);

    // clear animations and sound
    ocargo.sound.stop_engine();
    ocargo.animation.resetAnimation();
}

ocargo.Game.prototype.runProgramAndPrepareAnimation = function() {
    this.reset();

    var result = ocargo.controller.prepare();
    if (!result.success) {
        ocargo.sound.tension();
        ocargo.Drawing.startPopup(ocargo.messages.failTitle, "", result.error, false);
        return false;
    }
    var program = result.program;

    ocargo.blocklyControl.resetIncorrectBlock();

    // Starting sound
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: ocargo.sound.starting,
        description: 'starting sound',
        animationLength: 820
    });
    ocargo.animation.startNewTimestamp();

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: ocargo.sound.start_engine,
        description: 'starting engine',
    });

    program.run(ocargo.model);
    // Set controls ready for user to reset
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: function() {ocargo.game.onStopControls();},
        description: 'onStopControls'
    });

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: ocargo.sound.stop_engine,
        description: 'stopping engine'
    });

    return true;
};

ocargo.Game.prototype.sendAttempt = function(score) {

    function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    // Send out the submitted data.
    if (LEVEL_ID) {
        var csrftoken = $.cookie('csrftoken');
        $.ajax({
            url : '/rapidrouter/submit',
            type : 'POST',
            dataType: 'json',
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            data : {
                level : parseInt(LEVEL_ID),
                score : score,
                workspace : ocargo.blocklyControl.serialize()
            },
            error : function(xhr, errmsg, err) {
                console.error(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
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

        for (var i = 0; i < nodes.length; i++) {
            if (nodes[i].connectedNodes.length > 2) {
                return;
            }
        }
    }
};

ocargo.Game.prototype.setupDirectDriveListeners = function() {
    $('#moveForward').click(function() {
        if(ocargo.model.reasonForTermination != 'CRASH') {
            ocargo.game.onPlayControls();
            ocargo.blocklyControl.addBlockToEndOfProgram('move_forwards');
            ocargo.drawing.moveForward(0, ANIMATION_LENGTH, function() {ocargo.game.onStopControls();});
        }
    });
    $('#turnLeft').click(function() {
        if(ocargo.model.reasonForTermination != 'CRASH') {
            ocargo.game.onPlayControls();
            ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
            ocargo.drawing.moveLeft(0, ANIMATION_LENGTH, function() {ocargo.game.onStopControls();});
        }
    });
    $('#turnRight').click(function() {
        if(ocargo.model.reasonForTermination != 'CRASH') {
            ocargo.game.onPlayControls();
            ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
            ocargo.drawing.moveRight(0, ANIMATION_LENGTH, function() {ocargo.game.onStopControls();});
        }
    });
    $('#go').click(function() {
        $('#play_radio').trigger('click');
    });
};

ocargo.Game.prototype.setupSliderListeners = function() {
    var tabsWidth = $('#tabs').width();

    var startEvents = ['mousedown', 'touchstart'];
    var moveEvents = ['mousemove', 'touchmove'];
    var endEvents = ['mouseup', 'touchend', 'touchcancel'];

    var slider = $('#consoleSlider');
    var tabs =  $('#tabs');
    var halfSliderWidth;

    var endFunc = function(e) {
        for (var i = 0; i < moveEvents.length; i++) {
            slider.parent().off(moveEvents[i]);
            tabs.off(moveEvents[i]);
        }

        for (var i = 0; i < endEvents.length; i++) {
            // disable drag when mouse leaves this or the parent
            slider.parent().off(endEvents[i], endFunc);
            tabs.off(endEvents[i], endFunc);
        }

        ocargo.blocklyControl.redrawBlockly();
    };

    var moveFunc = function(e) {
        if (e.type == 'touchmove') {
            e = e.originalEvent.touches[0];
        }

        var consoleSliderPosition = e.pageX - tabsWidth - halfSliderWidth;
        var containerWidth = slider.parent().width();

        consoleSliderPosition *= 100.0 / containerWidth;

        if (consoleSliderPosition > 100) {
            consoleSliderPosition = 100;
        }
        if (consoleSliderPosition < 0) {
            consoleSliderPosition = 0;
        }

        $('#consoleSlider').css('left', consoleSliderPosition + '%');
        $('#paper').css('width', (100 - consoleSliderPosition) + '%');
        $('#tab_panes').css('width', consoleSliderPosition + '%');
        $('#direct_drive').css('left', consoleSliderPosition + '%');
        
        ocargo.blocklyControl.redrawBlockly();
    };

    var startFunc = function(e) {
        halfSliderWidth = slider.width()/2;

        for (var i = 0; i < moveEvents.length; i++) {
            slider.parent().on(moveEvents[i], moveFunc);
            tabs.on(moveEvents[i], moveFunc);
        }

        for (var i = 0; i < endEvents.length; i++) {
            // disable drag when mouse leaves this or the parent
            slider.parent().on(endEvents[i], endFunc);
            tabs.on(endEvents[i], endFunc);
        }
    };

    for (var i = 0; i < startEvents.length; i++) {
        slider.on(startEvents[i], startFunc);
    }
};

ocargo.Game.prototype.setupTabs = function() {
    var currentTabSelected;

    var tabs = [];

    tabs.blockly = new ocargo.Tab($('#blockly_radio'), $('#blockly_radio + label'), $('#blockly_pane'));
    tabs.python = new ocargo.Tab($('#python_radio'), $('#python_radio + label'), $('#python_pane'));

    tabs.play = new ocargo.Tab($('#play_radio'), $('#play_radio + label'));
    tabs.stop = new ocargo.Tab($('#stop_radio'), $('#stop_radio + label'));
    tabs.step = new ocargo.Tab($('#step_radio'), $('#step_radio + label'));

    tabs.load = new ocargo.Tab($('#load_radio'), $('#load_radio + label'), $('#load_pane'));
    tabs.save = new ocargo.Tab($('#save_radio'), $('#save_radio + label'), $('#save_pane'));
    tabs.clear_program = new ocargo.Tab($('#clear_program_radio'), $('#clear_program_radio + label'));

    // tabs.big_code_mode = new ocargo.Tab($('#big_code_mode_radio'), $('#big_code_mode_radio + label'));
    // tabs.print = new ocargo.Tab($('#print_radio'), $('#print_radio + label'));
    tabs.mute = new ocargo.Tab($('#mute_radio'), $('#mute_radio + label'));
    tabs.help = new ocargo.Tab($('#help_radio'), $('#help_radio + label'));
    tabs.quit = new ocargo.Tab($('#quit_radio'), $('#quit_radio + label'));

    setupBlocklyTab();
    setupPythonTab();
    setupClearTab();
    setupPlayTab();
    setupStopTab();
    setupStepTab();
    setupLoadTab();
    setupSaveTab();
    // setupPrintTab();
    setupHelpTab();
    // setupBigCodeModeTab();
    setupMuteTab();
    setupQuitTab();

    ocargo.game.tabs = tabs;

    if (!BLOCKLY_ENABLED) {
        $('#python_radio').click();
    }

    function setupBlocklyTab() {
        tabs.blockly.setOnChange(function () {
            var tab = tabs.blockly;
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            ocargo.blocklyControl.redrawBlockly();
            Blockly.mainWorkspace.render();
            // reset blockly to python converter
            Blockly.Python.init();
            ocargo.controller = ocargo.blocklyControl;
        });

        currentTabSelected = tabs.blockly;
        tabs.blockly.select();

        var flyoutOut = false;
        $('#flyoutButton').click(ocargo.blocklyControl.toggleFlyout);

        // TODO solve why we need to do this to prevent Firefox from not having the Toolbox fully initialised...
        setTimeout(function() {
            $('#flyoutButton').click();
            ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
        }, 100);
    }

    function setupPythonTab() {
        $('#clear_console').click(function (e) {
                $('#consoleOutput').text('');
        });

        tabs.python.setOnChange(function() {
            var tab = tabs.python;
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            ocargo.editor.setValue(ocargo.blocklyCompiler.workspaceToPython());
            ocargo.controller = ocargo.editor;
        });
    }

    function setupClearTab() {
        tabs.clear_program.setOnChange(function() {
            ocargo.blocklyControl.reset();
            ocargo.editor.reset();

            currentTabSelected.select();
        });
    }

    function setupPlayTab() {
        tabs.play.setOnChange(function() {
            var existingHtml = tabs.play.getText();

            if (existingHtml == "Play") {
                if (ocargo.game.runProgramAndPrepareAnimation()) {
                    ocargo.game.onPlayControls();
                    ocargo.animation.playAnimation();
                }
                
            }
            else if (existingHtml == 'Pause') {
                ocargo.game.onPauseControls();
                ocargo.animation.pauseAnimation();
            }
            else if (existingHtml == 'Resume') {
                // Important ordering
                ocargo.game.onResumeControls();
                ocargo.animation.playAnimation();
            }

            currentTabSelected.select();
        });
    }

    function setupStopTab() {
        tabs.stop.setOnChange(function() {
            ocargo.game.reset();
            ocargo.game.onStopControls();

            currentTabSelected.select();
        });
    }

    function setupStepTab() {
        tabs.step.setOnChange(function() {
            if (tabs.play.getText() == "Play") {
                ocargo.game.runProgramAndPrepareAnimation();
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
            currentTabSelected.select();
        });
    }

    
    function setupLoadTab() {
        var selectedWorkspace = null;
        tabs.load.setOnChange(function() {
            var tab = tabs.load;
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            selectedWorkspace = null;
            // TODO Disable the tab to stop users clicking it multiple times
            // whilst waiting for the table data to load
            // JQuery currently throwing errors :(

            ocargo.saving.retrieveListOfWorkspaces(function(err, workspaces) {
                if (err !== null) {
                    ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                    console.error(err);
                    return;
                }

                loadInWorkspaces(workspaces);
            });
        });

        $('#loadWorkspace').click(function() {
            if (selectedWorkspace) {
                ocargo.saving.retrieveWorkspace(selectedWorkspace, function(err, workspace) {
                    if (err !== null) {
                        ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                        console.error(err);
                        return;
                    }

                    ocargo.blocklyControl.deserialize(workspace);
                    ocargo.blocklyControl.redrawBlockly();

                    $('#loadModal').foundation('reveal', 'close');
                });

                tabs.blockly.select();
            }
        });

        $('#deleteWorkspace').click(function() {
            if (selectedWorkspace) {
                ocargo.saving.deleteWorkspace(selectedWorkspace, function(err, workspaces) {
                    if (err !== null) {
                        ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                        console.error(err);
                        return;
                    }

                    loadInWorkspaces(workspaces);
                });
            }
        });

        function loadInWorkspaces(workspaces) {
            populateTable("loadWorkspaceTable", workspaces);

            // Add click listeners to all rows
            $('#loadWorkspaceTable tr').on('click', function(event) {
                $('#loadWorkspaceTable tr').attr('selected', false);
                $(this).attr('selected', true);
                selectedWorkspace = $(event.target).attr('value');
                $('#loadWorkspace').removeAttr('disabled');
                $('#deleteWorkspace').removeAttr('disabled');
            });

            var empty = workspaces.length == 0;
            $('#load_pane .scrolling-table-wrapper').css('display',  empty ? 'none' : 'block');
            $('#load_pane #does_not_exist').css('display',  empty ? 'block' : 'none');
            
            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
            $('#loadWorkspace').attr('disabled', 'disabled');
            $('#deleteWorkspace').attr('disabled', 'disabled');
        }
    }

    function setupSaveTab() {
        var selectedWorkspace = null;

        tabs.save.setOnChange(function() {
            var tab = tabs.save;
            currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            currentTabSelected = tab;

            selectedWorkspace = null;

            // TODO Disable the tab to stop users clicking it multiple times
            // whilst waiting for the table data to load
            // JQuery currently throwing errors :()
            
            ocargo.saving.retrieveListOfWorkspaces(function(err, workspaces) {
                if (err !== null) {
                    ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                    console.error(err);
                    return;
                }
                
                loadInWorkspaces(workspaces);
            });
        });

        $('#saveWorkspace').click(function() {
            var newName = $('#workspaceNameInput').val();
            if (newName && newName !== "") {
                var table = $("#saveWorkspaceTable");
                for (var i = 0; i < table[0].rows.length; i++) {
                     var cell = table[0].rows[i].cells[0];
                     var wName = cell.innerHTML;
                     if (wName == newName) {
                        ocargo.saving.deleteWorkspace(cell.attributes[0].value, 
                                                        function(err, workspace) {
                                                            if (err !== null) {
                                                                ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                                                                console.error(err);
                                                                return;
                                                            }
                                                        });
                     }
                }

                ocargo.saving.createNewWorkspace(newName, ocargo.blocklyControl.serialize(), function(err, workspaces) {
                    if (err !== null) {
                        ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                        console.error(err);
                        return;
                    }
                    loadInWorkspaces(workspaces);
                });
            }
        });

        // If the user pressed the enter key in the textbox, should be the same as clicking the button
        $('#newWorkspaceName').on('keypress', function(e) {
            if (e.which == 13) {
                $('#saveWorkspace').trigger('click');
            }
        });

        function loadInWorkspaces(workspaces) {
            populateTable("saveWorkspaceTable", workspaces);

            // Add click listeners to all rows
            $('#saveWorkspaceTable tr').on('click', function(event) {
                $('#saveWorkspaceTable tr').attr('selected', false);
                $(this).attr('selected', true);
                selectedWorkspace = $(event.target).attr('value');
                var workspaceName = $(event.target)[0].innerHTML;
                document.getElementById("workspaceNameInput").value = workspaceName;
            });

            $('#save_pane .scrolling-table-wrapper').css('display',  workspaces.length == 0 ? 'none' : 'block');
            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
        }
    }

    function setupPrintTab() {
        tabs.print.setOnChange(function() {
            currentTabSelected.select();
            window.print();
        });
    }

    function setupHelpTab() {
        tabs.help.setOnChange(function() {
            currentTabSelected.select();
            ocargo.Drawing.startPopup('', '', HINT + ocargo.jsElements.closebutton("Close!"));
        });

    }

    function setupBigCodeModeTab() {
        tabs.big_code_mode.setOnChange(function() {
            tabs.blockly.select();

            if (ocargo.blocklyControl.bigCodeMode){
                tabs.big_code_mode.setContents(ocargo.Drawing.imageDir + 'icons/big_code_mode.svg', "Enlarge");
                ocargo.blocklyControl.decreaseBlockSize();
            } else {
                tabs.big_code_mode.setContents(ocargo.Drawing.imageDir + 'icons/big_code_mode.svg', "Shrink");
                ocargo.blocklyControl.increaseBlockSize();
            }

            // Note that toggleFlyout is misnamed and actually toggles the flyout.
            // So these two lines force the flyout to refresh and be the correct size.
            ocargo.blocklyControl.toggleFlyout();
            ocargo.blocklyControl.toggleFlyout();

            ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
        });
    }

    function setupMuteTab() {
        tabs.mute.setOnChange(function() {
            ocargo.game.mute($.cookie('muted') !== 'true');
            currentTabSelected.select();
        });
    }

    function setupQuitTab() {
        tabs.quit.setOnChange(function() {
            window.location.href = RETURN_URL;
        });
    }


    // Helper method for load and save tabs
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
            var tableRow = $('<tr>');
            var workspaceEntry = $('<td>');
            workspaceEntry.attr({
                'value':workspace.id
            });
            workspaceEntry.text(workspace.name);
            tableRow.append(workspaceEntry);
            table.append(tableRow);
        }
    }
};

ocargo.Game.prototype.onPlayControls = function() {
    this.allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';
    
    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/pause.svg', 'Pause');
    ocargo.game.tabs.step.setEnabled(false);

    ocargo.game.tabs.load.setEnabled(false);
    ocargo.game.tabs.save.setEnabled(false);
    ocargo.game.tabs.clear_program.setEnabled(false);
    // ocargo.game.tabs.big_code_mode.setEnabled(false);
    // ocargo.game.tabs.print.setEnabled(false);
    ocargo.game.tabs.help.setEnabled(false);
};

ocargo.Game.prototype.onStepControls = function() {
    this.allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';

    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/play.svg', 'Resume');
    ocargo.game.tabs.step.setEnabled(false);

    ocargo.game.tabs.load.setEnabled(false);
    ocargo.game.tabs.save.setEnabled(false);
    ocargo.game.tabs.clear_program.setEnabled(false);
    // ocargo.game.tabs.big_code_mode.setEnabled(false);
    // ocargo.game.tabs.print.setEnabled(false);
    ocargo.game.tabs.help.setEnabled(false);
};

ocargo.Game.prototype.onStopControls = function() {
    this.allowCodeChanges(true);

    // TODO make this hidden unless blocks are clear or something... 
    document.getElementById('direct_drive').style.visibility='visible';
    
    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/play.svg', 'Play');
    ocargo.game.tabs.step.setEnabled(true);

    ocargo.game.tabs.load.setEnabled(true);
    ocargo.game.tabs.save.setEnabled(true);
    ocargo.game.tabs.clear_program.setEnabled(true);
    // ocargo.game.tabs.big_code_mode.setEnabled(true);
    // ocargo.game.tabs.print.setEnabled(true);
    ocargo.game.tabs.help.setEnabled(true);
};

ocargo.Game.prototype.onPauseControls = function() {
    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/play.svg', 'Resume');
    ocargo.game.tabs.step.setEnabled(true);
};

ocargo.Game.prototype.onResumeControls = function() {
    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/pause.svg', 'Pause');
    ocargo.game.tabs.step.setEnabled(false);
};

ocargo.Game.prototype.mute = function(mute) {
    if (mute) {
        ocargo.sound.mute();
        $.cookie("muted", 'true');
        $('#mute_text').text('Unmute');
        $('#mute_img').attr('src', ocargo.Drawing.imageDir + 'icons/muted.svg');
    } else {
        ocargo.sound.unmute();
        $.cookie("muted", 'false');
        $('#mute_text').text('Mute');
        $('#mute_img').attr('src', ocargo.Drawing.imageDir + 'icons/unmuted.svg');
    }
};

$(document).ready(function() {
    ocargo.game = new ocargo.Game();
    ocargo.game.setup();
    ocargo.game.mute($.cookie('muted') === 'true');
});
