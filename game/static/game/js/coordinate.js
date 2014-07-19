'use strict';

var ocargo = ocargo || {};

ocargo.Coordinate = function(x, y) {
    this.x = x;
    this.y = y;
};

ocargo.Coordinate.prototype.equals = function(coord) {
	return coord.x === this.x && coord.y === this.y;
}