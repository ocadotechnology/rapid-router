var ocargo = ocargo || {};

function createUi() {
    return new SimpleUi();
}

function createDefaultLevel(ui) {

    var points = [
        [0, 3],
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 5],
        [3, 5],
        [3, 6],
        [3, 7],
        [4, 7],
        [5, 7],
        [5, 6],
        [5, 5],
        [6, 5],
        [7, 5],
        [8, 5],
        [9, 5]
    ];

	var nodes = generateNodes(points);  
	var map = new Map(nodes, ui);
	var van = new Van(nodes[0], nodes[1], ui);
	return new Level(map, van, nodes[nodes.length - 1], ui);
}

function generateNodes(points){
	var previousNode = null;
	var nodes = [];
	for (var i = 0; i < points.length; i++) {
	      var p = points[i];
	      var coordinate = new ocargo.Coordinate(p[0], p[1]);
	      var node = new Node(coordinate);
	      if (previousNode) {
	          node.addConnectedNodeWithBacklink(previousNode);
	      }
	      previousNode = node;
	      nodes.push(node);
	}
	return nodes;
}

/**
  * Generates a random road given a starting point and seed and length.
  * Seed - a number from the range <0, 1>, where 1 creates a completely straight road
  * and 0 does not influence the way the next road element is chosen at all.
  * Length - optional argument limiting the length of the path.
  */
function generateRandomPathPoints(current, seed, length) {
	var points = [];
	var visited = initialiseVisited();
	var possibleNext = null;
	var orientation = current[1] == 0 ? -1 : 2;
	var possibleStaight = null;
	length = length == undefined ? Number.POSITIVE_INFINITY : length;

	points.push(current);
	visited[current[0]][current[1]] = true;
	current = getNextBasedOnOrientation(current, orientation);

	while (!isOutOfBounds(current) && points.length < length) {
		
		visited[current[0]][current[1]] = true;
		possibleNext = getPossibleNextMoves(current, visited);
		possibleStraight = getNextBasedOnOrientation(current, orientation);
		
		if (Math.random() < seed && possibleStraight != -1 
			&& isFree(possibleStraight, visited)) {
			points.push(current);
			current = possibleStraight;
			console.debug(current);

		} else {

			if (possibleNext.length == 0) {
				if(isOnBorder(current)) {
					points.push(current);
					return points;
				}
				current = points.pop();

			} else {

				var decision = Math.floor((Math.random() * possibleNext.length));
				points.push(current);
				next = possibleNext[decision];
				orientation =  (2 * (next[0] - current[0]) + (next[1] - current[1]));
				current = possibleNext[decision];
			}
		}
	}
	console.debug("blah");
	for (var i = 0; i < points.length; i++) {
		console.debug(points[i]);
	}
	console.debug("blah2");
	return points;

	/*                      *(1, 0) 1
	 *		
	 *      *(-1,0) -2      x(0, 0)      *(1, 0) 2
	 *
	 *                      *(-1, 0) -1
	 *
	 * Returns next point in the same orientation or -1 if it would go out of bounds. 
	 */					
	function getNextBasedOnOrientation(point, orientation) {
		var result = null;
		switch(orientation) {
			case 1:
				result = [point[0], point[1] + 1];
				break;
			case -1:
				result = [point[0], point[1] - 1];
				break;
			case 2:
				result = [point[0] + 1, point[1]];
				break;
			case -2:
				result = [point[0] - 1, point[1]];
				break;
		}
		return isOutOfBounds(result) ? -1 : result;
	}

	function isOutOfBounds(point) {
		return point[0] < 0 || point[0] >= GRID_WIDTH || point[1] < 0 || point[1] >= GRID_HEIGHT;
	}

	function isOnBorder(point) {
		return point[0] == 0 || point[0] == GRID_WIDTH || point[1] == 0 || point[1] == GRID_HEIGHT;
	}

	function isFree(point, visited) {
		return !visited[point[0]][point[1]];
	}

	function getPossibleNextMoves(point, visited) {
		var possible = [];
		var possiblePoint = null;
		var considered = [[point[0], point[1] + 1], [point[0] + 1, point[1]], 
			[point[0] - 1, point[1]], [point[0], point[1] - 1]];
		for (var i= 0; i < 4; i++) {
			possiblePoint = considered[i];
			if(!isOutOfBounds(possiblePoint) && isFree(possiblePoint, visited)) {
				possible.push(possiblePoint);
			}
		}
		return possible;
	}

	function initialiseVisited() {
		var visited = new Array(GRID_WIDTH);
		for (var i = 0; i < GRID_WIDTH; i++) {
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

	$('#randomRoad').click(function() {
		var ui = createUi();
		var points = generateRandomPathPoints([0,3], 0.5, 13);
		var nodes = generateNodes(points);  
		var van = new Van(nodes[0], nodes[1], ui);
		var map = new Map(nodes, ui);
	})
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
