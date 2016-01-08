/*
Code for Life

Copyright (C) 2015, Ocado Innovation Limited

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

var forwardAngle = Math.PI;
var leftCutoffAngle = 5 * Math.PI / 6;
var rightCutoffAngle = 7 * Math.PI / 6;

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

	var nextNode = null;
    var nextNodeDeviation = null;

    var nodes = currentNode.connectedNodes;
    for (var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, node);
        var deviation = Math.abs(forwardAngle - angle);
        if (angle >= leftCutoffAngle && angle <= rightCutoffAngle &&
            (nextNode === null || deviation < nextNodeDeviation)) {
            nextNode = node;
            nextNodeDeviation = deviation;
        }
    }
    return nextNode;
};

ocargo.Map.prototype.isRoadLeft = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;

    var index = currentNode.connectedNodes.indexOf(previousNode) + 1;
    var nextNode;
    if (index === currentNode.connectedNodes.length) {
        nextNode = currentNode.connectedNodes[0];
    } else {
        nextNode = currentNode.connectedNodes[index];
    }

    var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, nextNode);
    return (angle > 0 && angle < leftCutoffAngle) ? nextNode : null;
};

ocargo.Map.prototype.isRoadRight = function(position) {
	var previousNode = position.previousNode;
	var currentNode = position.currentNode;

	var index = currentNode.connectedNodes.indexOf(previousNode) - 1;
    var nextNode;
    if (index === -1) {
        nextNode = currentNode.connectedNodes[currentNode.connectedNodes.length - 1];
    } else {
        nextNode = currentNode.connectedNodes[index];
    }

    var angle = ocargo.calculateClockwiseNodeAngle(previousNode, currentNode, nextNode);
    return (angle > rightCutoffAngle && angle < 2 * Math.PI) ? nextNode : null;
};

ocargo.Map.prototype.isDeadEnd = function(position) {
	var connectedNodes = position.currentNode.connectedNodes;
	if (connectedNodes.length === 1) {
		return connectedNodes[0];
	}
	return null;
};
