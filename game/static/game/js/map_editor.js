'use strict';

var BACKGROUND_COLOR = '#a8d44a';
var SELECTED_COLOR = '#70961f';
var SUGGESTED_COLOR = '#95b650';
var BORDER = '#bce369';

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
            var x = i * GRID_SPACE_SIZE;
            var y = j * GRID_SPACE_SIZE;
            var segment = paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
            segment.attr({stroke: BORDER, fill: BACKGROUND_COLOR, "fill-opacity": 0});

            segment.node.onclick = function () {
                var this_rect = segment;
                return function () {
                    var getBBox = this_rect.getBBox();
                    var point = [getBBox.x / 100, getBBox.y / 100];
                    if(ocargo.mapEditor.map[point[0]][point[1]] === undefined) {
                        ocargo.mapEditor.markPossible(point);
                        ocargo.mapEditor.mark(point, SELECTED_COLOR, 1, true);
                    }
                }
            }();
            this.grid[i][j] = segment;
            this.map[i][j] = false;
        }
    }
    this.current = [0,4];
    createHorizontalRoad(paper, 0, 4);
    this.mark(this.current, SELECTED_COLOR, 1, true);
    this.possibleNext = [[1,4]];
    this.mark([1,4], SUGGESTED_COLOR, 1, undefined);
    pushInstruction(ocargo.mapEditor.json, new ocargo.Coordinate(0,4), "H");
};

ocargo.MapEditor.prototype.markPossible = function(point) {
    var curr;
    for (var i = 0; i < this.possibleNext.length; i++) {
        curr = this.possibleNext[i];
        this.mark(curr, BACKGROUND_COLOR, 0, false);
    }
    this.possibleNext = getPossibleNextMoves(point, this.map);
    for (var i = 0; i < this.possibleNext.length; i++) {
        curr = this.possibleNext[i];
        this.mark(this.possibleNext[i], SUGGESTED_COLOR, 1, undefined);
    }
};

ocargo.MapEditor.prototype.mark = function(point, colour, opacity, occupied) {
    var element = this.grid[point[0]][point[1]];
    if (occupied) {
        this.current = point;
        this.submittedPoints.push([point[0], GRID_HEIGHT - 1 - point[1]]);
    }
    this.map[point[0]][point[1]] = occupied;
    element.attr({fill:colour, "fill-opacity": opacity});
};

ocargo.MapEditor.prototype.trackCreation = function() {
    function up() {
        var point = ocargo.mapEditor.current.slice(0);
        point[1] -= 1;
        point = handle(point);
    }

    function down() {
        var point = ocargo.mapEditor.current.slice(0);
        point[1] += 1;
        point = handle(point);
    }

    function left() {
        var point = ocargo.mapEditor.current.slice(0);
        point[0] -= 1;
        point = handle(point);
    }

    function right() {
        var point = ocargo.mapEditor.current.slice(0);
        point[0] += 1;
        point = handle(point);
    }

    document.onkeydown = function(event) {
        var code = event.keyCode;
        console.debug(code);
        switch (code) {
            case 37:
                left();
                break;
            case 38:
                up()
                break;
            case 39:
                right();
                break;
            case 40:
                down();
                break;
            default:
                console.debug("Hit default.");
        }
    };

    $('#up').click(function() {
        up();
    });

    $('#down').click(function() {   
        down();
    });

    $('#left').click(function() {
        left();
    });

    $('#right').click(function() {
        right();
    });

    function handle(point) {
        var isPossible = false;
        for (var i = 0; i < ocargo.mapEditor.possibleNext.length; i++) {
            if (ocargo.mapEditor.possibleNext[i][0] === point[0] && 
                ocargo.mapEditor.possibleNext[i][1] === point[1]) {
                isPossible = true;
                break;
            }
        }
        if (!isOutOfBounds(point) && isPossible) {
            ocargo.mapEditor.markPossible(point);
            ocargo.mapEditor.mark(point, SELECTED_COLOR, 1, true);
            ocargo.mapEditor.current = point;
        }
    }
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
        this.submittedPoints.push([x, GRID_HEIGHT - 1 - y]);
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
        var transposedChange = [toChange[0], GRID_HEIGHT - 1 - toChange[1]];
        var current = ocargo.mapEditor.submittedPoints[ocargo.mapEditor.submittedPoints.length-1];
        ocargo.mapEditor.current = [current[0], GRID_HEIGHT - 1 - current[1]];
        ocargo.mapEditor.mark(transposedChange, BACKGROUND_COLOR, 0, false);
        ocargo.mapEditor.markPossible(ocargo.mapEditor.current, BACKGROUND_COLOR, 0, false);
    }
});

$('#dragMagic').click(function() {
    var message = "You are about to submit a road that is not completely connected. Are you sure " +
        "you want to continue?";
    var coord = [0, 4];
    ocargo.mapEditor.jsonToPoints(coord);
    var unified = ocargo.mapEditor.elements == ocargo.mapEditor.submittedPoints.length;

    if (ocargo.mapEditor.submittedPoints.length < 3) {
            startPopup("Oh no!", "", "Your map is too short! Try adding a few more segments.");
            return;
    }

    // If all the road segments are connected or user knows of the discontinuity and wants
    // to proceed.
    if (unified || window.confirm(message)) {
        console.debug("Creating a map from your choice.");
        var nodes = ocargo.mapEditor.generateNodes(ocargo.mapEditor.submittedPoints);
        var map = new ocargo.Map(nodes, nodes[nodes.length - 1], ocargo.ui);
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
    if (ocargo.mapEditor.submittedPoints.length < 3) {
        startPopup("Oh no!", "", "Your map is too short! Try adding a few more segments.");
        return;
    }
    var nodes = ocargo.mapEditor.generateNodes(ocargo.mapEditor.submittedPoints);  
    var map = new ocargo.Map(nodes, nodes[nodes.length - 1], ocargo.ui);
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
            var x = ox / GRID_SPACE_SIZE;
            var y = oy / GRID_SPACE_SIZE;
            ocargo.mapEditor.map[x][y] = false;
        },
        endFnc = function() {
            var point = getGridSpace(lx, ly);

            // Currently protecting against loops.
            if (!isOutOfBounds(point) && !ocargo.mapEditor.map[point[0]][point[1]]) {
                var coord = new ocargo.Coordinate(point[0], point[1]);
                var instruction = identifyInstruction(me);
                ox = point[0] * GRID_SPACE_SIZE;
                oy = point[1] * GRID_SPACE_SIZE;
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

// Submission of a path of the created level which is then processed in level_new view.
$(document).ready(function() {
    $("#export").click(function() {
        var input_string = JSON.stringify(ocargo.mapEditor.submittedPoints);

        var blockTypes = [];
        $('.js-block-checkbox:checked').each(function(index, checkbox) {
            blockTypes.push(checkbox.id);
        });

        $.ajax({
            url: "/game/levels/new",
            type: "POST",
            dataType: 'json',
            data: {
                path: input_string,
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
});
