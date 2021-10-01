'use strict';

var ocargo = ocargo || {};

ocargo.Coordinate = function(x, y) {
    this.x = x;
    this.y = y;
};

ocargo.Coordinate.prototype.equals = function(coord) {
	return coord && coord.x === this.x && coord.y === this.y;
};

ocargo.Coordinate.prototype.isAbove = function(coord) {
	return coord && this.y > coord.y;
};

ocargo.Coordinate.prototype.isRightOf = function(coord) {
	return coord && this.x > coord.x;
};

ocargo.Coordinate.prototype.isBelow = function(coord) {
	return coord && this.y < coord.y;
};

ocargo.Coordinate.prototype.isLeftOf = function(coord) {
	return coord && this.x < coord.x;
};

ocargo.Coordinate.prototype.getDirectionTo = function(coord) {
	if(this.isBelow(coord)) {
		return 'N';
	}
	else if(this.isLeftOf(coord)) {
		return 'E';
	}
	else if(this.isAbove(coord)) {
		return 'S';
	}
	else if(this.isRightOf(coord)) {
		return 'W';
	}
	return null;
};

ocargo.Coordinate.prototype.getNextInDirection = function(direction) {
	switch(direction) {
        case "N":   return new ocargo.Coordinate(this.x, this.y+1);
        case "E":   return new ocargo.Coordinate(this.x+1, this.y);
        case "S":   return new ocargo.Coordinate(this.x, this.y-1);
        case "W":   return new ocargo.Coordinate(this.x-1, this.y);
    }
};

ocargo.Coordinate.prototype.angleTo = function(coord) {
    return Math.atan2(coord.y - this.y, coord.x - this.x);
};
