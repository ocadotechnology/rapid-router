'use strict';

var ocargo = ocargo || {};

var grid = [];


function createGrid(paper) {
    for (var i = 0; i < GRID_WIDTH; i++) {
        for (var j = 0; j < GRID_HEIGHT; j++) {
            var x = i * GRID_SPACE_WIDTH;
            var y = j * GRID_SPACE_HEIGHT;
            var r = paper.rect(x, y, GRID_SPACE_WIDTH, GRID_SPACE_HEIGHT);
			r.attr({stroke: '#777', fill:"white", "fill-opacity": 0,});

            r.node.onclick = function () {
                var this_rect = r;
                return function () {
					var getBBox = this_rect.getBBox();
                	console.debug(getBBox);
                	grid.push([getBBox.x / 100, GRID_HEIGHT - 1 - getBBox.y / 100]);
                    this_rect.attr({fill:"gray", "fill-opacity": 1,});
                }
            }();
        }
    }
}

function generateNodes(points){
	var previousNode = null;
	var nodes = [];
	for (var i = 0; i < points.length; i++) {
	      var p = points[i];
	      var coordinate = new ocargo.Coordinate(p[0], p[1]);
	      var node = new ocargo.Node(coordinate);
	      if (previousNode) {
	          node.addConnectedNodeWithBacklink(previousNode);
	      }
	      previousNode = node;
	      nodes.push(node);
	}
	return nodes;
}

$(function() {
	paper.clear;
	createGrid(paper);
});

$('#createFromSelect').click(function() {
	ocargo.ui = new ocargo.SimpleUi();
	console.debug("MAGIG: " + grid);

	var nodes = generateNodes(grid);  
	var map = new ocargo.Map(nodes, ocargo.ui);
});

