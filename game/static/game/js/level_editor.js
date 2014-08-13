'use strict';

var ocargo = ocargo || {};

ocargo.LevelEditor = function() {
    
    /*************/
    /* Constants */
    /*************/

    var LIGHT_RED_URL = '/static/game/image/trafficLight_red.svg';
    var LIGHT_GREEN_URL = '/static/game/image/trafficLight_green.svg';

    var VALID_LIGHT_COLOUR = '#87E34D';
    var INVALID_LIGHT_COLOUR = '#E35F4D';

    var ADD_ROAD_MODE = 'Add road';
    var DELETE_ROAD_MODE = 'Delete road';
    var MARK_DESTINATION_MODE = 'Mark destination';
    var MARK_ORIGIN_MODE = 'Mark origin';
    var DELETE_DECOR_MODE = 'Delete decor';

    /*********/
    /* State */
    /*********/

    ocargo.saving = new ocargo.Saving();
    ocargo.drawing = new ocargo.Drawing();

    // Level information
    var nodes = [];
    var decor = [];
    var trafficLights = [];
    var originNode = null;
    var destinationNode = null;
    var currentTheme = null;

    // Reference to the Raphael elements for each square
    var grid = initialiseVisited();

    // Current mode the user is in
    var mode = ADD_ROAD_MODE;

    // Holds the state for when the user is drawing or deleting roads
    var strikeStart = null;

    // setup the toolbox
    setupToolbox();

    // initialises paper
    setTheme(THEMES["grass"])
    drawAll();

    /***************/
    /* Setup tools */
    /***************/
    // Sets up the left hand side toolbox (listeners/images etc.)

    function setupToolbox() {
        setupTabListeners();
        setupBlocksTab();
        setupDecorTab();
        setupMapTab();
        setupGenerateTab();
        setupLoadTab();
        setupSaveTab();
        setupHelpTab();

        /** Adds listeners to control the transitioning between tabs  **/
        function setupTabListeners() {
            var tabPanes = $('.tab_pane');
            var lastTabSelected = null;

            $('.tab.selectable input[type=radio]').each(function(tabIndex) {
                $(this).change(function() {
                    lastTabSelected = $(this);
                    tabPanes.each(function(tabPaneIndex) {
                        var status = (tabIndex === tabPaneIndex ? 'block' : 'none');
                        $(this).css({display: status});
                    });
                });
            });
            $('#map_radio').change();
            $('#map_radio').prop('checked', true);
        
            $('#quit_radio').change(function() {
                window.location.href = "/game/";
            });

            $("#play_radio").click(function() {

                function oldPathToNew() {
                    var newPath = [];

                    for (var i = 0; i < nodes.length; i++) {
                        var curr = nodes[i];
                        var node = {'coordinate': [curr.coordinate.x, curr.coordinate.y], 'connectedNodes': []};

                        for(var j = 0; j < curr.connectedNodes.length; j++) {
                            var index = ocargo.Node.findNodeIndexByCoordinate(curr.connectedNodes[j].coordinate, nodes);
                            node.connectedNodes.push(index);
                        }
                        newPath.push(node);
                    }
                    return newPath;
                };

                function stripOutImageProperty(objects) {
                    var newObjects = [];
                    for(var i = 0; i < objects.length; i++) {
                        var newObject = {};
                        for (var property in objects[i])  {
                            if (property !== "image") {
                                newObject[property] = objects[i][property];
                            }
                        }
                        newObjects.push(newObject);
                    }
                    return newObjects;
                }

                // Check to see if start and end nodes have been marked
                if (!originNode || !destinationNode) {
                     ocargo.Drawing.startPopup(ocargo.messages.ohNo, ocargo.messages.noStartOrEndSubtitle, ocargo.messages.noStartOrEnd);
                     lastTabSelected.prop('checked', true);
                     return;
                }

                // Check to see if path exists from start to end
                var destination = new ocargo.Destination(0, destinationNode);
                var pathToDestination = getOptimalPath(nodes, [destination]);
                if (pathToDestination.length === 0) {
                    ocargo.Drawing.startPopup(ocargo.messages.somethingWrong, ocargo.messages.noStartEndRouteSubtitle, 
                        ocargo.messages.noStartEndRoute);
                    return;
                }

                // Create node data
                sortNodes(nodes);
                var delinkedNodes = oldPathToNew(nodes);
                var nodeData = JSON.stringify(delinkedNodes);

                // Create traffic light data
                var trafficLightData = [];
                for(var i = 0; i < trafficLights.length; i++) {
                    var tl =  trafficLights[i];
                    if(tl.valid) {
                        trafficLightData.push(tl.getData());
                    }
                }
                trafficLightData = JSON.stringify(trafficLightData);

                // Create block data
                var blockData = [];
                for(var i = 0; i < BLOCKS.length; i++) {
                    var type = BLOCKS[i];
                    if($('#' + type + "_checkbox").is(':checked')) {
                        blockData.push(type);
                    }
                }
                blockData = JSON.stringify(blockData);
                
                // Create decor data
                var decorData = [];
                for(var i = 0; i < decor.length; i++) {
                    decorData.push(decor[i].getData());
                }
                decorData = JSON.stringify(decorData);


                // Create other data
                var destinationCoord = destinationNode.coordinate;
                var destinations = JSON.stringify([[destinationCoord.x, destinationCoord.y]]);
                var maxFuel = $('#max_fuel').val();
                var name = $('#level_name').val();

                // TODO character data
                

                var data = {nodes: nodeData,
                        trafficLights: trafficLightData,
                        blockTypes: blockData,
                        decor: decorData,
                        destinations: destinations,
                        theme: currentTheme.name,
                        name: name,
                        maxFuel: maxFuel}

                ocargo.saving.saveLevel(data, function(err, level_id) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }
                    window.location.href = "/game/" + level_id;
                });
            });
        }

        function setupMapTab() {
            $('#clear').click(function() {
                new ocargo.LevelEditor();
            });

            $('#start').click(function() {
                mode = MARK_ORIGIN_MODE;
            });

            $('#end').click(function() {
                mode = MARK_DESTINATION_MODE;
            });

            $('#add_road').click(function() {
                mode = ADD_ROAD_MODE;
            });

            $('#delete_road').click(function() {
                mode = DELETE_ROAD_MODE;
            });
        }

        /* Hacky, if a way can be found without initialising the entire work space that would be great */
        function setupBlocksTab() {

            function addListenerToImage(type) {
                $('#' + type + '_image').click(function() {
                    $('#' + type + '_checkbox').click();
                });
            }

            initCustomBlocksDescription();

            var blockly = document.getElementById('blockly');
            var toolbox = document.getElementById('toolbox');
            Blockly.inject(blockly, {
                path: '/static/game/js/blockly/',
                toolbox: toolbox,
                trashcan: true
            });

            for(var i = 0; i < BLOCKS.length; i++) {
                var type = BLOCKS[i];
                var block = Blockly.Block.obtain(Blockly.mainWorkspace, type);
                block.initSvg();
                block.render();

                var svg = block.getSvgRoot();
                var large = type == "controls_whileUntil" || 
                            type == "controls_repeat" ||
                            type == "controls_if" ||
                            type == "declare_proc";

                var content = '<svg class="block_image' + (large ? ' large' : '') + '">';
                content += '<g transform="translate(10,0)"';
                content += svg.innerHTML + '</g></svg>';

                $('#' + type + '_image').html(content);

                addListenerToImage(type);
            }

            $('#blockly').css('display','none');
        }

        function setupDecorTab() {

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
                new InternalTrafficLight({"redDuration": 3, "greenDuration": 3, 
                                                            "startTime": 0, "startingState": ocargo.TrafficLight.RED,
                                                            "controlledNode": -1, "sourceNode": -1});
            });

            $('#trafficLightGreen').click(function() {
                new InternalTrafficLight({"redDuration": 3, "greenDuration": 3, 
                                                            "startTime": 0, "startingState": ocargo.TrafficLight.GREEN,
                                                            "controlledNode": -1, "sourceNode": -1});
            });

            $('#delete_decor').click(function() {
                mode = DELETE_DECOR_MODE;
                console.log("Hi");
            });
        }

        function setupGenerateTab() {
            $('#generate').click(function() {
                $.ajax({
                    url: "/game/level_editor/level/random",
                    type: "POST",
                    dataType: 'json',
                    data: {
                        numberOfTiles: $('#size').val(),
                        branchiness: $('#branchiness').val()/10,
                        loopiness: $('#loopiness').val()/10,
                        curviness: $('#curviness').val()/10,
                        trafficLightsEnabled: true,
                        csrfmiddlewaretoken: $("#csrfmiddlewaretoken").val()
                    },

                    success: function (mapData) {
                        clear()

                        var path = JSON.parse(mapData.path);
                        for (var i = 0; i < path.length; i++) {
                            var node = new ocargo.Node(new ocargo.Coordinate(path[i].coordinate[0], path[i].coordinate[1]));
                            nodes.push(node);
                        }

                        for (var i = 0; i < path.length; i++) {
                            nodes[i].connectedNodes = [];
                            for(var j = 0; j < path[i].connectedNodes.length; j++) {
                                nodes[i].connectedNodes.push(nodes[path[i].connectedNodes[j]]);
                            }
                        }

                        // TODO add in support for multiple destinations
                        var destination = JSON.parse(mapData.destinations)[0];
                        var destinationCoord = new ocargo.Coordinate(destination[0], destination[1]);
                        destinationNode = ocargo.Node.findNodeByCoordinate(destinationCoord, nodes);
                        originNode = nodes[0];

                        var tls = JSON.parse(mapData.traffic_lights);
                        for(var i = 0; i < tls.length; i++) {
                            new InternalTrafficLight(tls[i]);
                        }

                        drawAll();
                    },
                    error: function (xhr, errmsg, err) {
                        console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
                    }
                });
            });
        }

        function setupLoadTab() {
            var selectedLevel = null;

            $('#own_levels_radio').change(function() {
                $('#loadOwnLevelTable').css('display','table');
                $('#loadSharedLevelTable').css('display','none');
            });

            $('#shared_levels_radio').change(function() {
                $('#loadOwnLevelTable').css('display','none');
                $('#loadSharedLevelTable').css('display','table');
            });

            $('#own_levels_radio').change();


            $('#load_radio').click(function() {
                // Disable the button to stop users clicking it multiple times
                // whilst waiting for the table data to load
                ocargo.saving.retrieveListOfLevels(function(err, ownLevels, sharedLevels) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }

                    populateTable("loadOwnLevelTable", ownLevels);

                    // Add click listeners to all rows
                    $('#loadOwnLevelTable td').on('click', function(event) {
                        var rowSelected = $(event.target.parentElement);
                        $('#loadOwnLevelTable tr').css('background-color', '#FFFFFF');
                        $('#loadSharedLevelTable tr').css('background-color', '#FFFFFF');
                        rowSelected.css('background-color', '#C0C0C0');
                        $('#loadLevel').removeAttr('disabled');
                        $('#deleteLevel').removeAttr('disabled');
                        selectedLevel = rowSelected.attr('value');
                    });

                    populateTable("loadSharedLevelTable", sharedLevels);

                    // Add click listeners to all rows
                    $('#loadSharedLevelTable td').on('click', function(event) {
                        var rowSelected = $(event.target.parentElement);
                        $('#loadOwnLevelTable tr').css('background-color', '#FFFFFF');
                        $('#loadSharedLevelTable tr').css('background-color', '#FFFFFF');
                        rowSelected.css('background-color', '#C0C0C0');
                        $('#loadLevel').removeAttr('disabled');
                        $('#deleteLevel').removeAttr('disabled');
                        selectedLevel = rowSelected.attr('value');
                    });

                    // But disable all the modal buttons as nothing is selected yet
                    selectedLevel = null;
                    $('#loadLevel').attr('disabled', 'disabled');
                    $('#deleteLevel').attr('disabled', 'disabled');
                });
            });

            $('#loadLevel').click(function() {
                if(!selectedLevel)
                {
                    return;
                }

                ocargo.saving.retrieveLevel(selectedLevel, function(err, level) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }

                    clear();

                    // Load node data
                    nodes = ocargo.Node.parsePathData(JSON.parse(level.path));

                    // Load traffic light data
                    var trafficLightData = JSON.parse(level.traffic_lights);
                    for(var i = 0; i < trafficLightData.length; i++) {
                        new InternalTrafficLight(trafficLightData[i]);
                    }

                    // Load in the decor data
                    var decorData = JSON.parse(level.decor);
                    for(var i = 0; i < decorData.length; i++) {
                        var decorObject = new InternalDecor(decorData[i].name);
                        decorObject.setCoordinate(decorData[i].coordinate);
                    }

                    // Load other data
                    originNode = nodes[0];
                    // TODO needs to be fixed in the long term with multiple destinations
                    var destinationList = $.parseJSON(level.destinations)[0];
                    var destinationCoordinate = new ocargo.Coordinate(destinationList[0],destinationList[1]);
                    destinationNode = ocargo.Node.findNodeByCoordinate(destinationCoordinate, nodes);

                    var themeID = JSON.parse(level.theme);
                    for(var theme in THEMES) {
                        if(THEMES[theme]['id'] == themeID) {
                            setTheme(THEMES[theme]);
                        }
                    }

                    drawAll();
                });
            });

            $('#deleteLevel').click(function() {
                if(!selectedLevel) 
                {
                    return;
                }

                ocargo.saving.deleteLevel(selectedLevel, function(err) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }

                    $('#loadOwnLevelTable tr[value=' + selectedLevel + ']').remove();
                    selectedLevel = null;
                });
            });
        }

        function setupSaveTab() {
            var selectedLevel = null;

            $('#save_radio').click(function() {
                ocargo.saving.retrieveListOfLevels(function(err, ownLevels, sharedLevels) {
                    if (err != null) {
                        console.debug(err);
                        return;
                    }

                    populateTable("saveLevelTable", ownLevels);

                    // Add click listeners to all rows
                    $('#saveLevelTable td').on('click', function(event) {
                        var rowSelected = $(event.target.parentElement);
                        $('#saveLevelTable tr').css('background-color', '#FFFFFF');
                        rowSelected.css('background-color', '#C0C0C0');
                        $('#saveLevel').removeAttr('disabled');
                        selectedLevel = rowSelected.attr('value');

                        for(var i = 0; i < ownLevels.length; i++) {
                            if(ownLevels[i].id == selectedLevel) {
                                $("#levelNameInput").val(ownLevels[i].name);
                            }
                        }
                    });

                    selectedLevel = null;
                });
            });

            $('#saveLevel').click(function() {
                var newName = $('#levelNameInput').val();
                if (newName && newName != "") {
                    var table = $("#saveLevelTable");
                    for (var i = 0; i < table[0].rows.length; i++) {
                         var cell = table[0].rows[i].cells[0];
                         var wName = cell.innerHTML;
                         if(wName == newName) {
                            deleteLevel(cell.attributes[0].value, 
                                            function(err, level) {
                                                if (err != null) {
                                                    console.debug(err);
                                                    return;
                                                }
                                            });
                         }
                    }

                    ocargo.saving.createNewLevel(newName, ocargo.blocklyControl.serialize(), function(err) {
                        if (err != null) {
                            console.debug(err);
                            return;
                        }
                    });
                }
            });
        }

        function setupHelpTab() {
            $('#help.tab_pane').html(ocargo.messages.levelEditorHelpText);
        }


        function populateTable(tableName, levels) {
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
            table.append('<tr>  <th>Name</th>   <th>Owner</th>  <th>Shared</th> </tr>')
            for (var i = 0, ii = levels.length; i < ii; i++) {
                var level = levels[i];
                table.append('<tr value=' + level.id + '>  <td>' + level.name + '</td>  <td>' + level.owner + '</td> <td>false</td>');
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
        return coordinate.x >= 0 && coordinate.x < GRID_WIDTH && coordinate.y >= 0 && coordinate.y < GRID_HEIGHT;
    }

    function canPlaceCFC(node) {
        return node.connectedNodes.length <= 1;
    }


    /*************/
    /* Rendering */
    /*************/

    function clear() {
        for(var i = 0; i < trafficLights.length; i++) {
            trafficLights[i].destroy();
        }
        trafficLights = [];
        decor = [];
        nodes = [];
        grid = initialiseVisited();
        strikeStart = null;
        originNode = null;
        destinationNode = null;

        ocargo.drawing.clearPaper();
    }

    function drawAll() {
        createGrid(paper);
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
        for(var i = 0; i < trafficLights.length; i++) {
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
    };

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
        if(originNode) {
            markAsOrigin(originNode.coordinate);
        }
        if(destinationNode) {
            markAsDestination(destinationNode.coordinate);
        }

        bringTrafficLightsToFront();
        bringDecorToFront();
    };

    function markTentativeRoad(currentEnd) {
        clearMarkings();
        applyAlongStrike(setup, currentEnd);

        var previousNode = null;
        function setup(x, y) {
            var coordinate = new ocargo.Coordinate(x, y);
            var node = new ocargo.Node(coordinate);
            if(previousNode)
            {
                node.addConnectedNodeWithBacklink(previousNode);
            }
            previousNode = node;
            markAsSelected(coordinate);
        }
    };

    /***************************/
    /* Paper interaction logic */
    /***************************/

    function handleMouseDown(this_rect) {
        return function () {
            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x / GRID_SPACE_SIZE, getBBox.y / GRID_SPACE_SIZE);
            var coordMap = ocargo.Drawing.translate(coordPaper);
            var existingNode = ocargo.Node.findNodeByCoordinate(coordMap, nodes);

            if(mode === MARK_ORIGIN_MODE && existingNode && canPlaceCFC(existingNode)) 
            {
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
            } 
            else if (mode === MARK_DESTINATION_MODE && existingNode) 
            {    
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

            } 
            else if (mode === ADD_ROAD_MODE || mode === DELETE_ROAD_MODE) {
                strikeStart = coordMap;
                markAsSelected(coordMap);
            }
        }
    }

    function handleMouseOver(this_rect) {
        return function() {
            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x / 100, getBBox.y / 100);
            var coordMap = ocargo.Drawing.translate(coordPaper);

            if (mode === ADD_ROAD_MODE || mode === DELETE_ROAD_MODE) 
            {
                if(strikeStart !== null)
                {
                    markTentativeRoad(coordMap);
                }
                else if(!isOriginCoordinate(coordMap) && !isDestinationCoordinate(coordMap))
                {
                    markAsHighlighted(coordMap);
                }
            }
            else if(mode === MARK_ORIGIN_MODE || mode === MARK_DESTINATION_MODE)
            {
                var node = ocargo.Node.findNodeByCoordinate(coordMap, nodes);
                if (node && destinationNode !== node && originNode !== node) 
                {
                    if(mode === MARK_DESTINATION_MODE)
                    {
                        mark(coordMap, 'blue', 0.3, true); 
                    }
                    else if(canPlaceCFC(node))
                    {
                        mark(coordMap, 'red', 0.5, true);
                    }
                }
            } 
        }
    }

    function handleMouseOut(this_rect) {
        return function() {
            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE, getBBox.y/GRID_SPACE_SIZE);
            var coordMap = ocargo.Drawing.translate(coordPaper);

            if(mode === MARK_ORIGIN_MODE || mode === MARK_DESTINATION_MODE) 
            {
                var node = ocargo.Node.findNodeByCoordinate(coordMap, nodes);
                if (node && destinationNode !== node && originNode !== node) 
                {
                    markAsBackground(coordMap);
                }
            }
            else if(mode === ADD_ROAD_MODE || mode === DELETE_ROAD_MODE)
            {
                if(!isOriginCoordinate(coordMap) && !isDestinationCoordinate(coordMap))
                {
                    markAsBackground(coordMap);
                }
            }
        }
    }

    function handleMouseUp(this_rect) {
        return function() {
            if (mode === ADD_ROAD_MODE || mode === DELETE_ROAD_MODE) {
                var getBBox = this_rect.getBBox();
                var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE, getBBox.y/GRID_SPACE_SIZE);
                var coordMap = ocargo.Drawing.translate(coordPaper);

                if (mode === DELETE_ROAD_MODE) 
                {
                    finaliseDelete(coordMap);
                } 
                else 
                {
                    finaliseMove(coordMap);
                }

                sortNodes(nodes);
                redrawRoad();
            }
        }
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

            // Stop it being dragged off the edge of the page
            if(paperX < 0) {
                paperX = 0;
            }
            else if(paperX + imageWidth > paperWidth) {
                paperX = paperWidth - imageWidth;
            }
            if(paperY < 0) {
                paperY =  0;
            }
            else if(paperY + imageHeight >  paperHeight) {
                paperY = paperHeight - imageHeight;
            }

            image.transform('t' + paperX + ',' + paperY);
        };

        function onDragStart(x, y) {
            var bBox = image.getBBox();
            imageWidth = bBox.width;
            imageHeight = bBox.height;

            var paperPosition = $('#paper').position();
            originX = x - paperPosition.left - imageWidth/2;
            originY = y - paperPosition.top - imageHeight/2;
        
            paperWidth = GRID_WIDTH * GRID_SPACE_SIZE;
            paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE;
        };

        function onDragEnd() {
            originX = paperX;
            originY = paperY;
        };

        image.drag(onDragMove, onDragStart, onDragEnd);

        image.click(function() {
            if(mode === DELETE_DECOR_MODE) {
                decor.destroy();
            }
        });
    };

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
            moved = dx != 0 || dy != 0;

            // Update image's position
            paperX = dx + originX;
            paperY = dy + originY;

            // Stop it being dragged off the edge of the page
            if(paperX < 0) {
                paperX = 0;
            }
            else if(paperX + imageWidth > paperWidth) {
                paperX = paperWidth - imageWidth;
            }
            if(paperY < 0) {
                paperY =  0;
            }
            else if(paperY + imageHeight >  paperHeight) {
                paperY = paperHeight - imageHeight;
            }
            
            // Adjust for the fact that we've rotated the image
            if(rotation == 90 || rotation == 270)  {
                paperX += (imageWidth - imageHeight)/2;
                paperY -= (imageWidth - imageHeight)/2;
            }

            // And perform the updatee
            image.transform('t' + paperX + ',' + paperY + 'r' + rotation + 's' + scaling);


            // Unmark the squares the light previously occupied
            if(sourceCoord) {
                markAsBackground(sourceCoord);
            }
            if(controlledCoord) {
                markAsBackground(controlledCoord);
            }
            if(originNode) {
                markAsOrigin(originNode.coordinate);
            }
            if(destinationNode) {
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
            if(!isCoordinateOnGrid(controlledCoord)) {
                controlledCoord = null;
            }

            // If source node is not on grid remove it
            if(!isCoordinateOnGrid(sourceCoord)) {
                sourceCoord = null;
            }

            if(sourceCoord && controlledCoord) {
                var colour;
                if(canGetFromSourceToControlled(sourceCoord, controlledCoord))
                {
                    // Valid placement
                    colour = VALID_LIGHT_COLOUR;
                    ocargo.drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
                }
                else
                {
                    // Invalid placement
                    colour = INVALID_LIGHT_COLOUR;
                }

                mark(controlledCoord, colour, 0.7, false);
                mark(sourceCoord, colour, 0.7, false);
            }
        };

        function onDragStart(x, y) {
            moved = false;

            scaling = getScaling(image);
            rotation = (image.matrix.split().rotate + 360) % 360;
            
            var bBox = image.getBBox();
            imageWidth = bBox.width;
            imageHeight = bBox.height;

            paperWidth = GRID_WIDTH * GRID_SPACE_SIZE;
            paperHeight = GRID_HEIGHT * GRID_SPACE_SIZE;

            var paperPosition = $('#paper').position();

            var mouseX = x - paperPosition.left;
            var mouseY = y - paperPosition.top;

            originX = mouseX - imageWidth/2;
            originY = mouseY - imageHeight/2;
        };

        function onDragEnd() {
            if(moved) {
                // Unmark squares currently occupied
                if(sourceCoord) {
                    markAsBackground(sourceCoord);
                }
                if(controlledCoord) {
                    markAsBackground(controlledCoord);
                }
                if(originNode) {
                    markAsOrigin(originNode.coordinate);
                }
                if(destinationNode) {
                    markAsDestination(destinationNode.coordinate);
                }

                // Add back to the list of traffic lights if on valid nodes
                if(canGetFromSourceToControlled(sourceCoord, controlledCoord)) {
                    var sourceIndex = ocargo.Node.findNodeIndexByCoordinate(sourceCoord, nodes);
                    var controlledIndex = ocargo.Node.findNodeIndexByCoordinate(controlledCoord, nodes);
                    trafficLight.valid = true;
                    trafficLight.sourceNode = sourceIndex;
                    trafficLight.controlledNode = controlledIndex;

                    ocargo.drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
                }
            }

            image.attr({'cursor':'pointer'});
        };

        image.drag(onDragMove, onDragStart, onDragEnd);
        
        image.dblclick(function() {
            image.transform('...r90');
        });

        image.click(function() {
            if(mode === DELETE_DECOR_MODE) {
                trafficLight.destroy();
            }
        });

        function getScaling(object) {
            var transform = object.transform();
            for(var i = 0; i < transform.length; i++) {
                if(transform[i][0] === 's') {
                    return transform[i][1] + ',' + transform[i][2];
                }
            }
            return "0,0";
        }

        function canGetFromSourceToControlled(sourceCoord, controlledCoord) {
            var sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, nodes);
            var controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, nodes);

            if(sourceNode && controlledNode) {
                for(var i = 0; i < sourceNode.connectedNodes.length; i++) {
                    if(sourceNode.connectedNodes[i] === controlledNode) {
                        return true;
                    }
                }
            }
            return false;
        }
    };

    /********************************/
    /* Miscaellaneous state methods */
    /********************************/

    function initialiseVisited() {
        var visited = new Array(10);
        for (var i = 0; i < 10; i++) {
            visited[i] = new Array(8);
        }
        return visited;
    };

    function createGrid() {
        grid = ocargo.drawing.renderGrid(currentTheme);

        for(var i = 0; i < grid.length; i++) {
            for(var j = 0; j < grid[i].length; j++) {
                grid[i][j].node.onmousedown = handleMouseDown(grid[i][j]);
                grid[i][j].node.onmouseover = handleMouseOver(grid[i][j]);
                grid[i][j].node.onmouseout = handleMouseOut(grid[i][j]);
                grid[i][j].node.onmouseup = handleMouseUp(grid[i][j]);
                grid[i][j].node.ontouchstart = handleMouseDown(grid[i][j]);
                grid[i][j].node.ontouchmove = handleMouseOver(grid[i][j]);
                grid[i][j].node.ontouchend = handleMouseUp(grid[i][j]);
            }
        }
    }

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
            if(node) {
                // Remove all the references to the node we're removing.
                for (var i = node.connectedNodes.length - 1; i >= 0; i--) {
                    node.removeDoublyConnectedNode(node.connectedNodes[i]);
                }
                var index = nodes.indexOf(node);
                nodes.splice(index, 1);
            }

            // Check if start or destination node        
            if(isOriginCoordinate(coord)) {
                markAsBackground(originNode.coordinate);
                originNode = null;
            }
            if(isDestinationCoordinate(coord)) {
                markAsBackground(destinationNode.coordinate);
                destinationNode = null;
            }     
        }
    };

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
            else
            {
                // If we've overwritten the origin node remove it as 
                // we can no longer place the CFC there
                if(node === originNode) {
                    markAsBackground(originNode.coordinate);
                    originNode = null;
                }
            }

            // Now connect it up with it's new neighbours
            if(previousNode && node.connectedNodes.indexOf(previousNode) == -1) {
                node.addConnectedNodeWithBacklink(previousNode);
            }
            previousNode = node;
        }
    };

    function applyAlongStrike(func, strikeEnd) {
        if (strikeStart.x <= strikeEnd.x) {
            for (var x = strikeStart.x; x <= strikeEnd.x; x++) {
                func(x, strikeStart.y);
            }
        } 
        else {
            for (var x = strikeStart.x; x >= strikeEnd.x; x--) {
                func(x, strikeStart.y);
            }
        }

        if (strikeStart.y <= strikeEnd.y) {
            for (var y = strikeStart.y + 1; y <= strikeEnd.y; y++) {
                func(strikeEnd.x, y);
            }
        } 
        else {
            for (var y = strikeStart.y - 1; y >= strikeEnd.y; y--) {
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

        for(var i = 0; i < decor.length; i++) {
            decor[i].updateTheme();
        }

        $('.decor_button').each(function(index, element) {
            element.src = theme.decor[element.id].url;
        });

        $('#wrapper').css({'background-color': theme.background});
    }

    function sortNodes(nodes) {
        for (var i = 0; i < nodes.length; i++) {
            // Remove duplicates.
            var newConnected = []
            for (var j = 0; j < nodes[i].connectedNodes.length; j++) {
                if (newConnected.indexOf(nodes[i].connectedNodes[j]) === -1) {
                    newConnected.push(nodes[i].connectedNodes[j]);
                }
            }
            nodes[i].connectedNodes.sort(function(a, b) { return comparator(a, b, nodes[i])}).reverse();
        }

        function comparator(node1, node2, centralNode) {
            var a1 = ocargo.calculateNodeAngle(centralNode, node1);
            var a2 = ocargo.calculateNodeAngle(centralNode, node2)
            if (a1 < a2) {
                return -1;
            } else if (a1 > a2) {
                return 1;
            } else {
                return 0;
            }
        }
    }

    /*****************************************/
    /* Internal traffic light representation */
    /*****************************************/

    function InternalTrafficLight(data) {
        this.redDuration = data.redDuration;
        this.greenDuration = data.greenDuration;
        this.startTime = data.startTime;
        this.startingState = data.startingState;
        this.controlledNode = data.controlledNode;
        this.sourceNode = data.sourceNode;

        this.valid = false;

        var imgStr = this.startingState == ocargo.TrafficLight.RED ? LIGHT_RED_URL : LIGHT_GREEN_URL;
        this.image = ocargo.drawing.createTrafficLightImage(imgStr);
        this.image.transform('...s-1,1');

        if(this.controlledNode != -1 && this.sourceNode != -1) {
            var sourceCoord = nodes[this.sourceNode].coordinate;
            var controlledCoord = nodes[this.controlledNode].coordinate;
            this.valid = true;
            ocargo.drawing.setTrafficLightImagePosition(sourceCoord, controlledCoord, this.image);
        }

        setupTrafficLightListeners(this);
        this.image.attr({'cursor':'pointer'});

        trafficLights.push(this);
    }

    InternalTrafficLight.prototype.getData = function() {
        if(!this.valid) {
            throw "Error: cannot create actual traffic light from invalid internal traffic light!";
        }

        return {"redDuration": this.redDuration, "greenDuration": this.greenDuration,
                "sourceNode": this.sourceNode, "controlledNode": this.controlledNode,
                "startTime": this.startTime, "startingState": this.startingState};
    }

    InternalTrafficLight.prototype.destroy = function() {
        this.image.remove();
        var index = trafficLights.indexOf(this);
        if(index != -1) {
            trafficLights.splice(index, 1);       
        }
    }

    /*********************************/
    /* Internal decor representation */
    /*********************************/

    function InternalDecor(name) {
        this.name = name;
        this.image = null;
        this.updateTheme();

        decor.push(this);
    }

    InternalDecor.prototype.getData = function() {
        var bBox = this.image.getBBox();
        return {'coordinate': new ocargo.Coordinate(bBox.x, bBox.y), 'name': this.name};
    }

    InternalDecor.prototype.setCoordinate = function(coordinate) {
        this.image.transform('t' + coordinate.x + ',' + coordinate.y);
    }

    InternalDecor.prototype.updateTheme = function() {
        var description = currentTheme.decor[this.name];
        var newImage = ocargo.drawing.createImage(description.url, 0, 0, description.width, description.height);

        if(this.image) {
            newImage.transform(this.image.matrix.toTransformString());
            this.image.remove();
        }

        this.image = newImage;
        this.image.attr({'cursor':'pointer'});
        setupDecorListeners(this);
    }

    InternalDecor.prototype.destroy = function() {
        this.image.remove();
        var index = decor.indexOf(this);
        if(index != -1) {
            decor.splice(index, 1);       
        }
    }
};

/******************/
/* Initialisation */
/******************/

$(function() {
    new ocargo.LevelEditor();
});


