'use strict';

var ocargo = ocargo || {};

ocargo.LevelEditor = function() {
    
    /*************/
    /* Constants */
    /*************/

    var LIGHT_RED_URL = '/static/game/image/trafficLight_red.svg';
    var LIGHT_GREEN_URL = '/static/game/image/trafficLight_green.svg';
    
    var DELETE_DECOR_IMG_URL = "/static/game/image/icons/delete_decor.svg";
    var ADD_ROAD_IMG_URL = "/static/game/image/icons/add_road.svg";
    var DELETE_ROAD_IMG_URL = "/static/game/image/icons/delete_road.svg";
    var MARK_START_IMG_URL = "/static/game/image/icons/origin.svg";
    var MARK_END_IMG_URL = "/static/game/image/icons/destination.svg";

    var VALID_LIGHT_COLOUR = '#87E34D';
    var INVALID_LIGHT_COLOUR = '#E35F4D';

    var IS_SCROLLING = false;

    var paper = $('#paper'); // May as well cache this

    var modes = {
        ADD_ROAD_MODE: {name: 'Add Road', url: "/static/game/image/icons/add_road.svg"},
        DELETE_ROAD_MODE: {name: 'Delete Road', url: "/static/game/image/icons/delete_road.svg"},
        MARK_DESTINATION_MODE: {name: 'Mark end', url: "/static/game/image/icons/destination.svg"},
        MARK_ORIGIN_MODE: {name: 'Mark start', url: "/static/game/image/icons/origin.svg"},
        DELETE_DECOR_MODE: {name: 'Delete decor', url: "/static/game/image/icons/delete_decor.svg"}
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

    // So that we store the current state when the page unloads
    window.addEventListener('unload', storeStateInLocalStorage);

    // Initialise the grid
    initialiseGrid();

    // Setup the toolbox
    setupToolbox();

    // If there's any previous state in local storage retrieve it
    retrieveStateFromLocalStorage();

    // Draw everything
    drawAll();

    // Set the default theme
    setTheme(THEMES.grass);



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
            IS_SCROLLING = true;
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
            IS_SCROLLING = false;
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
                            console.debug(error)
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
            $('#currentToolImg').attr("src", mode.url);            
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
                    ocargo.Drawing.startPopup('', '', ocargo.messages.trafficLightsWarning);
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

            $('#delete_decor').click(function() {
                if (mode === modes.DELETE_DECOR_MODE) {
                    document.getElementById('delete_caption').style.visibility='hidden';
                    mode = prevMode;
                    prevMode = null;
                    changeCurrentToolDisplay(mode);
                } else {
                    document.getElementById('delete_caption').style.visibility='visible';
                    prevMode = mode;
                    mode = modes.DELETE_DECOR_MODE;
                    changeCurrentToolDisplay(modes.DELETE_DECOR_MODE);
                }
            });
        }

        function setupCharacterTab() {
            tabs.character.setOnChange(function() {
                transitionTab(tabs.character);
            });

            $('#Van_radio').prop("checked", true);
            $("#character-form").on('change', ':input', function() { 
                CHARACTER_NAME = $('input:checked', '#character-form').val();
                redrawRoad();
            });
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
                var data = {numberOfTiles: $('#size').val(),
                            branchiness: $('#branchiness').val()/10,
                            loopiness: $('#loopiness').val()/10,
                            curviness: $('#curviness').val()/10,
                            trafficLightsEnabled: $('#trafficLightsEnabled').val() == "yes",
                            csrfmiddlewaretoken: $.cookie('csrftoken')};
                
                ocargo.saving.retrieveRandomLevel(data, function(error, mapData) {
                    if (error) {
                        console.debug(error);
                        ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown);
                        return;
                    }

                    clear();

                    var path = JSON.parse(mapData.path);
                    var i;
                    for (i = 0; i < path.length; i++) {
                        var node = new ocargo.Node(new ocargo.Coordinate(path[i].coordinate[0],
                                                   path[i].coordinate[1]));
                        nodes.push(node);
                    }

                    for (i = 0; i < path.length; i++) {
                        nodes[i].connectedNodes = [];
                        for (var j = 0; j < path[i].connectedNodes.length; j++) {
                            nodes[i].connectedNodes.push(nodes[path[i].connectedNodes[j]]);
                        }
                    }

                    // TODO add in support for multiple destinations
                    var destination = JSON.parse(mapData.destinations)[0];
                    var destinationCoord = new ocargo.Coordinate(destination[0], destination[1]);
                    destinationNode = ocargo.Node.findNodeByCoordinate(destinationCoord, nodes);
                    originNode = nodes[0];

                    var tls = JSON.parse(mapData.traffic_lights);
                    for (i = 0; i < tls.length; i++) {
                        new InternalTrafficLight(tls[i]);
                    }

                    drawAll();
                });
            });
        }

        function setupLoadTab() {
            var selectedLevel = null;

            tabs.load.setOnChange(function() {
                ocargo.saving.retrieveListOfLevels(function(err, ownLevels, sharedLevels) {
                    if (err !== null) {
                        console.debug(err);
                        currentTabSelected.select();
                        ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown);
                        return;
                    }

                    populateLoadSaveTable("loadOwnLevelTable", ownLevels);

                    // Add click listeners to all rows
                    $('#loadOwnLevelTable tr[value]').on('click', function(event) {
                        $('#loadOwnLevelTable tr').css('background-color', '#FFFFFF');
                        $('#loadSharedLevelTable tr').css('background-color', '#FFFFFF');
                        $(this).css('background-color', '#C0C0C0');
                        $('#loadLevel').removeAttr('disabled');
                        $('#deleteLevel').removeAttr('disabled');
                        selectedLevel = $(this).attr('value');
                    });

                    populateLoadSaveTable("loadSharedLevelTable", sharedLevels);

                    // Add click listeners to all rows
                    $('#loadSharedLevelTable tr[value]').on('click', function(event) {
                        $('#loadOwnLevelTable tr').css('background-color', '#FFFFFF');
                        $('#loadSharedLevelTable tr').css('background-color', '#FFFFFF');
                        $(this).css('background-color', '#C0C0C0');
                        $('#loadLevel').removeAttr('disabled');
                        $('#deleteLevel').removeAttr('disabled');
                        selectedLevel = $(this).attr('value');
                    });

                    // But disable all the modal buttons as nothing is selected yet
                    selectedLevel = null;
                    $('#loadLevel').attr('disabled', 'disabled');
                    $('#deleteLevel').attr('disabled', 'disabled');


                    transitionTab(tabs.load);
                });
            });

            // Setup own/shared levels radio
            $('#own_levels_radio').change(function() {
                $('#loadOwnLevelTable').css('display','table');
                $('#loadSharedLevelTable').css('display','none');

                if (selectedLevel) {
                    $('#deleteLevel').attr('disabled', false);
                }
            });
            $('#shared_levels_radio').change(function() {
                $('#loadOwnLevelTable').css('display','none');
                $('#loadSharedLevelTable').css('display','table');

                $('#deleteLevel').attr('disabled', true);
            });
            $('#own_levels_radio').change();

            $('#loadLevel').click(function() {
                if (selectedLevel) {
                    loadLevel(selectedLevel); 
                }
            });

            $('#deleteLevel').click(function() {
                if (!selectedLevel) {
                    return;
                }

                ocargo.saving.deleteLevel(selectedLevel, function(err) {
                    if (err !== null) {
                        console.debug(err);
                        return;
                    }

                    if (selectedLevel == savedLevelID) {
                        savedLevelID = -1;
                        savedState = null;
                        ownsSavedLevel = false;
                    }

                    $('#loadOwnLevelTable tr[value=' + selectedLevel + ']').remove();
                    selectedLevel = null;
                });
            });
        }

        function setupSaveTab() {
            var selectedLevel = null;

            tabs.save.setOnChange(function () {
                if (!isLevelValid()) {
                    currentTabSelected.select();
                    return;
                }

                ocargo.saving.retrieveListOfLevels(processListOfLevels);
            });
            
            $('#saveLevel').click(function() {
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
                        //ocargo.Drawing.startPopup("Overwriting","Warning",ocargo.messages.saveOverwriteWarning(newName, onYes));
                        saveLevel(newName, existingID, processListOfLevels);
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
                    console.debug(err);
                    ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown);
                    return;
                }

                populateLoadSaveTable("saveLevelTable", ownLevels);

                // Add click listeners to all rows
                $('#saveLevelTable tr').on('click', function(event) {
                    var rowSelected = $(event.target.parentElement);
                    $('#saveLevelTable tr').css('background-color', '#FFFFFF');
                    rowSelected.css('background-color', '#C0C0C0');
                    $('#saveLevel').removeAttr('disabled');
                    selectedLevel = parseInt(rowSelected.attr('value'));

                    for (var i = 0; i < ownLevels.length; i++) {
                        if (ownLevels[i].id === selectedLevel) {
                            $("#levelNameInput").val(ownLevels[i].name);
                        }
                    }
                });

                transitionTab(tabs.save);
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
                if (!isLevelSaved() || !isLevelOwned()) {
                    currentTabSelected.select();
                    return;
                }
                
                ocargo.saving.getSharingInformation(savedLevelID, processSharingInformation);
            });

            var classesTaught;
            var fellowTeachers;
            var currentClassID;
            var allShared;

            // Setup the teachers/classes radio buttons for the teacher panel
            $('#classes_radio').change(function() {
                $('#class_selection').css('display','block');
                $('#class_select').val(currentClassID);
                $('#class_select').change();
            });
            $('#teachers_radio').change(function() {
                $('#class_selection').css('display','none');
                populateSharingTable(fellowTeachers);
            });
            $('#classes_radio').change();

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
                if (isLevelSaved() && isLevelOwned()) {
                    var statusDesired = allShared ? 'shared' : 'unshared';
                    var actionDesired = allShared ? 'unshare' : 'share';

                    var recipientIDs = [];
                    $('#levelSharingTable tr[value]').each(function() {
                        recipientIDs.push(this.getAttribute('value'));
                    });

                    var recipientData = {recipientIDs: recipientIDs, 
                                         action: actionDesired};

                    ocargo.saving.shareLevel(savedLevelID, recipientData, processSharingInformation);
                }
            });

            // Method to call when we get an update on the level's sharing information
            function processSharingInformation(error, validRecipients, role) {
                if (error !== null) {
                    console.debug(error);
                    ocargo.Drawing.startPopup("Error","",ocargo.messages.internetDown);
                    return;
                }

                if (role !== "student" && role !== 'teacher') {
                    ocargo.Drawing.startPopup("Not logged in", "", ocargo.messages.notLoggedIn);
                    currentTabSelected.select();
                    return;
                }

                if (role === "student") {
                    $('#teacher_sharing').css('display','none');
                    $('#student_sharing').css('display','block');

                    var classmates = validRecipients.classmates;
                    var teacher = validRecipients.teacher;

                    populateSharingTable(classmates);
                }
                else if (role == "teacher") {
                    $('#teacher_sharing').css('display','block');
                    $('#student_sharing').css('display','none');

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

                    if ($('#teachers_radio').is(':checked')) {
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

                transitionTab(tabs.share);
            }

            function populateSharingTable(recipients) {
                // Remove click listeners to avoid memory leak and remove all rows
                var table = $('#levelSharingTable');
                $('#levelSharingTable tr').off('click');
                table.empty();

                table.append('<tr>  <th>Name</th>  <th>Shared</th> </tr>');
                
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
                    $('#shareWithAll img').attr('src','/static/game/image/icons/quit.svg');
                }
                else {
                    $('#shareWithAll span').html('Share with all');
                    $('#shareWithAll img').attr('src','/static/game/image/icons/share.svg');
                }

                // update click listeners in the new rows
                $('#levelSharingTable tr[value]').on('click', function(event) {
                    if (isLevelSaved() && isLevelOwned()) {
                        var status = this.getAttribute('status');

                        var recipientData = {recipientIDs: [this.getAttribute('value')], 
                                             action: (status === 'shared' ? 'unshare' : 'share')};

                        ocargo.saving.shareLevel(savedLevelID, recipientData, processSharingInformation);
                    }
                });
            }
        }

        function setupHelpTab() {
            var message = ocargo.Drawing.isMobile() ? ocargo.messages.levelEditorMobileSubtitle :
                ocargo.messages.levelEditorPCSubtitle;

            message += "<br><br>" + ocargo.messages.levelEditorHelpText;

            tabs.help.setOnChange(function() {
                currentTabSelected.select();
                ocargo.Drawing.startPopup('', '', message);
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
            var table = $('#'+tableName);

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
            table.append('<tr>  <th>Name</th>   <th>Owner</th> </tr>');
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
        }
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

    function handleTouchStart(this_rect) {
        return function (ev) {
            if (ev.touches.length === 1 && !IS_SCROLLING) {
                var paperPosition = paper.position();
                var x = ev.touches[0].pageX - paperPosition.left + paper.scrollLeft();
                var y = ev.touches[0].pageY - paperPosition.top + paper.scrollTop();

                x /= GRID_SPACE_SIZE;
                y /= GRID_SPACE_SIZE;

                x = Math.min(Math.max(0, Math.floor(x)), GRID_WIDTH - 1);
                y = Math.min(Math.max(0, Math.floor(y)), GRID_HEIGHT - 1);

                handleMouseDown(grid[x][y])(ev);
            }
        };
    }

    function handleTouchMove(this_rect) {
        return function(ev) {
            if (ev.touches.length === 1 && !IS_SCROLLING) {
                var paperPosition = paper.position();
                var x = ev.touches[0].pageX - paperPosition.left + paper.scrollLeft();
                var y = ev.touches[0].pageY - paperPosition.top + paper.scrollTop();

                x /= GRID_SPACE_SIZE;
                y /= GRID_SPACE_SIZE;

                x = Math.min(Math.max(0, Math.floor(x)), GRID_WIDTH - 1);
                y = Math.min(Math.max(0, Math.floor(y)), GRID_HEIGHT - 1);

                handleMouseOver(grid[x][y])(ev);
            }
        };
    }

    function handleTouchEnd(this_rect) {
        return function(ev) {
            if (ev.changedTouches.length === 1 && !IS_SCROLLING) {
                var paperPosition = paper.position();
                var x = ev.changedTouches[0].pageX - paperPosition.left + paper.scrollLeft();
                var y = ev.changedTouches[0].pageY - paperPosition.top + paper.scrollTop();

                x /= GRID_SPACE_SIZE;
                y /= GRID_SPACE_SIZE;

                x = Math.min(Math.max(0, Math.floor(x)), GRID_WIDTH - 1);
                y = Math.min(Math.max(0, Math.floor(y)), GRID_HEIGHT - 1);

                handleMouseUp(grid[x][y])(ev);
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
            if (mode !== modes.DELETE_DECOR_MODE) {
                paperX = dx + originX;
                paperY = dy + originY;

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

                image.transform('t' + paperX + ',' + paperY);
            }
        }

        function onDragStart(x, y) {
            if (mode !== modes.DELETE_DECOR_MODE) {
                var bBox = image.getBBox();
                imageWidth = bBox.width;
                imageHeight = bBox.height;

                var paperPosition = paper.position();
                originX = x - paperPosition.left + paper.scrollLeft() - imageWidth/2;
                originY = y - paperPosition.top + paper.scrollTop() - imageHeight/2;

                paperWidth = GRID_WIDTH * GRID_SPACE_SIZE;
                paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE;
            }
        }

        function onDragEnd() {
            if (mode !== modes.DELETE_DECOR_MODE) {
                originX = paperX;
                originY = paperY;
            }
        }

        image.drag(onDragMove, onDragStart, onDragEnd);

        $(image.node).on('click touchstart', function() {
            if (mode === modes.DELETE_DECOR_MODE) {
                decor.destroy();
            }
        });
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
            // Needs to be in onDragMove, not in onDragStart, to stop clicks triggering drag behaviour
            trafficLight.valid = false;
            image.attr({'cursor':'default'});
            moved = dx !== 0 || dy !== 0;

            // Update image's position
            paperX = dx + originX;
            paperY = dy + originY;

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
            
            // Adjust for the fact that we've rotated the image
            if (rotation === 90 || rotation === 270)  {
                paperX += (imageWidth - imageHeight)/2;
                paperY -= (imageWidth - imageHeight)/2;
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
                if (canGetFromSourceToControlled(sourceCoord, controlledCoord)) {
                    // Valid placement
                    colour = VALID_LIGHT_COLOUR;
                    ocargo.drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
                } else {
                    // Invalid placement
                    colour = INVALID_LIGHT_COLOUR;
                }

                mark(controlledCoord, colour, 0.7, false);
                mark(sourceCoord, colour, 0.7, false);
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

            originX = mouseX - imageWidth/2;
            originY = mouseY - imageHeight/2;
        }

        function onDragEnd() {
            if (moved) {
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

                // Add back to the list of traffic lights if on valid nodes
                if (canGetFromSourceToControlled(sourceCoord, controlledCoord)) {
                    trafficLight.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
                    trafficLight.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);
                    trafficLight.valid = true;

                    ocargo.drawing.setTrafficLightImagePosition(trafficLight.sourceNode.coordinate,
                                                                trafficLight.controlledNode.coordinate,
                                                                image);
                }
            }

            image.attr({'cursor':'pointer'});
        }

        image.drag(onDragMove, onDragStart, onDragEnd);
        
        image.dblclick(function() {
            image.transform('...r90');
        });

        image.click(function() {
            if (mode === modes.DELETE_DECOR_MODE) {
                trafficLight.destroy();
            }
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

        function canGetFromSourceToControlled(sourceCoord, controlledCoord) {
            var sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
            var controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);

            if (sourceNode && controlledNode) {
                for (var i = 0; i < sourceNode.connectedNodes.length; i++) {
                    if (sourceNode.connectedNodes[i] === controlledNode) {
                        return true;
                    }
                }
            }
            return false;
        }
    }

    /********************************/
    /* Miscaellaneous state methods */
    /********************************/

    function finaliseDelete(strikeEnd) {
        
        applyAlongStrike(deleteNode, strikeEnd);
        strikeStart = null;

        // Delete any nodes isolated through deletion
        for (var i = nodes.length - 1; i >= 0; i--) {
            if (nodes[i].connectedNodes.length === 0) {
                var coordinate = nodes[i].coordinate;
                deleteNode(coordinate.x, coordinate.y);
            }
        }
        
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
    }

    function finaliseMove(strikeEnd) {

        applyAlongStrike(addNode, strikeEnd);
        strikeStart =  null;

        var previousNode = null;
        function addNode(x, y) {
            var coord = new ocargo.Coordinate(x,y);
            var node = ocargo.Node.findNodeByCoordinate(coord, nodes);
            if (!node) {
                node = new ocargo.Node(coord);
                nodes.push(node);
            }
            else {
                // If we've overwritten the origin node remove it as 
                // we can no longer place the CFC there
                if (node === originNode) {
                    markAsBackground(originNode.coordinate);
                    originNode = null;
                }
            }

            // Now connect it up with it's new neighbours
            if (previousNode && node.connectedNodes.indexOf(previousNode) === -1) {
                node.addConnectedNodeWithBacklink(previousNode);
            }
            previousNode = node;
        }
    }

    function applyAlongStrike(func, strikeEnd) {
        var x, y;
        if (!strikeStart || strikeStart.x === strikeEnd.x && strikeStart.y === strikeEnd.y) {
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

        $('#wrapper').css({'background-color': theme.background});
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
        var blockData = [];
        for (i = 0; i < BLOCKS.length; i++) {
            var type = BLOCKS[i];
            if ($('#' + type + "_checkbox").is(':checked')) {
                blockData.push(type);
            }
        }
        state.block_types = JSON.stringify(blockData);

        // Create decor data
        var decorData = [];
        for (i = 0; i < decor.length; i++) {
            decorData.push(decor[i].getData());
        }
        state.decor = JSON.stringify(decorData);

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
        state.max_fuel = $('#max_fuel').val();
        
        state.themeID = currentTheme.id;
        state.character_name = CHARACTER_NAME;

        return state;
    }

    function restoreState(state, origin) {
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
        var themeID = state.themeID;
        for (var theme in THEMES) {
            if (THEMES[theme].id === themeID) {
                setTheme(THEMES[theme]);
            }
        }

        // Load in the decor data
        var decorData = JSON.parse(state.decor);
        for (var i = 0; i < decorData.length; i++) {
            var decorObject = new InternalDecor(decorData[i].name);
            decorObject.setCoordinate(new ocargo.Coordinate(decorData[i].coordinate.x,
                PAPER_HEIGHT - decorData[i].height - decorData[i].coordinate.y));
        }
    }

    function loadLevel(levelID) { 
        ocargo.saving.retrieveLevel(levelID, function(err, level, owned) {
            if (err !== null) {
                console.debug(err);
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
                console.debug(error);
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
                                       ocargo.messages.noStartOrEnd);
             return false;
        }

        // Check to see if path exists from start to end
        var destination = new ocargo.Destination(0, destinationNode);
        var pathToDestination = getOptimalPath(nodes, [destination]);
        if (!pathToDestination) {
            ocargo.Drawing.startPopup(ocargo.messages.somethingWrong,
                                      ocargo.messages.noStartEndRouteSubtitle,
                                      ocargo.messages.noStartEndRoute);
            return false;
        }
        return true;
    }

    function isLevelSaved() {
        var currentState = JSON.stringify(extractState());

        if (!savedState) {
            ocargo.Drawing.startPopup("Sharing", "", ocargo.messages.notSaved);
            return false;
        }
        else if (currentState !== savedState) {
            ocargo.Drawing.startPopup("Sharing", "", ocargo.messages.changesSinceLastSave);
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

        setupTrafficLightListeners(this);
        this.image.attr({'cursor':'pointer'});

        trafficLights.push(this);
    }

    /*********************************/
    /* Internal decor representation */
    /*********************************/

    function InternalDecor(name) {

        // public methods
        this.getData = function() {
            var bBox = this.image.getBBox();
            return {'coordinate': new ocargo.Coordinate(Math.floor(bBox.x),
                                                        PAPER_HEIGHT - bBox.height - Math.floor(bBox.y)),
                    'name': this.name, 'height': bBox.height};
        };

        this.setCoordinate = function(coordinate) {
            this.image.transform('t' + coordinate.x + ',' + coordinate.y);
        };

        this.updateTheme = function() {
            var description = currentTheme.decor[this.name];
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
        this.name = name;
        this.image = null;
        this.updateTheme();

        decor.push(this);
    }
};

/******************/
/* Initialisation */
/******************/

$(function() {
    new ocargo.LevelEditor();
    ocargo.Drawing.startPopup(ocargo.messages.levelEditorTitle, ocargo.messages.levelEditorSubtitle);
});
