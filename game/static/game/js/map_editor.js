'use strict';

var ocargo = ocargo || {};

ocargo.MapEditor = function() {
	this.submittedPoints = [];
	this.map = initialiseVisited();
    this.grid = initialiseVisited();
	this.current = [];
	this.possibleNext = [];
	this.json = {};
    this.elements = 1;
};

ocargo.MapEditor.prototype.createGrid = function(paper) {
    for (var i = 0; i < GRID_WIDTH; i++) {
        for (var j = 0; j < GRID_HEIGHT; j++) {
            var x = i * GRID_SPACE_WIDTH;
            var y = j * GRID_SPACE_HEIGHT;
            var segment = paper.rect(x, y, GRID_SPACE_WIDTH, GRID_SPACE_HEIGHT);
			segment.attr({stroke: '#777', fill:"white", "fill-opacity": 0});

            segment.node.onclick = function () {
                var this_rect = segment;
                return function () {
                	var getBBox = this_rect.getBBox();
                	var point = [getBBox.x / 100, getBBox.y / 100];
                	if(ocargo.mapEditor.map[point[0]][point[1]] === undefined) {
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
	element.attr({fill:colour, "fill-opacity": opacity});
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
			if (ocargo.mapEditor.possibleNext[i][0] === point[0] 
			   && ocargo.mapEditor.possibleNext[i][1] === point[1]) {
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

/* Pass in the coordinate in top-down orientation - applies to JSON and paper, not nodes. */
ocargo.MapEditor.prototype.jsonToPoints = function(startCoord) {
    this.submittedPoints = [];
    var x = startCoord[0]; 
    var y = startCoord[1];  
    var progressiveX = true;
    var progressiveY = undefined;
    var currDirection = null;
    var bool = true;

    while (bool) {
        this.submittedPoints.push([x, y]);
        if (this.json.hasOwnProperty(x.toString())) {
            currDirection = this.json[x.toString()][y.toString()];
        } else {
            break;
        }
        process();
    }
    this.submittedPoints.pop();

    function process() {
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
                    progressiveX = undefined;
                    progressiveY = true;
                } else if (progressiveY === false) {
                    x--;
                    progressiveX = false;
                    progressiveY = undefined;
                }
                break;
            case 'DR':
                if (progressiveX === false) {
                    y++;
                    progressiveX = undefined;
                    progressiveY = true;
                } else if (progressiveY === false) {
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
                } else if (progressiveX === false) {
                    y--;
                    progressiveX = undefined;
                    progressiveY = false;
                }
                break;
            default:
                bool = false;      
        }
    }
};

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
	if (ocargo.mapEditor.submittedPoints.length > 1) {
		var toChange = ocargo.mapEditor.submittedPoints.pop();
		ocargo.mapEditor.current 
			= ocargo.mapEditor.submittedPoints[ocargo.mapEditor.submittedPoints.length-1];
		ocargo.mapEditor.mark(toChange, "white", 0, false);
		ocargo.mapEditor.markPossible(ocargo.mapEditor.current, "white", 0, false);
	}
});

$('#dragMagic').click(function() {
    var message = "You are about to submit a road that is not completely connected. Are you sure "
        + "you want to continue?";
    var coord = [0, 4];
    ocargo.mapEditor.jsonToPoints(coord);
    var unified = ocargo.mapEditor.elements == ocargo.mapEditor.submittedPoints.length;

    // If all the road segments are connected or user knows of the discontinuity and wants
    // to proceed.
    if (unified || window.confirm(message)) {
        console.debug("Creating a map from your choice.");
        var nodes = ocargo.mapEditor.generateNodes(ocargo.mapEditor.submittedPoints);
        var map = new ocargo.Map(nodes, ocargo.ui);
    }
    if (!unified) {
        // Clear the map to get rid of the seperate road segments.
        ocargo.mapEditor.elements = ocargo.mapEditor.submittedPoints.length;
        for (var i = 0; i < ocargo.mapEditor.map.length; i++) {
            for(var j = 0; j < ocargo.mapEditor.map[0].length; j++) {
                ocargo.mapEditor.map[i][j] = false;
            }
        }
        // Mark the remaining road elements on the map.
        for (var i = 0; i < ocargo.mapEditor.submittedPoints.length; i++) {
            var point = ocargo.mapEditor.submittedPoints[i];
            ocargo.mapEditor.map[point[0]][point[1]] = true;
        }
    }
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

            // Currently protecting against loops.
            if (!isOutOfBounds(point) && !ocargo.mapEditor.map[point[0]][point[1]]) {
    	      	var coord = new ocargo.Coordinate(point[0], point[1]);
    	      	var instruction = identifyInstruction(me);
    	      	ox = point[0] * GRID_SPACE_WIDTH;
    	        oy = point[1] * GRID_SPACE_HEIGHT;
    	      	me.transform('t' + ox + ',' + oy);
    	        pushInstruction(ocargo.mapEditor.json, coord, instruction);
                ocargo.mapEditor.map[point[0]][point[1]] = true;

            } else {
                me.transform('t' + ox + ',' + oy);
            }
      	};

	this.drag(moveFnc, startFnc, endFnc);

	function isEmpty(map) {
	   	for (var key in map) {
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
    ocargo.mapEditor.elements++;
});

$('#DR').click(function() {
   	var myset = createTurn(paper, 0, 0, 'DR');
    myset.draggable();
    ocargo.mapEditor.elements++;
});

$('#DL').click(function() {
   	var myset = createTurn(paper, 0, 0, 'DL');
    myset.draggable();
    ocargo.mapEditor.elements++;
});

$('#UR').click(function() {
   	var myset = createTurn(paper, 0, 0, 'UR');
    myset.draggable();
    ocargo.mapEditor.elements++;
});

$('#H').click(function() {
	var turn = createHorizontalRoad(paper, 0, 0);
	turn.draggable();
    ocargo.mapEditor.elements++;
});

$('#V').click(function() {
	var turn = createVerticalRoad(paper, 0, 0);
	turn.draggable();
    ocargo.mapEditor.elements++;
});

$(document).ready(function() {
    $("#export").click(function() {
        var input_string = JSON.stringify(ocargo.mapEditor.submittedPoints);
        $.ajax({
            url : "/game/levels/new",
            type : "POST",
            dataType: "json",
            data : {
              path : input_string,
              csrfmiddlewaretoken :$( "#csrfmiddlewaretoken" ).val()
            },
            success : function(json) {
             // $('#result').append( 'Server Response: ' + json.server_response);
             // window.location.href = "/game/level"
             console.debug("Success")
            },
            error : function(xhr,errmsg,err) {
              console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
        return false;
    });
});
