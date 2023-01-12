'use strict';

var ocargo = ocargo || {};

ocargo.Map = function(nodeData, origin, destinationCoordinates) {
	this.nodeData = nodeData;
	this.nodes = ocargo.Node.parsePathData(nodeData);

    this.destinations = [];
    for(var i = 0; i < destinationCoordinates.length; i++) {
        var coordinate = new ocargo.Coordinate(destinationCoordinates[i][0],destinationCoordinates[i][1]);
        var destinationNode = this.nodes[ocargo.Node.findNodeIndexByCoordinate(coordinate, this.nodes)];
        this.destinations.push(new ocargo.Destination(i,destinationNode));
    }

    this.originCoordinate = new ocargo.Coordinate(origin.coordinate[0], origin.coordinate[1]);
    this.originDirection = origin.direction;

    var originCurrentCoord = this.originCoordinate.getNextInDirection(this.originDirection);
    this.originPreviousNode = ocargo.Node.findNodeByCoordinate(this.originCoordinate, this.nodes);
    this.originCurrentNode = ocargo.Node.findNodeByCoordinate(originCurrentCoord, this.nodes);
};

ocargo.Map.prototype.startingPosition = function() {
    return {previousNode: this.originPreviousNode,
            currentNode: this.originCurrentNode};
};

ocargo.Map.prototype.getDestinations = function() {
	return this.destinations;
};

/////////////////////////
// The following four functions test if a road exists and return the
// next node if it exists or null otherwise

ocargo.Map.prototype.isRoadForward = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;
    var nextCoordinates = {};
    // Moving up, down or sideways?
    var movingHorizontally = previousNode.coordinate.x != currentNode.coordinate.x;

    if (movingHorizontally) {
        nextCoordinates.y = currentNode.coordinate.y; // y-axis isn't changing
        var movingRight = previousNode.coordinate.x < currentNode.coordinate.x; // going left or right?
        if (movingRight){
            nextCoordinates.x = currentNode.coordinate.x + 1;
            if (nextCoordinates.x > 9) { // right-most extremity
                return null;
            }
        } else {  // moving left
            nextCoordinates.x = currentNode.coordinate.x - 1
            if (nextCoordinates.x < 0){ // left-most extremity
                return null;
            }
        }
    } else { // moving vertically
        nextCoordinates.x = currentNode.coordinate.x;
        var movingUpwards = previousNode.coordinate.y < currentNode.coordinate.y;
        if (movingUpwards) {
            nextCoordinates.y = currentNode.coordinate.y + 1;
            if (nextCoordinates.y > 9) {
                return null;
            }
        } else { // moving downwards
            nextCoordinates.y = currentNode.coordinate.y - 1;
            if (nextCoordinates.y < 0) {
                return null;
            }
        }
    }
    var connected = currentNode.connectedNodes;
    for (var i = 0; i < connected.length; i++){
        var coordinate = connected[i].coordinate;
        if (coordinate.x == nextCoordinates.x && coordinate.y == nextCoordinates.y){
            return connected[i];
        }
    }
    return null;
};

ocargo.Map.prototype.isRoadLeft = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;

    var nextCoordinates = {};
    // Moving up, down or sideways?
    var movingHorizontally = previousNode.coordinate.x != currentNode.coordinate.x;
    if (movingHorizontally){
        nextCoordinates.x = currentNode.coordinate.x;
        var movingRight = previousNode.coordinate.x < currentNode.coordinate.x;
        if (movingRight) {
            nextCoordinates.y = currentNode.coordinate.y + 1;
        } else { // moving left
            nextCoordinates.y = currentNode.coordinate.y - 1;
        }
        if (nextCoordinates.y < 0 || nextCoordinates.y > 9){
            return null;
        }
    } else { // moving up and down
        nextCoordinates.y = currentNode.coordinate.y;
        var movingUp = previousNode.coordinate.y < currentNode.coordinate.y;
        if (movingUp) {
            nextCoordinates.x = previousNode.coordinate.x - 1;
        } else { // moving down
            nextCoordinates.x = previousNode.coordinate.x + 1;
        }
        if (nextCoordinates.x < 0 || nextCoordinates.x > 9){
            return null;
        }
    }
    var connected = currentNode.connectedNodes;
    for (var i = 0; i < connected.length; i++){
        var coordinate = connected[i].coordinate;
        if (coordinate.x == nextCoordinates.x && coordinate.y == nextCoordinates.y){
            return connected[i];
        }
    }
    return null;
};


ocargo.Map.prototype.isRoadRight = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;

    var nextCoordinates = {};
    // Moving up, down or sideways?
    var movingHorizontally = previousNode.coordinate.x != currentNode.coordinate.x;
    if (movingHorizontally){
        nextCoordinates.x = currentNode.coordinate.x;
        var movingRight = previousNode.coordinate.x < currentNode.coordinate.x;
        if (movingRight) {
            nextCoordinates.y = currentNode.coordinate.y - 1;
        } else { // moving left
            nextCoordinates.y = currentNode.coordinate.y + 1;
        }
        if (nextCoordinates.y < 0 || nextCoordinates.y > 9){
            return null;
        }
    } else { // moving up and down
        nextCoordinates.y = currentNode.coordinate.y;
        var movingUp = previousNode.coordinate.y < currentNode.coordinate.y;
        if (movingUp) {
            nextCoordinates.x = previousNode.coordinate.x + 1;
        } else { // moving down
            nextCoordinates.x = previousNode.coordinate.x - 1;
        }
        if (nextCoordinates.x < 0 || nextCoordinates.x > 9){
            return null;
        }
    }
    var connected = currentNode.connectedNodes;
    for (var i = 0; i < connected.length; i++){
        var coordinate = connected[i].coordinate;
        if (coordinate.x == nextCoordinates.x && coordinate.y == nextCoordinates.y){
            return connected[i];
        }
    }
    return null;
};

ocargo.Map.prototype.isDeadEnd = function(position) {
	var connectedNodes = position.currentNode.connectedNodes;
	if (connectedNodes.length === 1) {
		return connectedNodes[0];
	}
	return null;
};
