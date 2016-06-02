/*
Code for Life

Copyright (C) 2016, Ocado Innovation Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
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
