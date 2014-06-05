'use strict';

var ocargo = ocargo || {};

var BACKGROUND_COLOR = '#a8d44a';
var SELECTED_COLOR = '#70961f';
var SUGGESTED_COLOR = '#95b650';
var BORDER = '#bce369';

ocargo.LevelEditor = function() {
    this.nodes = [];
    this.start = null;
    this.end = null;
    this.currentStrike = [];
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
                    ocargo.levelEditor.start = segment;
                    console.debug("Not null");
                    var getBBox = this_rect.getBBox();
                    var point = [getBBox.x / 100, getBBox.y / 100];
                    ocargo.levelEditor.mark(point, SELECTED_COLOR, 1, true);
                    ocargo.levelEditor.current.push(point);
                }
            } ();

            segment.node.onmouseover = function() {
                var this_rect = segment;

                return function () {
                    if (ocargo.levelEditor.start !== null) {
                        var getBBox = this_rect.getBBox();
                        var getBBox = this_rect.getBBox();
                        ocargo.levelEditor.mark(point, SELECTED_COLOR, 1, true);
                        ocargo.levelEditor.current.push(point);
                    }
                }
                return;
            } ();

            segment.node.onmouseup = function() {
                var this_rect = segment;

                return function () {
                    console.debug("null");
                    ocargo.levelEditor.end = segment;
                    ocargo.levelEditor.start = null;
                    var getBBox = this_rect.getBBox();
                    var point = [getBBox.x / 100, getBBox.y / 100];
                    ocargo.levelEditor.current.push(point);
                    //Generate the road
                }
            } ();

            this.grid[i][j] = segment;
            this.map[i][j] = false;
        }
    }
};

ocargo.LevelEditor.prototype.mark = function(point, colour, opacity, occupied) {
    var element = this.grid[point[0]][point[1]];
    this.map[point[0]][point[1]] = occupied;
    element.attr({fill:colour, "fill-opacity": opacity});
};


$(function() {
    paper.clear();
    ocargo.ui = new ocargo.SimpleUi();
    ocargo.levelEditor = new ocargo.LevelEditor();
    ocargo.levelEditor.createGrid(paper);
});

