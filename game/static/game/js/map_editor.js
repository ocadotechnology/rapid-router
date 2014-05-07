'use strict';

var ocargo = ocargo || {};

ocargo.MapEditor = function() {
	this.submittedPoints = [];
	this.map = initialiseVisited();
	this.grid = initialiseVisited();
	this.current = [];
	this.possibleNext = [];
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
                	var getBBox = this_rect.getBBox();
                	var point = [getBBox.x / 100, getBBox.y / 100];
                	if(ocargo.mapEditor.map[point[0]][point[1]] == undefined) {
	                    ocargo.mapEditor.markPossible(point);
	                    ocargo.mapEditor.mark(point, "grey", 1, true);
	                }
                }
            }();
            this.grid[i][j] = segment;
            this.map[i][j] = false;
        }
    }
    this.current = [0,4];
    this.mark(this.current, "grey", 1, true);
    this.markPossible(this.current);
};

ocargo.MapEditor.prototype.markPossible = function(point) {
	for (var i = 0; i < this.possibleNext.length; i++) {
		var curr = this.possibleNext[i];
		this.mark(curr, "white", 0, false);
	}
	this.possibleNext = getPossibleNextMoves(point, this.map);
	for (var i = 0; i < this.possibleNext.length; i++) {
		var curr = this.possibleNext[i];
		this.mark(this.possibleNext[i], "#a4a4a6", 1, undefined);
	}
};

ocargo.MapEditor.prototype.mark = function(point, colour, opacity, occupied) {
	var element = this.grid[point[0]][point[1]];
	if(occupied) {
		this.current = point;
		this.submittedPoints.push([point[0], point[1]]);
	}
	this.map[point[0]][point[1]] = occupied;
	element.attr({fill:colour, "fill-opacity": opacity,});
};

ocargo.MapEditor.prototype.trackCreation = function() {

	$('#up').click(function() {
		var point = ocargo.mapEditor.current.slice(0);
	 	point[1] -= 1;
		point = handle(point);
	});

	$('#down').click(function() {	
		var point = ocargo.mapEditor.current.slice(0);
		point[1] += 1;
		point = handle(point);
	});

	$('#left').click(function() {
		var point = ocargo.mapEditor.current.slice(0);
		point[0] -= 1;
		point = handle(point);
	});

	$('#right').click(function() {
		var point = ocargo.mapEditor.current.slice(0);
		point[0] += 1;
		point = handle(point);
	});


	function handle(point) {
		if (!isOutOfBounds(point) && isFree(point, ocargo.mapEditor.map)) {
			ocargo.mapEditor.markPossible(point);
			ocargo.mapEditor.mark(point, "grey", 1, true);
			ocargo.mapEditor.current = point;
		}
	}
};

ocargo.MapEditor.prototype.generateNodes = function(points) {
	var previousNode = null;
	var nodes = [];
	for (var i = 0; i < points.length; i++) {
	      var p = points[i];
	      var coordinate = new ocargo.Coordinate(p[0], GRID_HEIGHT -1 -p[1]);
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
	if(ocargo.mapEditor.submittedPoints.length > 1) {
		var toChange = ocargo.mapEditor.submittedPoints.pop();
		ocargo.mapEditor.current 
			= ocargo.mapEditor.submittedPoints[ocargo.mapEditor.submittedPoints.length-1];
		ocargo.mapEditor.mark(toChange, "white", 0, false);
		ocargo.mapEditor.markPossible(ocargo.mapEditor.current, "white", 0, false);

	}
});


$('#clear').click(function() {
	paper.clear();
	ocargo.mapEditor = new ocargo.MapEditor();
	ocargo.mapEditor.createGrid(paper)
});

$('#createFromSelect').click(function() {
	ocargo.ui = new ocargo.SimpleUi();
	var nodes = ocargo.mapEditor.generateNodes(ocargo.mapEditor.submittedPoints);  
	var map = new ocargo.Map(nodes, ocargo.ui);
});

Raphael.st.draggable = function() {
  var me = this,
      lx = 0,
      ly = 0,
      ox = 0,
      oy = 0,
      moveFnc = function(dx, dy) {
        lx = dx + ox;
        ly = dy + oy;
        me.transform('t' + lx + ',' + ly);
      },
      startFnc = function() {},
      endFnc = function() {
      	var point = getGridSpace(lx, ly);
      	console.debug("Moved to: " + point);
      	me.transform('t' + point[0] * GRID_SPACE_WIDTH + ',' + point[1]* GRID_SPACE_HEIGHT);
        ox = point[0] * GRID_SPACE_WIDTH;
        oy = point[1] * GRID_SPACE_HEIGHT;
      };
  
  this.drag(moveFnc, startFnc, endFnc);
};

$('#UL').click(function() {
   	var myset = createTurn(paper, 0, 0, 'UL');
    myset.draggable();
});

$('#DR').click(function() {
   	var myset = createTurn(paper, 0, 0, 'DR');
    myset.draggable();

});

$('#DL').click(function() {
   	var myset = createTurn(paper, 0, 0, 'DL');
    myset.draggable();

});

$('#UR').click(function() {
   	var myset = createTurn(paper, 0, 0, 'UR');
    myset.draggable();

});

$('#H').click(function() {
	var turn = createHorizontalRoad(paper, 0, 0);
	turn.draggable();
});

$('#V').click(function() {
	var turn = createVerticalRoad(paper, 0, 0);
	turn.draggable();
});

