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
	var possibleStraight = null;
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
				var next = possibleNext[decision];
				orientation =  (2 * (next[0] - current[0]) + (next[1] - current[1]));
				current = possibleNext[decision];
			}
		}
	}
	for (var i = 0; i < points.length; i++) {
		console.debug(points[i]);
	}
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
}

function initialiseVisited() {
	var visited = new Array(10);
	for (var i = 0; i < 10; i++) {
		visited[i] = new Array(8);
	}
	return visited;
}

function isOutOfBounds(point) {
	return point[0] < 0 || point[0] >= 10 || point[1] < 0 || point[1] >= 8;
}

function isOnBorder(point) {
	return point[0] == 0 || point[0] == 10 || point[1] == 0 || point[1] == 8;
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

$('#randomRoad').click(function() {
    var path = JSON.stringify(generateRandomPathPoints([0,3], 0.5, 13));
    $.ajax({
            url: "/game/levels/new",
	    type: "POST",
	    dataType: "json",
	    data: {
                path: path,
	        csrfmiddlewaretoken: $("#csrfmiddlewaretoken").val()
	    },
	    success: function(json) {
                window.location.href = ("/game/" + json.server_response);
	    },
            error: function(xhr, errmsg, err) {
                console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            },
        });
    return false;
});
