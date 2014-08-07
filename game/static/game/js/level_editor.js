'use strict';

var ocargo = ocargo || {};

var DECOR_LIST = JSON.parse(DECOR);

var BUSH_URL = findDecorUrl('bush');
var TREE1_URL = findDecorUrl('tree1');
var TREE2_URL = findDecorUrl('tree2');
var POND_URL = findDecorUrl('pond');
var HOUSE_URL = findDecorUrl('house');
var CFC_URL = '/static/game/image/OcadoCFC_no_road.svg';
var LIGHT_RED_URL = '/static/game/image/trafficLight_red.svg';
var LIGHT_GREEN_URL = '/static/game/image/trafficLight_green.svg';

var VALID_LIGHT_COLOUR = "#87E34D";
var INVALID_LIGHT_COLOUR = "#E35F4D";

ocargo.LevelEditor = function() {
    this.nodes = [];
    this.start = null;
    this.end = null;
    this.currentStrike = [];
    this.decor = [];
    this.grid = this.initialiseVisited();
    this.trafficLights = [];
    this.theme = THEME;

    ocargo.saving = new ocargo.Saving();

    // The current mode
    this.mode = ocargo.LevelEditor.ADD_ROAD_MODE;

    // type: Node
    this.originNode = null;
    this.destinationNode = null;

    // setup listeners
    setupBlocksTab();
    setupTabListeners();
    setupToolboxListeners();
    setupLoadSaveListeners();
    setupOtherMenuListeners();

    // initialises paper
    this.drawAll();
};

ocargo.LevelEditor.ADD_ROAD_MODE = 0;
ocargo.LevelEditor.DELETE_ROAD_MODE = 1;
ocargo.LevelEditor.MARK_END_MODE = 2;
ocargo.LevelEditor.MARK_START_MODE = 3;
ocargo.LevelEditor.DELETE_DECOR_MODE = 4;

ocargo.LevelEditor.prototype.initialiseVisited = function() {
    var visited = new Array(10);
    for (var i = 0; i < 10; i++) {
        visited[i] = new Array(8);
    }
    return visited;
};

ocargo.LevelEditor.prototype.createGrid = function(paper) {
    for (var i = 0; i < GRID_WIDTH; i++) {
        for (var j = 0; j < GRID_HEIGHT; j++) {
            var x = i * GRID_SPACE_SIZE;
            var y = j * GRID_SPACE_SIZE;
            var segment = paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
            segment.attr({stroke: BORDER, fill: BACKGROUND_COLOR, "fill-opacity": 1});

            segment.node.onmousedown = function() {
                var this_rect = segment;
                return handleMouseDown(this_rect, segment);
            } ();

            segment.node.onmouseover = function() {
                var this_rect = segment;
                return handleMouseOver(this_rect, segment);
            } ();

            segment.node.onmouseout = function() {
                var this_rect = segment;
                return handleMouseOut(this_rect, segment);
            } ();

            segment.node.onmouseup = function() {
                var this_rect = segment;
                return handleMouseUp(this_rect, segment);
            } ();

            segment.node.ontouchstart = function() {
                var this_rect = segment;
                return handleMouseDown(this_rect, segment);
            } ();

            segment.node.ontouchmove = function() {
                var this_rect = segment;
                return handleMouseOver(this_rect, segment);
            } ();

            segment.node.ontouchend = function() {
                var this_rect = segment;
                return handleMouseUp(this_rect, segment);
            } ();

            this.grid[i][j] = segment;
        }
    }
};

ocargo.LevelEditor.prototype.finaliseDelete = function(coord) {
    var x, y;
    if (this.start.x <= coord.x) {
        for (x = this.start.x; x <= coord.x; x++) {
            deleteNode(x, this.start.y);
        }
    } 
    else {
        for (x = this.start.x; x >= coord.x; x--) {
            deleteNode(x, this.start.y);
        }
    }

    if (this.start.y <= coord.y) {
        for (y = this.start.y + 1; y <= coord.y; y++) {
            deleteNode(coord.x, y);
        }
    } 
    else {
        for (y = this.start.y - 1; y >= coord.y; y--) {
            deleteNode(coord.x, y);
        }
    }

    // Delete any nodes made isolated through deletion
    for (var i = ocargo.levelEditor.nodes.length - 1; i >= 0; i--) {
        if (ocargo.levelEditor.nodes[i].connectedNodes.length === 0) {
            var coordinate = ocargo.levelEditor.nodes[i].coordinate;
            deleteNode(coordinate.x, coordinate.y);
        }
    }

    this.currentStrike = [];
    this.start = null;

    function deleteNode(x, y) {
        var coord = new ocargo.Coordinate(x, y);
        var node = ocargo.Node.findNodeByCoordinate(coord, ocargo.levelEditor.nodes);
        if (node) {
            // Remove all the references to the node we're removing.
            for (var i = node.connectedNodes.length - 1; i >= 0; i--) {
                node.removeDoublyConnectedNode(node.connectedNodes[i]);
            }
            var index = ocargo.levelEditor.nodes.indexOf(node);
            ocargo.levelEditor.nodes.splice(index, 1);
        }

        // Check if start or destination node        
        if (ocargo.levelEditor.isOriginCoordinate(coord)) {
            ocargo.levelEditor.markAsBackground(ocargo.levelEditor.originNode.coordinate);
            ocargo.levelEditor.originNode = null;
        }
        if (ocargo.levelEditor.isDestinationCoordinate(coord)) {
            ocargo.levelEditor.markAsBackground(ocargo.levelEditor.destinationNode.coordinate);
            ocargo.levelEditor.destinationNode = null;
        }     
    }
};

ocargo.LevelEditor.prototype.finaliseMove = function() {
    for (var i = 0; i < ocargo.levelEditor.currentStrike.length; i++) {
        var current = ocargo.levelEditor.currentStrike[i];

        var existingNode = ocargo.Node.findNodeByCoordinate(current.coordinate, this.nodes);
        if (existingNode) {
            // If a node already exists at that coordinate, find the 
            // existing node's new neighbours and connect them.
            var newNeighbours = [];
            for (var j = 0; j < current.connectedNodes.length; j++) {
                var neighbour = current.connectedNodes[j];
                if (!ocargo.Node.findNodeByCoordinate(neighbour.coordinate, existingNode.connectedNodes)) {
                    existingNode.addConnectedNodeWithBacklink(neighbour);
                    newNeighbours.push(neighbour);
                }
            }

            // Remove connections to the current node as it has been
            // replaced by the existing node
            for (var k = 0; k < newNeighbours.length; k++) {
                newNeighbours[k].removeDoublyConnectedNode(current);
            }

            // If we've overwritten the origin node remove it as 
            // we can no longer place the CFC there
            if(existingNode === ocargo.levelEditor.originNode) {
                ocargo.levelEditor.markAsBackground(ocargo.levelEditor.originNode.coordinate);
                ocargo.levelEditor.originNode = null;
            }
        } 
        else {
            this.nodes.push(current);
        }
    }
    this.start =  null;
    this.currentStrike = [];
};

ocargo.LevelEditor.prototype.findTrafficLight = function(firstIndex, secondIndex) {
    var light;
    for (var i = 0; i < this.trafficLights.length; i++) {
        light = this.trafficLights[i];
        if (light.node === firstIndex && light.sourceNode === secondIndex) {
            return i;
        }
    }
    return -1;
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


function findDecorDimensions(decorName) {
    var list = DECOR_LIST;
    for (var i = 0; i < list.length; i++) {
        if (list[i].name === decorName) {
            return {"width": list[i].width, "height": list[i].height};
        }
    }
    return null;
}

function findDecorUrl(decorName) {
    var list = DECOR_LIST;
    for (var i = 0; i < list.length; i++) {
        if (list[i].name === decorName) {
            return list[i].url;
        }
    }
    return null;
}

/************************/
/** Current state tests */
/************************/

// Functions simply to improve readability of complex conditional code
ocargo.LevelEditor.prototype.isOriginCoordinate = function(coordinate) {
    return this.originNode && this.originNode.coordinate.equals(coordinate);
}

ocargo.LevelEditor.prototype.isDestinationCoordinate = function(coordinate) {
    return this.destinationNode && this.destinationNode.coordinate.equals(coordinate);
}

ocargo.LevelEditor.prototype.isCoordinateOnGrid = function(coordinate) {
    return coordinate.x >= 0 && coordinate.x < GRID_WIDTH && coordinate.y >= 0 && coordinate.y < GRID_HEIGHT;
}

ocargo.LevelEditor.prototype.inAddRoadMode = function() {
    return this.mode === ocargo.LevelEditor.ADD_ROAD_MODE;
}

ocargo.LevelEditor.prototype.inDeleteRoadMode = function() {
    return this.mode === ocargo.LevelEditor.DELETE_ROAD_MODE;
}

ocargo.LevelEditor.prototype.inMarkStartMode = function() {
    return this.mode === ocargo.LevelEditor.MARK_START_MODE;
}

ocargo.LevelEditor.prototype.inMarkEndMode = function() {
    return this.mode === ocargo.LevelEditor.MARK_END_MODE;
}

ocargo.LevelEditor.prototype.inDeleteDecorMode = function() {
    return this.mode == ocargo.LevelEditor.DELETE_DECOR_MODE;
}

ocargo.LevelEditor.prototype.canPlaceCFC = function(node) {
    return node.connectedNodes.length <= 1;
}

/*************/
/* Rendering */
/*************/

ocargo.LevelEditor.prototype.clear = function() {
    for(var i = 0; i < this.trafficLights.length; i++) {
        this.trafficLights[i].destroy();
    }
    this.trafficLights = [];
    this.decor = [];
    this.nodes = [];
    this.grid = this.initialiseVisited();
    this.start = null;
    this.end = null;
    this.originNode = null;
    this.destinationNode = null;
    this.currentStrike = [];

    paper.clear();
}

ocargo.LevelEditor.prototype.drawAll = function() {
    this.createGrid(paper);
    this.redrawRoad();
}

ocargo.LevelEditor.prototype.redrawRoad = function() {
    createRoad(this.nodes);
    this.clearMarkings();
    this.bringTrafficLightsToFront();
    this.bringDecorToFront();
}

ocargo.LevelEditor.prototype.bringDecorToFront = function() {
    for (var i = 0; i < this.decor.length; i++) {
        this.decor[i].image.toFront();
    }
}

ocargo.LevelEditor.prototype.bringTrafficLightsToFront = function() {
    for(var i = 0; i < this.trafficLights.length; i++) {
        this.trafficLights[i].image.toFront();
    }
}

function initialiseTrafficLight(state) {
    new ocargo.LevelEditor.InternalTrafficLight({"redDuration": 3, "greenDuration": 3, 
                                                 "startTime": 0, "startingState": state,
                                                 "controlledNode": -1, "sourceNode": -1});
}

function initialiseDecorGraphic(url, name) {
    new ocargo.LevelEditor.InternalDecor({"url": url, "coordinate": null}, name);
}

/************/
/*  Marking */
/************/

ocargo.LevelEditor.prototype.mark = function(coordMap, colour, opacity, occupied) {
    var coordPaper = translate(coordMap);
    var element = this.grid[coordPaper.x][coordPaper.y];
    element.attr({fill:colour, "fill-opacity": opacity});
};

ocargo.LevelEditor.prototype.markAsOrigin = function(coordinate) {
    this.mark(coordinate, 'red', 0.7, true);
}

ocargo.LevelEditor.prototype.markAsDestination = function(coordinate) {
    this.mark(coordinate, 'blue', 0.7, true);
}

ocargo.LevelEditor.prototype.markAsBackground = function(coordinate) {
    this.mark(coordinate, BACKGROUND_COLOR, 0, false);
}

ocargo.LevelEditor.prototype.markAsSelected = function(coordinate) {
    this.mark(coordinate, SELECTED_COLOR, 1, true);
}

ocargo.LevelEditor.prototype.redrawTentativeRoad = function(coordinate) {
    this.clearMarkings();
    this.markTentativeRoad(coordinate);
};

ocargo.LevelEditor.prototype.clearMarkings = function() {
    for (var i = 0; i < GRID_WIDTH; i++) {
        for (var j = 0; j < GRID_HEIGHT; j++) {
            this.markAsBackground(new ocargo.Coordinate(i,j));
            this.grid[i][j].toFront();
        }
    }
    if(this.originNode) {
        this.markAsOrigin(this.originNode.coordinate);
    }
    if(this.destinationNode) {
        this.markAsDestination(this.destinationNode.coordinate);
    }
};

ocargo.LevelEditor.prototype.markTentativeRoad = function(coord) {
    ocargo.levelEditor.currentStrike = [new ocargo.Node(this.start)];
    ocargo.levelEditor.markAsSelected(this.start);

    if (this.start.x <= coord.x) {
        for (var x = this.start.x + 1; x <= coord.x; x++) {
            setup(x, this.start.y);
        }
    } 
    else {
        for (var x = this.start.x - 1; x >= coord.x; x--) {
            setup(x, this.start.y);
        }
    }
    if (this.start.y <= coord.y) {
        for (var y = this.start.y + 1; y <= coord.y; y++) {
            setup(coord.x, y);
        }
    } 
    else {
        for (var y = this.start.y - 1; y >= coord.y; y--) {
            setup(coord.x, y);
        }
    }

    function setup(x, y) {
        var coordinate = new ocargo.Coordinate(x, y);
        var node = new ocargo.Node(coordinate);
        var previousNode = ocargo.levelEditor.currentStrike[ocargo.levelEditor.currentStrike.length - 1];
        node.addConnectedNodeWithBacklink(previousNode);
        ocargo.levelEditor.currentStrike.push(node);
        ocargo.levelEditor.markAsSelected(coordinate);
    }
};

/****************/
/* Button setup */
/****************/

function setupTabListeners() {

    function setListenerForTab(i) {
        tabs[i].change(function() {
            for(var j = 0; j < tabs.length; j++) {
                var status = (i == j ? "block" : "none");
                tabContents[j].css({display: status});
            }
        });
    }

    var tabContents = [$('#tab-content-map'), $('#tab-content-decor'), $('#tab-content-character'), $('#tab-content-blocks'), $('#tab-content-random')]
    var tabs = [$('#tab1'), $('#tab2'), $('#tab3'), $('#tab4'), $('#tab5')];

    for(var i = 0; i < tabs.length; i++) {
        setListenerForTab(i);
    }

    tabs[0].change();
}

/* Adds blockly images to the blocks tab. Hacky, if a way can 
be found without initialising the entire work space that would
be great */
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

        var content = '<svg class="block_image' + (large ? ' large' : '') + '">' +  svg.innerHTML + '</svg>';
        $('#' + type + '_image').html(content);

        addListenerToImage(type);
    }

    $('#blockly').css('display','none');
}

function setupToolboxListeners() {
    $('#bush').click(function() {
        initialiseDecorGraphic(BUSH_URL, 'bush');
    });

    $('#tree1').click(function() {
        initialiseDecorGraphic(TREE1_URL, 'tree1');
    });

    $('#tree2').click(function() {
        initialiseDecorGraphic(TREE2_URL, 'tree2');
    });

    $('#pond').click(function() {
        initialiseDecorGraphic(POND_URL, 'pond');
    });

    $('#trafficLightRed').click(function() {
        initialiseTrafficLight(ocargo.TrafficLight.RED);
    });

    $('#trafficLightGreen').click(function() {
        initialiseTrafficLight(ocargo.TrafficLight.GREEN);
    });

    $('#clear').click(function() {
        ocargo.levelEditor = new ocargo.LevelEditor();
    });

    $('#start').click(function() {
        ocargo.levelEditor.mode = ocargo.LevelEditor.MARK_START_MODE;
    });

    $('#end').click(function() {
        ocargo.levelEditor.mode = ocargo.LevelEditor.MARK_END_MODE;
    });

    $('#add_road').click(function() {
        ocargo.levelEditor.mode = ocargo.LevelEditor.ADD_ROAD_MODE;
    });

    $('#delete_road').click(function() {
        ocargo.levelEditor.mode = ocargo.LevelEditor.DELETE_ROAD_MODE;
    });

    $('#delete_decor').click(function() {
        ocargo.levelEditor.mode = ocargo.LevelEditor.DELETE_DECOR_MODE;
    });

    $('#generate').click(function() {
        var size = $('#size').val();
        var branchiness = $('#branchiness').val()/10;
        var loopiness = $('#loopiness').val()/10;
        var curviness = $('#curviness').val()/10;

        $.ajax({
            url: "/game/level_editor/random",
            type: "POST",
            dataType: 'json',
            data: {
                numberOfTiles: size,
                branchiness: branchiness,
                loopiness: loopiness,
                curviness: curviness,
                csrfmiddlewaretoken: $("#csrfmiddlewaretoken").val()
            },

            success: function (json) {
                ocargo.levelEditor.clear();

                for (var i = 0; i < json.length; i++) {
                    var node = new ocargo.Node(new ocargo.Coordinate(json[i].coordinate[0], json[i].coordinate[1]));
                    ocargo.levelEditor.nodes.push(node);
                }

                for (var i = 0; i < json.length; i++) {
                    ocargo.levelEditor.nodes[i].connectedNodes = [];
                    for(var j = 0; j < json[i].connectedNodes.length; j++) {
                        ocargo.levelEditor.nodes[i].connectedNodes.push(ocargo.levelEditor.nodes[json[i].connectedNodes[j]]);
                    }
                }

                ocargo.levelEditor.drawAll();
            },
            error: function (xhr, errmsg, err) {
                console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    });
}

function setupLoadSaveListeners() {
    var selectedLevel = null;

    var populateTable = function(tableName, levels) {
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

    $('#load').click(function() {
        // Disable the button to stop users clicking it multiple times
        // whilst waiting for the table data to load
        $('#load').attr('disabled', 'disabled');

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

            // Finally show the modal dialog and reenable the button
            $('#loadModal').foundation('reveal', 'open');
            $('#load').removeAttr('disabled');

            // But disable all the modal buttons as nothing is selected yet
            selectedLevel = null;
            $('#loadLevel').attr('disabled', 'disabled');
            $('#deleteLevel').attr('disabled', 'disabled');
        });
    });

    $('#save').click(function() {
        // Disable the button to stop users clicking it multiple times
        // whilst waiting for the table data to load
        $('#save').attr('disabled', 'disabled');

        ocargo.saving.retrieveListOfLevels(function(err, workspaces) {
            if (err != null) {
                console.debug(err);
                return;
            }

            populateTable("saveLevelTable", workspaces);

            // Add click listeners to all rows
            $('#saveLevelTable td').on('click', function(event) {
                $('#saveLevelTable td').css('background-color', '#FFFFFF');
                $(event.target).css('background-color', '#C0C0C0');
                selectedLevel = $(event.target).attr('value');
                var workspaceName = $(event.target)[0].innerHTML;
                document.getElementById("workspaceNameInput").value = workspaceName;
            });

            // Finally show the modal dialog and reenable the button
            $('#saveModal').foundation('reveal', 'open');
            $('#save').removeAttr('disabled');

            // But disable all the modal buttons as nothing is selected yet
            selectedLevel = null;
            $('#overwriteLevel').attr('disabled', 'disabled');
        });
    });

    $('#loadLevel').click(function() {
        if (selectedLevel) {
            ocargo.saving.retrieveLevel(selectedLevel, function(err, level) {
                if (err != null) {
                    console.debug(err);
                    return;
                }

                ocargo.levelEditor.clear();

                // Load node data
                ocargo.levelEditor.nodes = ocargo.Node.parsePathData(JSON.parse(level.path));

                // Load traffic light data
                var trafficLightData = JSON.parse(level.traffic_lights);
                for(var i = 0; i < trafficLightData.length; i++) {
                    new ocargo.LevelEditor.InternalTrafficLight(trafficLightData[i]);
                }

                // TO-DO a serious amount of work
                /*
                var decorData = JSON.parse(level.decor);
                for(var i = 0; i < decorData.length; i++) {
                    new ocargo.LevelEditor.InternalDecor(decorData[i]);
                }*/

                // Load other data
                ocargo.levelEditor.originNode = ocargo.levelEditor.nodes[0];
                // TODO needs to be fixed in the long term with multiple destinations
                var destinationList = $.parseJSON(level.destinations)[0];
                var destinationCoordinate = new ocargo.Coordinate(destinationList[0],destinationList[1]);
                ocargo.levelEditor.destinationNode = ocargo.Node.findNodeByCoordinate(destinationCoordinate,
                                                                                    ocargo.levelEditor.nodes);

                ocargo.levelEditor.drawAll();

                // Close the popup
                $('#loadModal').foundation('reveal', 'close');
            });
        }
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
                $('#saveModal').foundation('reveal', 'close');
            });
        }
    });

    $('#deleteLevel').click(function() {
        if (selectedLevel) {
            ocargo.saving.deleteLevel(selectedLevel, function(err) {
                if (err != null) {
                    console.debug(err);
                    return;
                }
                $('#loadLevelTable td[value=' + selectedLevel + ']').remove();
                selectedLevel = null;
            });
        }
    });
}

function setupOtherMenuListeners() {
    $('#help').click(function() {
        var subtitle = isMobile() ? ocargo.messages.levelEditorMobileSubtitle : ocargo.messages.levelEditorPCSubtitle;
        startPopup(ocargo.messages.levelEditorTitle, subtitle, ocargo.messages.levelEditorMainText);
    });

    $("#play").click(function() {

        function oldPathToNew() {
            var newPath = [];

            for (var i = 0; i < ocargo.levelEditor.nodes.length; i++) {
                var curr = ocargo.levelEditor.nodes[i];
                var node = {'coordinate': [curr.coordinate.x, curr.coordinate.y], 'connectedNodes': []};

                for(var j = 0; j < curr.connectedNodes.length; j++) {
                    var index = ocargo.Node.findNodeIndexByCoordinate(curr.connectedNodes[j].coordinate, ocargo.levelEditor.nodes);
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
        if (!ocargo.levelEditor.originNode || !ocargo.levelEditor.destinationNode) {
             startPopup(ocargo.messages.ohNo, ocargo.messages.noStartOrEndSubtitle, ocargo.messages.noStartOrEnd);
             return;
        }

        // Check to see if path exists from start to end
        var destination = new ocargo.Destination(0, ocargo.levelEditor.destinationNode);
        var pathToDestination = getOptimalPath(ocargo.levelEditor.nodes, [destination]);
        if (pathToDestination.length === 0) {
            startPopup(ocargo.messages.somethingWrong, ocargo.messages.noStartEndRouteSubtitle, 
                ocargo.messages.noStartEndRoute);
            return;
        }

        // Create node data
        sortNodes(ocargo.levelEditor.nodes);
        var delinkedNodes = oldPathToNew(ocargo.levelEditor.nodes);
        var nodeData = JSON.stringify(delinkedNodes);

        // Create traffic light data
        var trafficLightData = [];
        for(var i = 0; i < ocargo.levelEditor.trafficLights.length; i++) {
            var tl =  ocargo.levelEditor.trafficLights[i];
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
        for(var i = 0; i < ocargo.levelEditor.decor.length; i++) {
            decor.push(ocargo.levelEditor.decor[i].getData());
        }
        decorData = JSON.stringify(decorData);


        // Create other data
        var destinationCoord = ocargo.levelEditor.destinationNode.coordinate;
        var destinations = JSON.stringify([[destinationCoord.x, destinationCoord.y]]);
        var maxFuel = $('#maxFuel').val();
        var name = $('#name').val();

        
        $.ajax({
            url: "/game/levels/new",
            type: "POST",
            dataType: 'json',
            data: {
                nodes: nodeData,
                trafficLights: trafficLightData,
                blockTypes: blockData,
                decor: decorData,
                destinations: destinations,
                theme: ocargo.levelEditor.theme,
                name: name,
                maxFuel: maxFuel,
                
                csrfmiddlewaretoken: $("#csrfmiddlewaretoken").val()
            },
            success: function (json) {
                window.location.href = ("/game/" + json.server_response);

            },
            error: function (xhr, errmsg, err) {
                console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });

        return false;
    });

    $('#quit').click(function() {
        window.location.href = "/game/"
    });
}

/******************************/
/* Paper interaction handlers */
/******************************/

function handleMouseDown(this_rect, segment) {
    return function () {
        var getBBox = this_rect.getBBox();
        var coordPaper = new ocargo.Coordinate(getBBox.x / GRID_SPACE_SIZE, getBBox.y / GRID_SPACE_SIZE);
        var coordMap = translate(coordPaper);
        var existingNode = ocargo.Node.findNodeByCoordinate(coordMap, ocargo.levelEditor.nodes);

        if(ocargo.levelEditor.inMarkStartMode() && existingNode && ocargo.levelEditor.canPlaceCFC(existingNode)) 
        {
            if (ocargo.levelEditor.originNode) {
                var prevStart = ocargo.levelEditor.originNode.coordinate;
                ocargo.levelEditor.markAsBackground(prevStart);
            }
            // Check if same as destination node
            if (ocargo.levelEditor.isDestinationCoordinate(coordMap)) {
                ocargo.levelEditor.destinationNode = null;
            }
            ocargo.levelEditor.markAsOrigin(coordMap);
            var newStartIndex = ocargo.Node.findNodeIndexByCoordinate(coordMap, ocargo.levelEditor.nodes);

            // Putting the new start in the front of the nodes list.
            var temp = ocargo.levelEditor.nodes[newStartIndex];
            ocargo.levelEditor.nodes[newStartIndex] = ocargo.levelEditor.nodes[0];
            ocargo.levelEditor.nodes[0] = temp;
            ocargo.levelEditor.originNode = ocargo.levelEditor.nodes[0];
        } 
        else if (ocargo.levelEditor.inMarkEndMode() && existingNode) 
        {    
            if (ocargo.levelEditor.destinationNode) {
                var prevEnd = ocargo.levelEditor.destinationNode.coordinate;
                ocargo.levelEditor.markAsBackground(prevEnd);
            }
            // Check if same as starting node
            if (ocargo.levelEditor.isOriginCoordinate(coordMap)) {
                ocargo.levelEditor.originNode = null;
            }
            ocargo.levelEditor.markAsDestination(coordMap);
            var newEnd = ocargo.Node.findNodeIndexByCoordinate(coordMap, ocargo.levelEditor.nodes);
            ocargo.levelEditor.destinationNode = ocargo.levelEditor.nodes[newEnd];

        } 
        else if (ocargo.levelEditor.inAddRoadMode() || ocargo.levelEditor.inDeleteRoadMode()) {
            ocargo.levelEditor.start = coordMap;
            ocargo.levelEditor.markAsSelected(coordMap);
        }
    }
}

function handleMouseOver(this_rect, segment) {
    return function() {
        var getBBox = this_rect.getBBox();
        var coordPaper = new ocargo.Coordinate(getBBox.x / 100, getBBox.y / 100);
        var coordMap = translate(coordPaper);

        if (ocargo.levelEditor.inAddRoadMode() || ocargo.levelEditor.inDeleteRoadMode()) 
        {
            if(ocargo.levelEditor.start !== null)
            {
                ocargo.levelEditor.redrawTentativeRoad(coordMap);
            }
            else if(!ocargo.levelEditor.isOriginCoordinate(coordMap) && !ocargo.levelEditor.isDestinationCoordinate(coordMap))
            {
                ocargo.levelEditor.mark(coordMap, SELECTED_COLOR, 0.3, true);
            }
        }
        else if(ocargo.levelEditor.inMarkStartMode() || ocargo.levelEditor.inMarkEndMode()) 
        {
            var node = ocargo.Node.findNodeByCoordinate(coordMap, ocargo.levelEditor.nodes);
            if (node && ocargo.levelEditor.destinationNode !== node && ocargo.levelEditor.originNode !== node) 
            {
                if(ocargo.levelEditor.inMarkEndMode())
                {
                    ocargo.levelEditor.mark(coordMap, 'blue', 0.3, true); 
                }
                else if(ocargo.levelEditor.canPlaceCFC(node))
                {
                    ocargo.levelEditor.mark(coordMap, 'red', 0.5, true);
                }
            }
        } 
    }
}

function handleMouseOut(this_rect, segment) {
    return function() {
        var getBBox = this_rect.getBBox();
        var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE, getBBox.y/GRID_SPACE_SIZE);
        var coordMap = translate(coordPaper);

        if(ocargo.levelEditor.inMarkStartMode() || ocargo.levelEditor.inMarkEndMode()) 
        {
            var node = ocargo.Node.findNodeByCoordinate(coordMap, ocargo.levelEditor.nodes);
            if (node && ocargo.levelEditor.destinationNode !== node && ocargo.levelEditor.originNode !== node) 
            {
                ocargo.levelEditor.markAsBackground(coordMap);
            }
        }
        else if(ocargo.levelEditor.inAddRoadMode() || ocargo.levelEditor.inDeleteRoadMode())
        {
            if(!ocargo.levelEditor.isOriginCoordinate(coordMap) && !ocargo.levelEditor.isDestinationCoordinate(coordMap))
            {
                ocargo.levelEditor.markAsBackground(coordMap);
            }
        }
    }
}

function handleMouseUp(this_rect, segment) {
    return function() {
        if (ocargo.levelEditor.inAddRoadMode() || ocargo.levelEditor.inDeleteRoadMode()) {
            ocargo.levelEditor.end = segment;
            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE, getBBox.y/GRID_SPACE_SIZE);
            var coordMap = translate(coordPaper);

            if (ocargo.levelEditor.inDeleteRoadMode()) 
            {
                ocargo.levelEditor.finaliseDelete(coordMap);
            } 
            else 
            {
                ocargo.levelEditor.finaliseMove(coordMap);
            }

            sortNodes(ocargo.levelEditor.nodes);

            ocargo.levelEditor.redrawRoad();
        }
    }
}

function setupDecorDragListeners(decor) {
    var image = decor.image;

    var paperX;
    var paperY;

    var originX = decor.coordinate.x;
    var originY = decor.coordinate.y;
    var mapCoordinate;

    function onDragMove(dx, dy) {
        paperX = dx + originX;
        paperY = dy + originY;

        mapCoordinate = new ocargo.Coordinate(paperX, PAPER_HEIGHT - paperY - DECOR_SIZE);
        image.transform('t' + paperX + ',' + paperY);
    };

    function onDragStart() {
        mapCoordinate = new ocargo.Coordinate(paperX, PAPER_HEIGHT - paperY - DECOR_SIZE);
    };

    function onDragEnd() {
        originX = paperX;
        originY = paperY;
    };

    image.drag(onDragMove, onDragStart, onDragEnd);
};

function setupTrafficLightDragListeners(trafficLight) {

    var image = trafficLight.image;

    // Position in map coordinates.
    var sourceCoord;                        
    var controlledCoord;

    // Current position of the element in paper coordinates
    var paperX = 0;                                 
    var paperY = 0;

    // Where the drag started in paper coordinates
    var originX = 0;                                 
    var originY = 0;

    // Orientation and rotation transformations
    var s = 0;
    var rotation = 0;

    var moved = false;
    var firstMove = false;

    function onDragMove(dx, dy) {
        // Needs to be in onDragMove, not in onDragStart, to stop clicks triggering drag behaviour
        trafficLight.valid = false;
        image.attr({'cursor':'default'});
        moved = dx != 0 || dy != 0;

        // Update image's position
        paperX = dx + originX;
        paperY = dy + originY;
        image.transform('t' + paperX + ',' + paperY + s + 'r' + rotation);

        // Unmark the squares it previously occupied
        if(sourceCoord) {
            ocargo.levelEditor.markAsBackground(sourceCoord);
        }
        if(controlledCoord) {
            ocargo.levelEditor.markAsBackground(controlledCoord);
        }

        var box = image.getBBox();
        var absX = (box.x + box.width/2) / GRID_SPACE_SIZE;
        var absY = (box.y + box.height/2) / GRID_SPACE_SIZE;

        if(rotation == 0) {
            absY += 0.5;
        }
        else if(rotation == 90) {
            absX -= 0.5;
        }
        else if(rotation == 180) {
            absY -= 0.5;
        }
        else if(rotation == 270) {
            absX += 0.5;
        }

        // Find source position in map coordinates
        var x = Math.min(Math.max(0, Math.floor(absX)), GRID_WIDTH - 1);
        var y = GRID_HEIGHT - Math.min(Math.max(0, Math.floor(absY)), GRID_HEIGHT - 1) - 1;
        sourceCoord = new ocargo.Coordinate(x,y);

        // Find controlled position in map coordinates
        
        switch(rotation) {
            case 0:
                controlledCoord = new ocargo.Coordinate(sourceCoord.x, sourceCoord.y + 1);
                break;
            case 90:
                controlledCoord = sourceCoord;
                sourceCoord = new ocargo.Coordinate(sourceCoord.x + 1, sourceCoord.y);
                break;
            case 180:
                controlledCoord = new ocargo.Coordinate(sourceCoord.x, sourceCoord.y - 1);
                break;
            case 270:
                controlledCoord = sourceCoord;
                sourceCoord = new ocargo.Coordinate(sourceCoord.x - 1, sourceCoord.y);
                break;
        }

        // If controlled node is not on grid, remove it
        if(!ocargo.levelEditor.isCoordinateOnGrid(controlledCoord)) {
            controlledCoord = null;
        }

        // If source node is not on grid remove it
        if(!ocargo.levelEditor.isCoordinateOnGrid(sourceCoord)) {
            sourceCoord = null;
        }

        if(sourceCoord && controlledCoord) {
            var colour;
            if(canGetFromSourceToControlled(sourceCoord, controlledCoord))
            {
                colour = VALID_LIGHT_COLOUR;
                setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
            }
            else
            {
                colour = INVALID_LIGHT_COLOUR;
            }

            ocargo.levelEditor.mark(controlledCoord, colour, 0.7, false);
            ocargo.levelEditor.mark(sourceCoord, colour, 0.7, false);
        }
    };

    function onDragStart(x, y) {
        moved = false;
        firstMove = true;

        s = getOrientation(image);
        rotation = getRotation(image);

        var bBox = image.getBBox();
        var paperPosition = $('#paper').position();

        originX = x - paperPosition.left - bBox.width/2;
        originY = y - paperPosition.top - bBox.height/2;

        if(rotation == 90 || rotation == 270) {
            var adjustmentForRotation = (bBox.height - bBox.width)/2;
            originX -= adjustmentForRotation;
            originY += adjustmentForRotation;
        }
    };

    function onDragEnd() {
        if(moved) {
            // Unmark squares currently occupied
            ocargo.levelEditor.markAsBackground(sourceCoord);
            ocargo.levelEditor.markAsBackground(controlledCoord);

            // Add back to the list of traffic lights if on valid nodes
            if(canGetFromSourceToControlled(sourceCoord, controlledCoord)) {
                var sourceIndex = ocargo.Node.findNodeIndexByCoordinate(sourceCoord, ocargo.levelEditor.nodes);
                var controlledIndex = ocargo.Node.findNodeIndexByCoordinate(controlledCoord, ocargo.levelEditor.nodes);
                trafficLight.valid = true;
                trafficLight.sourceNode = sourceIndex;
                trafficLight.controlledNode = controlledIndex;

                setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
            }
        }

        image.attr({'cursor':'pointer'});
    };

    image.drag(onDragMove, onDragStart, onDragEnd);

    function getOrientation(object) {
        var transform = object.transform();
        for(var i = 0; i < transform.length; i++) {
            if(transform[i][0] === 's') {
                return 's' + transform[i][1] + ',' + transform[i][2];
            }
        }
        return "";
    }

    function getRotation(object) {
        var ro = object.matrix.split().rotate;
        if(ro == -90  || ro == 90) {
            // Then compensate for the s -1 1, set in the initiation
            ro += 180;
        }
        return ro % 360;
    }

    function canGetFromSourceToControlled(sourceCoord, controlledCoord) {
        var sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoord, ocargo.levelEditor.nodes);
        var controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoord, ocargo.levelEditor.nodes);

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

/*****************************************/
/* Internal traffic light representation */
/*****************************************/

ocargo.LevelEditor.InternalTrafficLight = function(data) {
    this.redDuration = data.redDuration;
    this.greenDuration = data.greenDuration;
    this.startTime = data.startTime;
    this.startingState = data.startingState;
    this.controlledNode = data.controlledNode;
    this.sourceNode = data.sourceNode;

    this.valid = false;

    var imgStr = this.startingState == ocargo.TrafficLight.RED ? LIGHT_RED_URL : LIGHT_GREEN_URL;
    this.image = paper.image(imgStr, 0, 0, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT);
    this.image.transform('...s-1,1');

    if(this.controlledNode != -1 && this.sourceNode != -1) {
        var sourceCoord = ocargo.levelEditor.nodes[this.sourceNode].coordinate;
        var controlledCoord = ocargo.levelEditor.nodes[this.controlledNode].coordinate;
        this.valid = true;
        setTrafficLightImagePosition(sourceCoord, controlledCoord, this.image);
    }

    setupTrafficLightDragListeners(this);
    this.image.node.ondblclick = function() {
        this.image.transform('...r90');
    };
    this.image.attr({'cursor':'pointer'});

    ocargo.levelEditor.trafficLights.push(this);
}

ocargo.LevelEditor.InternalTrafficLight.prototype.getData = function() {
    if(!this.valid) {
        throw "Error: cannot create actual traffic light from invalid internal traffic light!";
    }

    return {"redDuration": this.redDuration, "greenDuration": this.greenDuration,
            "sourceNode": this.sourceNode, "controlledNode": this.controlledNode,
            "startTime": this.startTime, "startingState": this.startingState};
}

ocargo.LevelEditor.InternalTrafficLight.prototype.destroy = function() {
    this.image.remove();
}

/*********************************/
/* Internal decor representation */
/*********************************/

ocargo.LevelEditor.InternalDecor = function(data, name) {
    this.url = data.url;
    this.name = name;

    var dimensions = findDecorDimensions(this.name);
    this.image = paper.image(this.url, 0, 0, dimensions.width, dimensions.height);
    
    if(data.coordinate) {
        this.coordinate = data.coordinate;
    }
    else {
        var bBox = this.image.getBBox();
        this.coordinate = new ocargo.Coordinate(0, 0);
    }

    this.image.transform('t' + this.coordinate.x + ',' + this.coordinate.y);
    this.image.attr({'cursor':'pointer'});
    setupDecorDragListeners(this);
    
    ocargo.levelEditor.decor.push(this);
}

ocargo.LevelEditor.InternalDecor.prototype.getData = function() {
    return {'coordinate': coordinate, 'url': url};
}

ocargo.LevelEditor.InternalDecor.prototype.destory = function() {
    this.image.remove();
}

/******************/
/* Initialisation */
/******************/

$(function() {
    ocargo.levelEditor = new ocargo.LevelEditor();
});


