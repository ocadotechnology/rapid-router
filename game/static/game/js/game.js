/*
Code for Life

Copyright (C) 2015, Ocado Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
'use strict';

var ocargo = ocargo || {};

ocargo.Game = function() {
    this.tabs = [];
    this.failures = 0;
    this.currentTabSelected;
};

ocargo.Game.prototype.setup = function() {
    if (NIGHT_MODE_FEATURE_ENABLED) {
        $('#nightmode_tab').show()
    }
    restoreCmsLogin();
    initCustomBlocks();
    ocargo.blocklyControl = new ocargo.BlocklyControl();
    ocargo.blocklyControl.blocklyCustomisations.setupDoubleclick();
    ocargo.blocklyControl.blocklyCustomisations.setupLimitedBlocks();
    ocargo.pythonControl = new ocargo.PythonControl();
    ocargo.blocklyCompiler = new ocargo.BlocklyCompiler();
    ocargo.model = new ocargo.Model(PATH, ORIGIN, DESTINATIONS, TRAFFIC_LIGHTS, COWS, MAX_FUEL);
    ocargo.drawing = new ocargo.Drawing(ocargo.model.startingPosition());
    ocargo.drawing.preloadRoadTiles();
    ocargo.animation = new ocargo.Animation(ocargo.model, DECOR);
    ocargo.saving = new ocargo.Saving();

    // Setup the blockly workspace
    //ocargo.blocklyControl.reset();
    ocargo.blocklyControl.loadPreviousAttempt();
    ocargo.pythonControl.loadPreviousAttempt();

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
        ocargo.controller = ocargo.pythonControl;
    }

    // Setup blockly to python
    Blockly.Python.init(Blockly.getMainWorkspace());
    window.addEventListener('unload', function(event) {
        ocargo.pythonControl.teardown();
        ocargo.blocklyControl.teardown();
    });

    var loggedOutWarning = '';
    // Check if logged on
    if (USER_STATUS == 'UNTRACKED') {
        loggedOutWarning = '<br>' + ocargo.messages.loggedOutWarning;
    }
    // Start the popup
    var title = "Try solving this one...";
    if (LEVEL_ID) {
        if (NIGHT_MODE) {
            title = "Night Level " + LEVEL_NAME;
        } else if (DEFAULT_LEVEL) {
            title = "Level " + LEVEL_NAME;
        }
        else {
            title = LEVEL_NAME;
        }
    }

    var message;
    if (NIGHT_MODE) {
        message = '<br>' + ocargo.messages.nightMode;
    } else {
        message = loggedOutWarning;
    }
    ocargo.Drawing.startPopup(title, LESSON, message, true, ocargo.button.dismissButtonHtml('play_button', 'Play'));
};

ocargo.Game.prototype.reset = function() {
    ocargo.blocklyControl.clearAllSelections();

    // Needed so animation can reset with the right information
    ocargo.model.reset(0);

    // clear animations and sound
    ocargo.sound.stop_engine();
    ocargo.animation.resetAnimation();
};

ocargo.Game.prototype.runProgramAndPrepareAnimation = function(blocks) {
    this.reset();

    ocargo.event.sendEvent("PlayButtonPressed", { levelName: LEVEL_NAME,
                                                  defaultLevel: DEFAULT_LEVEL,
                                                  workspace: ocargo.blocklyControl.serialize(),
                                                  failures: this.failures,
                                                  pythonWorkspace: ocargo.pythonControl.getCode() });

    var result = ocargo.controller.prepare(blocks);
    if (!result.success) {
        ocargo.sound.tension();
        ocargo.Drawing.startPopup(ocargo.messages.failTitle, "",
                                    result.error);
        return false;
    }
    var program = result.program;

    ocargo.blocklyControl.resetIncorrectBlock();

    // Starting sound
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'playSound',
        functionCall: ocargo.sound.starting,
        description: 'starting sound',
        animationLength: 820
    });
    ocargo.animation.startNewTimestamp();

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'playSound',
        functionCall: ocargo.sound.start_engine,
        description: 'starting engine'
    });

    program.run(ocargo.model);
    // Set controls ready for user to reset
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'onStopControls',
        functionCall: function() {ocargo.game.onStopControls();},
        description: 'onStopControls'
    });

    ocargo.animation.appendAnimation({
        type: 'callable',
        functionType: 'playSound',
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

    // hack scores so that it works for demo and python TODO implement max scores and remove this!!
    if (PYTHON_ENABLED) {
        score *= 2;
    }

    // Check that we should actually be sending an attempt - either if only blockly's enabled
    // or if python's enabled and we're on the python tab (assumes they don't change tab quickly...)
    if ((BLOCKLY_ENABLED && !PYTHON_ENABLED) ||
        (PYTHON_ENABLED && ocargo.game.currentTabSelected == ocargo.game.tabs.python)) {
        // Send out the submitted data.
        if (LEVEL_ID) {
            var csrftoken = $.cookie('csrftoken');
            $.ajax({
                url : '/rapidrouter/submit/',
                type : 'POST',
                dataType: 'json',
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },
                data : {
                    nightmode: (NIGHT_MODE) ? "True" : "False",
                    level: parseInt(LEVEL_ID),
                    score: score,
                    workspace: ocargo.blocklyControl.serialize(),
                    python_workspace: ocargo.pythonControl.getCode()
                },
                error : function(xhr, errmsg, err) {
                    console.error(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
                }
            });
        }
    }
};

ocargo.Game.prototype.registerFailure = function() {
    this.failures += 1;
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

        for(var i = 0; i < blocks.length; i++) {
            if(blocks[i].type === "turn_around" || blocks[i].type === "wait") {
                return;
            }
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
            ocargo.drawing.moveForward(ocargo.animation.genericAnimationLength, function () {
                ocargo.game.onStopControls();
            });
        }
    });
    $('#turnLeft').click(function() {
        if(ocargo.model.reasonForTermination != 'CRASH') {
            ocargo.game.onPlayControls();
            ocargo.blocklyControl.addBlockToEndOfProgram('turn_left');
            ocargo.drawing.moveLeft(ocargo.animation.genericAnimationLength, function () {
                ocargo.game.onStopControls();
            });
        }
    });
    $('#turnRight').click(function() {
        if(ocargo.model.reasonForTermination != 'CRASH') {
            ocargo.game.onPlayControls();
            ocargo.blocklyControl.addBlockToEndOfProgram('turn_right');
            ocargo.drawing.moveRight(ocargo.animation.genericAnimationLength, function () {
                ocargo.game.onStopControls();
            });
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
    var tabs = [];

    tabs.blockly = new ocargo.Tab($('#blockly_radio'), $('#blockly_radio + label'), $('#blockly_pane'));
    tabs.python = new ocargo.Tab($('#python_radio'), $('#python_radio + label'), $('#python_pane'));

    tabs.play = new ocargo.Tab($('#play_radio'), $('#play_radio + label'));
    tabs.stop = new ocargo.Tab($('#stop_radio'), $('#stop_radio + label'));
    tabs.fast = new ocargo.Tab($('#fast_radio'), $('#fast_radio + label'));
    tabs.step = new ocargo.Tab($('#step_radio'), $('#step_radio + label'));

    tabs.load = new ocargo.Tab($('#load_radio'), $('#load_radio + label'), $('#load_pane'));
    tabs.save = new ocargo.Tab($('#save_radio'), $('#save_radio + label'), $('#save_pane'));
    tabs.clear_program = new ocargo.Tab($('#clear_program_radio'), $('#clear_program_radio + label'));

    // tabs.big_code_mode = new ocargo.Tab($('#big_code_mode_radio'), $('#big_code_mode_radio + label'));
    // tabs.print = new ocargo.Tab($('#print_radio'), $('#print_radio + label'));
    tabs.mute = new ocargo.Tab($('#mute_radio'), $('#mute_radio + label'));
    tabs.help = new ocargo.Tab($('#help_radio'), $('#help_radio + label'));
    tabs.quit = new ocargo.Tab($('#quit_radio'), $('#quit_radio + label'));
    tabs.nightmode = new ocargo.Tab($('#nightmode_radio'), $('#nightmode_radio + label'));

    setupBlocklyTab();
    setupPythonTab();
    setupClearTab();
    setupPlayTab();
    setupStopTab();
    setupFastTab();
    setupStepTab();
    setupLoadTab();
    setupSaveTab();
    // setupPrintTab();
    setupHelpTab();
    // setupBigCodeModeTab();
    setupMuteTab();
    setupQuitTab();
    setupNightModeTab();

    ocargo.game.tabs = tabs;

    if (!BLOCKLY_ENABLED) {
        $('#python_radio').click();
    }

    function setupBlocklyTab() {
        tabs.blockly.setOnChange(function () {
            var tab = tabs.blockly;
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            ocargo.blocklyControl.redrawBlockly();
            // reset blockly to python converter
            Blockly.Python.init(Blockly.getMainWorkspace());
            ocargo.controller = ocargo.blocklyControl;
        });

        ocargo.game.currentTabSelected = tabs.blockly;
        tabs.blockly.select();

        // Function wrapper needed
        $('#flyoutButton').click(function(){ocargo.blocklyControl.toggleFlyout();});

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

        $('#van_commands_help').click(function (e) {
            var leadMsg = ocargo.messages.pythonCommands;
            ocargo.Drawing.startPopup("Python Commands", leadMsg, "", true);
        });

        $('#convert_from_blockly').click(function (e) {
            ocargo.pythonControl.appendCode(ocargo.blocklyCompiler.workspaceToPython());
        });

        tabs.python.setOnChange(function() {
            var tab = tabs.python;
            // Only clear console when changing *to* python?
            if (ocargo.game.currentTabSelected !== tab) {
                $('#clear_console').click();
            }
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            ocargo.controller = ocargo.pythonControl;
        });
    }

    function setupClearTab() {
        tabs.clear_program.setOnChange(function() {
            if (ocargo.game.currentTabSelected == tabs.blockly) {
                ocargo.blocklyControl.reset();
            }
            if (ocargo.game.currentTabSelected == tabs.python) {
                ocargo.pythonControl.reset();
            }
            ocargo.game.reset();

            ocargo.game.currentTabSelected.select();
        });
    }

    function setupPlayTab() {
        tabs.play.setOnChange(function() {
            var existingHtml = tabs.play.getText();

            if (existingHtml == "Play") {
                if (ocargo.game.runProgramAndPrepareAnimation()) {
                    ocargo.game.onPlayControls();
                    ocargo.animation.playAnimation();
                    $('#clear_console').click();
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

            ocargo.game.currentTabSelected.select();
        });
    }

    function setupStopTab() {
        tabs.stop.setOnChange(function() {
            ocargo.game.reset();
            ocargo.game.onStopControls();

            ocargo.game.currentTabSelected.select();
        });
    }

    function setupFastTab() {
        tabs.fast.setOnChange(function() {
            var playTextPreSpeedControl = tabs.play.getText();

            if (tabs.fast.getText() == "Fast") {
                ocargo.game.onFastControls();
                ocargo.animation.speedUpAnimation();
            } else {
                ocargo.game.onSlowControls();
                ocargo.animation.resetAnimationLength();
            }

            if (playTextPreSpeedControl == "Play") {
                if (ocargo.game.runProgramAndPrepareAnimation()) {
                    ocargo.animation.playAnimation();
                    $('#clear_console').click();
                }else{
                    // When error occurs during the compilation of the program
                    ocargo.game.onStopControls();
                }
            } else if (playTextPreSpeedControl == "Resume") {
                ocargo.animation.playAnimation();
            }

            ocargo.game.currentTabSelected.select();
        });
    }

    function setupStepTab() {
        tabs.step.setOnChange(function() {
            if (tabs.play.getText() == "Play") {
                ocargo.game.runProgramAndPrepareAnimation();
                $('#clear_console').click();
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
        });
    }

    function setupLoadTab() {
        var selectedWorkspace = null;
        tabs.load.setOnChange(function() {
            var tab = tabs.load;
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            selectedWorkspace = null;
            // TODO Disable the tab to stop users clicking it multiple times
            // whilst waiting for the table data to load
            // JQuery currently throwing errors :(

            ocargo.saving.retrieveListOfWorkspaces(function(err, workspaces) {
                if (err !== null) {
                    ocargo.Drawing.startInternetDownPopup();
                    console.error(err);
                    return;
                }

                loadInWorkspaces(workspaces);
            });
        });

        function loadSelectedWorkspace() {
            if (selectedWorkspace) {

                // Blockly or Python tab must be selected before domToWorkspace is called
                // Otherwise blocks will be chopped off or python editor will not be updated
                if (PYTHON_ENABLED) {
                    tabs.python.select();
                }
                if (BLOCKLY_ENABLED) {
                    tabs.blockly.select();
                }

                ocargo.saving.retrieveWorkspace(selectedWorkspace, function(err, workspace) {
                    if (err !== null) {
                        ocargo.Drawing.startInternetDownPopup();
                        console.error(err);
                        return;
                    }
                    if (BLOCKLY_ENABLED) {
                        ocargo.blocklyControl.deserialize(workspace.contents);
                        ocargo.blocklyControl.redrawBlockly();
                    }
                    if (PYTHON_ENABLED) {
                        ocargo.pythonControl.setCode(workspace.python_contents);
                    }

                    $('#loadModal').foundation('reveal', 'close');
                });

            }
        }

        $('#loadWorkspace').click(loadSelectedWorkspace);

        $('#deleteWorkspace').click(function() {
            if (selectedWorkspace) {
                ocargo.saving.deleteWorkspace(selectedWorkspace, function(err, workspaces) {
                    if (err !== null) {
                        ocargo.Drawing.startInternetDownPopup();
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
            var rows = $('#loadWorkspaceTable tr');
            rows.on('click', function() {
                rows.attr('selected', false);
                $(this).attr('selected', true);
                selectedWorkspace = $(this).attr('value');
                $('#loadWorkspace').removeAttr('disabled');
                $('#deleteWorkspace').removeAttr('disabled');
            });

            // Add double click listener to load the workspace selected by the first click
            rows.on('dblclick', loadSelectedWorkspace);

            var empty = workspaces.length === 0;
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
            ocargo.game.currentTabSelected.setPaneEnabled(false);
            tab.setPaneEnabled(true);
            ocargo.game.currentTabSelected = tab;

            selectedWorkspace = null;

            // TODO Disable the tab to stop users clicking it multiple times
            // whilst waiting for the table data to load
            // JQuery currently throwing errors :()

            ocargo.saving.retrieveListOfWorkspaces(function(err, workspaces) {
                if (err !== null) {
                    ocargo.Drawing.startInternetDownPopup();
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
                var existingID = null;

                for (var i = 0; i < table[0].rows.length; i++) {
                     var row = table[0].rows[i];
                     var existingName = row.cells[0].innerHTML;
                     if (existingName === newName) {
                        existingID = row.getAttribute('value');
                        break;
                     }
                }

                var workspace = {name: newName,
                                 contents: ocargo.blocklyControl.serialize(),
                                 python_contents: ocargo.pythonControl.getCode()};

                ocargo.saving.saveWorkspace(workspace, existingID, function(err, workspaces) {
                    if (err !== null) {
                        ocargo.Drawing.startInternetDownPopup();
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

            $('#save_pane .scrolling-table-wrapper').css(
                'display',  workspaces.length === 0 ? 'none' : 'block');
            // But disable all the modal buttons as nothing is selected yet
            selectedWorkspace = null;
        }
    }

    function setupPrintTab() {
        tabs.print.setOnChange(function() {
            ocargo.game.currentTabSelected.select();
            window.print();
        });
    }

    function setupHelpTab() {
        tabs.help.setOnChange(function() {
            ocargo.game.currentTabSelected.select();
            ocargo.Drawing.startPopup('', '', HINT);
        });
    }

    function setupBigCodeModeTab() {
        tabs.big_code_mode.setOnChange(function() {
            tabs.blockly.select();

            if (ocargo.blocklyControl.bigCodeMode){
                tabs.big_code_mode.setContents(
                    ocargo.Drawing.imageDir + 'icons/big_code_mode.svg', "Enlarge");
                ocargo.blocklyControl.disableBigCodeMode();
            } else {
                tabs.big_code_mode.setContents(
                    ocargo.Drawing.imageDir + 'icons/big_code_mode.svg', "Shrink");
                ocargo.blocklyControl.enableBigCodeMode();
            }

            ocargo.blocklyControl.toggleFlyout();
            ocargo.blocklyControl.toggleFlyout();

            ocargo.blocklyControl.bringStartBlockFromUnderFlyout();
        });
    }

    function setupMuteTab() {
        tabs.mute.setOnChange(function() {
            ocargo.game.mute($.cookie('muted') !== 'true');
            ocargo.game.currentTabSelected.select();
        });
    }

    function setupQuitTab() {
        tabs.quit.setOnChange(function() {
            window.location.href = RETURN_URL;
        });
    }

    function setupNightModeTab() {
        tabs.nightmode.setOnChange(function() {
            if (NIGHT_MODE) {
                var str = window.location.pathname
                var newstr = str.replace('night','')
                window.location.assign(newstr)
            } else {
                window.location.href = 'night';
            }
        });
    }


    // Helper method for load and save tabs
    function populateTable (tableName, workspaces) {

        var table = $('#'+tableName),
            sortedWorkspaces = [];

        // Remove click listeners to avoid memory leak and remove all rows
        $('#'+tableName+' td').off('click');
        table.empty();

        // Order them alphabetically
        sortedWorkspaces = ocargo.utils.sortObjects(workspaces,'name');

        workspaces = sortedWorkspaces;

        // Add a row to the table for each workspace saved in the database
        for (var i = 0, ii = workspaces.length; i < ii; i++) {
            var workspace = workspaces[i];
            var tableRow = $('<tr>');
            tableRow.attr('value', workspace.id);
            var workspaceEntry = $('<td>');
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
    ocargo.game.tabs.fast.setEnabled(true);

    ocargo.game.tabs.load.setEnabled(false);
    ocargo.game.tabs.save.setEnabled(false);
    ocargo.game.tabs.clear_program.setEnabled(false);
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
    ocargo.game.tabs.help.setEnabled(false);
};

ocargo.Game.prototype.onFastControls = function() {
    this.allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';

    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/pause.svg', 'Pause');
    ocargo.game.tabs.fast.setContents(ocargo.Drawing.imageDir + 'icons/slow.svg', 'Slow');
    ocargo.game.tabs.step.setEnabled(false);

    ocargo.game.tabs.load.setEnabled(false);
    ocargo.game.tabs.save.setEnabled(false);
    ocargo.game.tabs.clear_program.setEnabled(false);
    ocargo.game.tabs.help.setEnabled(false);
};

ocargo.Game.prototype.onSlowControls = function() {
    this.allowCodeChanges(false);

    document.getElementById('direct_drive').style.visibility='hidden';

    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/pause.svg', 'Pause');
    ocargo.game.tabs.fast.setContents(ocargo.Drawing.imageDir + 'icons/fast.svg', 'Fast');
    ocargo.game.tabs.step.setEnabled(false);

    ocargo.game.tabs.load.setEnabled(false);
    ocargo.game.tabs.save.setEnabled(false);
    ocargo.game.tabs.clear_program.setEnabled(false);
    ocargo.game.tabs.help.setEnabled(false);
};

ocargo.Game.prototype.onStopControls = function() {
    this.allowCodeChanges(true);

    // TODO make this hidden unless blocks are clear or something...
    document.getElementById('direct_drive').style.visibility='visible';

    ocargo.game.tabs.play.setContents(ocargo.Drawing.imageDir + 'icons/play.svg', 'Play');
    ocargo.game.tabs.fast.setContents(ocargo.Drawing.imageDir + 'icons/fast.svg', 'Fast');
    ocargo.animation.resetAnimationLength();
    ocargo.game.tabs.step.setEnabled(true);

    ocargo.game.tabs.load.setEnabled(true);
    ocargo.game.tabs.save.setEnabled(true);
    ocargo.game.tabs.clear_program.setEnabled(true);
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


function restoreCmsLogin() {
    $("#id_cms-password").css("height", "20px").css("display", "inline");
    $("#id_cms-username").css("height", "20px").css("display", "inline");
}

$(document).ready(function() {
    ocargo.game = new ocargo.Game();
    ocargo.game.setup();
    ocargo.game.mute($.cookie('muted') === 'true');
});
