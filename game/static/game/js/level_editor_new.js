'use strict';

var ocargo = ocargo || {};

var BACKGROUND_COLOR = '#a8d44a';
var SELECTED_COLOR = '#70961f';
var SUGGESTED_COLOR = '#95b650';
var BORDER = '#bce369';


// NODES <---- translate ------> MAP, GRID, PAPER
ocargo.LevelEditor = function() {
    this.nodes = [];
    // History is stored as a list of ranges of each road segment created, i.e. [[0,4], [4,8]],
    // where 0, 4, 8 are indices of nodes pushed to nodes.
    this.history = [];
    this.start = null;
    this.end = null;
    this.currentStrike = [];
    // Do I need this? \/
    this.map = this.initialiseVisited();
    this.grid = this.initialiseVisited();    
}

ocargo.LevelEditor.prototype.initialiseVisited = function() {
    var visited = new Array(10);
    for (var i = 0; i < 10; i++) {
        visited[i] = new Array(8);
    }
    return visited;
}

ocargo.LevelEditor.prototype.createGrid = function(paper) {
    for (var i = 0; i < GRID_WIDTH; i++) {
        for (var j = 0; j < GRID_HEIGHT; j++) {
            var x = i * GRID_SPACE_SIZE;
            var y = j * GRID_SPACE_SIZE;
            // Create node to be inserted into nodes list.
            var segment = paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
            segment.attr({stroke: BORDER, fill: BACKGROUND_COLOR, "fill-opacity": 0});

            segment.node.onmousedown = function() {
                var this_rect = segment;

                return function () {
                    var getBBox = this_rect.getBBox();
                    var coord = new ocargo.Coordinate(getBBox.x / 100, getBBox.y / 100);
                    ocargo.levelEditor.start = coord;
                    ocargo.levelEditor.mark(coord, SELECTED_COLOR, 1, true);
                }
            } ();

            segment.node.onmouseover = function() {
                var this_rect = segment;

                return function () {
                    if (ocargo.levelEditor.start !== null) {
                        var getBBox = this_rect.getBBox();
                        var coord = new ocargo.Coordinate(getBBox.x / 100, getBBox.y / 100);
                        ocargo.levelEditor.recalculatePredictedRoad(coord);
                    }
                }
                return;
            } ();

            segment.node.onmouseup = function() {
                var this_rect = segment;

                return function () {
                    ocargo.levelEditor.end = segment;
                    ocargo.levelEditor.start = null;
                    var getBBox = this_rect.getBBox();
                    var coord = new ocargo.Coordinate(getBBox.x / 100, getBBox.y / 100);
                    ocargo.levelEditor.finaliseMove(coord);
                    //Generate the road
                    console.debug(ocargo.levelEditor.nodes.length)
                    for (var i = 0; i < ocargo.levelEditor.nodes.length; i++) {
                        console.debug("node",i, ocargo.levelEditor.nodes[i].coordinate, 
                             ocargo.levelEditor.nodes[i].connectedNodes);
                    }
                    createRoad(ocargo.levelEditor.nodes);
                }
            } ();

            this.grid[i][j] = segment;
            this.map[i][j] = false;
        }
    }
};

ocargo.LevelEditor.prototype.finaliseMove = function(coord) {
    var current;
    var prev;
    for (var i = 0; i < ocargo.levelEditor.currentStrike.length; i++) {
        current = ocargo.levelEditor.currentStrike[i];
        var index = this.findNodeByCoordinate(this.nodes, current.coordinate);
        if (index > -1) {
            var alreadyExisting = ocargo.levelEditor.nodes[index]
            console.debug(alreadyExisting.connectedNodes);
            for (var j = 0; j < current.connectedNodes.length; j++) {
                var neighbour = current.connectedNodes[j];
                console.debug("neighbourskhadkhdkajhd", neighbour);
                alreadyExisting.addConnectedNodeWithBacklink(neighbour);
                neighbour.addConnectedNodeWithBacklink(alreadyExisting);
                neighbour.removeDoublyConnectedNode(current);
            }
        } else {
            this.nodes.push(current);
        }
    }
    this.currentStrike = [];
}

ocargo.LevelEditor.prototype.findNodeByCoordinate = function(nodes, coordinate) {
    for (var i = 0; i < nodes.length; i++) {
        if (nodes[i].coordinate.x === coordinate.x && nodes[i].coordinate.y === coordinate.y) {
            return i;
        }
    }
    return -1;
}

ocargo.LevelEditor.prototype.recalculatePredictedRoad = function(coordinate) {
    ocargo.levelEditor.cleanPredictedRoad(coordinate);
    ocargo.levelEditor.markFromStart(coordinate);
};

ocargo.LevelEditor.prototype.markFromStart = function(coord) {
    //console.debug(this.start, this.start.coordinate, coord, coord.x)
    ocargo.levelEditor.currentStrike.push(new ocargo.Node(this.translate(this.start)));
    ocargo.levelEditor.mark(this.start, SELECTED_COLOR, 1, true);
    var x, y;

    if (this.start.x <= coord.x) {
        for (x = this.start.x + 1; x <= coord.x; x++) {
            setup(x, this.start.y);
        }
    } else {
        for (x = this.start.x - 1; x >= coord.x; x--) {
            setup(x, this.start.y);
        }
    }
    if (this.start.y <= coord.y) {
        for (y = this.start.y + 1; y <= coord.y; y++) {
            setup(coord.x, y);
        }
    } else {
        for (y = this.start.y - 1; y >= coord.y; y--) {
            setup(coord.x, y);
        }
    }

    function setup(x, y) {
        var coordinate = new ocargo.Coordinate(x, y);
        var node = new ocargo.Node(ocargo.levelEditor.translate(coordinate));
        node.addConnectedNodeWithBacklink(
            ocargo.levelEditor.currentStrike[ocargo.levelEditor.currentStrike.length - 1]);
        ocargo.levelEditor.currentStrike.push(node);
        ocargo.levelEditor.mark(coordinate, SELECTED_COLOR, 1, true);
    }
};

ocargo.LevelEditor.prototype.cleanPredictedRoad = function() {
    var node;
    var coord;
    for (var i = this.currentStrike.length - 1; i >=0; i--) {
        node = ocargo.levelEditor.currentStrike[i];
        coord = ocargo.levelEditor.translate(node.coordinate);
        ocargo.levelEditor.mark(coord, BACKGROUND_COLOR, 0, false);
        // Handle removing remaining references - although we pop, we think we are pointing to another node. §
    }
    ocargo.levelEditor.currentStrike = [];
};

ocargo.LevelEditor.prototype.translate = function(coordinate) {
    return new ocargo.Coordinate(coordinate.x, GRID_HEIGHT - 1 - coordinate.y);
}

ocargo.LevelEditor.prototype.mark = function(point, colour, opacity, occupied) {
    var element = this.grid[point.x][point.y];
    this.map[point.x][point.y] = occupied;
    element.attr({fill:colour, "fill-opacity": opacity});
};


$(function() {
    paper.clear();
    ocargo.ui = new ocargo.SimpleUi();
    ocargo.levelEditor = new ocargo.LevelEditor();
    ocargo.levelEditor.createGrid(paper);
});

