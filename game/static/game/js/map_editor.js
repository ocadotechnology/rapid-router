'use strict';

var ocargo = ocargo || {};

ocargo.MapEditor = function() {
	this.submittedPoints = [];
	this.map = initialiseVisited();
	this.grid = initialiseVisited();
	this.current = [];
	this.possibleNext = [];
	this.json = {};
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
    createHorizontalRoad(paper, 0, 4);
    this.mark(this.current, "grey", 1, true);
    this.possibleNext = [[1,4]];
    this.mark([1,4], "#a4a4a6", 1, undefined);
    pushInstruction(ocargo.mapEditor.json, new ocargo.Coordinate(0,4), "H");
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
		var isPossible = false;
		for (var i = 0; i < ocargo.mapEditor.possibleNext.length; i++) {
			if (ocargo.mapEditor.possibleNext[i][0] == point[0] 
			   && ocargo.mapEditor.possibleNext[i][1] == point[1]) {
				isPossible = true;
				break;
			}
		}
		if (!isOutOfBounds(point) && isPossible) {
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
	      var coordinate = new ocargo.Coordinate(p[0], GRID_HEIGHT - 1 - p[1]);
	      var node = new ocargo.Node(coordinate);
	      if (previousNode) {
	          node.addConnectedNodeWithBacklink(previousNode);
	      }
	      previousNode = node;
	      nodes.push(node);
	}
	return nodes;
};

ocargo.MapEditor.prototype.jsonToNodes = function(startCoord) {
    var nodes = [];
    var x = startCoord.x; 
    var y = startCoord.y;  
    var progressiveX = true;
    var progressiveY = undefined;
    var currDirection = this.json[x.toString()][y.toString()];
    var coordinate = new ocargo.Coordinate(x, GRID_HEIGHT - 1 - y);
    var currNode = new ocargo.Node(startCoord);
    nodes.push(currNode);
    var counter = 0;
    var bool = true;

    do {
        switch (currDirection) {
            case 'H':
                if (progressiveX)
                    x++;
                else
                    x--;
                break;
            case 'V':
                if(progressiveY)
                    y++;
                else 
                    y--;
                break;
            case 'UL':
                if (progressiveX) {
                    y--;
                    progressiveX = undefined;
                    progressiveY = false;
                } else if (progressiveY) {
                    x--;
                    progressiveX = false;
                    progressiveY = undefined;
                }
                break;
            case 'DL':
                if (progressiveX) {
                    y++;
                    progressiveX = undefined
                    progressiveY = true;
                } else if (progressiveY == false) {
                    x--;
                    progressiveX = false;
                    progressiveY = undefined;
                }
                break;
            case 'DR':
                if (progressiveX == false) {
                    y++;
                    progressiveX = undefined;
                    progressiveY = true;
                } else if (progressiveY == false) {
                    x++;
                    progressiveX = true;
                    progressiveY = undefined;
                }
                break;
            case 'UR':
                if (progressiveY) {
                    x++;
                    progressiveX = true;
                    progressiveY = undefined;
                } else if (progressiveX == false) {
                    y--;
                    progressiveX = undefined;
                    progressiveY = false;
                }
                break;
            case undefined:
                x++;
                break;
            default:
                console.debug('hit default;');
                bool = false;
                
        }
        coordinate = new ocargo.Coordinate(x, GRID_HEIGHT - 2 - y);
        var node = new ocargo.Node(coordinate);
        node.addConnectedNodeWithBacklink(currNode);
        nodes.push(node);
        if (this.json.hasOwnProperty(x.toString())) {
            currDirection = this.json[x.toString()][y.toString()];
        } else {
            break;
        }
        currNode = node;
    } while (bool);

    return nodes;
}

ocargo.MapEditor.prototype.clear = function() {
    paper.clear();
    ocargo.mapEditor = new ocargo.MapEditor();
    ocargo.mapEditor.createGrid(paper);
};

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

$('#dragMagic').click(function() {
    ocargo.ui = new ocargo.SimpleUi();
    var coord = new ocargo.Coordinate(0, 3);
            console.debug("Tadaaaam");

    var nodes = ocargo.mapEditor.jsonToNodes(coord);
    nodes.pop();

//    console.debug("Tadaaaam, length of nodes" + nodes.length);
 //   for (var i = 0; i < nodes.length; i++) {
//        console.debug(nodes[i] == null);
 //       console.debug(nodes[i].coordinate.x, nodes[i].coordinate.y);
 //   }
    var map = new ocargo.Map(nodes, ocargo.ui);

});

$('#clear').click(function() {
	ocargo.mapEditor.clear();
});

$('#tab1').click(function() {
   ocargo.mapEditor.clear();
});

$('#tab2').click(function() {
    ocargo.mapEditor.clear();
});

$('#createFromSelect').click(function() {
	console.debug(ocargo.mapEditor.submittedPoints);
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
      	startFnc = function() {
     		var x = ox / GRID_SPACE_WIDTH;
	     	var y = oy / GRID_SPACE_HEIGHT;
	     	if (ocargo.mapEditor.json.hasOwnProperty(x))
	     	 	if(ocargo.mapEditor.json[x].hasOwnProperty(y))
	     			delete ocargo.mapEditor.json[x][y];
	     		if (isEmpty(ocargo.mapEditor.json))
	     			delete ocargo.mapEditor.json[x];

     	},
      	endFnc = function() {
	      	var point = getGridSpace(lx, ly);
	      	var coord = new ocargo.Coordinate(point[0], point[1]);
	      	var instruction = identifyInstruction(me);
	      	ox = point[0] * GRID_SPACE_WIDTH;
	        oy = point[1] * GRID_SPACE_HEIGHT;
	      	me.transform('t' + ox + ',' + oy);
	        pushInstruction(ocargo.mapEditor.json, coord, instruction);
	        console.debug(JSON.stringify(ocargo.mapEditor.json));
      	};

	this.drag(moveFnc, startFnc, endFnc);

	function isEmpty(map) {
	   	for(var key in map) {
			if (map.hasOwnProperty(key)) {
				return false;
			}
		}
  		return true;
  	}
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

