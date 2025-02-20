'use strict';

var ocargo = ocargo || {};

ocargo.LevelEditor = function(levelId) {

    /*************/
    /* Constants */
    /*************/

    const TAB_PANE_WIDTH = 500;

    var LIGHT_RED_URL = ocargo.Drawing.raphaelImageDir + 'trafficLight_red.svg';
    var LIGHT_GREEN_URL = ocargo.Drawing.raphaelImageDir + 'trafficLight_green.svg';

    var COW_GROUP_COLOR_PALETTE = [
        // From https://en.wikipedia.org/wiki/Help:Distinguishable_colors
        '#FFFFFF', // White
        '#FFA405', // Orpiment
        '#0075DC', // Blue
        '#C20088', // Mallow
        '#9DCC00', // Lime
        '#FF5005', // Zinnia
        '#808080', // Iron
        '#F0A3FF', // Amethyst
        '#993F00', // Caramel
        '#740AFF', // Violet
        '#FFFF00', // Wine
        '#4C005C', // Damson
        '#94FFB5', // Jade
        '#FFCC99', // Honeydew
        '#00998F', // Turqoise
        '#E0FF66', // Uranium
        '#005C31', // Forest
        '#FFFF80', // Xanthin
        '#5EF1F2', // Sky
        '#003380', // Navy
        '#8F7C00'  // Khaki
    ];

    var VALID_LIGHT_COLOUR = '#87E34D';
    var INVALID_LIGHT_COLOUR = '#E35F4D';

    var paper = $('#paper'); // May as well cache this

    var modes = {
        ADD_ROAD_MODE: {
            name: gettext('Add road'),
            url: ocargo.Drawing.imageDir + 'icons/add_road.svg',
            id: 'add_road',
        },
        DELETE_ROAD_MODE: {
            name: gettext('Delete road'),
            url: ocargo.Drawing.imageDir + 'icons/delete_road.svg',
            id: 'delete_road',
        },
        MARK_ORIGIN_MODE: {
            name: gettext('Mark start'),
            url: ocargo.Drawing.imageDir + 'icons/origin.svg',
            id: 'start',
        },
        ADD_HOUSE_MODE: {
            name: gettext('Add house'),
            url: ocargo.Drawing.imageDir + 'icons/add_house.svg',
            id: 'add_house',
        },
        DELETE_HOUSE_MODE: {
            name: gettext('Delete house'),
            url: ocargo.Drawing.imageDir + 'icons/delete_house.svg',
            id: 'delete_house',
        }
    };

    /*********/
    /* State */
    /*********/

    var saving = new ocargo.Saving();
    var drawing = new ocargo.Drawing();
    drawing.preloadRoadTiles();

    // Level information
    var nodes = [];
    var decor = [];
    var trafficLights = [];
    var cows = [];
    var originNode = null;
    var houseNodes = [];
    var currentTheme = THEMES.grass;
    var needsApproval = false;

    // Reference to the Raphael elements for each square
    var grid;

    // Current mode the user is in
    var mode = modes.ADD_ROAD_MODE;
    var prevMode = null;

    // Holds the state for when the user is drawing or deleting roads
    var strikeStart = null;

    var saveState = new ocargo.LevelSaveState();
    var ownedLevels = new ocargo.OwnedLevels(saveState);

    var sharing = new ocargo.Sharing(
        () => saveState.id,
        () => canShare() && isLevelOwned()
    );

    // Whether the user is scrolling on a tablet
    var isScrolling = false;

    // Whether the trashcan is currently open
    var trashcanOpen = false;
    var trashcanAbsolutePaperX;
    var trashcanAbsolutePaperY;

    var cowGroups = {};
    var currentCowGroupId = 1;

    if (NIGHT_MODE_FEATURE_ENABLED) {
        $('#play_night_tab').show()
    }

    // Setup max_fuel
    setupMaxFuel();

    // Initialise the grid
    initialiseGrid();
    setTheme(THEMES.grass);

    // Setup the toolbox
    setupToolbox();

    if (levelId !== null) {
        loadLevel(levelId);
    }

    setupTrashcan();

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

        tabs.play = new ocargo.Tab($('#play_radio'), $("#run-code-button"), $('#play_radio + label'));
        tabs.playNight = new ocargo.Tab($('#play_night_radio'), $('#play_night_radio + label'));
        tabs.map = new ocargo.Tab($('#map_radio'), $('#map_radio + label'), $('#map_pane'));
        tabs.scenery = new ocargo.Tab($('#scenery_radio'), $('#scenery_radio + label'), $('#scenery_pane'));
        tabs.character = new ocargo.Tab($('#character_radio'), $('#character_radio + label'), $('#character_pane'));
        tabs.blocks = new ocargo.Tab($('#blocks_radio'), $('#blocks_radio + label'), $('#blocks_pane'));
        tabs.random = new ocargo.Tab($('#random_radio'), $('#random_radio + label'), $('#random_pane'));
        tabs.description = new ocargo.Tab($('#description_radio'), $('#description_radio + label'), $('#description_pane'));
        tabs.hint = new ocargo.Tab($('#hint_radio'), $('#hint_radio + label'), $('#hint_pane'));
        tabs.load = new ocargo.Tab($('#load_radio'), $('#load_radio + label'), $('#load_pane'));
        tabs.save = new ocargo.Tab($('#save_radio'), $('#save_radio + label'), $('#save_pane'));
        tabs.share = new ocargo.Tab($('#share_radio'), $('#share_radio + label'), $('#share_pane'));
        tabs.help = new ocargo.Tab($('#help_radio'), $('#help_radio + label'));
        tabs.quit = new ocargo.Tab($('#quit_radio'), $('#quit_radio + label'));

        setupPlayTab();
        setupPlayNightTab();
        setupMapTab();
        setupSceneryTab();
        setupCharacterTab();
        setupBlocksTab();
        setupRandomTab();
        setupDescriptionTab();
        setupHintTab();
        setupLoadTab();
        setupSaveTab();
        setupShareTab();
        setupHelpTab();
        setupQuitTab();
        ownedLevels.update();

        // enable the map tab by default
        currentTabSelected = tabs.map;
        tabs.map.select();

        function restorePreviousTab() {
            currentTabSelected.select();
        }

        function playFunction(night) {
            function playLevel(url) {
                var nightSuffix = night ? '?night=1' : '';
                window.location.href = url + nightSuffix;
            }
            return function() {
                if (isLevelValid()) {
                    var state = extractState();
                    state.name = "Custom level";

                    if (hasLevelChangedSinceSave()) {
                        saving.saveLevel(state, null, true, function (levelId) {
                            playLevel(Urls.play_anonymous_level(levelId));
                        }, console.error);
                    } else {
                        playLevel(Urls.play_custom_level_from_editor(saveState.id));
                    }
                } else {
                    restorePreviousTab();
                }
            };
        }

        function setupPlayTab() {
            tabs.play.setOnChange(playFunction(false));
        }

        function setupPlayNightTab() {
            tabs.playNight.setOnChange(playFunction(true));
        }

        function changeCurrentToolDisplay(mode){
            $('#currentToolText').text(mode.name);
            $('#currentToolIcon').attr("src", mode.url);
            Object.values(modes).forEach((element) => {
                $(`#${element.id}`).addClass('unselected');
            });
            $(`#${mode.id}`).removeClass('unselected');
        }

        function setupMapTab() {
            tabs.map.setOnChange(function() {
                transitionTab(tabs.map);
                mode = modes.ADD_ROAD_MODE;
                changeCurrentToolDisplay(modes.ADD_ROAD_MODE);
            });

            $('#clear').click(function() {
                clear();
                drawAll();
            });

            $('#start').click(function() {
                mode = modes.MARK_ORIGIN_MODE;
                changeCurrentToolDisplay(modes.MARK_ORIGIN_MODE);
            });

            $('#add_road').click(function() {
                mode = modes.ADD_ROAD_MODE;
                changeCurrentToolDisplay(modes.ADD_ROAD_MODE);
            });

            $('#delete_road').click(function() {
                mode = modes.DELETE_ROAD_MODE;
                changeCurrentToolDisplay(modes.DELETE_ROAD_MODE);
            });

            $('#add_house').click(function() {
                mode = modes.ADD_HOUSE_MODE;
                changeCurrentToolDisplay(modes.ADD_HOUSE_MODE);
            });

            $('#delete_house').click(function() {
                mode = modes.DELETE_HOUSE_MODE;
                changeCurrentToolDisplay(modes.DELETE_HOUSE_MODE);
            });

            if(DEVELOPER) {
                $('#djangoText').click(function() {
                    ocargo.Drawing.startPopup('Django level migration',
                        'Copy the text in the console into the Django migration file.',
                        'You will have to change the level name and fill in the model solution field.');
                });
            }
        }

        function setupSceneryTab() {
            tabs.scenery.popup = true;

            tabs.scenery.setOnChange(function() {
                transitionTab(tabs.scenery);
            });

            $('#theme_select').change(function() {
                var selectedValue = $(this).val();
                var theme = THEMES[selectedValue];
                if (theme) {
                    setTheme(theme);
                }
            });

            $('.decor_button').mousedown(handleDraggableDecorMouseDown);

            $('#trafficLightRed').mousedown(function(e) {
                handleDraggableTrafficLightsMouseDown(e, ocargo.TrafficLight.RED);
            });

            $('#trafficLightGreen').mousedown(function(e) {
                handleDraggableTrafficLightsMouseDown(e, ocargo.TrafficLight.GREEN);
            });

            if(COW_LEVELS_ENABLED) {
                if (Object.keys(cowGroups).length == 0) {
                    addCowGroup();
                }
                $('#cow').mouseover(function(e) {
                    e.target.style.cursor = "pointer";
                })
                $('#cow').mousedown(function(e) {
                    handleDraggableCowMouseDown(e, "group1")
                });
            }
        }

        function setupCharacterTab() {
            tabs.character.setOnChange(function() {
                transitionTab(tabs.character);
            });

            $("#character_select").change(function() {
                var selectedValue = $(this).val();
                var character = CHARACTERS[selectedValue];
                if (character) {
                    var CHARACTER_NAME = character.name;
                    $('#character_image').attr('src', character.image);
                    redrawRoad();
                }
            });

            $("#character_select").change();
        }

        function setupBlocksTab() {
            tabs.blocks.setOnChange(function() {
                transitionTab(tabs.blocks);
            });

            setupBlocks();

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

            // Language controls
            $('#language_select').change(function() {
                var value = $(this).val();
                $('#blockly_blocks_div').css('display', this.value === 'python' ? 'none' : 'block');
            });

            function setupBlocks() {
                function addListenerToImage(type) {
                    $('#' + type + '_image').click(function() {
                        $('#' + type + '_checkbox').click();
                    });
                }

                // Setup the block images
                initCustomBlocksDescription();

                // Hacky, if a way can be found without initialising the entire work space that would be great!
                var blockly = document.getElementById('blockly');
                var toolbox = document.getElementById('blockly_toolbox');
                Blockly.inject(blockly, {
                    path: '/static/game/js/blockly/',
                    toolbox: toolbox,
                    trashcan: true
                });

                for (var i = 0; i < BLOCKS.length; i++) {
                    var type = BLOCKS[i];
                    let usePigeons = type === "cow_crossing" && currentTheme == THEMES.city
                    var block = usePigeons ? Blockly.mainWorkspace.newBlock("pigeon_crossing_IMAGE_ONLY") : Blockly.mainWorkspace.newBlock(type);
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

                // Hide blockly
                $('#blockly').css('display','none');
            }
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
                            scenery: $('#sceneryEnabled').val() == "yes"};

                $('#generate').attr('disabled', true);

                saving.retrieveRandomLevel(data, function(error, mapData) {
                    if (error) {
                        console.error(error);
                        ocargo.Drawing.startInternetDownPopup();
                        return;
                    }

                    restoreState(mapData);

                    $('#generate').attr('disabled', false);
                });
            });
        }

        function setupDescriptionTab() {
            tabs.description.setOnChange(function() {
                transitionTab(tabs.description);
            });
        }

        function setupHintTab() {
            tabs.hint.setOnChange(function() {
                transitionTab(tabs.hint);
            });
        }

        function goToMapTab() {
            tabs.map.select();
        }

        function setupLoadTab() {
            var selectedLevel = null;
            var listOfOwnedLevels = null;
            var sharedLevels = [];

            ownedLevels.addListener(processListOfOwnedLevels);

            function updateSharedLevels() {
                saving.retrieveSharedLevels(processListOfSharedLevels, processError);
            }

            tabs.load.setOnChange(function() {
                if(!isLoggedIn("load")) {
                    restorePreviousTab();
                    return;
                }

                transitionTab(tabs.load);

                updateSharedLevels();
            });

            // Setup own/shared levels radio
            $('#load_type_select').change(function() {
                var ownLevelsSelected = this.value === "ownLevels";
                var sharedLevelsSelected = this.value === "sharedLevels";

                var levels = ownLevelsSelected ? listOfOwnedLevels : sharedLevels;
                populateLoadSaveTable("loadLevelTable", levels);

                // Add click listeners to all rows
                var rows = $('#loadLevelTable tr[value]');
                rows.on('click', function(event) {
                    $('#loadLevelTable tr').attr('selected', false);
                    $('#loadLevelTable tr').css('selected', false);
                    $(this).attr('selected', true);
                    $('#loadLevel').removeAttr('disabled');
                    $('#deleteLevel').attr('disabled', sharedLevelsSelected);

                    selectedLevel = $(this).attr('value');
                });
                rows.on('dblclick', loadSelectedLevel);

                $('#deleteLevel').attr('disabled', sharedLevelsSelected || !selectedLevel);
                $('#loadLevel').attr('disabled', !selectedLevel);

                $('#load_pane .scrolling-table-wrapper').css('display', levels.length === 0 ? 'none' : 'block');
            });

            function loadSelectedLevel() {
                if (selectedLevel) {
                    loadLevel(selectedLevel);
                    goToMapTab();
                }
            }

            $('#loadLevel').click(loadSelectedLevel);

            $('#deleteLevel').click(function() {
                if (!selectedLevel) {
                    return;
                }
                var levelId = selectedLevel;

                ownedLevels.deleteLevel(levelId);
            });

            function processError(err) {
                console.error(err);
                restorePreviousTab();
                ocargo.Drawing.startInternetDownPopup();
                return;
            }

            function adjustPaneDisplay() {
                if (listOfOwnedLevels.length == 0 && sharedLevels.length == 0) {
                    $('#load_pane #does_exist').css('display', 'none');
                    $('#load_pane #does_not_exist').css('display', 'block');
                } else {
                    $('#load_pane #does_exist').css('display', 'block');
                    $('#load_pane #does_not_exist').css('display', 'none');
                }
            }

            function reloadList() {
                $('#load_type_select').change();
            }

            function processListOfOwnedLevels(newOwnedLevels) {
                listOfOwnedLevels = newOwnedLevels;

                // Important: done before change() call
                // Table cells need to have rendered to match th with td widths

                reloadList();

                // But disable all the modal buttons as nothing is selected yet
                selectedLevel = null;
                adjustPaneDisplay();
            }

            function processListOfSharedLevels(listOfSharedLevels) {
                sharedLevels = listOfSharedLevels;

                reloadList();

                // But disable all the modal buttons as nothing is selected yet
                selectedLevel = null;

                adjustPaneDisplay();
            }
        }

        function setupSaveTab() {
            var selectedLevel = null;

            ownedLevels.addListener(processListOfLevels);

            tabs.save.setOnChange(function () {
                //getLevelTextForDjangoMigration();
                if (!isLoggedIn("save") || !isLevelValid()) {
                    restorePreviousTab();
                    return;
                }

                transitionTab(tabs.save);
            });

            function save() {
                if(!isLevelValid()) {
                    return;
                }

                const nameInput = $('#levelNameInput')
                const newName = nameInput.val();
                if (!newName || newName === "") {
                    ocargo.Drawing.startPopup(
                        "Oh no!",
                        "No level title!",
                        "Sorry, you need to specify a title for your" +
                            " level to be saved.",
                    );
                    return;
                }

                const regex = /^[\w ]*$/;
                const validString = regex.exec(nameInput.val());
                if (!validString) {
                    ocargo.Drawing.startPopup(
                        "Oh no!",
                        "You used some invalid characters.",
                        "Try saving your level again using only" +
                        " letters and numbers."
                    );
                    return;
                }

                function saveLevelLocal(existingId) {
                    saveLevel(newName, existingId, goToMapTab);
                }

                // Test to see if we already have the level saved
                const table = $("#saveLevelTable");
                let existingId = -1;

                for (let i = 0; i < table[0].rows.length; i++) {
                     const row = table[0].rows[i];
                     const existingName = row.cells[0].innerHTML;
                     if (existingName === newName) {
                        existingId = row.getAttribute('value');
                        break;
                     }
                }

                if (existingId !== -1) {
                    if (!saveState.isCurrentLevel(existingId)) {
                        const onYes = function(){
                            saveLevelLocal(existingId);
                            $("#myModal").hide()
                            $("#ocargo-modal").hide()
                        };
                        const onNo = function(){
                            $("#myModal").hide()
                            $("#ocargo-modal").hide()
                        };
                        ocargo.Drawing.startYesNoPopup(
                            "Overwriting",
                            "Warning",
                            `Level ${newName} already exists. Are
                            you sure you want to overwrite it?`,
                            onYes,
                            onNo
                        );
                    } else {
                        saveLevelLocal(existingId);
                    }
                } else {
                    saveLevelLocal(null);
                }
            }

            $('#saveLevel').click(save);

            function processListOfLevels(ownedLevels) {

                // Important: done before change() call
                // Table cells need to have rendered to match th with td widths

                populateLoadSaveTable("saveLevelTable", ownedLevels);

                // Add click listeners to all rows
                var rows = $('#saveLevelTable tr[value]');
                rows.on('click', function(event) {
                    var rowSelected = $(event.target.parentElement);
                    $('#saveLevelTable tr').attr('selected', false);
                    $(this).attr('selected', true);
                    $('#saveLevel').removeAttr('disabled');
                    selectedLevel = parseInt(rowSelected.attr('value'));

                    for (var i = 0; i < ownedLevels.length; i++) {
                        if (ownedLevels[i].id === selectedLevel) {
                            $("#levelNameInput").val(ownedLevels[i].name);
                        }
                    }
                });
                rows.on('dblclick', save);

                $('#save_pane .scrolling-table-wrapper').css('display', ownedLevels.length === 0 ? 'none' : 'block');
                selectedLevel = null;
            }
        }

        function setupShareTab() {
            // Set up the behaviour for when the tab is selected
            tabs.share.setOnChange(function() {
                if (!isIndependentStudent() ||  !isLoggedIn("share") || !canShare() || !isLevelOwned()) {
                    restorePreviousTab();
                    return;
                }

                saving.getSharingInformation(saveState.id, function(error, validRecipients) {
                    if(error) {
                        console.error(error);
                        return;
                    }

                    transitionTab(tabs.share);
                    sharing.processSharingInformation(error, validRecipients);
                });
            });

            sharing.setupTeacherPanel();
            sharing.setupSelectAllButton();
        }

        function setupHelpTab() {
            var helpMessages = [
                gettext('To get started, draw a road.'),
                gettext('Click on the square you want the road to start from. Then, without letting go of the mouse button, ' +
                    'drag to the square you’d like the road to end on. Do this as many times as you like to add new sections ' +
                    'of road.'),
                interpolate(
                    gettext('In %(map_icon)s%(map_label)s menu, click %(mark_start_icon)s%(mark_start_label)s and select a ' +
                        'square for your road to start from. The starting point can only be placed on dead ends. You need a ' +
                        'road first before adding a starting point. Make sure you use %(add_house_icon)s%(add_house_label)s to ' +
                        'select houses for delivery. Setting a fuel level means the route will need to be short enough for the ' +
                        'fuel not to run out.'
                    ), {
                        map_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/map.svg', 'popupIcon'),
                        map_label: '<b>' + gettext('Map') + '</b>',
                        mark_start_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/origin.svg', 'popupIcon'),
                        mark_start_label: '<b>' + gettext('Mark start') + '</b>',
                        add_house_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/add_house.svg', 'popupIcon'),
                        add_house_label: '<b>' + gettext('Add house') + '</b>'
                    },
                    true
                ),
                interpolate(
                    gettext('To remove road, click the %(delete_road_icon)s%(delete_road_label)s button and select a section ' +
                        'to get rid of. To remove a house for delivery, click the %(delete_house_icon)s%(delete_house_label)s button' +
                        'and select a house to get rid of.'
                    ), {
                        delete_road_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/delete_road.svg', 'popupIcon'),
                        delete_road_label: '<b>' + gettext('Delete road') + '</b>',
                        delete_house_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/delete_house.svg', 'popupIcon'),
                        delete_house_label: '<b>' + gettext('Delete house') + '</b>'
                    },
                    true
                ),
                interpolate(
                    gettext('Click %(random_icon)s%(random_label)s if you want the computer to create a random route for you.'), {
                        random_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/random.svg', 'popupIcon'),
                        random_label: '<b>' + gettext('Random') + '</b>'
                    },
                    true
                ),
                interpolate(
                    gettext('Select %(scenery_icon)s%(scenery_label)s and choose trees, bushes and more to place around your ' +
                        'road. These will show in the top left corner - drag them into place. Delete items by dragging them ' +
                        'into the bin in the bottom right. To rotate a traffic light, simply double click on it. Remember, ' +
                        'using the traffic lights is not covered until level 44.'
                    ), {
                        scenery_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/decor.svg', 'popupIcon'),
                        scenery_label: '<b>' + gettext('Scenery') + '</b>'
                    },
                    true
                ),
                interpolate(
                    gettext('Choose a character to play with from the %(character_icon)s%(character_label)s menu.'), {
                        character_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/character.svg', 'popupIcon'),
                        character_label: '<b>' + gettext('Character') + '</b>'
                    },
                    true
                ),
                interpolate(
                    gettext('Select which blocks of code you want to be used to create a route for your character from the ' +
                        '%(blocks_icon)s%(blocks_label)s menu.'
                    ), {
                        blocks_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/blockly.svg', 'popupIcon'),
                        blocks_label: '<b>' + gettext('Blocks') + '</b>'
                    },
                    true
                ),
                interpolate(
                    gettext('When you\'re ready click %(play_icon)s%(play_label)s, or %(save_icon)s%(save_label)s your road or ' +
                        '%(share_icon)s%(share_label)s it with a friend. Don\'t forget to choose a good name for it!'
                    ), {
                        play_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/play.svg', 'popupIcon'),
                        play_label: '<b>' + gettext('Play') + '</b>',
                        save_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/save.svg', 'popupIcon'),
                        save_label: '<b>' + gettext('Save') + '</b>',
                        share_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/share.svg', 'popupIcon'),
                        share_label: '<b>' + gettext('Share') + '</b>'
                    },
                    true
                ),
                interpolate(
                    gettext('%(quit_icon)s%(quit_label)s will take you back to the Rapid Router homepage.'
                    ), {
                        quit_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/quit.svg', 'popupIcon'),
                        quit_label: '<b>' + gettext('Quit') + '</b>'
                    },
                    true
                )
            ];

            tabs.help.setOnChange(function() {
                restorePreviousTab();
                ocargo.Drawing.startPopup('', '', helpMessages.join('<br><br>'));
            });
        }

        function setupQuitTab() {
            tabs.quit.setOnChange(function() {
                window.location.href = Urls.levels();
            });
        }


        // Helper methods
        function transitionTab(newTab) {
            var previousTab = currentTabSelected;
            previousTab.setPaneEnabled(false);
            newTab.setPaneEnabled(true);
            currentTabSelected = newTab;
            return previousTab;
        }

        function populateLoadSaveTable(tableName, levels) {
            var table = $('#' + tableName + ' tbody');

            $('#' + tableName).css('display', levels.length == 0 ? 'none' : 'table');
            $('#' + tableName + 'Header').css('display', levels.length == 0 ? 'none' : 'table');

            // Remove click listeners to avoid memory leak and remove all rows
            $('#' + tableName + ' tr').off('click');
            table.empty();

            // Order them alphabetically
            levels.sort(function (a, b) {
                if (a.name < b.name) {
                    return -1;
                } else if (a.name > b.name) {
                    return 1;
                }
                return 0;
            });

            // Add a row to the table for each level saved in the database
            for (var i = 0, ii = levels.length; i < ii; i++) {
                var level = levels[i];
                var row = $('<tr></tr>').attr({ value: level.id }).appendTo(table);
                $('<td></td>').text(level.name).appendTo(row);
                $('<td></td>').text(level.owner).appendTo(row);
            }
            for (var i = 0; i < 2; i++) {
                var td = $('#' + tableName + ' td:eq(' + i + ')');
                var td2 = $('#' + tableName + 'Header th:eq(' + i + ')');
                td2.width(td.width());
            }
        }
    }

    /************/
    /*   Cows   */
    /************/

    function addCowGroup() {
        if(COW_LEVELS_ENABLED) {
            var color = COW_GROUP_COLOR_PALETTE[(currentCowGroupId - 1) % COW_GROUP_COLOR_PALETTE.length];
            var style = 'background-color: ' + color;
            var value = 'group' + currentCowGroupId++;
            var type = currentTheme == THEMES.city ? ocargo.Cow.PIGEON : ocargo.Cow.WHITE;

            cowGroups[value] = {
                id: value,
                color: color,
                minCows: 1,
                maxCows: 1,
                type: type
            };

            var text = interpolate(gettext('Group %(cow_group)s'), {cow_group: Object.keys(cowGroups).length}, true);
            $('#cow_group_select').append($('<option>', {value: value, style: style})
                .text(text));
            $('#cow_group_select').val(value).change();
        }
    }

    function removeCowGroup() {
        if(Object.keys(cowGroups).length > 1) {
            var selectedGroupId = $('#cow_group_select').val();

            //Remove cows from map
            for(var i = cows.length - 1; i >= 0; i--) {
                if(cows[i].data.group.id === selectedGroupId) {
                    cows[i].destroy();
                }
            }

            //Remove group from group list
            delete cowGroups[selectedGroupId];

            // Select previous option select element if present
            var selectedOption = $('#cow_group_select > option:selected');
            if(selectedOption.prev('option').length > 0) {
                selectedOption.prev('option').attr('selected', 'selected');
            } else {
                selectedOption.next('option').attr('selected', 'selected');
            }

            // Remove old option
            selectedOption.remove();

            // Trigger change event on select element
            $('#cow_group_select').change();

            //Renumber groups in select element
            var groupNo = 1;
            $('#cow_group_select').find('option').each(function() {
                $(this).text(interpolate(gettext('Group %(cow_group)s'), {cow_group: groupNo++}, true));
            });
        }
    }

    /************/
    /*  MaxFuel */
    /************/


    function setupMaxFuel(){
        var MAX_FUEL = 99;
        var DEFAULT_FUEL = 50;
        var lastCorrectFuel = $('#max_fuel').val();
        if (!onlyContainsDigits(lastCorrectFuel)) {
            $('#max_fuel').val(DEFAULT_FUEL);
            lastCorrectFuel = DEFAULT_FUEL;
        }

        $('#max_fuel').on('input', function () {
            var value = $(this).val();
            $(this).val(updatedValue(value));
        });

        function restrictValue(value){
            if (value > MAX_FUEL) {
                return MAX_FUEL;
            } else {
                return value;
            }
        }
        function updatedValue(value){
            if (onlyContainsDigits(value)) {
                value = parseInt(value);
                var newValue = restrictValue(value);
                lastCorrectFuel = newValue;
                return newValue;
            } else {
                return lastCorrectFuel;
            }
        }
        function onlyContainsDigits(n){
            return n !== ''  && /^\d+$/.test(n);
        }
    }
    /************/
    /* Trashcan */
    /************/

    function placeTrashcan(trashcan) {
        // Iffy way of making sure the trashcan stays inside the grid
        // when window bigger than grid
        var windowWidth = $(window).width();
        var windowHeight = $(window).height();

        var paperRightEdge = EXTENDED_PAPER_WIDTH + $('#tools').width();
        var paperBottomEdge = EXTENDED_PAPER_HEIGHT;

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
    }

    function setupTrashcan() {

        var trashcan = $('#trashcanHolder');

        placeTrashcan(trashcan);

        $(window).resize(function() {
            placeTrashcan(trashcan);
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
        } else {
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

    function isHouseCoordinate(coordinate) {
        return houseNodes.includes(ocargo.Node.findNodeByCoordinate(coordinate, nodes));
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
        var x = globalX - paperPosition.left + paper.scrollLeft() + PAPER_PADDING;
        var y = globalY - paperPosition.top + paper.scrollTop() + PAPER_PADDING;

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
        grid = drawing.createGrid();
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

    function clearLevelNameInputInSaveTab() {
        $('#levelNameInput').val('');
    }

    function clear() {
        for (var i = trafficLights.length-1; i >= 0; i--) {
            trafficLights[i].destroy();
        }
        for (var i = decor.length-1; i >= 0; i--) {
            decor[i].destroy();
        }

        for (var i = cows.length-1; i >= 0; i--) {
            cows[i].destroy();
        }

        nodes = [];
        strikeStart = null;
        originNode = null;
        houseNodes = [];

        cowGroups = {};
        currentCowGroupId = 1;
        $('#cow_group_select').find('option').remove();
        // Add initial cow group
        addCowGroup();

        clearLevelNameInputInSaveTab();
    }

    function drawAll() {
        drawing.renderGrid(grid, currentTheme);
        redrawRoad();
    }

    function redrawRoad() {
        drawing.renderRoad(nodes);
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

    function bringCowsToFront() {
        for (var i = 0; i < cows.length; i++) {
            cows[i].image.toFront();
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

    function markAsHouse(coordinate) {
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

    function markCowNodes() {
        if (cows) {
            for (var i = 0; i < cows.length; i++) {
                var internalCow = cows[i];
                if (internalCow.coordinate) {
                    mark(internalCow.coordinate, internalCow.data.group.color, 0.3, true);
                }
            }
        }
    }

    function clearMarkings() {
        for (var i = 0; i < GRID_WIDTH; i++) {
            for (var j = 0; j < GRID_HEIGHT; j++) {
                markAsBackground(new ocargo.Coordinate(i,j));
                grid[i][j].toFront();
            }
        }

        markCowNodes();

        if (originNode) {
            markAsOrigin(originNode.coordinate);
        }
        if (houseNodes.length > 0) {
            for (let i = 0; i < houseNodes.length; i++) {
                markAsHouse(houseNodes[i].coordinate);
            }
        }

        bringTrafficLightsToFront();
        bringCowsToFront();
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
    }

    function handleMouseDown(this_rect) {
        return function (ev) {
            ev.preventDefault();

            var getBBox = this_rect.getBBox();
            var coordPaper = getCoordinateFromBBox(getBBox);
            var coordMap = ocargo.Drawing.translate(coordPaper);
            var existingNode = ocargo.Node.findNodeByCoordinate(coordMap, nodes);

            if (mode === modes.MARK_ORIGIN_MODE && existingNode && canPlaceCFC(existingNode)) {
                if (originNode) {
                    var prevStart = originNode.coordinate;
                    markAsBackground(prevStart);
                }
                // Check if same as a house node
                if (isHouseCoordinate(coordMap)) {
                    houseNodes.splice(houseNodes.indexOf(ocargo.Node.findNodeByCoordinate(coordMap, nodes)), 1)
                }

                markAsOrigin(coordMap);
                var newStartIndex = ocargo.Node.findNodeIndexByCoordinate(coordMap, nodes);

                // Putting the new start in the front of the nodes list.
                var temp = nodes[newStartIndex];
                nodes[newStartIndex] = nodes[0];
                nodes[0] = temp;
                originNode = nodes[0];
            } else if (mode === modes.ADD_HOUSE_MODE && existingNode) {
                // Check if same as starting node
                if (isOriginCoordinate(coordMap)) {
                    originNode = null;
                }

                markAsHouse(coordMap);
                var newEnd = ocargo.Node.findNodeIndexByCoordinate(coordMap, nodes);
                houseNodes.push(nodes[newEnd]);

            } else if (mode === modes.DELETE_HOUSE_MODE && existingNode) {
                if (isHouseCoordinate(coordMap)) {
                    houseNodes.splice(houseNodes.indexOf(ocargo.Node.findNodeByCoordinate(coordMap, nodes)), 1);
                    markAsBackground(coordMap);
                }
            } else if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                strikeStart = coordMap;
                markAsSelected(coordMap);
            }
        };
    }

    function getCoordinateFromBBox(bBox){
        return new ocargo.Coordinate((bBox.x - PAPER_PADDING) / GRID_SPACE_SIZE, (bBox.y - PAPER_PADDING) / GRID_SPACE_SIZE);
    }

    function handleMouseOver(this_rect) {
        return function(ev) {
            ev.preventDefault();

            var getBBox = this_rect.getBBox();
            var coordPaper = getCoordinateFromBBox(getBBox);
            var coordMap = ocargo.Drawing.translate(coordPaper);

            if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                if (strikeStart !== null) {
                    markTentativeRoad(coordMap);
                } else if (!isOriginCoordinate(coordMap) && !isHouseCoordinate(coordMap)) {
                    markAsHighlighted(coordMap);
                }
            } else if (mode === modes.MARK_ORIGIN_MODE || mode === modes.ADD_HOUSE_MODE || mode === modes.DELETE_HOUSE_MODE) {
                var node = ocargo.Node.findNodeByCoordinate(coordMap, nodes);
                if (node && originNode !== node && !houseNodes.includes(node)) {
                    if (mode === modes.ADD_HOUSE_MODE) {
                        mark(coordMap, 'blue', 0.3, true);
                    } else if (mode === modes.MARK_ORIGIN_MODE && canPlaceCFC(node)) {
                        mark(coordMap, 'red', 0.5, true);
                    }
                } else if (node && houseNodes.includes(node) && mode === modes.DELETE_HOUSE_MODE) {
                    mark(coordMap, 'blue', 0.3, true);
                }
            }
        };
    }

    function handleMouseOut(this_rect) {
        return function(ev) {
            ev.preventDefault();

            var getBBox = this_rect.getBBox();
            var coordPaper = getCoordinateFromBBox(getBBox);
            var coordMap = ocargo.Drawing.translate(coordPaper);

            if (mode === modes.MARK_ORIGIN_MODE || mode === modes.ADD_HOUSE_MODE || mode === modes.DELETE_HOUSE_MODE) {
                var node = ocargo.Node.findNodeByCoordinate(coordMap, nodes);
                if (node && originNode !== node && !houseNodes.includes(node)) {
                    markAsBackground(coordMap);
                    markCowNodes();
                } else if (node && houseNodes.includes(node)) {
                    markAsHouse(coordMap);
                    markCowNodes();
                }
            } else if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                if (!isOriginCoordinate(coordMap) && !isHouseCoordinate(coordMap)) {
                    markAsBackground(coordMap);
                    markCowNodes();
                }
            }
        };
    }

    function handleMouseUp(this_rect) {
        return function(ev) {
            ev.preventDefault();

            if (mode === modes.ADD_ROAD_MODE || mode === modes.DELETE_ROAD_MODE) {
                var getBBox = this_rect.getBBox();
                var coordPaper = getCoordinateFromBBox(getBBox);
                var coordMap = ocargo.Drawing.translate(coordPaper);

                if (mode === modes.DELETE_ROAD_MODE) {
                    finaliseDelete(coordMap);
                } else {
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

    function draggedObjectOnGrid(e, dragged_object) {
    // object location is relative to the whole page, so need to factor in paper and padding size, grid canvas scroll amount, width of toolbar, etc.
        return e.pageX >= (TAB_PANE_WIDTH + PAPER_PADDING)
            && (e.pageY + paper.scrollTop() + dragged_object.height / 2) <= (PAPER_HEIGHT + PAPER_PADDING)
            && (e.pageX + paper.scrollLeft() + dragged_object.width / 2) <= (TAB_PANE_WIDTH + PAPER_WIDTH + PAPER_PADDING)
    }

    function getAbsCoordinates(e) {
        const absX = (e.pageX + paper.scrollLeft() - TAB_PANE_WIDTH) / GRID_SPACE_SIZE;
        const absY = (e.pageY + paper.scrollTop()) / GRID_SPACE_SIZE;
        return [absX, absY];
    }

    function draggedCursorOverGrid(absX, absY) {
        return absY <= SEMI_EXTENDED_PAPER_HEIGHT / 100 && absX <= EXTENDED_PAPER_WIDTH / 100 && absX >= 0
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
            checkImageOverTrashcan(paperX, paperY, imageWidth, imageHeight);

            // Stop it being dragged off the edge of the page
            if (paperX < 0) {
                paperX = 0;
            } else if (paperX + imageWidth > EXTENDED_PAPER_WIDTH) {
                paperX = EXTENDED_PAPER_WIDTH - imageWidth;
            }

            if (paperY < 0) {
                paperY = 0;
            } else if (paperY + imageHeight >  EXTENDED_PAPER_HEIGHT) {
                paperY = EXTENDED_PAPER_HEIGHT - imageHeight;
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

            paperWidth = GRID_WIDTH * GRID_SPACE_SIZE + PAPER_PADDING;
            paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE + PAPER_PADDING;
        }

        function onDragEnd() {
            originX = paperX;
            originY = paperY;

            if (trashcanOpen) {
                decor.destroy();
            } else {
                if (paperWidth < paperX + imageWidth) {
                    originX = paperWidth - imageWidth;
                }
                if (paperHeight < paperY + imageHeight) {
                    originY = paperHeight - imageHeight;
                }

                image.transform('t' + originX + ',' + originY);
            }

            closeTrashcan();
        }

        image.drag(onDragMove, onDragStart, onDragEnd);
        addReleaseListeners(image.node);
    }

    function handleDraggableDecorMouseDown(e){
        e.preventDefault();

        window.dragged_decor = {};
        dragged_decor.pageX0 = e.pageX;
        dragged_decor.pageY0 = e.pageY;
        dragged_decor.elem = this;
        dragged_decor.offset0 = $(this).offset();
        dragged_decor.width = parseInt(currentTheme.decor[this.id].width);
        dragged_decor.height = parseInt(currentTheme.decor[this.id].height);
        dragged_decor.parent = this.parentElement;

        const clone = $(this).clone(true);

        function handleDraggableDecorDragging(e){
            const left = dragged_decor.offset0.left + (e.pageX - dragged_decor.pageX0);
            const top = dragged_decor.offset0.top + (e.pageY - dragged_decor.pageY0);
            $(dragged_decor.elem).offset({top: top, left: left});
        }

        function handleDraggableDecorMouseUp(e){
            if (dragged_decor.elem.id !== null) {
                if (draggedObjectOnGrid(e, dragged_decor)) {
                    let decorObject = new InternalDecor(dragged_decor.elem.id);
                    decorObject.setPosition(e.pageX + paper.scrollLeft() - TAB_PANE_WIDTH - dragged_decor.width / 2, e.pageY + paper.scrollTop() - dragged_decor.height / 2);
                }
            }

            $(document)
            .off('mousemove', handleDraggableDecorDragging)
            .off('mouseup mouseleave', handleDraggableDecorMouseUp);

            $(dragged_decor.elem).remove();
            $(clone).appendTo(dragged_decor.parent);
        }

        $(document)
        .on('mouseup mouseleave', handleDraggableDecorMouseUp)
        .on('mousemove', handleDraggableDecorDragging);
    }

    function setupCowListeners(cow) {
        var image = cow.image;

        // Position in map coordinates.
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

        var moved = false;

        function onDragMove(dx, dy) {
            cow.valid = false;
            image.attr({'cursor':'default'});
            moved = dx !== 0 || dy !== 0;

            // Update image's position
            paperX = dx + originX;
            paperY = dy + originY;


            // Trashcan check
            checkImageOverTrashcan(paperX, paperY, imageWidth, imageHeight);

            // Stop it being dragged off the edge of the page
            if (paperX < 0) {
                paperX = 0;
            } else if (paperX + imageWidth > EXTENDED_PAPER_WIDTH) {
                paperX = EXTENDED_PAPER_WIDTH - imageWidth;
            }
            if (paperY < 0) {
                paperY =  0;
            } else if (paperY + imageHeight >  EXTENDED_PAPER_HEIGHT) {
                paperY = EXTENDED_PAPER_HEIGHT - imageHeight;
            }

            // And perform the updatee
            image.transform('t' + paperX + ',' + paperY );

            //Unmark the squares the cow previously occupied
            unmarkOldCowSquare(controlledCoord, cow);

            // Now calculate the source coordinate
            var box = image.getBBox();
            var absX = (box.x + box.width/2) / GRID_SPACE_SIZE;
            var absY = (box.y + box.height/2) / GRID_SPACE_SIZE;

            controlledCoord = markNewCowSquare(absX, absY, controlledCoord, cow);

            // Deal with trashcan
            var paperAbsX = paperX - paper.scrollLeft() + imageWidth/2;
            var paperAbsY = paperY - paper.scrollTop() + imageHeight/2;
            var trashcanWidth = $('#trashcanHolder').width();
            var trashcanHeight = $('#trashcanHolder').height();

            if(paperAbsX > trashcanAbsolutePaperX && paperAbsX <= trashcanAbsolutePaperX + trashcanWidth  &&
                paperAbsY > trashcanAbsolutePaperY - 20 && paperAbsY <= trashcanAbsolutePaperY + trashcanHeight) {
                openTrashcan();
            } else {
                closeTrashcan();
            }
        }

        function onDragStart(x, y) {
            // cow shouldn't be in the cow group during dragging
            removeCowFromCowList(cow);
            var bBox = image.getBBox();
            imageWidth = bBox.width;
            imageHeight = bBox.height;

            var paperPosition = paper.position();
            originX = x - paperPosition.left + paper.scrollLeft() - imageWidth/2;
            originY = y - paperPosition.top + paper.scrollTop() - imageHeight/2;

            paperWidth = GRID_WIDTH * GRID_SPACE_SIZE;
            paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE;

            adjustCowGroupMinMaxFields(cow);
        }

        function onDragEnd() {

            if (trashcanOpen) {
                cow.destroy();
                unmarkOldCowSquare(controlledCoord, cow);
                closeTrashcan();
            } else {
                setCowMarkingsOnMouseUp(controlledCoord, cow);
                cows.push(cow);
                cow.coordinate = controlledCoord;
                cow.valid = isValidDraggedCowPlacement(controlledCoord, cow);
                if (cow.isOnRoad()) {
                    const controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);
                    drawing.setCowImagePosition(controlledCoord, image, controlledNode);
                }
                else {
                    var cowX = paperX;
                    var cowY = paperY;

                    if (paperWidth < paperX + imageWidth) {
                        cowX = paperWidth - imageWidth
                    }

                    if (paperHeight < paperY + imageHeight) {
                        cowY = paperHeight - imageHeight
                    }

                    image.transform('t' + cowX + ',' + cowY);
                }
            }

            adjustCowGroupMinMaxFields(cow);
            image.attr({'cursor':'pointer'});
        }

        image.drag(onDragMove, onDragStart, onDragEnd);
        addReleaseListeners(image.node);
    }

    function removeCowFromCowList(cow) {
        var index = cows.indexOf(cow);
        if (index > -1) {
            cows.splice(index, 1);
        }
    }

    function isValidDraggedCowPlacement(controlledCoord, cow){
        if (isOriginCoordinate(controlledCoord) || isHouseCoordinate(controlledCoord))
            return false;
        for (var i=0; i < cows.length; i++) {
            var otherCow = cows[i];
            if (cow != otherCow && otherCow.coordinate && otherCow.coordinate.equals(controlledCoord))
                return false;
        }
        return true;
    }

    function adjustCowGroupMinMaxFields(draggedCow) {
        var draggedCowGroupId = draggedCow.data.group.id;

        var noOfValidCowsInGroup = 0;
        for (var i=0; i < cows.length; i++) {
            if(cows[i].valid && cows[i].data.group.id === draggedCowGroupId) {
                noOfValidCowsInGroup++;
            }
        }

        var draggedCowGroup = cowGroups[draggedCowGroupId];
        draggedCowGroup.minCows = Math.max(1, Math.min(draggedCowGroup.minCows, noOfValidCowsInGroup));
        draggedCowGroup.maxCows = Math.max(1, Math.min(draggedCowGroup.maxCows, noOfValidCowsInGroup));
        $('#cow_group_select').val(draggedCowGroupId).change();
    }

    function unmarkOldCowSquare(controlledCoord, cow = "undefined") {
        if (controlledCoord) {
            markAsBackground(controlledCoord);
        }
        if (originNode) {
            markAsOrigin(originNode.coordinate);
        }
        if (houseNodes.length > 0) {
            for (let i = 0; i < houseNodes.length; i++){
                markAsHouse(houseNodes[i].coordinate);
            }
        }
    }

    function setCowMarkingsOnMouseUp(controlledCoord, cow) {
        if (cow.isOnRoad()) {
            markAsBackground(cow.coordinate);
        }
        if (controlledCoord) {
            mark(controlledCoord, cow.data.group.color, 0.3, true);
        }
        if (originNode) {
            markAsOrigin(originNode.coordinate);
        }
        if (houseNodes.length > 0) {
            for (let i = 0; i < houseNodes.length; i++) {
                markAsHouse(houseNodes[i].coordinate);
            }
        }
    }

    function markNewCowSquare(absX, absY, controlledCoord, cow = "undefined") {
        const x = Math.min(Math.max(0, Math.floor(absX)), GRID_WIDTH - 1);
        const y = GRID_HEIGHT - Math.min(Math.max(0, Math.floor(absY)), GRID_HEIGHT - 1) - 1;
        controlledCoord = new ocargo.Coordinate(x,y);

        // If source node is not on grid remove it
        if (!isCoordinateOnGrid(controlledCoord)) {
            controlledCoord = null;
        }

        // mark square valid or invalid
        if (controlledCoord) {
            let colour;
            if(isValidDraggedCowPlacement(controlledCoord, cow)) {
                colour = VALID_LIGHT_COLOUR;
            } else {
                colour = INVALID_LIGHT_COLOUR;
            }

            mark(controlledCoord, colour, 0.7, false);
        }

        return controlledCoord;
    }

    function handleDraggableCowMouseDown(e, cowGroup){
        e.preventDefault();

        window.dragged_cow = {};
        dragged_cow.pageX0 = e.pageX;
        dragged_cow.pageY0 = e.pageY;
        dragged_cow.elem = e.target;
        dragged_cow.offset0 = $(e.target).offset();
        dragged_cow.parent = e.target.parentElement;
        dragged_cow.group = cowGroups[cowGroup];
        dragged_cow.width = COW_WIDTH;
        dragged_cow.height = COW_HEIGHT;

        const clone = $(e.target).clone(true);
        let controlledCoord;

        function handleDraggableCowDragging(e){
            e.target.style.cursor = "pointer";

            const left = dragged_cow.offset0.left + (e.pageX - dragged_cow.pageX0);
            const top = dragged_cow.offset0.top + (e.pageY - dragged_cow.pageY0);
            $(dragged_cow.elem).offset({top: top, left: left});

            unmarkOldCowSquare(controlledCoord);

            const [absX, absY] = getAbsCoordinates(e);
            if (draggedCursorOverGrid(absX, absY)) {
                controlledCoord = markNewCowSquare(absX, absY, controlledCoord);
            }
        }

        function handleDraggableCowMouseUp(e){
            let internalCow = new InternalCow({group: cowGroups["group1"]});
            let image = internalCow.image;
            internalCow.coordinate = controlledCoord;
            internalCow.valid = isValidDraggedCowPlacement(controlledCoord, internalCow);

            if (internalCow.isOnRoad()) {
                const controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);
                drawing.setCowImagePosition(controlledCoord, image, controlledNode);
            } else {
                const cowX = e.pageX + paper.scrollLeft() - TAB_PANE_WIDTH - dragged_cow.width / 2;
                const cowY = e.pageY + paper.scrollTop() - dragged_cow.height / 2;

                if (draggedObjectOnGrid(e, dragged_cow)) {
                    image.transform('t' + cowX + ',' + cowY);
                } else {
                    internalCow.destroy();
                }
            }

            if (!trashcanOpen) {
                setCowMarkingsOnMouseUp(controlledCoord, internalCow);
                adjustCowGroupMinMaxFields(internalCow);
            }

            $(document)
            .off('mousemove', handleDraggableCowDragging)
            .off('mouseup mouseleave', handleDraggableCowMouseUp);

            $(dragged_cow.elem).remove();
            $(clone).appendTo(dragged_cow.parent);
        }

        $(document)
        .on('mouseup mouseleave', handleDraggableCowMouseUp)
        .on('mousemove', handleDraggableCowDragging);
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
            } else if (paperX + imageWidth > EXTENDED_PAPER_WIDTH) {
                paperX = EXTENDED_PAPER_WIDTH - imageWidth;
            }
            if (paperY < 0) {
                paperY =  0;
            } else if (paperY + imageHeight >  EXTENDED_PAPER_HEIGHT) {
                paperY = EXTENDED_PAPER_HEIGHT - imageHeight;
            }

            // And perform the update
            image.transform('t' + paperX + ',' + paperY + 'r' + rotation + 's' + scaling);

            // Unmark the squares the light previously occupied
            unmarkOldTrafficLightSquare(sourceCoord, controlledCoord);

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

            [sourceCoord, controlledCoord] = markNewTrafficLightSquare(absX, absY, isValidTrafficLightPlacement, sourceCoord, controlledCoord, rotation, image);

            // Deal with trashcan
            var paperAbsX = paperX - paper.scrollLeft() + imageWidth/2;
            var paperAbsY = paperY - paper.scrollTop() + imageHeight/2;
            var trashcanWidth = $('#trashcanHolder').width();
            var trashcanHeight = $('#trashcanHolder').height();

            if(paperAbsX > trashcanAbsolutePaperX && paperAbsX <= trashcanAbsolutePaperX + trashcanWidth  &&
                paperAbsY > trashcanAbsolutePaperY - 20 && paperAbsY <= trashcanAbsolutePaperY + trashcanHeight) {
                openTrashcan();
            } else {
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

            paperWidth = GRID_WIDTH * GRID_SPACE_SIZE + PAPER_PADDING;
            paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE + PAPER_PADDING;

            var paperPosition = paper.position();

            var mouseX = x - paperPosition.left;
            var mouseY = y - paperPosition.top;

            originX = mouseX + paper.scrollLeft()- imageWidth/2;
            originY = mouseY + paper.scrollTop() - imageHeight/2;
        }

        function onDragEnd() {
            // Unmark squares currently occupied
            unmarkOldTrafficLightSquare(sourceCoord, controlledCoord);

            if(trashcanOpen) {
                trafficLight.destroy();
            } else if(isValidTrafficLightPlacement(sourceCoord, controlledCoord)) {
                // Add back to the list of traffic lights if on valid nodes
                trafficLight.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
                trafficLight.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);
                trafficLight.valid = true;

                drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
            } else {
                var trafficLightX = paperX;
                var trafficLightY = paperY;

                if (paperWidth < paperX + imageWidth) {
                    trafficLightX = paperWidth - imageWidth
                    image.transform('t' + trafficLightX + ',' + trafficLightY + 'r' + rotation + 's' + scaling);
                }
                if (paperHeight < paperY + imageHeight) {
                    trafficLightY = paperHeight - imageHeight
                    image.transform('t' + trafficLightX + ',' + trafficLightY + 'r' + rotation + 's' + scaling);
                }
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
    }

    function isValidTrafficLightPlacement(sourceCoord, controlledCoord) {
        var sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
        var controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);

        // Test if two connected nodes exist
        var connected = false;
        if (sourceNode && controlledNode) {
            for (var i = 0; i < sourceNode.connectedNodes.length; i++) {
                if (sourceNode.connectedNodes[i] === controlledNode) {
                    connected = true;
                    break;
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

    function unmarkOldTrafficLightSquare(sourceCoord, controlledCoord) {
        // Unmark the squares the light previously occupied
        if (sourceCoord) {
            markAsBackground(sourceCoord);
        }
        if (controlledCoord) {
            markAsBackground(controlledCoord);
        }

        markCowNodes();

        if (originNode) {
            markAsOrigin(originNode.coordinate);
        }
        if (houseNodes.length > 0) {
            for (let i = 0; i < houseNodes.length; i++) {
                markAsHouse(houseNodes[i].coordinate);
            }
        }
    }

    function markNewTrafficLightSquare(absX, absY, validityCheckFunction, sourceCoord, controlledCoord, rotation, image = "undefined") {
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
            if(validityCheckFunction(sourceCoord, controlledCoord)) {
                colour = VALID_LIGHT_COLOUR;
                if (image !== "undefined") {
                    drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
                }
            } else {
                colour = INVALID_LIGHT_COLOUR;
            }

            mark(controlledCoord, colour, 0.7, false);
            mark(sourceCoord, colour, 0.7, false);
        }

        return [sourceCoord, controlledCoord];
    }

    function handleDraggableTrafficLightsMouseDown(e, startingState){
        e.preventDefault();

        window.dragged_light = {};
        dragged_light.pageX0 = e.pageX;
        dragged_light.pageY0 = e.pageY;
        dragged_light.elem = e.target;
        dragged_light.offset0 = $(e.target).offset();
        dragged_light.width = TRAFFIC_LIGHT_WIDTH;
        dragged_light.height = TRAFFIC_LIGHT_HEIGHT;
        dragged_light.parent = e.target.parentElement;

        const clone = $(e.target).clone(true);

        let sourceCoord;
        let controlledCoord;

        function handleDraggableTrafficLightsDragging(e){
            const left = dragged_light.offset0.left + (e.pageX - dragged_light.pageX0);
            const top = dragged_light.offset0.top + (e.pageY - dragged_light.pageY0);
            $(dragged_light.elem).offset({top: top, left: left});

            unmarkOldTrafficLightSquare(sourceCoord, controlledCoord);

            const [absX, absY] = getAbsCoordinates(e);
            if (draggedCursorOverGrid(absX, absY)) {
                [sourceCoord, controlledCoord] = markNewTrafficLightSquare(absX, absY, isValidTrafficLightPlacement, sourceCoord, controlledCoord, 0);
            }
        }

        function handleDraggableTrafficLightsMouseUp(e){
            let internalTrafficLight = new InternalTrafficLight({"redDuration": 3, "greenDuration": 3, "startTime": 0, "startingState": startingState, "sourceCoordinate": null,  "direction": null});
            let image = internalTrafficLight.image;

            const lightX = e.pageX + paper.scrollLeft() - TAB_PANE_WIDTH - dragged_light.width;
            const lightY = e.pageY + paper.scrollTop() - dragged_light.width / 2;

            unmarkOldTrafficLightSquare(sourceCoord, controlledCoord);

            if (isValidTrafficLightPlacement(sourceCoord, controlledCoord)) {
                internalTrafficLight.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
                internalTrafficLight.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);
                internalTrafficLight.valid = true;

                drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
            } else {
                internalTrafficLight.sourceCoord = null;
                internalTrafficLight.controlledCoord = null;
                internalTrafficLight.valid = false;

                if (draggedObjectOnGrid(e, dragged_light)) {
                        image.transform('t' + lightX + ',' + lightY + ' s-1,1');
                } else {
                    internalTrafficLight.destroy();
                }
            }

            $(document)
            .off('mousemove', handleDraggableTrafficLightsDragging)
            .off('mouseup mouseleave', handleDraggableTrafficLightsMouseUp);

            $(dragged_light.elem).remove();
            $(clone).appendTo(dragged_light.parent);
        }

        $(document)
        .on('mouseup mouseleave', handleDraggableTrafficLightsMouseUp)
        .on('mousemove', handleDraggableTrafficLightsDragging);
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

                // Check if start or house node
                if (isOriginCoordinate(coord)) {
                    markAsBackground(originNode.coordinate);
                    originNode = null;
                }
                if (isHouseCoordinate(coord)) {
                    markAsBackground(houseNodes[houseNodes.indexOf(coord)]);
                    houseNodes.splice(houseNodes.indexOf(ocargo.Node.findNodeByCoordinate(coordMap, nodes)), 1);
                }

                //  Check if any traffic lights present
                for (var i = trafficLights.length-1; i >= 0;  i--) {
                    var trafficLight  =  trafficLights[i];
                    if (node === trafficLight.sourceNode || node === trafficLight.controlledNode) {
                        trafficLights.splice(i, 1);
                        trafficLight.destroy();
                    }
                }

                //  Check if any cows present
                for (var i = cows.length-1; i >= 0;  i--) {
                    var cow  =  cows[i];
                    if (node === cow.controlledNode) {
                        cows.splice(i, 1);
                        cow.destroy();
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
        } else {
            for (x = strikeStart.x; x >= strikeEnd.x; x--) {
                func(x, strikeStart.y);
            }
        }

        if (strikeStart.y <= strikeEnd.y) {
            for (y = strikeStart.y + 1; y <= strikeEnd.y; y++) {
                func(strikeEnd.x, y);
            }
        } else {
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
        let newType = currentTheme == THEMES.city ? ocargo.Cow.PIGEON : ocargo.Cow.WHITE;

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

        const animalSource = theme == THEMES.city ? "/static/game/image/pigeon.svg" : "/static/game/image/Clarice.svg";

        $('#cow').each(function(index, element) {
            element.src = animalSource;
        })

        $('#animals_label').each(function(index, element) {
            element.innerHTML = theme == THEMES.city ? "Pigeons" : "Cows";
        })

        for (let [key, value] of Object.entries(cowGroups)) {
            value["type"] = theme == THEMES.city ? ocargo.Cow.PIGEON : ocargo.Cow.WHITE;
        }

        for (let i = 0; i < cows.length; i++) {
            cows[i].updateTheme();
        }

        const pigeonHTML = `<svg class="block_image"><g transform="translate(10,0)" <path="" class="blocklyPathDark" fill="#496684" d="m 0,0 H 111.34375 v 30 H 0 V 20 c 0,-10 -8,8 -8,-7.5 s 8,2.5 8,-7.5 z
                            "><path class="blocklyPath" stroke="none" fill="#5b80a5" d="m 0,0 H 111.34375 v 30 H 0 V 20 c 0,-10 -8,8 -8,-7.5 s 8,2.5 8,-7.5 z
                            "></path><path class="blocklyPathLight" stroke="#8ca6c0" d="m 0.5,0.5 H 110.84375 M 110.84375,0.5 M 0.5,29.5 V 18.5 m -7.36,-0.5 q -1.52,-5.5 0,-11 m 7.36,1 V 0.5 H 1
                            "></path><text class="blocklyText" y="12.5" transform="translate(10,5)">pigeons</text><g transform="translate(71.34375,5)"><image height="20px" width="30px" xlink:href="/static/game/image/pigeon.svg" alt=""></image></g></g></svg>`;

        const cowHTML = `<svg class="block_image"><g transform="translate(10,0)" <path="" class="blocklyPathDark" fill="#496684" d="m 0,0 H 93.40625 v 30 H 0 V 20 c 0,-10 -8,8 -8,-7.5 s 8,2.5 8,-7.5 z
                            "><path class="blocklyPath" stroke="none" fill="#5b80a5" d="m 0,0 H 93.40625 v 30 H 0 V 20 c 0,-10 -8,8 -8,-7.5 s 8,2.5 8,-7.5 z
                            "></path><path class="blocklyPathLight" stroke="#8ca6c0" d="m 0.5,0.5 H 92.90625 M 92.90625,0.5 M 0.5,29.5 V 18.5 m -7.36,-0.5 q -1.52,-5.5 0,-11 m 7.36,1 V 0.5 H 1
                            "></path><text class="blocklyText" y="12.5" transform="translate(10,5)">cows</text><g transform="translate(53.40625,5)"><image height="20px" width="30px" xlink:href="/static/game/image/Clarice.svg" alt=""></image></g></g></svg>`;

        $("#cow_crossing_image").html(newType == ocargo.Cow.PIGEON ? pigeonHTML : cowHTML);
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

        var cowsData = [];

        var cowGroupData = {};
        for( var i = 0; i < cows.length; i++){
            if(cows[i].valid) {
                var groupId = cows[i].data.group.id;
                if(!cowGroupData[groupId]) {
                    cowGroupData[groupId] = {minCows : cowGroups[groupId].minCows,
                        maxCows : cowGroups[groupId].maxCows,
                        potentialCoordinates : [],
                        type: cowGroups[groupId].type}; //editor can only add white cow for now
                }

                var coordinates = cows[i].coordinate;
                var strCoordinates = {'x':coordinates.x, 'y':coordinates.y};
                cowGroupData[groupId].potentialCoordinates.push(strCoordinates);
            }
        }

        for(var groupId in cowGroupData) {
            cowsData.push(cowGroupData[groupId]);
        }

        state.cows = JSON.stringify(cowsData);

        // Create block data
        state.blocks = [];
        for (i = 0; i < BLOCKS.length; i++) {
            var type = BLOCKS[i];
            if ($('#' + type + "_checkbox").is(':checked')) {
                var block = {'type': type};
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
        state.decor = ocargo.utils.sortObjects(state.decor, "z");

        // Destination and origin data
        if (houseNodes.length > 0) {
            state.destinations = JSON.stringify(houseNodes.map(function (houseNode) {
                return [houseNode.coordinate.x, houseNode.coordinate.y]
            }));
        }
        if (originNode) {
            var originCoord = originNode.coordinate;
            var nextCoord = originNode.connectedNodes[0].coordinate;
            var direction = originCoord.getDirectionTo(nextCoord);
            state.origin = JSON.stringify({coordinate: [originCoord.x, originCoord.y], direction: direction});
        }

        // Starting fuel of the level
        state.max_fuel = $('#max_fuel').val();

        // Language data
        var language = $('#language_select').val();
        state.blockly_enabled = language === 'blockly' || language === 'both' || language === 'blocklyWithPythonView';
        state.python_view_enabled = language === 'blocklyWithPythonView';
        state.python_enabled = language === 'python' || language === 'both';

        const regex = /^[\w.?!', ]*$/;
        const subtitleValue = $('#subtitle').val();
        const descriptionValue = $('#description').val();
        const hintValue = $('#hint').val();

        // Description and hint data
        if (subtitleValue.length > 0) {
            if (regex.exec(subtitleValue)) {
                state.subtitle = subtitleValue;
            }
            else {
                ocargo.Drawing.startPopup(
                    "Oh no!",
                    "You used some invalid characters for your level subtitle.",
                    "Try saving your level again using only" +
                    " letters, numbers and standard punctuation."
                );
                return
            }
        }

        if (descriptionValue.length > 0) {
            if (regex.exec(descriptionValue)) {
                state.lesson = descriptionValue;
            }
            else {
                ocargo.Drawing.startPopup(
                    "Oh no!",
                    "You used some invalid characters for your level description.",
                    "Try saving your level again using only" +
                    " letters and numbers and standard punctuation."
                );
                return
            }
        }

        if (hintValue.length > 0) {
            if (regex.exec(hintValue)) {
                state.hint = hintValue;
            }
            else {
                ocargo.Drawing.startPopup(
                    "Oh no!",
                    "You used some invalid characters for your level hint.",
                    "Try saving your level again using only" +
                    " letters and numbers and standard punctuation."
                );
                return
            }
        }

        // Other data
        state.theme = currentTheme.id;
        state.character = $('#character_select').val();
        state.disable_algorithm_score = true;

        return state;
    }

    function restoreState(state) {
        console.log("restoring state");

        // Get character id from saved character name
        var characterName = state.character_name;
        if (characterName) {
            var characterId = null;
            for (var id in CHARACTERS) {
                if (characterName == CHARACTERS[id].name) {
                    characterId = id;
                    break;
                }
            }
        }
        clear();

        // Load node data
        nodes = ocargo.Node.parsePathData(JSON.parse(state.path));

        // Load traffic light data
        var trafficLightData = JSON.parse(state.traffic_lights);
        for (var i = 0; i < trafficLightData.length; i++) {
            new InternalTrafficLight(trafficLightData[i]);
        }

        // Load in destination and origin nodes
        if (state.destinations) {
            var houses = JSON.parse(state.destinations);
            var houseCoordinates = houses.map(function (house) {
                return new ocargo.Coordinate(house[0], house[1]);
            })
            houseNodes = houseCoordinates.map(function (houseCoord) {
                return ocargo.Node.findNodeByCoordinate(houseCoord, nodes);
            })
        }

        if (state.origin) {
            var origin = JSON.parse(state.origin);
            var originCoordinate = new ocargo.Coordinate(origin.coordinate[0], origin.coordinate[1]);
            originNode = ocargo.Node.findNodeByCoordinate(originCoordinate, nodes);
        }

        // Load in character
        $('#character_select').val(characterId);
        $('#character_select').change();

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
            decorObject.setPosition(decor[i].x + PAPER_PADDING,
                                    PAPER_HEIGHT - currentTheme.decor[decor[i].decorName].height - decor[i].y + PAPER_PADDING);
        }

        //Load in cow data
        if(COW_LEVELS_ENABLED) {
            var cowGroupData = JSON.parse(state.cows);
            for (var i = 0; i < cowGroupData.length; i++) {
                // Add new group to group select element
                if (i >= Object.keys(cowGroups).length) {
                    addCowGroup();
                }
                var cowGroupId = Object.keys(cowGroups)[i];
                cowGroups[cowGroupId].minCows = cowGroupData[i].minCows;
                cowGroups[cowGroupId].maxCows = cowGroupData[i].maxCows;
                cowGroups[cowGroupId].type = cowGroupData[i].type;

                if (cowGroupData[i].potentialCoordinates != null) {
                    for (var j = 0; j < cowGroupData[i].potentialCoordinates.length; j++) {
                        var cowData = {
                            coordinates: [cowGroupData[i].potentialCoordinates[j]],
                            group: cowGroups[cowGroupId]
                        };
                        new InternalCow(cowData);
                    }
                }
            }

            // Trigger change listener on cow group select box to set initial min/max values
            $('#cow_group_select').change();

            markCowNodes();
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

        // Load in language data
        var languageSelect = $('#language_select');
        if (state.blockly_enabled && state.python_view_enabled){
            languageSelect.val('blocklyWithPythonView');
        } else if(state.blockly_enabled && state.python_enabled) {
            languageSelect.val('both');
        } else if(state.python_enabled) {
            languageSelect.val('python');
        } else {
            languageSelect.val('blockly');
        }
        languageSelect.change();

        // Load in description and hint data
        $('#subtitle').val(state.subtitle);
        $('#description').val(state.lesson);
        $('#hint').val(state.hint);

        // Other data
        if(state.max_fuel) {
            $('#max_fuel').val(state.max_fuel);
        }

        needsApproval = state.needs_approval;
    }

    function loadLevel(levelID) {
        saving.retrieveLevel(levelID, function(err, level, owned) {
            if (err !== null) {
                console.error(err);
                return;
            }

            restoreState(level, true);

            saveState.loaded(owned, extractState(), level.id);
        });
    }

    function saveLevel(name, levelId, callback) {
        var level = extractState();
        level.name = name;

        ownedLevels.save(level, levelId, callback);
    }

    function isLevelValid() {
        // Check to see if a road has been created
	if (nodes === undefined || nodes.length == 0) {
        var noRoad = interpolate(
            gettext('In %(map_icon)s%(map_label)s menu, click on %(add_road_icon)s%(add_road_label)s. Draw a road by clicking ' +
                'on a square then dragging to another square.'
            ), {
                map_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/map.svg', 'popupIcon'),
                map_label: '<b>' + gettext('Map') + '</b>',
                add_road_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/add_road.svg', 'popupIcon'),
                add_road_label: '<b>' + gettext('Add road') + '</b>'
            },
            true
        );
	    ocargo.Drawing.startPopup(gettext('Oh no!'), gettext('You forgot to create a road.'), noRoad);
             return false;
	}
	// Check to see if start and end nodes have been marked
        if (!originNode) {
            var noStart = interpolate(
                gettext('In %(map_icon)s%(map_label)s menu, click on %(mark_start_icon)s%(mark_start_label)s ' +
                    'and then select the square where you want the road to start.'
                ), {
                    map_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/map.svg', 'popupIcon'),
                    map_label: '<b>' + gettext('Map') + '</b>',
                    mark_start_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/origin.svg', 'popupIcon'),
                    mark_start_label: '<b>' + gettext('Mark start') + '</b>',
                },
                true
            );
             ocargo.Drawing.startPopup(gettext('Oh no!'), gettext('You forgot to mark the start point.'), noStart);
             return false;
        }

        if (houseNodes.length === 0) {
            var noHouses = interpolate(
                gettext('In %(map_icon)s%(map_label)s menu, click on %(add_house_icon)s%(add_house_label)s ' +
                    'and then select the square(s) where you want to add houses for delivery.'
                ), {
                    map_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/map.svg', 'popupIcon'),
                    map_label: '<b>' + gettext('Map') + '</b>',
                    add_house_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/add_house.svg', 'popupIcon'),
                    add_house_label: '<b>' + gettext('Add house') + '</b>'
                },
                true
            );
            ocargo.Drawing.startPopup(gettext('Oh no!'), gettext('You forgot to mark the houses.'), noHouses);
            return false;
        }

        // Check to see if path exists from start to each house
        if (!areDestinationsReachable(originNode, houseNodes, nodes)) {
            ocargo.Drawing.startPopup(gettext('Something is wrong...'),
                                      gettext('There is no way to get from the start to all of your houses.'),
                                      gettext('Edit your level to allow the driver to get to the end.'));
            return false;
        }

        // Check to see if at least one block selected
        // (not perfect but ensures that they don't think the blockly toolbar is broken)
        if($(".block_checkbox:checked").length == 0) {
            var noBlocks = interpolate(
                gettext('Go to %(code_icon)s%(code_label)s and select some to use. Remember to include the move and turn ' +
                    'commands!'
                ), {
                    code_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/blockly.svg', 'popupIcon'),
                    code_label: '<b>' + gettext('Code') + '</b>'
                },
                true
            );
            ocargo.Drawing.startPopup(gettext('Something is wrong...'),
                                      gettext('You haven\'t selected any blocks to use in your level'),
                                      noBlocks);
            return false;
        }

        return true;
    }

    function hasLevelChangedSinceSave() {
        var currentState = JSON.stringify(extractState());
        return saveState.hasChanged(currentState)
    }

    function canShare() {
        if (!saveState.isSaved()) {
            ocargo.Drawing.startPopup("Sharing", "", "Please save your level before continuing!");
            return false;
        } else if (hasLevelChangedSinceSave()) {
            ocargo.Drawing.startPopup("Sharing", "", "Please save your latest changes!");
            return false;
        } else if (needsApproval) {
            ocargo.Drawing.startPopup("Sharing", "", "Your teacher hasn't approved your level so you can't share it yet. Please let your teacher know they need to approve it first.")
            return false;
        }
        return true;
    }

    function isLevelOwned() {
        if (!saveState.isOwned()) {
            ocargo.Drawing.startPopup(gettext('Sharing'), '',
                gettext('You do not own this level. If you would like to share it you will first have to save your own copy!')
            );
            return false;
        }
        return true;
    }

    function isLoggedIn(activity) {
        if (USER_STATUS !== "SCHOOL_STUDENT" && USER_STATUS !== "TEACHER" && USER_STATUS !== "INDEPENDENT_STUDENT") {
            var getNotLoggedInMessage = function() {
                var notLoggedInMessages = [];
                switch (activity) {
                    case 'save':
                        notLoggedInMessages.push(gettext('Unfortunately you need to be logged in to save levels.'));
                        break;
                    case 'load':
                        notLoggedInMessages.push(gettext('Unfortunately you need to be logged in to load levels.'));
                        break;
                    case 'share':
                        notLoggedInMessages.push(gettext('Unfortunately you need to be logged in to share levels.'));
                        break;
                }

                notLoggedInMessages.push(interpolate(gettext('You can log in as a %(student_login_url)s, '
                    + '%(teacher_login_url)s or %(independent_login_url)s.'), {
                    student_login_url: '<a href="' + Urls.student_login_access_code() + '">' + pgettext('login_url', 'student') + '</a>',
                    teacher_login_url: '<a href="' + Urls.teacher_login() + '">' + pgettext('login_url', 'teacher') + '</a>',
                    independent_login_url: '<a href="' + Urls.independent_student_login() + '">'
                        + pgettext('login_url', 'independent student') + '</a>'
                }, true));
                return notLoggedInMessages.join(' ');
            };

            ocargo.Drawing.startPopup(gettext('Not logged in'), '', getNotLoggedInMessage());
            return false;
        }
        return true;
    }

    function isIndependentStudent() {
        if (USER_STATUS === "INDEPENDENT_STUDENT") {
            ocargo.Drawing.startPopup(gettext('Sharing as an independent student'), '', gettext(
              'Sorry but as an independent student you\'ll need to join a school or club to share your levels with others.'
            ));
            return false;
        }
        return true;
    }

    function getLevelTextForDjangoMigration() {
        // Put a call to this function in restoreState and you should get a string
        // you can copy and paste into a Django migration file
        var state = extractState();

        var boolFields = ["python_enabled", "blockly_enabled", 'fuel_gauge'];
        var stringFields =  ['path', 'traffic_lights', 'cows', 'origin', 'destinations'];
        var otherFields = ['max_fuel'];

        var decor = null;
        var blocks = null;

        var string = "levelNUMBER = Level(\n";
        string += "\t\tname='NUMBER',\n";
        string += "\t\tdefault=True,\n";

        for(var propertyName in state) {
            if(propertyName === 'decor') {
                decor = JSON.stringify(state[propertyName]);
            } else if(propertyName === 'blocks') {
                blocks = JSON.stringify(state[propertyName]);
            } else if(propertyName === 'character') {
                string += "\t\tcharacter=Character.objects.get(id='" + state[propertyName] + "'),\n";
            } else if(propertyName === 'theme') {
                string += "\t\ttheme=Theme.objects.get(id=" + state[propertyName] + "),\n";
            } else if(stringFields.indexOf(propertyName) != -1) {
                string += "\t\t" + propertyName + "='" + state[propertyName] + "',\n";
            } else if(boolFields.indexOf(propertyName) != -1) {
                string += "\t\t" + propertyName + "=" + (state[propertyName] ? "True" : "False") + ",\n";
            } else if(otherFields.indexOf(propertyName) != -1) {
                string += "\t\t" + propertyName + "=" + state[propertyName] + ",\n";
            } else {
                console.log("DISCARDING " + propertyName)
            }
        }
        string += "\t\tmodel_solution=FILL_IN,\n";
        string += "\t)\n";
        string += "\tlevelNUMBER.save()\n";
        string += "\tset_decor(levelNUMBER, json.loads('" + decor + "'))\n";
        string += "\tset_blocks(levelNUMBER, json.loads('" + blocks + "'))\n";

        console.log("Copy this to a Django Migration file:\n" + string);
        return string;
    }

    /*****************************************/
    /* Internal cow representation */
    /*****************************************/

    function InternalCow(data) {
        this.data = data;

        this.getData = function() {
            if (!this.valid) {
                throw "Error: cannot create actual cow from invalid internal cow!";
            }
            // Where the cow is placed.
            var coordinates = this.coordinate;
            var strCoordinates= {'x':coordinates.x, 'y':coordinates.y};

            return { "coordinates": [strCoordinates],
                "groupId" : this.data.group.id
            };

        };

        this.setCoordinate = function(){

        };

        this.destroy = function() {
            this.image.remove();
            var index = cows.indexOf(this);
            if (index !== -1) {
                cows.splice(index, 1);
            }

        };

        this.isOnRoad = function() {
            return this.coordinate && ocargo.Node.findNodeByCoordinate(this.coordinate, nodes);
        }

        this.updateTheme = function() {
            let newType = currentTheme == THEMES.city ? ocargo.Cow.PIGEON : ocargo.Cow.WHITE;
            let transformDimensions = this["image"]["_"]["transform"][0]
            let rotateDimensions = this["image"]["_"]["transform"][1]
            let x = transformDimensions[1]
            let y = transformDimensions[2]
            let r = 0;
            if (rotateDimensions) {
                r = rotateDimensions[1];
            }

            this.image.remove();

            this.image = drawing.createCowImage(newType);
            if (this.isOnRoad()) {
                let controlledNode = ocargo.Node.findNodeByCoordinate(coordinates, nodes);
                drawing.setCowImagePosition(this.coordinate, this.image, controlledNode);
            } else {
                this.image.transform("t" + x + "," + y + " r" + r);
            }

            setupCowListeners(this);
        }

        this.image = drawing.createCowImage(data.group.type);
        this.valid = false;

        if ( data.coordinates && data.coordinates.length > 0 ) {
            this.coordinate = new ocargo.Coordinate(data.coordinates[0].x, data.coordinates[0].y);
            this.valid = isValidDraggedCowPlacement(this.coordinate, this);

            if (this.isOnRoad()) {
                const controlledNode = ocargo.Node.findNodeByCoordinate(this.coordinate, nodes);
                drawing.setCowImagePosition(this.coordinate, this.image, controlledNode);
            } else {
                const box = this.image.getBBox();
                // calculate position of the image
                const paperX = (this.coordinate.x + 1) * GRID_SPACE_SIZE - box.width/2;
                const paperY = (GRID_HEIGHT - this.coordinate.y) * GRID_SPACE_SIZE - box.height/2;
                this.image.transform('t' + paperX + ',' + paperY );
            }
        } else {
            this.image.transform('...t' + (-paper.scrollLeft())  +  ',' +  paper.scrollTop());
        }

        setupCowListeners(this);
        this.image.attr({'cursor':'pointer'});
        this.image.attr({'position': 'absolute'});
        cows.push(this);

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
        this.image = drawing.createTrafficLightImage(imgStr);
        this.image.transform('...s-1,1');

        this.valid = false;

        if (data.sourceCoordinate && data.direction) {
            var sourceCoordinate = new ocargo.Coordinate(data.sourceCoordinate.x, data.sourceCoordinate.y);
            var controlledCoordinate = sourceCoordinate.getNextInDirection(data.direction);

            this.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoordinate, nodes);
            this.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoordinate, nodes);

            if (this.controlledNode && this.sourceNode) {
                this.valid = true;
                drawing.setTrafficLightImagePosition(this.sourceNode.coordinate, this.controlledNode.coordinate, this.image);
            }
        } else {
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
                            'x': Math.floor(bBox.x) - PAPER_PADDING,
                            'y': PAPER_HEIGHT - bBox.height - Math.floor(bBox.y) + PAPER_PADDING,
                            'z': currentTheme.decor[this.decorName].z_index,
                            'decorName': this.decorName
                        };
            return data;
        };

        this.setPosition = function(x, y) {
            this.image.transform('t' + x + ',' + y);
        };

        this.updateTheme = function() {
            var description = currentTheme.decor[this.decorName];
            var newImage = drawing.createImage(description.url, 0, 0, description.width,
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
    new ocargo.LevelEditor(LEVEL);
    var subtitle = interpolate(
        gettext('Click %(help_icon)s%(help_label)s for clues on getting started.'), {
            help_icon: ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/help.svg', 'popupHelp'),
            help_label: '<b>' + gettext('Help') + '</b>'
        },
        true
    );
    if (LEVEL === null){
        ocargo.Drawing.startPopup(gettext('Welcome to the Level editor!'), subtitle, '');
    } else {
        let buttons = '';
        buttons += ocargo.button.dismissButtonHtml("edit_button", "Edit");
        buttons += ocargo.button.redirectButtonHtml("play_button", Urls.levels() + "custom/" + LEVEL, "Play");

        ocargo.Drawing.startPopup(
            gettext('Welcome back!'),
            gettext('Would you like to edit or play with your design?'),
            '',
            false,
            buttons,
          );
    }

});
