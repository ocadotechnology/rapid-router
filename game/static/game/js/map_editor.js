'use strict';

var ocargo = ocargo || {};

ocargo.MapEditor = function() {
	this.submittedPoints = [];
	this.grid = initialiseVisited();
	this.current = [];
}

ocargo.MapEditor.prototype.mark = function(element) {
	var getBBox = element.getBBox();
	console.debug([getBBox.x / 100, (GRID_HEIGHT - 1) - getBBox.y / 100] + " " + this.current);
	ocargo.mapEditor.current = [getBBox.x / 100, (GRID_HEIGHT -1) - getBBox.y / 100];
	ocargo.mapEditor.submittedPoints.push(ocargo.mapEditor.current);
	ocargo.mapEditor.grid[ocargo.mapEditor.current[0]][ocargo.mapEditor.current[1]] = true;
	element.attr({fill:"grey", "fill-opacity": 1,});
}

ocargo.MapEditor.prototype.createGrid = function(paper) {
    for (var i = 0; i < GRID_WIDTH; i++) {
        for (var j = 0; j < GRID_HEIGHT; j++) {
            var x = i * GRID_SPACE_WIDTH;
            var y = j * GRID_SPACE_HEIGHT;
            var segment = paper.rect(x, y, GRID_SPACE_WIDTH, GRID_SPACE_HEIGHT);
			segment.attr({stroke: '#777', fill:"white", "fill-opacity": 0,});

            segment.node.onclick = function () {
                var this_rect = segment;
                return function () {
					ocargo.mapEditor.mark(this_rect);
                }
            }();
        }
    }
    this.current = [0,4];
    //ocargo.mapEditor.mark(this.current);
};

// #A0A0A0 for the suggestion.
ocargo.MapEditor.prototype.trackCreation = function() {
	var point = this.current;

	$('#up').click(function() {
		point[1] += 1;
		handle(point);
	});

	$('#down').click(function() {
	 	point[1] -= 1;
		handle(point);
	});

	$('#left').click(function() {
		point[0] -= 1;
		handle(point);
	});

	$('#right').click(function() {
		point[0] += 1;
		handle(point);
	});


	function handle(point) {
		var pointless = [];
		pointless[0] = point[0];
		pointless[1] = point[1] - 1;
		if (!isOutOfBounds(point)) {
			var element = ocargo.mapEditor.getPaperElement(point[0], point[1]);
			ocargo.mapEditor.mark(element);
		} else {
			if(!isFree(point, ocargo.mapEditor.grid)) {
				console.debug("apparently didn't fulfil");
			}
		}
	}
};

ocargo.MapEditor.prototype.getPaperElement = function(x, y) {
	return paper.getElementByPoint((x + 1) * 100, (GRID_HEIGHT - y)*100);
};

ocargo.MapEditor.prototype.generateNodes = function(points) {
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
	paper.clear();
	ocargo.ui = new ocargo.SimpleUi();
	ocargo.mapEditor = new ocargo.MapEditor();
	ocargo.mapEditor.createGrid(paper);
	ocargo.mapEditor.trackCreation();
});

$('#undo').click(function() {
	if(ocargo.mapEditor.submittedPoints.length > 0) {
		var toChange = ocargo.mapEditor.submittedPoints.pop();
		ocargo.mapEditor.grid[toChange[0]][toChange[1]] = false;
		var changed = ocargo.mapEditor.getPaperElement(toChange[0], toChange[1]);
		changed.attr({stroke: '#777', fill:"white", "fill-opacity": 0,});
	}
});

$('#clear').click(function() {
	paper.clear();
	ocargo.mapEditor = new ocargo.MapEditor();
	ocargo.mapEditor.createGrid(paper)
	ocargo.mapEditor.current = [0,4];
});

$('#createFromSelect').click(function() {
	ocargo.ui = new ocargo.SimpleUi();
	var nodes = ocargo.mapEditor.generateNodes(ocargo.mapEditor.submittedPoints);  
	var map = new ocargo.Map(nodes, ocargo.ui);
});

