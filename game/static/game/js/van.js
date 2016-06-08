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

ocargo.Van = function(position, maxFuel) {
    this.startingPosition = position;

    /**
     * Keeps track of where the van has been
     *
     * Position at index 0 is the previous position at the start of the run, so
     * this array is effectively indexed from 1 onwards. It's guaranteed to have
     * at least two elements in it (the starting node and previous node at the
     * start).
     *
     * @type {ocargo.Node[]}
     */
    this.visitedNodes = [position.previousNode, position.currentNode];
    this.maxFuel = maxFuel;
    this.fuel = maxFuel;
    this.crashStatus = 'NOT_CRASHED';
    this.sizeOfVan = 1;
};

ocargo.Van.prototype.reset = function() {
    this.visitedNodes = [this.startingPosition.previousNode, this.startingPosition.currentNode];
    this.fuel = this.maxFuel;
    this.crashStatus = 'NOT_CRASHED';
    this.sizeOfVan = 1;
};

ocargo.Van.prototype.move = function(nextNode) {
    if (nextNode !== this.visitedNodes[this.visitedNodes.length - 1]) {
        this.visitedNodes.push(nextNode);
    }

    this.fuel -= 1 * this.sizeOfVan;
};

ocargo.Van.prototype.getPosition = function() {
    return { previousNode: this.visitedNodes[this.visitedNodes.length - 2], currentNode: this.visitedNodes[this.visitedNodes.length - 1] };
};

ocargo.Van.prototype.getFuelPercentage = function() {
    return 100 * this.fuel / this.maxFuel;
};

ocargo.Van.prototype.getDistanceTravelled = function() {
    return this.visitedNodes.length - 2; // Don't count starting position, or previous position at start
};

ocargo.Van.prototype.puffUp = function(){
    this.sizeOfVan = 3;
};

ocargo.Van.prototype.puffDown = function(){
    this.sizeOfVan = 1;
};
