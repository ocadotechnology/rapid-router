function createUi() {
    return new SimpleUi();
}

function createDefaultLevel(ui) {
/*
    var points = [
        [0, 0],
        [1, 0],
        [1, 1],
        [1, 2],
        [2, 2],
        [3, 2],
        [3, 3],
        [3, 4],
        [4, 4],
        [5, 4],
        [5, 3],
        [5, 2],
        [6, 2],
        [7, 2],
        [8, 2],
        [9, 2]
    ];
*/
	var points = generateRandomPathPoints([0, 0]);
	for(var i = 0 ; i < points.length; i++) {
		console.debug(points[i]);
	}

    var previousNode = null;
	  var nodes = [];
	  for (var i = 0; i < points.length; i++) {
	      var p = points[i];
	      var coordinate = new Coordinate(p[0], p[1]);
	      var node = new Node(coordinate);
	      if (previousNode) {
	          node.addConnectedNodeWithBacklink(previousNode);
	      }
	      previousNode = node;
	      nodes.push(node);
	  }
	  var map = new Map(nodes, ui);
	  var van = new Van(nodes[0], nodes[1], ui);
	  return new Level(map, van, nodes[nodes.length - 1], ui);
}

function generateRandomPathPoints(source, seed) {
	var points = [];
	var visited = initialiseVisited();
	var current = source;
	var decision = null;
	var possibleNext = null;
	while(!isOutOfBounds(current)) {
		console.debug(current[0] + ' ' + current[1]);
		visited[current[0]][current[1]] = true;
		possibleNext = getPossibleNextMoves(current, visited);
		if(possibleNext.length == 0) {
			current = points[points.length - 1];
			return points;
		} else {
			decision = Math.floor((Math.random() * possibleNext.length));
			points.push(current);
			current = possibleNext[decision];
		}
	}
	return points;


	function isOutOfBounds(point) {
		return point[0] < 0 || point[0] >= GRID_WIDTH || point[1] < 0 || point[1] >= GRID_HEIGHT;
	}

	function isFree(point, visited) {
		return !visited[point[0]][point[1]];
	}

	function getPossibleNextMoves(point, visited) {
		var possible = [];
		var possiblePoint = null;
		var considered = [[point[0], point[1] + 1], [point[0] + 1, point[1]], 
			[point[0] - 1, point[1]], [point[0], point[1] - 1]];
		for(var i= 0; i < 4; i++) {
			possiblePoint = considered[i];
			if(!isOutOfBounds(possiblePoint) && isFree(possiblePoint, visited)) {
				possible.push(possiblePoint);
			}
		}
		return possible;
	}

	function initialiseVisited() {
		var visited = new Array(GRID_WIDTH);
		for(var i = 0; i < GRID_WIDTH; i++) {
			visited[i] = new Array(GRID_HEIGHT);
		}
		return visited;
	}
}

function defaultProgram(level) {
	  var program = new Program(
	          [TURN_LEFT,
	              FORWARD,
	              TURN_RIGHT,
	              FORWARD,
	              TURN_LEFT,
	              FORWARD,
	              TURN_RIGHT,
	              FORWARD,
	              TURN_RIGHT,
	              FORWARD,
	              TURN_LEFT,
	              FORWARD,
	              FORWARD,
	              FORWARD
	          ]);
	
	  level.play(program);
}

function trackDevelopment(level) {
	var program = new Program([]);
	
	$('#moveForward').click(function() {
		program.instructions.push(FORWARD);
    });
	
    $('#turnLeft').click(function() {
    	program.instructions.push(TURN_LEFT);
    });

    $('#turnRight').click(function() {
		program.instructions.push(TURN_RIGHT);
	});
    
    $('#play').click(function() {
    	level.play(program);
	});
}

$(function() {
    'use strict';

    var ui = createUi();
    
    var level = createDefaultLevel(ui);
    
    $('#runDefaultProgram').click(function() {
    	defaultProgram(level);
	});

    trackDevelopment(level);
});
