'use strict';

var ocargo = ocargo || {};

ocargo.Coordinate = function(x, y) {
    this.x = x;
    this.y = y;
};

ocargo.Coordinate.prototype.equals = function(coord) {
	return coord && coord.x === this.x && coord.y === this.y;
}

ocargo.Coordinate.prototype.isAbove = function(coord) {
	return coord && this.y > coord.y;
}

ocargo.Coordinate.prototype.isRightOf = function(coord) {
	return coord && this.x > coord.x;
}

ocargo.Coordinate.prototype.isBelow = function(coord) {
	return coord && this.y < coord.y;
}

ocargo.Coordinate.prototype.isLeftOf = function(coord) {
	return coord && this.x < coord.x;
}

ocargo.Coordinate.prototype.angleTo = function(coord) {
    return Math.atan2(coord.y - this.y, coord.x - this.x);
};
