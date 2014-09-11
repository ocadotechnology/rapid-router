'use strict';

var ocargo = ocargo || {};

ocargo.LevelEditor = function() {
    
    /*************/
    /* Constants */
    /*************/

    var LIGHT_RED_URL = ocargo.Drawing.raphaelImageDir + 'trafficLight_red.svg';
    var LIGHT_GREEN_URL = ocargo.Drawing.raphaelImageDir + 'trafficLight_green.svg';
    
    var ADD_ROAD_IMG_URL = ocargo.Drawing.imageDir + "icons/add_road.svg";
    var DELETE_ROAD_IMG_URL = ocargo.Drawing.imageDir + "icons/delete_road.svg";
    var MARK_START_IMG_URL = ocargo.Drawing.imageDir + "icons/origin.svg";
    var MARK_END_IMG_URL = ocargo.Drawing.imageDir + "icons/destination.svg";

    var VALID_LIGHT_COLOUR = '#87E34D';
    var INVALID_LIGHT_COLOUR = '#E35F4D';

    var paper = $('#paper'); // May as well cache this

    var modes = {
        ADD_ROAD_MODE: {name: 'Add road', url: ocargo.Drawing.imageDir + "icons/add_road.svg"},
        DELETE_ROAD_MODE: {name: 'Delete road', url: ocargo.Drawing.imageDir + "icons/delete_road.svg"},
        MARK_DESTINATION_MODE: {name: 'Mark end', url: ocargo.Drawing.imageDir + "icons/destination.svg"},
        MARK_ORIGIN_MODE: {name: 'Mark start', url: ocargo.Drawing.imageDir + "icons/origin.svg"}
    };

    /*********/
    /* State */
    /*********/

    ocargo.saving = new ocargo.Saving();
    ocargo.drawing = new ocargo.Drawing();
    ocargo.drawing.preloadRoadTiles();

    // Level information
    var nodes = [];
    var decor = [];
    var trafficLights = [];
    var originNode = null;
    var destinationNode = null;
    var currentTheme = THEMES.grass;

    // Reference to the Raphael elements for each square
    var grid;

    // Current mode the user is in
    var mode = modes.ADD_ROAD_MODE;
    var prevMode = null;

    // Holds the state for when the user is drawing or deleting roads
    var strikeStart = null;

    // Holds the state to do with saving
    var savedState = null;
    var ownsSavedLevel = null;
    var savedLevelID = -1;

    // Whether the user is scrolling on a tablet
    var isScrolling = false;

    // Whether the trashcan is currently open
    var trashcanOpen = false;
    var trashcanAbsolutePaperX;
    var trashcanAbsolutePaperY;

    // So that we store the current state when the page unloads
    window.addEventListener('unload', storeStateInLocalStorage);

    // Initialise the grid
    initialiseGrid();
    setTheme(THEMES.grass);

    // Setup the toolbox
    setupToolbox();
    setupTrashcan();

    // If there's any previous state in local storage retrieve it
    retrieveStateFromLocalStorage();

    // Draw everything
    drawAll();


    /*********************************/
    /* Two finger scrolling of paper */
    /*********************************/

    var scrollStartPosX = 0;
    var scrollStartPosY = 0;
    var touchStartPosX = 0;
    var touchStartPosY = 0;

    paper.on('touchstart', function(ev) {
        if (ev.originalEvent.touches.length === 2) {
            ev.preventDefault();
            scrollStartPosX = paper.scrollLeft();
            touchStartPosX = ev.originalEvent.touches[0].pageX;
            scrollStartPosY = paper.scrollTop();
            touchStartPosY = ev.originalEvent.touches[0].pageY;
            isScrolling = true;
        }
    });

    paper.on('touchmove', function(ev) {
        if (ev.originalEvent.touches.length === 2) {
            ev.preventDefault();
            paper.scrollLeft(scrollStartPosX - (ev.originalEvent.touches[0].pageX - touchStartPosX));
            paper.scrollTop(scrollStartPosY - (ev.originalEvent.touches[0].pageY - touchStartPosY));
        }
    });

    paper.on('touchend touchcancel', function(ev) {
        if (ev.originalEvent.touches.length === 0) {
            isScrolling = false;
        }
    });

    /***************/
    /* Setup tools */
    /***************/
    // Sets up the left hand side toolbox (listeners/images etc.)

    function setupToolbox() {
        var tabs = [];
        var currentTabSelected = null;

        tabs.play = new ocargo.Tab($('#play_radio'), $('#play_radio + label'));
        tabs.map = new ocargo.Tab($('#map_radio'), $('#map_radio + label'), $('#map_pane'));
        tabs.scenery = new ocargo.Tab($('#scenery_radio'), $('#scenery_radio + label'), $('#scenery_pane'));
        tabs.character = new ocargo.Tab($('#character_radio'), $('#character_radio + label'), $('#character_pane'));
        tabs.blocks = new ocargo.Tab($('#blocks_radio'), $('#blocks_radio + label'), $('#blocks_pane'));
        tabs.random = new ocargo.Tab($('#random_radio'), $('#random_radio + label'), $('#random_pane'));
        tabs.load = new ocargo.Tab($('#load_radio'), $('#load_radio + label'), $('#load_pane'));
        tabs.save = new ocargo.Tab($('#save_radio'), $('#save_radio + label'), $('#save_pane'));
        tabs.share = new ocargo.Tab($('#share_radio'), $('#share_radio + label'), $('#share_pane'));
        tabs.help = new ocargo.Tab($('#help_radio'), $('#help_radio + label'));
        tabs.quit = new ocargo.Tab($('#quit_radio'), $('#quit_radio + label'));  

        setupPlayTab();
        setupMapTab();
        setupSceneryTab();
        setupCharacterTab();
        setupBlocksTab();
        setupRandomTab();
        setupLoadTab();
        setupSaveTab();
        setupShareTab();
        setupHelpTab();
        setupQuitTab();

        // enable the map tab by default
        currentTabSelected = tabs.map;
        tabs.map.select();

        function setupPlayTab() {
            tabs.play.setOnChange(function() {
                if (isLevelValid()) {
                    var state = extractState()
                    state.name = "Custom level"
                    ocargo.saving.saveLevel(state, null, true, function(error, levelID) {
                        if(error) {
                            console.error(error)
                            return;
                        }
                        window.location.href = '/rapidrouter/level_editor/level/play_anonymous/' + levelID;
                    });
                } else {
                    currentTabSelected.select();
                }
            });
        }

        function changeCurrentToolDisplay(mode){
            $('#currentToolText').text(mode.name);
            $('#currentToolIcon').attr("src", mode.url);            
        }
        
        function setupMapTab() {
            tabs.map.setOnChange(function() {
                transitionTab(tabs.map);
                mode = modes.ADD_ROAD_MODE;
                changeCurrentToolDisplay(modes.ADD_ROAD_MODE);
            });

            $('#clear').click(function() {
                clear();
                localStorage.removeItem('levelEditorState'); 
                drawAll();
            });

            $('#start').click(function() {
                mode = modes.MARK_ORIGIN_MODE;
                changeCurrentToolDisplay(modes.MARK_ORIGIN_MODE);
            });

            $('#end').click(function() {
                mode = modes.MARK_DESTINATION_MODE;
                changeCurrentToolDisplay(modes.MARK_DESTINATION_MODE);
            });

            $('#add_road').click(function() {
                mode = modes.ADD_ROAD_MODE;
                changeCurrentToolDisplay(modes.ADD_ROAD_MODE);
            });

            $('#delete_road').click(function() {
                mode = modes.DELETE_ROAD_MODE;
                changeCurrentToolDisplay(modes.DELETE_ROAD_MODE);
            });
        }

        function setupSceneryTab() {
            tabs.scenery.popup = true;

            tabs.scenery.setOnChange(function() {
                if (tabs.scenery.popup) {
                    tabs.scenery.popup = false;
                    ocargo.Drawing.startPopup('', '', ocargo.messages.trafficLightsWarning + ocargo.jsElements.closebutton("Close"));
                }

                transitionTab(tabs.scenery);
            });

            $('#theme_select').change(function() {
                setTheme(THEMES[$(this).val()]);
            });

            $('#bush').click(function() {
                new InternalDecor('bush');
            });

            $('#tree1').click(function() {
                new InternalDecor('tree1');
            });

            $('#tree2').click(function() {
                new InternalDecor('tree2');
            });

            $('#pond').click(function() {
                new InternalDecor('pond');
            });

            $('#trafficLightRed').click(function() {
                new InternalTrafficLight({"redDuration": 3, "greenDuration": 3, "startTime": 0,
                                          "startingState": ocargo.TrafficLight.RED,
                                          "sourceCoordinate": null,  "direction": null});
            });

            $('#trafficLightGreen').click(function() {
                new InternalTrafficLight({"redDuration": 3, "greenDuration": 3, "startTime": 0,
                                          "startingState": ocargo.TrafficLight.GREEN,
                                          "sourceCoordinate": null,  "direction": null});
            });
        }

        function setupCharacterTab() {
            tabs.character.setOnChange(function() {
                transitionTab(tabs.character);
            });

            $("#character_select").change(function() { 
                CHARACTER_NAME = $(this).val();
                redrawRoad();
                $('#character_image').attr('src', CHARACTERS[CHARACTER_NAME].image);
            });

            $("#character_select").change();
        }  

        function setupBlocksTab() {
            tabs.blocks.setOnChange(function() {
                transitionTab(tabs.blocks);
            });
            
            // Hacky, if a way can be found without initialising the entire work space that would be great!

            // Initial selection
            $('#move_forwards_checkbox').prop('checked', true);
            $('#turn_left_checkbox').prop('checked', true);
            $('#turn_right_checkbox').prop('checked', true);

            // Select all functionality
            var selectAll = $('#select_all_checkbox');
            selectAll.change(function() {
                var checked = selectAll.prop('checked');
                $('.block_checkbox').each(function() {
                    if ($(this) !== selectAll) {
                        $(this).prop('checked', checked);
                    }
                });
            });

            // Setup the block images
            function addListenerToImage(type) {
                $('#' + type + '_image').click(function() {
                    $('#' + type + '_checkbox').click();
                });
            }

            // Disable block numbers if not developer
            if(!DEVELOPER) {
                $('.block_number').css('display', 'none');
            }

            initCustomBlocksDescription();

            var blockly = document.getElementById('blockly');
            var toolbox = document.getElementById('blockly_toolbox');
            Blockly.inject(blockly, {
                path: '/static/game/js/blockly/',
                toolbox: toolbox,
                trashcan: true
            });

            for (var i = 0; i < BLOCKS.length; i++) {
                var type = BLOCKS[i];
                var block = Blockly.Block.obtain(Blockly.mainWorkspace, type);
                block.initSvg();
                block.render();

                var svg = block.getSvgRoot();
                var large = type === "controls_whileUntil" || 
                            type === "controls_repeat" ||
                            type === "controls_if" ||
                            type === "declare_proc" ||
                            type === "controls_repeat_while" ||
                            type === "controls_repeat_until";

                var content = '<svg class="block_image' + (large ? ' large' : '') + '">';
                content += '<g transform="translate(10,0)"';
                content += svg.innerHTML ? svg.innerHTML : '';
                content += '</g></svg>';

                $('#' + type + '_image').html(content);

                addListenerToImage(type);
            }

            $('#blockly').css('display','none');
        }

        function setupRandomTab() {
            tabs.random.setOnChange(function() {
                transitionTab(tabs.random);
            });

            $('#generate').click(function() {
                var numberOfTiles = Math.max(Math.min($('#size').val(), 40), 2);
                var branchiness = Math.max(Math.min($('#branchiness').val(), 10), 0);
                var loopiness = Math.max(Math.min($('#loopiness').val(), 10), 0); 
                var curviness = Math.max(Math.min($('#curviness').val(), 10), 0);
               
                $('#size').val(numberOfTiles);
                $('#branchiness').val(branchiness);
                $('#loopiness').val(loopiness);
                $('#curviness').val(curviness);

                var data = {numberOfTiles: numberOfTiles,
                            branchiness: branchiness/10.0,
                            loopiness: loopiness/10.0,
                            curviness: curviness/10.0,
                            trafficLights: $('#trafficLightsEnabled').val() == "yes",
                            scenery: $('#sceneryEnabled').val() == "yes",
                            csrfmiddlewaretoken: $.cookie('csrftoken')};
                
                $('#generate').attr('disabled', true);

                ocargo.saving.retrieveRandomLevel(data, function(error, mapData) {
                    if (error) {
                        console.error(error);
                        ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                        return;
                    }

                    restoreState(mapData);

                    $('#generate').attr('disabled', false);
                });
            });
        }

        function setupLoadTab() {
            var selectedLevel = null;
            var ownLevels = null;
            var sharedLevels = null;

            tabs.load.setOnChange(function() {
                if(!isLoggedIn("load")) {
                    currentTabSelected.select();
                    return;
                }

                ocargo.saving.retrieveListOfLevels(processListOfLevels);
            });

            // Setup own/shared levels radio
            $('#load_type_select').change(function() {
                var value = this.value;

                var levels = value === "ownLevels" ? ownLevels : sharedLevels;
                populateLoadSaveTable("loadLevelTable", levels);

                // Add click listeners to all rows
                $('#loadLevelTable tr[value]').on('click', function(event) {
                    $('#loadLevelTable tr').attr('selected', false);
                    $('#loadLevelTable tr').css('selected', false);
                    $(this).attr('selected', true);
                    $('#loadLevel').removeAttr('disabled');
                    $('#deleteLevel').removeAttr('disabled');
                    selectedLevel = $(this).attr('value');
                });

                $('#deleteLevel').attr('disabled', value === "sharedLevels" || !selectedLevel);
                $('#loadLevel').attr('disabled', !selectedLevel);

                $('#load_pane .scrolling-table-wrapper').css('display', levels.length === 0 ? 'none' : 'block');
            });

            $('#loadLevel').click(function() {
                if (selectedLevel) {
                    loadLevel(selectedLevel); 
                }
            });

            $('#deleteLevel').click(function() {
                if (!selectedLevel) {
                    return;
                }

                ocargo.saving.deleteLevel(selectedLevel, function(err, ownedLevels, sharedLevels) {
                    if (err !== null) {
                        console.error(err);
                        return;
                    }

                    if (selectedLevel == savedLevelID) {
                        savedLevelID = -1;
                        savedState = null;
                        ownsSavedLevel = false;
                    }

                    processListOfLevels(err, ownedLevels, sharedLevels);
                });
            });

            function processListOfLevels(err, listOfOwnLevels, listOfSharedLevels) {
                if (err !== null) {
                    console.error(err);
                    currentTabSelected.select();
                    ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                    return;
                }

                ownLevels = listOfOwnLevels;
                sharedLevels = listOfSharedLevels;

                // Important: done before change() call
                // Table cells need to have rendered to match th with td widths
                transitionTab(tabs.load);

                $('#load_type_select').change();

                // But disable all the modal buttons as nothing is selected yet
                selectedLevel = null;

                if(ownLevels.length == 0 && sharedLevels.length == 0) {
                    $('#load_pane #does_exist').css('display', 'none');
                    $('#load_pane #does_not_exist').css('display', 'block');
                }
                else {
                    $('#load_pane #does_exist').css('display', 'block');
                    $('#load_pane #does_not_exist').css('display', 'none');
                }
            }
        }

        function setupSaveTab() {
            var selectedLevel = null;

            tabs.save.setOnChange(function () {
                if (!isLoggedIn("save") || !isLevelValid()) {
                    currentTabSelected.select();
                    return;
                }

                ocargo.saving.retrieveListOfLevels(processListOfLevels);
            });
            
            $('#saveLevel').click(function() {
                if(!isLevelValid()) {
                    return;
                }

                var newName = $('#levelNameInput').val();
                if (!newName || newName === "") {
                    // TODO error message?
                    return;
                }

                // Test to see if we already have the level saved
                var table = $("#saveLevelTable");
                var existingID = -1;

                for (var i = 0; i < table[0].rows.length; i++) {
                     var row = table[0].rows[i];
                     var existingName = row.cells[0].innerHTML;
                     if (existingName === newName) {
                        existingID = row.getAttribute('value');
                        break;
                     }
                }

                if (existingID != -1) {
                    if (existingID != savedLevelID) {
                        var onYes = function(){
                            saveLevel(newName, existingID, processListOfLevels);
                            $("#close-modal").click();
                        };
                        var onNo = function(){
                            $("#close-modal").click();
                        };
                        ocargo.Drawing.startYesNoPopup("Overwriting","Warning",ocargo.messages.saveOverwriteWarning(newName), onYes, onNo);
                    }
                    else {
                        saveLevel(newName, existingID, processListOfLevels);
                    }
                }
                else {
                    saveLevel(newName, null, processListOfLevels);
                }
            });

            function processListOfLevels(err, ownLevels, sharedLevels) {
                if (err !== null) {
                    console.error(err);
                    ocargo.Drawing.startPopup("Error", "", ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                    return;
                }

                // Important: done before change() call
                // Table cells need to have rendered to match th with td widths
                transitionTab(tabs.save);

                populateLoadSaveTable("saveLevelTable", ownLevels);

                // Add click listeners to all rows
                $('#saveLevelTable tr[value]').on('click', function(event) {
                    var rowSelected = $(event.target.parentElement);
                    $('#saveLevelTable tr').attr('selected', false);
                    $(this).attr('selected', true);
                    $('#saveLevel').removeAttr('disabled');
                    selectedLevel = parseInt(rowSelected.attr('value'));

                    for (var i = 0; i < ownLevels.length; i++) {
                        if (ownLevels[i].id === selectedLevel) {
                            $("#levelNameInput").val(ownLevels[i].name);
                        }
                    }
                });

                $('#save_pane .scrolling-table-wrapper').css('display', ownLevels.length === 0 ? 'none' : 'block');
                selectedLevel = null;
            }
        }

        function setupShareTab() {
            var text = [];
            text.shared = "Yes";
            text.unshared = "No";
            text.pending = "...";

            // Setup the behaviour for when the tab is selected
            tabs.share.setOnChange(function() {
                if (!isSoloStudent() ||  !isLoggedIn("share") || !isLevelSaved() || !isLevelOwned()) {
                    currentTabSelected.select();
                    return;
                }
                
                ocargo.saving.getSharingInformation(savedLevelID, function(error, validRecipients) {
                    if(error) {
                        console.error(error);
                        return;
                    }

                    transitionTab(tabs.share);
                    processSharingInformation(error, validRecipients);
                });
            });

            var classesTaught;
            var fellowTeachers;
            var currentClassID;
            var allShared;

            // Setup the teachers/classes radio buttons for the teacher panel
            $('#share_type_select').change(function() {
                if(this.value == "classes") {
                    $('#class_selection').css('display', 'block');
                    $('#class_select').val(currentClassID);
                    $('#class_select').change();
                }
                else {
                    $('#class_selection').css('display', 'none');
                    populateSharingTable(fellowTeachers);
                }
            });

            // Setup the class dropdown menu for the teacher panel
            $('#class_select').change(function() {
                var classID = $('#class_select').val();
                
                for (var i = 0; i < classesTaught.length; i++) {
                    if (classesTaught[i].id == classID) {
                        populateSharingTable(classesTaught[i].students);
                        currentClassID = classesTaught[i].id;
                        break;
                    }
                }
            });

            // Setup the select all button
            $('#shareWithAll').click(function() {
                if (!isLevelSaved() || !isLevelOwned()) {
                    return;
                }

                var statusDesired = allShared ? 'shared' : 'unshared';
                var actionDesired = allShared ? 'unshare' : 'share';

                var recipientIDs = [];
                $('#shareLevelTable tr[value]').each(function() {
                    recipientIDs.push(this.getAttribute('value'));
                });

                var recipientData = {recipientIDs: recipientIDs, 
                                     action: actionDesired};

                ocargo.saving.shareLevel(savedLevelID, recipientData, processSharingInformation);
            });

            // Method to call when we get an update on the level's sharing information
            function processSharingInformation(error, validRecipients) {
                if (error !== null) {
                    console.error(error);
                    ocargo.Drawing.startPopup("Error", "", ocargo.messages.internetDown + ocargo.jsElements.closebutton("Close"));
                    return;
                }

                if (USER_STATUS === "SCHOOL_STUDENT") {
                    var classmates = validRecipients.classmates;
                    var teacher = validRecipients.teacher;

                    populateSharingTable(classmates);
                }
                else if (USER_STATUS === "TEACHER") {
                    classesTaught = validRecipients.classes;
                    fellowTeachers = validRecipients.teachers;

                    $('#class_select').empty();
                    for (var i = 0; i < classesTaught.length; i++) {
                        var option = $('<option>');
                        option.attr( {
                            value: classesTaught[i].id,
                        });
                        option.text(classesTaught[i].name);
                        $('#class_select').append(option);
                    }

                    if ($('#share_type_select').val() === 'teachers') {
                        populateSharingTable(validRecipients.teachers);
                    }
                    else {
                        var found = false;
                        $('#class_select option').each(function() {
                            if (this.value == currentClassID) {
                                $('#class_select').val(currentClassID);
                                $('#class_select').change();
                                found = true;
                            }
                        });

                        if (!found) {
                            $('#class_select').change();
                        }
                    }
                }
            }

            function populateSharingTable(recipients) {
                // Remove click listeners to avoid memory leak and remove all rows
                var table = $('#shareLevelTable tbody');
                $('#shareLevelTable tr').off('click');
                table.empty();

                // Order them alphabetically
                recipients.sort(function(a, b) {
                    if (a.name < b.name) {
                        return -1;
                    }
                    else if (a.name > b.name) {
                        return 1;
                    }
                    return 0;
                });

                allShared = true;
                // Add a row to the table for each workspace saved in the database
                for (var i = 0; i < recipients.length; i++) {
                    var recipient = recipients[i];
                    var status = recipient.shared ? 'shared' : 'unshared';
                    
                    if (recipient.shared) {
                        status = 'shared';
                    }
                    else {
                        status = 'unshared';
                        allShared = false;
                    }

                    var tableRow = $('<tr>');
                    tableRow.attr( {
                        'value': recipient.id,
                        'status': status,
                    });
                    var rowName = $('<td>').text(recipient.name);

                    var rowStatus = $('<td>');
                    rowStatus.attr( {
                        'class': 'share_cell'
                    });
                    rowStatus.text(text[status]);
                    tableRow.append(rowName);
                    tableRow.append(rowStatus);

                    table.append(tableRow);
                }

                // Update the shareWithAll button
                if (allShared) {
                    $('#shareWithAll span').html('Unshare with all');
                    $('#shareWithAll img').attr('src',ocargo.Drawing.imageDir + 'icons/quit.svg');
                }
                else {
                    $('#shareWithAll span').html('Share with all');
                    $('#shareWithAll img').attr('src',ocargo.Drawing.imageDir + 'icons/share.svg');
                }

                // update click listeners in the new rows
                $('#shareLevelTable tr[value]').on('click', function(event) {
                    if (isLevelSaved() && isLevelOwned()) {
                        var status = this.getAttribute('status');

                        var recipientData = {recipientIDs: [this.getAttribute('value')], 
                                             action: (status === 'shared' ? 'unshare' : 'share')};

                        ocargo.saving.shareLevel(savedLevelID, recipientData, processSharingInformation);
                    }
                });

                // update column widths
                for(var i = 0; i < 2; i++){
                    var td = $('#shareLevelTable td:eq(' + i + ')');
                    var td2 = $('#shareLevelTableHeader th:eq(' + i + ')');
                    td2.width(td.width());
                }
            }
        }

        function setupHelpTab() {
            var message = ocargo.messages.levelEditorPCSubtitle;

            message += "<br><br>" + ocargo.messages.levelEditorHelpText;

            tabs.help.setOnChange(function() {
                currentTabSelected.select();
                ocargo.Drawing.startPopup('', '', message + ocargo.jsElements.closebutton("Close"));
            });
        }

        function setupQuitTab() {
            tabs.quit.setOnChange(function() {
                window.location.href = "/rapidrouter/";
            });
        }

                
        // Helper methods
        function transitionTab(newTab) {
            currentTabSelected.setPaneEnabled(false);
            newTab.setPaneEnabled(true);
            currentTabSelected = newTab;
        }

        function populateLoadSaveTable(tableName, levels) {
            var table = $('#'+tableName + ' tbody');

            $('#'+tableName).css('display', levels.length == 0 ? 'none' : 'table');
            $('#'+tableName + 'Header').css('display', levels.length == 0 ? 'none' : 'table');

            // Remove click listeners to avoid memory leak and remove all rows
            $('#'+tableName+' tr').off('click');
            table.empty();

            // Order them alphabetically
            levels.sort(function(a, b) {
                if (a.name < b.name) {
                    return -1;
                }
                else if (a.name > b.name) {
                    return 1;
                }
                return 0;
            });

            // Add a row to the table for each workspace saved in the database
            for (var i = 0, ii = levels.length; i < ii; i++) {
                var level = levels[i];
                var tableRow = $('<tr>');
                tableRow.attr( {
                    'value' : level.id
                });
                var rowName = $('<td>');
                rowName.text(level.name);
                var rowOwner = $('<td>');
                rowOwner.text(level.owner);
                tableRow.append(rowName);
                tableRow.append(rowOwner);
                table.append(tableRow);
            }

            for(var i = 0; i < 2; i++){
                var td = $('#' + tableName + ' td:eq(' + i + ')');
                var td2 = $('#' + tableName + 'Header th:eq(' + i + ')');
                td2.width(td.width());
            }
        }
    }

    /************/
    /* Trashcan */
    /************/

    function setupTrashcan() {

        var trashcan = $('#trashcanHolder');

        // Iffy way of making sure the trashcan stays inside the grid
        // when window bigger than grid
        $(window).resize(function() {
            var windowWidth = $(window).width();
            var windowHeight = $(window).height();

            var paperRightEdge = PAPER_WIDTH + $('#tools').width();
            var paperBottomEdge = PAPER_HEIGHT;

            var bottom = 50;
            if(windowHeight > paperBottomEdge) {
                bottom += windowHeight - paperBottomEdge
            }

            var right = 50;
            if(windowWidth > paperRightEdge) {
                right += windowWidth - paperRightEdge;
            } 

            trashcan.css('right', right);
            trashcan.css('bottom', bottom);


            var trashcanOffset = trashcan.offset();
            var paperOffset = paper.offset();
            trashcanAbsolutePaperX = trashcanOffset.left - paperOffset.left;
            trashcanAbsolutePaperY = trashcanOffset.top - paperOffset.top;
        });

        addReleaseListeners(trashcan[0]);
        closeTrashcan();
    }

    function checkImageOverTrashcan(paperX, paperY, imageWidth, imageHeight) {
        var paperAbsX = paperX - paper.scrollLeft() + imageWidth/2;
        var paperAbsY = paperY - paper.scrollTop() + imageHeight/2;
        var trashcanWidth = $('#trashcanHolder').width();
        var trashcanHeight = $('#trashcanHolder').height();

        if(paperAbsX > trashcanAbsolutePaperX && paperAbsX <= trashcanAbsolutePaperX + trashcanWidth  &&
            paperAbsY > trashcanAbsolutePaperY - 20 && paperAbsY <= trashcanAbsolutePaperY + trashcanHeight) {
            openTrashcan();
        }
        else {
            closeTrashcan();
        }
    }

    function openTrashcan() {
        $('#trashcanLidOpen').css('display', 'block');
        $('#trashcanLidClosed').css('display', 'none');
        trashcanOpen = true;
    }

    function closeTrashcan() {
        $('#trashcanLidOpen').css('display', 'none');
        $('#trashcanLidClosed').css('display', 'block');
        trashcanOpen = false;
    }

    /************************/
    /** Current state tests */
    /************************/
    // Functions simply to improve readability of complex conditional code
    
    function isOriginCoordinate(coordinate) {
        return originNode && originNode.coordinate.equals(coordinate);
    }

    function isDestinationCoordinate(coordinate) {
        return destinationNode && destinationNode.coordinate.equals(coordinate);
    }

    function isCoordinateOnGrid(coordinate) {
        return coordinate.x >= 0 && coordinate.x < GRID_WIDTH &&
            coordinate.y >= 0 && coordinate.y < GRID_HEIGHT;
    }

    function canPlaceCFC(node) {
        return node.connectedNodes.length <= 1;
    }

    function getGridItem(globalX, globalY) {
        var paperPosition = paper.position();
        var x = globalX - paperPosition.left + paper.scrollLeft();
        var y = globalY - paperPosition.top + paper.scrollTop();

        x /= GRID_SPACE_SIZE;
        y /= GRID_SPACE_SIZE;

        x = Math.min(Math.max(0, Math.floor(x)), GRID_WIDTH - 1);
        y = Math.min(Math.max(0, Math.floor(y)), GRID_HEIGHT - 1);

        return grid[x][y];
    }

    /*************/
    /* Rendering */
    /*************/

    function initialiseGrid() {
        grid = ocargo.drawing.createGrid();
        for (var i = 0; i < grid.length; i++) {
            for (var j = 0; j < grid[i].length; j++) {
                grid[i][j].node.onmousedown = handleMouseDown(grid[i][j]);
                grid[i][j].node.onmouseover = handleMouseOver(grid[i][j]);
                grid[i][j].node.onmouseout = handleMouseOut(grid[i][j]);
                grid[i][j].node.onmouseup = handleMouseUp(grid[i][j]);

                grid[i][j].node.ontouchstart = handleTouchStart(grid[i][j]);
                grid[i][j].node.ontouchmove = handleTouchMove(grid[i][j]);
                grid[i][j].node.ontouchend = handleTouchEnd(grid[i][j]);
            }
        }
    }

    function clear() {
        for (var i = trafficLights.length-1; i >= 0; i--) {
            trafficLights[i].destroy();
        }
        for (var i = decor.length-1; i >= 0; i--) {
            decor[i].destroy();
        }

        nodes = [];
        strikeStart = null;
        originNode = null;
        destinationNode = null;
    }

    function drawAll() {
        ocargo.drawing.renderGrid(grid, currentTheme);
        redrawRoad();
    }

    function redrawRoad() {
        ocargo.drawing.renderRoad(nodes);
        clearMarkings();
        bringTrafficLightsToFront();
        bringDecorToFront();
    }

    function bringDecorToFront() {
        for (var i = 0; i < decor.length; i++) {
            decor[i].image.toFront();
        }
    }

    function bringTrafficLightsToFront() {
        for (var i = 0; i < trafficLights.length; i++) {
            trafficLights[i].image.toFront();
        }
    }

    /************/
    /*  Marking */
    /************/
    // Methods for highlighting squares

    function mark(coordMap, colour, opacity, occupied) {
        var coordPaper = ocargo.Drawing.translate(coordMap);
        var element = grid[coordPaper.x][coordPaper.y];
        element.attr({fill:colour, "fill-opacity": opacity});
    }

    function markAsOrigin(coordinate) {
        mark(coordinate, 'red', 0.7, true);
    }

    function markAsDestination(coordinate) {
        mark(coordinate, 'blue', 0.7, true);
    }

    function markAsBackground(coordinate) {
        mark(coordinate, currentTheme.background, 0, false);
    }

    function markAsSelected(coordinate) {
        mark(coordinate, currentTheme.selected, 1, true);
    }

    function markAsHighlighted(coordinate) {
        mark(coordinate, currentTheme.selected, 0.3, true);
    }

    function clearMarkings() {
        for (var i = 0; i < GRID_WIDTH; i++) {
            for (var j = 0; j < GRID_HEIGHT; j++) {
                markAsBackground(new ocargo.Coordinate(i,j));
                grid[i][j].toFront();
            }
        }
        if (originNode) {
            markAsOrigin(originNode.coordinate);
        }
        if (destinationNode) {
            markAsDestination(destinationNode.coordinate);
        }

        bringTrafficLightsToFront();
        bringDecorToFront();
    }

    function markTentativeRoad(currentEnd) {
        clearMarkings();
        applyAlongStrike(setup, currentEnd);

        var previousNode = null;
        function setup(x, y) {
            var coordinate = new ocargo.Coordinate(x, y);
            var node = new ocargo.Node(coordinate);
            if (previousNode) {
                node.addConnectedNodeWithBacklink(previousNode);
            }
            previousNode = node;
            markAsSelected(coordinate);
        }
    }

    /***************************/
    /* Paper interaction logic */
    /***************************/

    // Function for making an element "transparent" to mouse events
    // e.g. decor, traffic lights, rubbish bin etc.
    function addReleaseListeners(element) {
        var lastGridItem;

        element.onmouseover = 
            function(e) {
                lastGridItem = getGridItem(e.pageX, e.pageY);
                if(strikeStart) {
                    handleMouseOver(lastGridItem)(e);
                }
            };

        element.onmousemove = 
            function(e) {
                var item = getGridItem(e.pageX, e.pageY);
                if(item != lastGridItem) {
                    if(lastGridItem) {
                        handleMouseOut(lastGridItem)(e);
                    }
                    if(strikeStart) {
                        handleMouseOver(item)(e);
                    }
                    lastGridItem = item;
                }
            };

        element.onmouseup = 
            function(e) {
                if(strikeStart) {
                    handleMouseUp(getGridItem(e.pageX, e.pageY))(e);
                }
            };

        // Touch events seem to have this behaviour automatically
    };

    function handleMouseDown(this_rect) {
        return function (ev) {
            ev.preventDefault();

            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x / GRID_SPACE_SIZE,
                                                   getBBox.y / GRID_SPACE_SIZE);
            var coordMap = ocargo.Drawing.translate(coordPaper);
            var existingNode = ocargo.Node.findNodeByCoordinate(coordMap, nodes);

            if (mode === modes.MARK_ORIGIN_MODE && existingNode && canPlaceCFC(existingNode)) {
                if (originNode) {
                    var prevStart = originNode.coordinate;
                    markAsBackground(prevStart);
                }
                // Check if same as destination node
                if (isDestinationCoordinate(coordMap)) {
                    destinationNode = null;
                }
                markAsOrigin(coordMap);
                var newStartIndex = ocargo.Node.findNodeIndexByCoordinate(coordMap, nodes);

                // Putting the new start in the front of the nodes list.
                var temp = nodes[newStartIndex];
                nodes[newStartIndex] = nodes[0];
                nodes[0] = temp;
                originNode = nodes[0];
            } else if (mode === modes.MARK_DESTINATION_MODE && existingNode) {    
                if (destinationNode) {
                    var prevEnd = destinationNode.coordinate;
                    markAsBackground(prevEnd);
                }
                // Check if same as starting node
                if (isOriginCoordinate(coordMap)) {
                    originNode = null;
                }
                markAsDestination(coordMap);
                var newEnd = ocargo.Node.findNodeIndexByCoordinate(coordMap, nodes);
                destinationNode = nodes[newEnd];

            }  else if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                strikeStart = coordMap;
                markAsSelected(coordMap);
            }
        };
    }

    function handleMouseOver(this_rect) {
        return function(ev) {
            ev.preventDefault();

            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x / 100, getBBox.y / 100);
            var coordMap = ocargo.Drawing.translate(coordPaper);

            if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                if (strikeStart !== null) {
                    markTentativeRoad(coordMap);
                }
                else if (!isOriginCoordinate(coordMap) && !isDestinationCoordinate(coordMap)) {
                    markAsHighlighted(coordMap);
                }
            }
            else if (mode === modes.MARK_ORIGIN_MODE || mode === modes.MARK_DESTINATION_MODE) {
                var node = ocargo.Node.findNodeByCoordinate(coordMap, nodes);
                if (node && destinationNode !== node && originNode !== node) {
                    if (mode === modes.MARK_DESTINATION_MODE) {
                        mark(coordMap, 'blue', 0.3, true); 
                    }
                    else if (canPlaceCFC(node)) {
                        mark(coordMap, 'red', 0.5, true);
                    }
                }
            }
        };
    }

    function handleMouseOut(this_rect) {
        return function(ev) {
            ev.preventDefault();

            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE,
                                                   getBBox.y/GRID_SPACE_SIZE);
            var coordMap = ocargo.Drawing.translate(coordPaper);

            if (mode === modes.MARK_ORIGIN_MODE || mode === modes.MARK_DESTINATION_MODE) {
                var node = ocargo.Node.findNodeByCoordinate(coordMap, nodes);
                if (node && destinationNode !== node && originNode !== node) {
                    markAsBackground(coordMap);
                }
            }
            else if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                if (!isOriginCoordinate(coordMap) && !isDestinationCoordinate(coordMap)) {
                    markAsBackground(coordMap);
                }
            }
        };
    }

    function handleMouseUp(this_rect) {
        return function(ev) {
            ev.preventDefault();

            if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                var getBBox = this_rect.getBBox();
                var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE,
                                                       getBBox.y/GRID_SPACE_SIZE);
                var coordMap = ocargo.Drawing.translate(coordPaper);

                if (mode === modes.DELETE_ROAD_MODE) {
                    finaliseDelete(coordMap);
                } 
                else {
                    finaliseMove(coordMap);
                }

                sortNodes(nodes);
                redrawRoad();
            }
        };
    }

    function handleTouchStart() {
        return function (ev) {
            if (ev.touches.length === 1 && !isScrolling) {
                var gridItem = getGridItem(ev.touches[0].pageX, ev.touches[0].pageY);
                handleMouseDown(gridItem)(ev);
            }
        };
    }

    function handleTouchMove() {
        return function(ev) {
            if (ev.touches.length === 1 && !isScrolling) {
                var gridItem = getGridItem(ev.touches[0].pageX, ev.touches[0].pageY);
                handleMouseOver(gridItem)(ev);
            }
        };
    }

    function handleTouchEnd() {
        return function(ev) {
            if (ev.changedTouches.length === 1 && !isScrolling) {
                var gridItem = getGridItem(ev.changedTouches[0].pageX, ev.changedTouches[0].pageY);
                handleMouseUp(gridItem)(ev);
            }
        };
    }

    function setupDecorListeners(decor) {
        var image = decor.image;

        var originX;
        var originY;

        var paperX;
        var paperY;

        var paperWidth; 
        var paperHeight;

        var imageWidth;
        var imageHeight;

        function onDragMove(dx, dy) {
            paperX = dx + originX;
            paperY = dy + originY;

            // Deal with trashcan
            checkImageOverTrashcan(paperX, paperY, imageWidth, imageHeight);;

            // Stop it being dragged off the edge of the page
            if (paperX < 0) {
                paperX = 0;
            }
            else if (paperX + imageWidth > paperWidth) {
                paperX = paperWidth - imageWidth;
            }

            if (paperY < 0) {
                paperY = 0;
            }
            else if (paperY + imageHeight >  paperHeight) {
                paperY = paperHeight - imageHeight;
            }

            image.transform('t' + paperX + ',' + paperY);
        }

        function onDragStart(x, y) {
            var bBox = image.getBBox();
            imageWidth = bBox.width;
            imageHeight = bBox.height;

            var paperPosition = paper.position();
            originX = x - paperPosition.left + paper.scrollLeft() - imageWidth/2;
            originY = y - paperPosition.top + paper.scrollTop() - imageHeight/2;

            paperWidth = GRID_WIDTH * GRID_SPACE_SIZE;
            paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE;
        }

        function onDragEnd() {
            originX = paperX;
            originY = paperY;

            if(trashcanOpen) {
                decor.destroy();
            }

            closeTrashcan();
        }

        image.drag(onDragMove, onDragStart, onDragEnd);
        addReleaseListeners(image.node);
    }

    function setupTrafficLightListeners(trafficLight) {

        var image = trafficLight.image;

        // Position in map coordinates.
        var sourceCoord;                        
        var controlledCoord;

        // Current position of the element in paper coordinates
        var paperX;                                 
        var paperY;

        // Where the drag started in paper coordinates
        var originX;                                 
        var originY;

        // Size of the paper
        var paperWidth;
        var paperHeight;

        // Size of the image
        var imageWidth;
        var imageHeight;

        // Orientation and rotation transformations
        var scaling;
        var rotation;

        var moved = false;

        function onDragMove(dx, dy) {
            trafficLight.valid = false;
            image.attr({'cursor':'default'});
            moved = dx !== 0 || dy !== 0;

            // Update image's position
            paperX = dx + originX;
            paperY = dy + originY;

            // Adjust for the fact that we've rotated the image
            if (rotation === 90 || rotation === 270)  {
                paperX += (imageWidth - imageHeight)/2;
                paperY -= (imageWidth - imageHeight)/2;
            }

            // Trashcan check
            checkImageOverTrashcan(paperX, paperY, imageWidth, imageHeight);

            // Stop it being dragged off the edge of the page
            if (paperX < 0) {
                paperX = 0;
            }
            else if (paperX + imageWidth > paperWidth) {
                paperX = paperWidth - imageWidth;
            }
            if (paperY < 0) {
                paperY =  0;
            }
            else if (paperY + imageHeight >  paperHeight) {
                paperY = paperHeight - imageHeight;
            }
            
            // And perform the updatee
            image.transform('t' + paperX + ',' + paperY + 'r' + rotation + 's' + scaling);

            // Unmark the squares the light previously occupied
            if (sourceCoord) {
                markAsBackground(sourceCoord);
            }
            if (controlledCoord) {
                markAsBackground(controlledCoord);
            }
            if (originNode) {
                markAsOrigin(originNode.coordinate);
            }
            if (destinationNode) {
                markAsDestination(destinationNode.coordinate);
            }

            // Now calculate the source coordinate
            var box = image.getBBox();
            var absX = (box.x + box.width/2) / GRID_SPACE_SIZE;
            var absY = (box.y + box.height/2) / GRID_SPACE_SIZE;

            switch(rotation) {
                case 0:
                    absY += 0.5;
                    break;
                case 90:
                    absX -= 0.5;
                    break;
                case 180:
                    absY -= 0.5;
                    break;
                case 270:
                    absX += 0.5;
                    break;
            }

            var x = Math.min(Math.max(0, Math.floor(absX)), GRID_WIDTH - 1);
            var y = GRID_HEIGHT - Math.min(Math.max(0, Math.floor(absY)), GRID_HEIGHT - 1) - 1;
            sourceCoord = new ocargo.Coordinate(x,y);

            // Find controlled position in map coordinates
            switch(rotation) {
                case 0:
                    controlledCoord = new ocargo.Coordinate(sourceCoord.x, sourceCoord.y + 1);
                    break;
                case 90:
                    controlledCoord = new ocargo.Coordinate(sourceCoord.x + 1, sourceCoord.y);
                    break;
                case 180:
                    controlledCoord = new ocargo.Coordinate(sourceCoord.x, sourceCoord.y - 1);
                    break;
                case 270:
                    controlledCoord = new ocargo.Coordinate(sourceCoord.x - 1, sourceCoord.y);
                    break;
            }

            // If controlled node is not on grid, remove it
            if (!isCoordinateOnGrid(controlledCoord)) {
                controlledCoord = null;
            }

            // If source node is not on grid remove it
            if (!isCoordinateOnGrid(sourceCoord)) {
                sourceCoord = null;
            }

            if (sourceCoord && controlledCoord) {
                var colour;
                if(isValidPlacement(sourceCoord, controlledCoord)) {
                    colour = VALID_LIGHT_COLOUR;
                    ocargo.drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
                } 
                else {
                    colour = INVALID_LIGHT_COLOUR;
                }

                mark(controlledCoord, colour, 0.7, false);
                mark(sourceCoord, colour, 0.7, false);
            }

            // Deal with trashcan
            var paperAbsX = paperX - paper.scrollLeft() + imageWidth/2;
            var paperAbsY = paperY - paper.scrollTop() + imageHeight/2;
            var trashcanWidth = $('#trashcanHolder').width();
            var trashcanHeight = $('#trashcanHolder').height();

            if(paperAbsX > trashcanAbsolutePaperX && paperAbsX <= trashcanAbsolutePaperX + trashcanWidth  &&
                paperAbsY > trashcanAbsolutePaperY - 20 && paperAbsY <= trashcanAbsolutePaperY + trashcanHeight) {
                openTrashcan();
            }
            else {
                closeTrashcan();
            }
        }

        function onDragStart(x, y) {
            moved = false;

            scaling = getScaling(image);
            rotation = (image.matrix.split().rotate + 360) % 360;
            
            var bBox = image.getBBox();
            imageWidth = bBox.width;
            imageHeight = bBox.height;

            paperWidth = GRID_WIDTH * GRID_SPACE_SIZE;
            paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE;

            var paperPosition = paper.position();

            var mouseX = x - paperPosition.left;
            var mouseY = y - paperPosition.top;

            originX = mouseX + paper.scrollLeft()- imageWidth/2;
            originY = mouseY + paper.scrollTop() - imageHeight/2;
        }

        function onDragEnd() {
            // Unmark squares currently occupied
            if (sourceCoord) {
                markAsBackground(sourceCoord);
            }
            if (controlledCoord) {
                markAsBackground(controlledCoord);
            }
            if (originNode) {
                markAsOrigin(originNode.coordinate);
            }
            if (destinationNode) {
                markAsDestination(destinationNode.coordinate);
            }

            if(trashcanOpen) {
                trafficLight.destroy();
            }
            else if(isValidPlacement(sourceCoord, controlledCoord)) {
                // Add back to the list of traffic lights if on valid nodes
                trafficLight.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
                trafficLight.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);
                trafficLight.valid = true;

                ocargo.drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
            }

            image.attr({'cursor':'pointer'});
            closeTrashcan();
        }

        image.drag(onDragMove, onDragStart, onDragEnd);

        addReleaseListeners(image.node);
        
        var myLatestTap;
        $(image.node).on('click touchstart', function() {
           var now = new Date().getTime();
           var timesince = now - myLatestTap;

           if ((timesince < 300) && (timesince > 0)) {
                image.transform('...r90');
           }
           myLatestTap = new Date().getTime();
        });

        function getScaling(object) {
            var transform = object.transform();
            for (var i = 0; i < transform.length; i++) {
                if (transform[i][0] === 's') {
                    return transform[i][1] + ',' + transform[i][2];
                }
            }
            return "0,0";
        }

        function isValidPlacement(sourceCoord, controlledCoord) {
            var sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
            var controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);

            // Test if two connected nodes exist
            var connected = false;
            if (sourceNode && controlledNode) {
                for (var i = 0; i < sourceNode.connectedNodes.length; i++) {
                    if (sourceNode.connectedNodes[i] === controlledNode) {
                        connected = true;
                    }
                }
            }

            if(!connected) {
                return false;
            }

            // Test it's not already occupied
            for(var i = 0; i < trafficLights.length; i++) {
                var tl = trafficLights[i];
                if(tl.valid && 
                    ((tl.sourceNode === sourceNode && tl.controlledNode === controlledNode) ||
                    (tl.sourceNode === controlledNode && tl.controlledNode === sourceNode))) {
                    return false;
                }
            }
            
            return true;
        }

        function occupied(sourceCoord, controlledCoord) {
            
        }
    }

    /********************************/
    /* Miscaellaneous state methods */
    /********************************/

    function finaliseDelete(strikeEnd) {

        function deleteNode(x, y) {
            var coord = new ocargo.Coordinate(x, y);
            var node = ocargo.Node.findNodeByCoordinate(coord, nodes);
            if (node) {
                // Remove all the references to the node we're removing.
                for (var i = node.connectedNodes.length - 1; i >= 0; i--) {
                    node.removeDoublyConnectedNode(node.connectedNodes[i]);
                }
                nodes.splice(nodes.indexOf(node), 1);

                // Check if start or destination node        
                if (isOriginCoordinate(coord)) {
                    markAsBackground(originNode.coordinate);
                    originNode = null;
                }
                if (isDestinationCoordinate(coord)) {
                    markAsBackground(destinationNode.coordinate);
                    destinationNode = null;
                }

                //  Check if any traffic lights present
                for (var i = trafficLights.length-1; i >= 0;  i--) {
                    var trafficLight  =  trafficLights[i];
                    if (node === trafficLight.sourceNode || node === trafficLight.controlledNode) {
                        trafficLights.splice(i, 1);
                        trafficLight.destroy();
                    }
                }
            }
        }


        applyAlongStrike(deleteNode, strikeEnd);
        strikeStart = null;

        // Delete any nodes isolated through deletion
        for (var i = nodes.length - 1; i >= 0; i--) {
            if (nodes[i].connectedNodes.length === 0) {
                var coordinate = nodes[i].coordinate;
                deleteNode(coordinate.x, coordinate.y);
            }
        }
    }

    function finaliseMove(strikeEnd) {
        var previousNode = null;
        function addNode(x, y) {
            var coord = new ocargo.Coordinate(x,y);
            var node = ocargo.Node.findNodeByCoordinate(coord, nodes);
            if (!node) {
                node = new ocargo.Node(coord);
                nodes.push(node);
            }

            // Now connect it up with it's new neighbours
            if (previousNode && node.connectedNodes.indexOf(previousNode) === -1) {
                node.addConnectedNodeWithBacklink(previousNode);

                // If we've overwritten the origin node remove it as 
                // we can no longer place the CFC there
                if (node === originNode || previousNode == originNode) {
                    markAsBackground(originNode.coordinate);
                    originNode = null;
                }
            }
            previousNode = node;
        }


        if(strikeStart && !(strikeStart.x === strikeEnd.x && strikeStart.y === strikeEnd.y)) {
            applyAlongStrike(addNode, strikeEnd);
        }
        strikeStart = null;
    }

    function applyAlongStrike(func, strikeEnd) {
        var x, y;
        if (!strikeStart) {
            return;
        }

        if (strikeStart.x <= strikeEnd.x) {
            for (x = strikeStart.x; x <= strikeEnd.x; x++) {
                func(x, strikeStart.y);
            }
        } 
        else {
            for (x = strikeStart.x; x >= strikeEnd.x; x--) {
                func(x, strikeStart.y);
            }
        }

        if (strikeStart.y <= strikeEnd.y) {
            for (y = strikeStart.y + 1; y <= strikeEnd.y; y++) {
                func(strikeEnd.x, y);
            }
        } 
        else {
            for (y = strikeStart.y - 1; y >= strikeEnd.y; y--) {
                func(strikeEnd.x, y);
            }
        }    
    }

    function findTrafficLight(firstIndex, secondIndex) {
        var light;
        for (var i = 0; i < trafficLights.length; i++) {
            light = trafficLights[i];
            if (light.node === firstIndex && light.sourceNode === secondIndex) {
                return i;
            }
        }
        return -1;
    }

    function setTheme(theme) {
        currentTheme = theme;

        for (var x = 0; x < GRID_WIDTH; x++) {
            for (var y = 0; y < GRID_HEIGHT; y++) {
                grid[x][y].attr({stroke: theme.border});
            }
        }

        for (var i = 0; i < decor.length; i++) {
            decor[i].updateTheme();
        }

        $('.decor_button').each(function(index, element) {
            element.src = theme.decor[element.id].url;
        });

        $('#paper').css({'background-color': theme.background});
    }

    function sortNodes(nodes) {
        var sorter = function(a, b) {
            return comparator(a, b, nodes[i]);
        };
        for (var i = 0; i < nodes.length; i++) {
            // Remove duplicates.
            var newConnected = [];
            for (var j = 0; j < nodes[i].connectedNodes.length; j++) {
                if (newConnected.indexOf(nodes[i].connectedNodes[j]) === -1) {
                    newConnected.push(nodes[i].connectedNodes[j]);
                }
            }
            nodes[i].connectedNodes.sort(sorter).reverse();
        }

        function comparator(node1, node2, centralNode) {
            var a1 = ocargo.calculateNodeAngle(centralNode, node1);
            var a2 = ocargo.calculateNodeAngle(centralNode, node2);
            if (a1 < a2) {
                return -1;
            } else if (a1 > a2) {
                return 1;
            } else {
                return 0;
            }
        }
    }

    /**********************************/
    /* Loading/saving/sharing methods */
    /**********************************/

    function extractState() {
        var state = {};

        // Create node data
        sortNodes(nodes);
        state.path = JSON.stringify(ocargo.Node.composePathData(nodes));

        // Create traffic light data
        var trafficLightData = [];
        var i;
        for (i = 0; i < trafficLights.length; i++) {
            var tl =  trafficLights[i];
            if (tl.valid) {
                trafficLightData.push(tl.getData());
            }
        }
        state.traffic_lights = JSON.stringify(trafficLightData);

        // Create block data
        state.blocks = [];
        for (i = 0; i < BLOCKS.length; i++) {
            var type = BLOCKS[i];
            if ($('#' + type + "_checkbox").is(':checked')) {
                var block = {'type': type}
                var number = $('#' + type + "_number").val();
                if(number !== "infinity") {
                    block.number = parseInt(number);
                }

                state.blocks.push(block);
            }
        }

        // Create decor data
        state.decor = [];
        for (i = 0; i < decor.length; i++) {
            state.decor.push(decor[i].getData());
        }

        // Destination and origin data
        if (destinationNode) {
            var destinationCoord = destinationNode.coordinate;
            state.destinations = JSON.stringify([[destinationCoord.x, destinationCoord.y]]);
        }
        if (originNode) {
            var originCoord = originNode.coordinate;
            var nextCoord = originNode.connectedNodes[0].coordinate;
            var direction = originCoord.getDirectionTo(nextCoord);
            state.origin = JSON.stringify({coordinate: [originCoord.x, originCoord.y], direction: direction});
        }

        // Other data
        var maxFuel = $('#max_fuel').val();
        if(isNaN(maxFuel) ||  maxFuel ===  '' || parseInt(maxFuel) <= 0 || parseInt(maxFuel) > 99)
        {
            maxFuel = 50;
            $('#max_fuel').val(50);
        }
        state.max_fuel = maxFuel;
        
        state.theme = currentTheme.id;
        state.character_name = CHARACTER_NAME;

        state.blocklyEnabled = true;
        state.pythonEnabled = false;

        return state;
    }

    function restoreState(state) {
        clear();

        // Load node data
        nodes = ocargo.Node.parsePathData(JSON.parse(state.path));

        // Load traffic light data
        var trafficLightData = JSON.parse(state.traffic_lights);
        for (var i = 0; i < trafficLightData.length; i++) {
            new InternalTrafficLight(trafficLightData[i]);
        }

        // Load in destination and origin nodes
        // TODO needs to be fixed in the long term with multiple destinations
        if (state.destinations) {
            var destination = JSON.parse(state.destinations)[0];
            var destinationCoordinate = new ocargo.Coordinate(destination[0], destination[1]);
            destinationNode = ocargo.Node.findNodeByCoordinate(destinationCoordinate, nodes);
        }

        if (state.origin) {
            var origin = JSON.parse(state.origin);
            var originCoordinate = new ocargo.Coordinate(origin.coordinate[0], origin.coordinate[1]);
            originNode = ocargo.Node.findNodeByCoordinate(originCoordinate, nodes);
        }
        
        drawAll();

        // Set the theme
        var themeFound = false;
        var themeID = state.theme;
        for (var themeName in THEMES) {
            var theme = THEMES[themeName];
            if (theme.id === themeID) {
                setTheme(theme);
                themeFound = true;
                $('#theme_select').val(themeName);
                break;
            }
        }
        if(!themeFound) {
            setTheme(THEMES.grass);
        }

        // Load in the decor data
        var decor = state.decor;
        for (var i = 0; i < decor.length; i++) {
            var decorObject = new InternalDecor(decor[i].decorName);
            decorObject.setPosition(decor[i].x, 
                                    PAPER_HEIGHT - currentTheme.decor[decor[i].decorName].height - decor[i].y);
        }

        // Load in block data
        if(state.blocks) {
            for(var i = 0; i < BLOCKS.length; i++) {
                var type = BLOCKS[i];
                $('#' + type + '_checkbox').prop('checked', false);
                $('#' + type + '_number').val('infinity');
            }
            var blocks = state.blocks;
            for(var i = 0; i < blocks.length; i++) {
                var type = blocks[i].type;
                $('#' + type + '_checkbox').prop('checked', true);
                if(blocks[i].number) {
                    $('#' + type + '_number').val(blocks[i].number);
                }
            }
        }
        

        // Other data
        if(state.max_fuel) {
            $('#max_fuel').val(state.max_fuel);
        }
    }

    function loadLevel(levelID) { 
        ocargo.saving.retrieveLevel(levelID, function(err, level, owned) {
            if (err !== null) {
                console.error(err);
                return;
            }

            restoreState(level, true);

            ownsSavedLevel = owned;
            savedState = JSON.stringify(extractState());
            savedLevelID = level.id;
        });
    }

    function saveLevel(name, levelID, callback) {
        var level = extractState();
        level.name = name;

        ocargo.saving.saveLevel(level, levelID, false, function(error, newLevelID, ownedLevels, sharedLevels) {
            if (error !== null) {
                console.error(error);
                return;
            }

            // Delete name so that we can use if for comparison purposes
            // to see if changes have been made to the level later on
            delete level.name;
            ownsSavedLevel = true;
            savedState = JSON.stringify(level);
            savedLevelID = newLevelID;

            callback(null, ownedLevels, sharedLevels);
        });
    }

    function storeStateInLocalStorage() {
        if (localStorage) {
            var state = extractState();
            
            // Append additional non-level orientated editor state
            state.savedLevelID = savedLevelID;
            state.savedState = savedState;
            state.ownsSavedLevel = ownsSavedLevel;

            localStorage.levelEditorState = JSON.stringify(state);
        }
    }

    function retrieveStateFromLocalStorage() { 
        if (localStorage) {
            if (localStorage.levelEditorState) {
                var state = JSON.parse(localStorage.levelEditorState);
                if (state) {
                    restoreState(state);
                }

                // Restore additional non-level orientated editor state
                savedLevelID = state.savedLevelID;
                savedState = state.savedState;
                ownsSavedLevel = state.ownsSavedLevel;
            }

        }
    }

    function isLevelValid() {
        // Check to see if start and end nodes have been marked
        if (!originNode || !destinationNode) {
             ocargo.Drawing.startPopup(ocargo.messages.ohNo,
                                       ocargo.messages.noStartOrEndSubtitle,
                                       ocargo.messages.noStartOrEnd + ocargo.jsElements.closebutton("Close"));
             return false;
        }

        // Check to see if path exists from start to end
        var destination = new ocargo.Destination(0, destinationNode);
        var pathToDestination = getOptimalPath(nodes, [destination]);
        if (!pathToDestination) {
            ocargo.Drawing.startPopup(ocargo.messages.somethingWrong,
                                      ocargo.messages.noStartEndRouteSubtitle,
                                      ocargo.messages.noStartEndRoute + ocargo.jsElements.closebutton("Close"));
            return false;
        }

        // Check to see if at least one block selected
        // (not perfect but ensures that they don't think the blockly toolbar is broken)
        if($(".block_checkbox:checked").length == 0) {
            ocargo.Drawing.startPopup(ocargo.messages.somethingWrong,
                                      ocargo.messages.noBlocksSubtitle,
                                      ocargo.messages.noBlocks + ocargo.jsElements.closebutton("Close"));
            return false;
        }

        return true;
    }

    function isLevelSaved() {
        var currentState = JSON.stringify(extractState());

        if (!savedState) {
            ocargo.Drawing.startPopup("Sharing", "", ocargo.messages.notSaved + ocargo.jsElements.closebutton("Close"));
            return false;
        }
        else if (currentState !== savedState) {
            ocargo.Drawing.startPopup("Sharing", "", ocargo.messages.changesSinceLastSave + ocargo.jsElements.closebutton("Close"));
            return false;
        }
        return true;
    }

    function isLevelOwned() {
        if (!ownsSavedLevel)
        {
            ocargo.Drawing.startPopup("Sharing", "", ocargo.messages.notOwned);
            return false;
        }
        return true;
    }

    function isLoggedIn(activity) {
        if (USER_STATUS !== "SCHOOL_STUDENT" && USER_STATUS !== "TEACHER" && USER_STATUS !== "SOLO_STUDENT") {
            ocargo.Drawing.startPopup("Not logged in", 
                                      "", 
                                      ocargo.messages.notLoggedIn(activity) + ocargo.jsElements.closebutton("Close"));
            return false;
        }
        return true;
    }

    function isSoloStudent() {
        if (USER_STATUS === "SOLO_STUDENT") {
            ocargo.Drawing.startPopup("Sharing as an independent student", 
                                      "", 
                                      ocargo.messages.soloSharing + ocargo.jsElements.closebutton("Close"));
            return false;
        }
        return true;
    }

    /*****************************************/
    /* Internal traffic light representation */
    /*****************************************/

    function InternalTrafficLight(data) {

        // public methods
        this.getData = function() {
            if (!this.valid) {
                throw "Error: cannot create actual traffic light from invalid internal traffic light!";
            }

            var sourceCoord = this.sourceNode.coordinate;
            var sourceCoordinate = {'x':sourceCoord.x, 'y':sourceCoord.y};
            var direction = sourceCoord.getDirectionTo(this.controlledNode.coordinate);

            return {"redDuration": this.redDuration, "greenDuration": this.greenDuration,
                    "sourceCoordinate": sourceCoordinate, "direction": direction,
                    "startTime": this.startTime, "startingState": this.startingState};
        };

        this.destroy = function() {
            this.image.remove();
            var index = trafficLights.indexOf(this);
            if (index !== -1) {
                trafficLights.splice(index, 1);       
            }
        };

        // data
        this.redDuration = data.redDuration;
        this.greenDuration = data.greenDuration;
        this.startTime = data.startTime;
        this.startingState = data.startingState;

        var imgStr = this.startingState === ocargo.TrafficLight.RED ? LIGHT_RED_URL : LIGHT_GREEN_URL;
        this.image = ocargo.drawing.createTrafficLightImage(imgStr);
        this.image.transform('...s-1,1');

        this.valid = false;

        if (data.sourceCoordinate && data.direction) {
            var sourceCoordinate = new ocargo.Coordinate(data.sourceCoordinate.x, data.sourceCoordinate.y);
            var controlledCoordinate = sourceCoordinate.getNextInDirection(data.direction);

            this.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoordinate, nodes);
            this.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoordinate, nodes);

            if (this.controlledNode && this.sourceNode) {
                this.valid = true;
                ocargo.drawing.setTrafficLightImagePosition(this.sourceNode.coordinate, this.controlledNode.coordinate, this.image);
            }
        }
        else {
            this.image.transform('...t' + (-paper.scrollLeft())  +  ',' +  paper.scrollTop());
        }

        setupTrafficLightListeners(this);
        this.image.attr({'cursor':'pointer'});

        trafficLights.push(this);
    }

    /*********************************/
    /* Internal decor representation */
    /*********************************/

    function InternalDecor(decorName) {

        // public methods
        this.getData = function() {
            var bBox = this.image.getBBox();
            var data =  {
                            'x': Math.floor(bBox.x),
                            'y': PAPER_HEIGHT - bBox.height - Math.floor(bBox.y),
                            'decorName': this.decorName
                        };
            return data;
        };

        this.setPosition = function(x, y) {
            this.image.transform('t' + x + ',' + y);
        };

        this.updateTheme = function() {
            var description = currentTheme.decor[this.decorName];
            var newImage = ocargo.drawing.createImage(description.url, 0, 0, description.width,
                                                      description.height);

            if (this.image) {
                newImage.transform(this.image.matrix.toTransformString());
                this.image.remove();
            }

            this.image = newImage;
            this.image.attr({'cursor':'pointer'});
            setupDecorListeners(this);
        };

        this.destroy = function() {
            this.image.remove();
            var index = decor.indexOf(this);
            if (index !== -1) {
                decor.splice(index, 1);       
            }
        };

        // data
        this.decorName = decorName;
        this.image = null;

        // setup
        this.updateTheme();
        this.setPosition(paper.scrollLeft(), paper.scrollTop());

        decor.push(this);
    }
};

/******************/
/* Initialisation */
/******************/

$(function() {
    new ocargo.LevelEditor();
    ocargo.Drawing.startPopup(ocargo.messages.levelEditorTitle, ocargo.messages.levelEditorSubtitle + ocargo.jsElements.closebutton("Close"));
});
