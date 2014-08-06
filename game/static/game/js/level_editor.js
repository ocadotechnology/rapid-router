'use strict';

var ocargo = ocargo || {};

var DECOR_LIST = JSON.parse(DECOR);

var BUSH_URL = findDecorUrl('bush', DECOR_LIST);
var TREE1_URL = findDecorUrl('tree1', DECOR_LIST);
var TREE2_URL = findDecorUrl('tree2', DECOR_LIST);
var POND_URL = findDecorUrl('pond', DECOR_LIST);
var HOUSE_URL = findDecorUrl('house', DECOR_LIST);
var CFC_URL = '/static/game/image/OcadoCFC_no_road.svg';
var LIGHT_RED_URL = '/static/game/image/trafficLight_red.svg';
var LIGHT_GREEN_URL = '/static/game/image/trafficLight_green.svg';


ocargo.LevelEditor = function() {
    this.nodes = [];
    this.start = null;
    this.end = null;
    this.trafficLights = [];
    this.currentStrike = [];
    this.decor = [];
    this.trafficCounter = 0;
    this.grid = this.initialiseVisited();
    this.theme = THEME;

    ocargo.saving = new ocargo.Saving();

    // Is the start, end or delete mode on?
    this.startFlag = false;
    this.endFlag = false;
    this.deleteFlag = false;

    // type: Node
    this.originNode = null;
    this.destinationNode = null;

    // setup listeners
    setupBlocksTab();
    setupTabListeners();
    setupToolboxListeners();
    setupLoadSaveListeners();
    setupOtherMenuListeners();

    // reset the paper
    this.redrawAll();
};

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

ocargo.LevelEditor.prototype.isOriginCoordinate = function(coordinate) {
    return this.originNode && this.originNode.coordinate.equals(coordinate);
}

ocargo.LevelEditor.prototype.isDestinationCoordinate = function(coordinate) {
    return this.destinationNode && this.destinationNode.coordinate.equals(coordinate);
}

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

ocargo.LevelEditor.prototype.canPlaceCFC = function(node) {
    return node.connectedNodes.length <= 1;
}

function createAndAddTrafficLightsToNodes(nodes, trafficLightData) {
    var trafficLights = [];
    for(var i = 0; i < trafficLightData.length; i++){
        var trafficLight = trafficLightData[i];
        var light = new ocargo.TrafficLight(trafficLight.id, trafficLight, nodes);
        trafficLights.push(light);
        var controlledNode = nodes[trafficLight['node']];
        controlledNode.addTrafficLight(light);
    }
    return trafficLights;
}

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

function findDecorUrl(decor, list) {
    for (var i = 0; i < list.length; i++) {
        if (list[i].name === decor) {
            return list[i].url;
        }
    }
    return -1;
}

/*************/
/* Rendering */
/*************/

ocargo.LevelEditor.prototype.redrawAll = function() {
    paper.clear();
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

function initialiseDecorGraphic(name, url, width, height) {
    var image = paper.image(url, 0, 0, width, height);
    var coord = new ocargo.Coordinate(0, PAPER_HEIGHT - DECOR_SIZE);

    image.draggableDecor(name, 0, 0);
    ocargo.levelEditor.decor.push({'coordinate': new ocargo.Coordinate(0,0), 'name': name, 'image': image});    
}

function initialiseTrafficLight(red) {
    var imgStr = red ? LIGHT_RED_URL : LIGHT_GREEN_URL;
    var image = paper.image(imgStr, 0, 0, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT);

    setupTrafficLightDragListeners(image, ocargo.levelEditor.trafficCounter, red);
    image.node.ondblclick = function() {
        return image.transform('...r90');
    };

    ocargo.levelEditor.trafficCounter++;
    image.transform('...s-1,1');
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

    var tabContents = [$('#tab-content-map'), $('#tab-content-decor'), $('#tab-content-blocks'), $('#tab-content-random')]
    var tabs = [$('#tab1'), $('#tab2'), $('#tab3'), $('#tab4')];

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
        initialiseDecorGraphic('bush', BUSH_URL, 70, 70);
    });

    $('#tree1').click(function() {
        initialiseDecorGraphic('tree1', TREE1_URL, 100, 100);
    });

    $('#tree2').click(function() {
        initialiseDecorGraphic('tree2', TREE2_URL, 100, 100);
    });

    $('#pond').click(function() {
        initialiseDecorGraphic('pond', POND_URL, 150, 100);
    });

    $('#trafficLightRed').click(function() {
        initialiseTrafficLight(true);
    });

    $('#trafficLightGreen').click(function() {
        initialiseTrafficLight(false);
    });

    $('#clear').click(function() {
        ocargo.levelEditor = new ocargo.LevelEditor();
    });

    $('#start').click(function() {
        ocargo.levelEditor.startFlag = true;
        ocargo.levelEditor.endFlag = false;
        ocargo.levelEditor.deleteFlag = false;
    });

    $('#end').click(function() {
        ocargo.levelEditor.startFlag = false;
        ocargo.levelEditor.endFlag = true;
        ocargo.levelEditor.deleteFlag = false;
    });

    $('#add').click(function() {
        ocargo.levelEditor.startFlag = false;
        ocargo.levelEditor.endFlag = false;
        ocargo.levelEditor.deleteFlag = false;
    });

    $('#delete').click(function() {
        ocargo.levelEditor.startFlag = false;
        ocargo.levelEditor.endFlag = false;
        ocargo.levelEditor.deleteFlag = true;
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
                ocargo.levelEditor.nodes = [];

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

                ocargo.levelEditor.redrawAll();
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

        ocargo.saving.retrieveListOfLevels(function(err, levels) {
            if (err != null) {
                console.debug(err);
                return;
            }

            populateTable("loadLevelTable", levels);

            // Add click listeners to all rows
            $('#loadLevelTable tr').on('click', function(event) {
                $('#loadLevelTable tr').css('background-color', '#FFFFFF');
                $(event.target.parentElement).css('background-color', '#C0C0C0');
                $('#loadLevel').removeAttr('disabled');
                $('#deleteLevel').removeAttr('disabled');
                selectedLevel = $(event.target.parentElement).attr('value');
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

                ocargo.levelEditor.nodes = ocargo.Node.parsePathData($.parseJSON(level.path));
                ocargo.levelEditor.decor = $.parseJSON(level.decor);

                ocargo.levelEditor.trafficLights = $.parseJSON(level.traffic_lights);
                ocargo.levelEditor.trafficCounter = ocargo.levelEditor.trafficLights.length;

                ocargo.levelEditor.originNode = ocargo.levelEditor.nodes[0];
                // TODO needs to be fixed in the long term with multiple destinations
                var destinationList = $.parseJSON(level.destinations)[0];
                var destinationCoordinate = new ocargo.Coordinate(destinationList[0],destinationList[1]);
                ocargo.levelEditor.destinationNode = ocargo.Node.findNodeByCoordinate(destinationCoordinate,
                                                                                    ocargo.levelEditor.nodes);

                ocargo.levelEditor.redrawRoad();

                // Reset interface state to be safe
                ocargo.levelEditor.currentStrike = [];
                ocargo.levelEditor.start = null;
                ocargo.levelEditor.end = null
                ocargo.levelEditor.startFlag = false;
                ocargo.levelEditor.endFlag = false;
                ocargo.levelEditor.deleteFlag = false;

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

        if (ocargo.levelEditor.originNode === null || ocargo.levelEditor.destinationNode === null) {
             startPopup(ocargo.messages.ohNo, ocargo.messages.noStartOrEndSubtitle, 
                ocargo.messages.noStartOrEnd);
             return;
        }

        var destination = new ocargo.Destination(0, ocargo.levelEditor.destinationNode);
        var pathToDestination = getOptimalPath(ocargo.levelEditor.nodes, [destination]);
        if (pathToDestination.length === 0) {
            startPopup(ocargo.messages.somethingWrong, ocargo.messages.noStartEndRouteSubtitle, 
                ocargo.messages.noStartEndRoute);
            return;
        }

        sortNodes(ocargo.levelEditor.nodes);
        var input = JSON.stringify(oldPathToNew(ocargo.levelEditor.nodes));
        var blockTypes = [];
        var endCoord = ocargo.levelEditor.destinationNode.coordinate;
        var destinations = JSON.stringify([[endCoord.x, endCoord.y]]);
        var decor = JSON.stringify(stripOutImageProperty(ocargo.levelEditor.decor));
        var trafficLights = JSON.stringify(stripOutImageProperty(ocargo.levelEditor.trafficLights));
        var maxFuel = $('#maxFuel').val();
        var name = $('#name').val();

        for(var i = 0; i < BLOCKS.length; i++) {
            if($('#' + BLOCKS[i] + "_checkbox").is(':checked')) {
                blockTypes.push(BLOCKS[i]);
            }
        }

        $.ajax({
            url: "/game/levels/new",
            type: "POST",
            dataType: 'json',
            data: {
                nodes: input,
                destinations: destinations,
                decor: decor,
                trafficLights: trafficLights,
                theme: ocargo.levelEditor.theme,
                name: name,
                maxFuel: maxFuel,
                blockTypes: JSON.stringify(blockTypes),
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

        if (ocargo.levelEditor.startFlag && existingNode && ocargo.levelEditor.canPlaceCFC(existingNode)) {
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

        } else if (ocargo.levelEditor.endFlag && existingNode) {
            
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

        } else if (ocargo.levelEditor.deleteFlag ||
            !(ocargo.levelEditor.endFlag || ocargo.levelEditor.startFlag)) {
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
        var startOrEnd = ocargo.levelEditor.endFlag || ocargo.levelEditor.startFlag;

        if (ocargo.levelEditor.start !== null && !startOrEnd) {
            ocargo.levelEditor.redrawTentativeRoad(coordMap);
        }
        else {
            if(startOrEnd) {
                var node = ocargo.Node.findNodeByCoordinate(coordMap, ocargo.levelEditor.nodes);
                if (node) {
                    if(ocargo.levelEditor.endFlag)
                    {
                        if (ocargo.levelEditor.destinationNode === node ||
                            ocargo.levelEditor.originNode === node)
                        {
                            return;
                        }
                        ocargo.levelEditor.mark(coordMap, 'blue', 0.3, true); 
                    }
                    else 
                    {
                        if (ocargo.levelEditor.destinationNode === node ||
                            ocargo.levelEditor.originNode === node ||
                            !ocargo.levelEditor.canPlaceCFC(node))
                        {
                            return;
                        }
                        ocargo.levelEditor.mark(coordMap, 'red', 0.5, true);
                    }
                }
            }
            else {
                if(ocargo.levelEditor.isOriginCoordinate(coordMap) || ocargo.levelEditor.isDestinationCoordinate(coordMap))
                {
                    return;
                }
                ocargo.levelEditor.mark(coordMap, SELECTED_COLOR, 0.3, true);
            }
        } 
    }
}

function handleMouseOut(this_rect, segment) {
    return function() {
        var startOrEnd = ocargo.levelEditor.endFlag || ocargo.levelEditor.startFlag;
        var getBBox = this_rect.getBBox();
        var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE, getBBox.y/GRID_SPACE_SIZE);
        var coordMap = translate(coordPaper);

        if(startOrEnd) {
            var node = ocargo.Node.findNodeByCoordinate(coordMap, ocargo.levelEditor.nodes);
            if (node) {
                if (ocargo.levelEditor.destinationNode === node ||
                    ocargo.levelEditor.originNode === node)
                {
                    return;
                }
                ocargo.levelEditor.markAsBackground(coordMap);
            }
        }
        else {
            if(ocargo.levelEditor.isOriginCoordinate(coordMap) || ocargo.levelEditor.isDestinationCoordinate(coordMap))
            {
                return;
            }
            ocargo.levelEditor.markAsBackground(coordMap);
        }
    }
}

function handleMouseUp(this_rect, segment) {
    return function() {
        var startOrEnd = ocargo.levelEditor.endFlag || ocargo.levelEditor.startFlag
        if (!startOrEnd) {
            ocargo.levelEditor.end = segment;
            var getBBox = this_rect.getBBox();
            var coordPaper = new ocargo.Coordinate(getBBox.x/GRID_SPACE_SIZE, getBBox.y/GRID_SPACE_SIZE);
            var coordMap = translate(coordPaper);

            if (ocargo.levelEditor.deleteFlag) {
                ocargo.levelEditor.finaliseDelete(coordMap);
            } else {
                ocargo.levelEditor.finaliseMove(coordMap);
            }

            sortNodes(ocargo.levelEditor.nodes);

            ocargo.levelEditor.redrawRoad();
        }
    }
}

Raphael.el.draggableDecor = function(name, initX, initY) {
    var image = this;
    var paperX = initX;
    var paperY = initY;
    var originX = 0;
    var originY = 0;
    var mapCoordinate;

    function onDragMove(dx, dy) {
        paperX = dx + originX;
        paperY = dy + originY;

        mapCoordinate = new ocargo.Coordinate(paperX, PAPER_HEIGHT - paperY - DECOR_SIZE);
        image.transform('t' + paperX + ',' + paperY);
    };

    function onDragStart() {
        mapCoordinate = new ocargo.Coordinate(paperX, PAPER_HEIGHT - paperY - DECOR_SIZE);

        // Find the element in decor and remove it.
        for (var i = 0; i < ocargo.levelEditor.decor.length; i++) {
            if (ocargo.levelEditor.decor[i].image === image) {
                ocargo.levelEditor.decor.splice(i, 1);
                break;
            }
        }
    };

    function onDragEnd() {
        originX = paperX;
        originY = paperY;
        ocargo.levelEditor.decor.push({'coordinate': mapCoordinate, 'name': name, 'image': image});
    };

    image.drag(onDragMove, onDragStart, onDragEnd);
};

function setupTrafficLightDragListeners(image, idIndex, red) {
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
    var s = "";
    var r = "";

    function onDragMove(dx, dy) {
        // Update image's position
        paperX = dx + originX;
        paperY = dy + originY;
        image.transform('t' + paperX + ',' + paperY + s + 'r' + r);

        // Unmark the squares it previously occupied
        if(sourceCoord) {
            ocargo.levelEditor.markAsBackground(sourceCoord);
        }
        if(controlledCoord) {
            ocargo.levelEditor.markAsBackground(controlledCoord);
        }

        // Find source position in map coordinates
        var box = image.getBBox();
        var x = Math.min(Math.max(0, Math.floor(box.x / GRID_SPACE_SIZE)), GRID_WIDTH - 1);
        var y = GRID_HEIGHT - Math.min(Math.max(0, Math.floor(box.y / GRID_SPACE_SIZE)), GRID_HEIGHT - 1) - 1;
        sourceCoord = new ocargo.Coordinate(x,y);

        // Find controlled position in map coordinates
        var rotation = getRotation(image) % 360;
        switch (rotation) {
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

        // If controlled node is not on grid remove it
        if(controlledCoord.x < 0 ||  controlledCoord.x  >=  GRID_WIDTH || 
           controlledCoord.y < 0 ||  controlledCoord.y  >=  GRID_HEIGHT) {
            controlledCoord = null;
        }

        // Mark the squares it currently occupies
        ocargo.levelEditor.mark(sourceCoord, SELECTED_COLOR, 0.7, false);
        if (controlledCoord) {
            ocargo.levelEditor.mark(controlledCoord, SELECTED_COLOR, 0.7, false);
        }
    };

    function onDragStart() {
        s = getOrientation(image);
        r = getRotation(image);

        // Find the element in trafficLights and remove it.
        var index = findTrafficLightByIndex(idIndex, ocargo.levelEditor.trafficLights);
        if (index > -1) {
            ocargo.levelEditor.trafficLights.splice(index, 1);
        }
    };

    function onDragEnd() {
        // Set origin for next drag
        originX = paperX;
        originY = paperY;

        // Unmark squares currently occupied
        ocargo.levelEditor.markAsBackground(sourceCoord);
        ocargo.levelEditor.markAsBackground(controlledCoord);

        // Add back to the list of traffic lights if on valid nodes
        var sourceIndex = ocargo.Node.findNodeIndexByCoordinate(sourceCoord, ocargo.levelEditor.nodes);
        var controlledIndex = ocargo.Node.findNodeIndexByCoordinate(controlledCoord, ocargo.levelEditor.nodes);
        if (sourceIndex > -1 && controlledIndex > -1) {
            var sourceNode =  ocargo.levelEditor.nodes[sourceIndex];
            var controlledNode = ocargo.levelEditor.nodes[controlledIndex];
            if(canGetFromSourceToControlled(sourceNode, controlledNode)) {
                ocargo.levelEditor.trafficLights.push({"index": idIndex, "node": controlledIndex, 
                                                       "sourceNode": sourceIndex, "redDuration":3,
                                                       "greenDuration": 3, "startTime": 0,
                                                       "startingState": (red ? "RED" : "GREEN"),
                                                       "image": image});

                setTrafficLightImagePosition(sourceCoord, controlledCoord, image);
            }
        }
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
        var transform = object.transform();
        var value = 0;
        for(var i = 0; i < transform.length; i++) {
            if(transform[i][0] === 'r') {
                value += Math.abs(transform[i][1]);
            }
        }
        return value % 360;   
    }

    function findTrafficLightByIndex(index, lights) {
        for (var i = 0; i < lights.length; i++) {
            if (lights[i].id === index) {
                return i;
            }
        }
        return -1;
    }

    function canGetFromSourceToControlled(sourceNode, controlledNode) {
        for(var i = 0; i < sourceNode.connectedNodes.length; i++) {
            if(sourceNode.connectedNodes[i] === controlledNode) {
                return true;
            }
        }
        return false;
    }
};

/******************/
/* Initialisation */
/******************/

$(function() {
    ocargo.levelEditor = new ocargo.LevelEditor();
});
