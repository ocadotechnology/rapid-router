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

ocargo.TrafficLight = function(id, data, nodes) {
    this.id = id;
    this.startingState = data.startingState;
    this.state = this.startingState;
    this.startTime = data.startTime;
    this.redDuration = data.redDuration;
    this.greenDuration = data.greenDuration;
    this.currentLightTime = this.startTime;

    var sourceCoordinate = new ocargo.Coordinate(data.sourceCoordinate.x, data.sourceCoordinate.y);
    var controlledCoordinate = sourceCoordinate.getNextInDirection(data.direction);

    this.sourceNode = ocargo.Node.findNodeByCoordinate(sourceCoordinate, nodes);
    this.controlledNode = ocargo.Node.findNodeByCoordinate(controlledCoordinate, nodes);
};

ocargo.TrafficLight.prototype.reset = function() {
    this.currentLightTime = this.startTime;
    this.state = this.startingState;
};

ocargo.TrafficLight.prototype.getState = function() {
    return this.state;
};

ocargo.TrafficLight.prototype.incrementTime = function(model) {
    this.currentLightTime++;

    if (this.state === ocargo.TrafficLight.RED && this.currentLightTime >= this.redDuration) {
    	this.state = ocargo.TrafficLight.GREEN;
    	this.currentLightTime = 0;
        this.queueAnimation(model);
    }
    else if (this.state === ocargo.TrafficLight.GREEN && this.currentLightTime >= this.greenDuration) {
    	this.state = ocargo.TrafficLight.RED;
    	this.currentLightTime = 0;
        this.queueAnimation(model);
    }
};

ocargo.TrafficLight.prototype.queueAnimation = function(model) {
    ocargo.animation.appendAnimation({
        type: 'trafficlight',
        id: this.id,
        colour: this.state,
        description: 'Traffic light: ' + this.state
    });
};

ocargo.TrafficLight.RED = 'RED';
ocargo.TrafficLight.GREEN = 'GREEN';
