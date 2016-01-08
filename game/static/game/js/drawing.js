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

var GRID_WIDTH = 10;
var GRID_HEIGHT = 8;
var GRID_SPACE_SIZE = 100;
var PAPER_WIDTH = GRID_SPACE_SIZE * GRID_WIDTH;
var PAPER_HEIGHT = GRID_SPACE_SIZE * GRID_HEIGHT;
var PAPER_PADDING = 30;
var EXTENDED_PAPER_WIDTH = PAPER_WIDTH + 2 * PAPER_PADDING;
var EXTENDED_PAPER_HEIGHT = PAPER_HEIGHT + 2 * PAPER_PADDING;

var DEFAULT_CHARACTER_WIDTH = 40;
var DEFAULT_CHARACTER_HEIGHT = 20;

var COW_WIDTH = 50;
var COW_HEIGHT = 50;

ocargo.Drawing = function(startingPosition) {

    /*************/
    /* Constants */
    /*************/

    var characterWidth = typeof CHARACTER_WIDTH !== 'undefined'? CHARACTER_WIDTH : DEFAULT_CHARACTER_WIDTH;
    var characterHeight =  typeof CHARACTER_HEIGHT !== 'undefined'? CHARACTER_HEIGHT : DEFAULT_CHARACTER_HEIGHT;

    var TRAFFIC_LIGHT_WIDTH = 60;
    var TRAFFIC_LIGHT_HEIGHT = 22;

    var INITIAL_CFC_OFFSET_X = -105;
    var INITIAL_CFC_OFFSET_Y = -7;

    var DESTINATION_NOT_VISITED_COLOUR = 'red';
    var DESTINATION_VISITED_COLOUR = 'green';

    /*********/
    /* State */
    /*********/

    var paper = new Raphael('paper', EXTENDED_PAPER_WIDTH, EXTENDED_PAPER_HEIGHT);
    var roadImages = [];

    var lightImages = {};
    var destinationImages = {};

    var character;

    if (!ocargo.Drawing.inLevelEditor()) {
        character = new ocargo.Character(paper, CHARACTER_URL, WRECKAGE_URL,
            characterWidth, characterHeight, startingPosition, NIGHT_MODE);
    }

    this.reset = function() {
        character.reset();
    };

    /*********************/
    /* Preloading images */
    /*********************/
    // Used by level editor to preload road tiles to prevent jittery drawing

    this.preloadRoadTiles = function () {
        var tiles = ['dead_end', 'crossroads', 'straight', 't_junction', 'turn'];
        var tileImages = [];
        var path = ocargo.Drawing.raphaelImageDir + 'road_tiles/';

        for (var i = 0; i < tiles.length; i++) {
            tileImages.push(paper.image(path + 'road/' + tiles[i] + '.svg', 0, 0, GRID_SPACE_SIZE, GRID_SPACE_SIZE));
            tileImages.push(paper.image(path + 'path/' + tiles[i] + '.svg', 0, 0, GRID_SPACE_SIZE, GRID_SPACE_SIZE));
        }

        for (var i = 0; i < tileImages.length; i++) {
            tileImages[i].remove()
        }
    };

    function calculateCFCInitialPosition(startNode) {
        var coord = ocargo.Drawing.translate(startNode.coordinate);
        return {
            x: coord.x * GRID_SPACE_SIZE + INITIAL_CFC_OFFSET_X + PAPER_PADDING,
            y: coord.y * GRID_SPACE_SIZE + INITIAL_CFC_OFFSET_Y + PAPER_PADDING
        }
    }

    function calculateInitialRotation(previousNode, startNode) {
        var nodeAngleRadians = ocargo.calculateNodeAngle(previousNode, startNode);
        var nodeAngleDegrees = nodeAngleRadians * (180 / Math.PI);
        return -nodeAngleDegrees; // Calculation is counterclockwise, transformations are clockwise
    }

    // Return a pair of letters which represent the orientation of the turn
    // Directions are relative to the centre point of the turn
    // E.g. an L-shape turn will be described as 'UR'
    // D: Down, U: Up, L: Left, R:Right
    function getRoadLetters(previous, node1, node2) {
        previous = ocargo.Drawing.translate(previous);
        node1 = ocargo.Drawing.translate(node1);
        node2 = ocargo.Drawing.translate(node2);

        if (isHorizontal(node1, node2) &&
            (previous === null || isHorizontal(previous, node1))) {
            return 'H';

        } else if (isVertical(node1, node2) &&
            (previous === null || isVertical(previous, node1))) {
            return 'V';
            // Handle turns.
        } else {
            if (isProgressive(previous.x, node1.x)) {
                return nextPointAbove(node1, node2) ? 'DL' : 'UL';
            }
            if (isProgressive(node1.x, previous.x)) {
                return nextPointAbove(node1, node2) ? 'DR' : 'UR';
            }
            if (isProgressive(previous.y, node1.y)) {
                return nextPointFurther(node1, node2) ? 'UR' : 'UL';
            }
            if (isProgressive(node1.y, previous.y)) {
                return nextPointFurther(node1, node2) ? 'DR' : 'DL';
            }
        }
    }

    function isHorizontal(prev, next) {
        return prev.y === next.y;
    }

    function isVertical(prev, next) {
        return prev.x === next.x;
    }

    function nextPointAbove(curr, next) {
        return curr.y < next.y;
    }

    function nextPointFurther(curr, next) {
        return curr.x < next.x;
    }

    function isProgressive(coord1, coord2) {
        return coord1 < coord2;
    }

    // Returns the direction of the middle branch
    // E.g. T-shaped junction will be described as 'down'
    function tJunctionOrientation(middle, node1, node2, node3) {
        var res1 = getRoadLetters(node1, middle, node2);
        var res2 = getRoadLetters(node2, middle, node3);

        if (res1 === 'H' && res2 === 'DR') {
            return 'down';
        } else if (res1 === 'UR' && res2 === 'DR') {
            return 'right';
        } else if (res1 === 'UL' && res2 === 'V') {
            return 'left';
        } else {
            return 'up';
        }
    }
    /***************/
    /** Rendering **/
    /***************/

    this.renderDestinations = function (destinations) {
        for (var i = 0; i < destinations.length; i++) {
            var destination = destinations[i].node;
            var variation = getDestinationPosition(destination);

            var destinationRect = paper.rect(destination.coordinate.x * GRID_SPACE_SIZE + PAPER_PADDING,
                PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - 100 + PAPER_PADDING,
                100, 100).attr({'stroke': DESTINATION_NOT_VISITED_COLOUR});

            var destinationHouse = paper.image(ocargo.Drawing.raphaelImageDir + HOUSE_URL,
                destination.coordinate.x * GRID_SPACE_SIZE + variation[0] + PAPER_PADDING,
                PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - variation[1] + PAPER_PADDING,
                50, 50).transform('r' + variation[2]);

            destinationImages[destinations[i].id] = {
                rect: destinationRect,
                house: destinationHouse
            };
        }

        //find a side of the road
        function getDestinationPosition(destination) {
            var roadLetters = [];

            //might be best to just use the coordinates rather than get road letters and then convert back to directions
            if (destination.connectedNodes.length === 1) {
                var previousNode = destination.connectedNodes[0];
                var nextNode = {};
                nextNode.coordinate = new ocargo.Coordinate(
                    destination.coordinate.x + (destination.coordinate.x - previousNode.coordinate.x),
                    destination.coordinate.y + (destination.coordinate.y - previousNode.coordinate.y));
                roadLetters.push(getRoadLetters(previousNode.coordinate, destination.coordinate,
                    nextNode.coordinate));
            } else {
                for (var i = 0; i < destination.connectedNodes.length; i++) {
                    var previousNode = destination.connectedNodes[i];
                    for (var j = i + 1; j < destination.connectedNodes.length; j++) {
                        roadLetters.push(getRoadLetters(previousNode.coordinate, destination.coordinate,
                            destination.connectedNodes[j].coordinate));
                    }
                }
            }
            var left = true;
            var right = true;
            var up = true;
            var down = true;

            //variation specifies x,y,rotation
            var variation = [25, 25, 90];

            // Set "default" variations of the house position
            // based on straight roads and turns
            if (roadLetters.indexOf('H') >= 0) {
                left = false;
                right = false;
                variation = [25, 25, 90];
            }
            if (roadLetters.indexOf('V') >= 0) {
                up = false;
                down = false;
                variation = [-25, 75, 180];
            }
            if (roadLetters.indexOf('UL') >= 0) {
                left = false;
                up = false;
                variation = [45, 55, 45];
            }
            if (roadLetters.indexOf('DL') >= 0) {
                left = false;
                down = false;
                variation = [45, 95, 315];
            }
            if (roadLetters.indexOf('UR') >= 0) {
                right = false;
                up = false;
                variation = [5, 55, 135];
            }
            if (roadLetters.indexOf('DR') >= 0) {
                right = false;
                down = false;
                variation = [5, 95, 225];
            }

            // Adapt for T-junctions and crossroads
            if (!(left || right || up || down)) {
                // 4-way junction, so hang it off to the bottom left
                variation = [-25, 25, 135];
            } else if (!(up || left || right)) {
                // T junction, road at bottom
                variation = [25, 25, 90];
            } else if (!(down || left || right)) {
                // T junction, road at top
                variation = [25, 125, 270];
            } else if (!(up || down || left)) {
                // T junction, road at right
                variation = [75, 75, 0];
            } else if (!(up || down || right)) {
                // T junction, road at left
                variation = [-25, 75, 180];
            }

            return variation;
        }
    };

    this.renderOrigin = function (position) {
        var initialPosition = calculateCFCInitialPosition(position.currentNode);
        var cfc = paper.image(ocargo.Drawing.raphaelImageDir + CFC_URL, initialPosition.x, initialPosition.y, 100, 107);
        var rotation = calculateInitialRotation(position.previousNode, position.currentNode);
        var transformation = ocargo.Drawing.rotationTransformationAroundCentreOfGridSpace(
            rotation,
            position.currentNode.coordinate.x,
            position.currentNode.coordinate.y);
        cfc.transform(transformation);
        cfc.transform('... r90');
    };

    this.renderRoad = function (nodes) {
        for (var i = 0; i < roadImages.length; i++) {
            var image = roadImages[i];
            if (image) {
                image.remove();
            }
        }

        var path = ocargo.Drawing.raphaelImageDir + 'road_tiles/';

        path += CHARACTER_NAME === 'Van' ? 'road/' : 'path/';

        roadImages = [];
        for (var i = 0; i < nodes.length; i++) {
            var node = nodes[i];
            var roadImage;
            switch (node.connectedNodes.length) {
                case 1:
                    roadImage = drawDeadEndRoad(node, path);
                    break;

                case 2:
                    roadImage = drawSingleRoadSegment(node.connectedNodes[0], node,
                        node.connectedNodes[1], path);
                    break;

                case 3:
                    roadImage = drawTJunction(node, path);
                    break;

                case 4:
                    roadImage = drawCrossRoads(node, path);
                    break;

                default:
                    break;
            }
            roadImages.push(roadImage);
        }

        function drawDeadEndRoad(node, path) {
            var previousNode = node.connectedNodes[0];

            var nextNode = {};
            nextNode.coordinate = new ocargo.Coordinate(
                node.coordinate.x + (node.coordinate.x - previousNode.coordinate.x),
                node.coordinate.y + (node.coordinate.y - previousNode.coordinate.y));

            var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

            var prevFlipped = ocargo.Drawing.translate(previousNode.coordinate);
            var flipped = ocargo.Drawing.translate(node.coordinate);

            var road = paper.image(path + 'dead_end.svg',
                flipped.x * GRID_SPACE_SIZE + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + PAPER_PADDING, GRID_SPACE_SIZE, GRID_SPACE_SIZE);

            if (roadLetters === 'H' && prevFlipped.x < flipped.x) {
                road.rotate(90, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING);
            }
            else if (roadLetters === 'H' && prevFlipped.x > flipped.x) {
                road.rotate(270, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING);
            }
            else if (roadLetters === 'V' && prevFlipped.y < flipped.y) {
                road.rotate(180, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING);
            }

            return road;
        }

        function drawSingleRoadSegment(previousNode, node, nextNode, path) {
            var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

            var flipped = ocargo.Drawing.translate(node.coordinate);
            var roadSrc = path + (roadLetters === 'H' || roadLetters === 'V' ? 'straight' : 'turn') + '.svg';
            var road = paper.image(roadSrc, flipped.x * GRID_SPACE_SIZE + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + PAPER_PADDING, GRID_SPACE_SIZE, GRID_SPACE_SIZE);

            if (roadLetters === 'H') {
                road.rotate(90);
            }
            else if (roadLetters === 'UL') {
                road.rotate(90, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING);
            }
            else if (roadLetters === 'UR') {
                road.rotate(180, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING);
            }
            else if (roadLetters === 'DR') {
                road.rotate(270, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING);
            }

            return road;
        }

        function drawTJunction(node, path) {
            var node1 = node.connectedNodes[0];
            var node2 = node.connectedNodes[1];
            var node3 = node.connectedNodes[2];

            var flipped = ocargo.Drawing.translate(node.coordinate);

            var letters12 = getRoadLetters(node1.coordinate, node.coordinate, node3.coordinate);
            var letters13 = getRoadLetters(node1.coordinate, node.coordinate, node2.coordinate);

            var rotation = 0;
            if ((letters12 === 'V' && (letters13 === 'UL' || letters13 === 'DL')) ||
                (letters12 === 'UL' && (letters13 === 'DL' || letters13 === 'V' )) ||
                (letters12 === 'DL' && (letters13 === 'UL' || letters13 === 'V' ))) {
                rotation = 0;
            }
            else if ((letters12 === 'H' && (letters13 === 'UL' || letters13 === 'UR')) ||
                (letters12 === 'UL' && (letters13 === 'UR' || letters13 === 'H' )) ||
                (letters12 === 'UR' && (letters13 === 'UL' || letters13 === 'H' ))) {
                rotation = 90;
            }
            else if ((letters12 === 'V' && (letters13 === 'UR' || letters13 === 'DR')) ||
                (letters12 === 'UR' && (letters13 === 'DR' || letters13 === 'V' )) ||
                (letters12 === 'DR' && (letters13 === 'UR' || letters13 === 'V' ))) {
                rotation = 180;
            }
            else if ((letters12 === 'H' && (letters13 === 'DL' || letters13 === 'DR')) ||
                (letters12 === 'DL' && (letters13 === 'DR' || letters13 === 'H' )) ||
                (letters12 === 'DR' && (letters13 === 'DL' || letters13 === 'H' ))) {
                rotation = 270;
            }

            var road = paper.image(path + 't_junction.svg',
                flipped.x * GRID_SPACE_SIZE + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + PAPER_PADDING, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
            road.rotate(rotation, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 + PAPER_PADDING);

            return road;
        }

        function drawCrossRoads(node, path) {
            var flipped = ocargo.Drawing.translate(node.coordinate);

            return paper.image(path + 'crossroads.svg',
                flipped.x * GRID_SPACE_SIZE + PAPER_PADDING, flipped.y * GRID_SPACE_SIZE + PAPER_PADDING, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
        }
    };

    this.renderBackground = function () {
        if (!ocargo.Drawing.isMobile()) {
            paper.rect(0, 0, EXTENDED_PAPER_WIDTH, EXTENDED_PAPER_HEIGHT)
                .attr({
                    fill: 'url(' + ocargo.Drawing.raphaelImageDir + BACKGROUND_URL + ')',
                    'stroke': 'none'
                });
        }
    };

    this.renderDecor = function (decors) {
        for (var i = 0; i < decors.length; i++) {
            var decor = decors[i];
            var src = ocargo.Drawing.raphaelImageDir + decor.url;
            var x = decor.x + PAPER_PADDING;
            var y = PAPER_HEIGHT - decor.y - decor.height + PAPER_PADDING;
            var width = decor.width;
            var height = decor.height;
            paper.image(src, x, y, width, height);
        }
    };

    this.createTrafficLightImage = function (url) {
        return paper.image(url, 0, 0, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT);
    };

    this.setTrafficLightImagePosition = function (sourceCoordinate, controlledCoordinate, image) {
        // get position based on nodes
        var x = (controlledCoordinate.x + sourceCoordinate.x) / 2.0;
        var y = (controlledCoordinate.y + sourceCoordinate.y) / 2.0;

        // get rotation based on nodes (should face source)
        var angle = sourceCoordinate.angleTo(controlledCoordinate) * (180 / Math.PI);
        var rotation = 90 - angle;

        // draw red and green lights, keep reference to both
        var drawX = x * GRID_SPACE_SIZE + TRAFFIC_LIGHT_HEIGHT + PAPER_PADDING;
        var drawY = PAPER_HEIGHT - (y * GRID_SPACE_SIZE) - TRAFFIC_LIGHT_WIDTH + PAPER_PADDING;

        image.transform('t' + drawX + ',' + drawY + ' r' + rotation + 's-1,1');
    };

    this.renderTrafficLights = function (trafficLights) {
        for (var i = 0; i < trafficLights.length; i++) {
            var trafficLight = trafficLights[i];
            var sourceCoordinate = trafficLight.sourceNode.coordinate;
            var controlledCoordinate = trafficLight.controlledNode.coordinate;

            trafficLight.greenLightEl = this.createTrafficLightImage(ocargo.Drawing.raphaelImageDir + 'trafficLight_green.svg');
            trafficLight.redLightEl = this.createTrafficLightImage(ocargo.Drawing.raphaelImageDir + 'trafficLight_red.svg');
            trafficLight.greenLightEl.node.id = 'trafficLight_' + i + '_green';
            trafficLight.redLightEl.node.id = 'trafficLight_' + i + '_red';

            this.setTrafficLightImagePosition(sourceCoordinate, controlledCoordinate, trafficLight.greenLightEl);
            this.setTrafficLightImagePosition(sourceCoordinate, controlledCoordinate, trafficLight.redLightEl);

            // hide light which isn't the starting state
            if (trafficLight.startingState === ocargo.TrafficLight.RED) {
                trafficLight.greenLightEl.attr({'opacity': 0});
            }
            else {
                trafficLight.redLightEl.attr({'opacity': 0});
            }

            lightImages[trafficLight.id] = [trafficLight.greenLightEl, trafficLight.redLightEl];
        }
    };

    this.determineCowOrientation = function (coordinate, node) {
        var x = coordinate.x;
        var y = coordinate.y;

        var xOffset = 0;
        var yOffset = 0;
        var rotation = 0;

        if (node.connectedNodes.length === 1) {
            // Deadends
            var previousNode = node.connectedNodes[0];
            var nextNode = {};
            nextNode.coordinate = new ocargo.Coordinate(
                node.coordinate.x + (node.coordinate.x - previousNode.coordinate.x),
                node.coordinate.y + (node.coordinate.y - previousNode.coordinate.y));

            var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

            if (roadLetters === 'V') {
                rotation = 90;
            }
        } else if (node.connectedNodes.length === 2) {
            // Turns
            var previousNode = node.connectedNodes[0];
            var nextNode = node.connectedNodes[1];

            var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

            if (roadLetters === 'V') {
                rotation = 90;
            } else if (roadLetters === 'UL') {
                xOffset = -0.15 * GRID_SPACE_SIZE;
                yOffset = -0.15 * GRID_SPACE_SIZE;
                rotation = -45;
            }
            else if (roadLetters === 'UR') {
                xOffset = +0.15 * GRID_SPACE_SIZE;
                yOffset = -0.15 * GRID_SPACE_SIZE;
                rotation = 45;
            }
            else if (roadLetters === 'DL') {
                xOffset = -0.15 * GRID_SPACE_SIZE;
                yOffset = +0.15 * GRID_SPACE_SIZE;
                rotation = -135;
            }
            else if (roadLetters === 'DR') {
                xOffset = +0.15 * GRID_SPACE_SIZE;
                yOffset = +0.15 * GRID_SPACE_SIZE;
                rotation = 135;
            }
        } else if (node.connectedNodes.length === 3) {
            // T-junctions
            var previousNode = node.connectedNodes[0];
            var nextNode = node.connectedNodes[1];
            var nextNextNode = node.connectedNodes[2];
            var res = tJunctionOrientation(node.coordinate, previousNode.coordinate,
                nextNode.coordinate, nextNextNode.coordinate);
            if (res === 'down') {
                rotation = 180;
            }
            else if (res === 'right') {
                rotation = 90;
            }
            else if (res === 'left') {
                rotation = -90
            }
            else if (res === 'top') {
            }
        }

        var drawX = (x + 0.5) * GRID_SPACE_SIZE - COW_WIDTH / 2 + xOffset + PAPER_PADDING;
        var drawY = PAPER_HEIGHT - ((y + 0.5) * GRID_SPACE_SIZE) - COW_HEIGHT / 2 + yOffset + PAPER_PADDING;

        return {drawX: drawX, drawY: drawY, rotation: rotation};
    };

    this.createCowImage = function(type) {
        return paper.image(ocargo.Drawing.raphaelImageDir + ocargo.Drawing.cowUrl(type), 0, 0, COW_WIDTH, COW_HEIGHT);
    };

    this.setCowImagePosition = function (coordinate, image, node) {

        var res = this.determineCowOrientation(coordinate, node);

        image.transform('t' + res.drawX + ',' + res.drawY + 'r' + res.rotation);
    };

    this.renderCow = function (id, coordinate, node, animationLength, type) {

        var res = this.determineCowOrientation(coordinate, node);
        var image = paper.image(ocargo.Drawing.raphaelImageDir + ocargo.Drawing.cowUrl(type), res.drawX, res.drawY, COW_WIDTH, COW_HEIGHT);
        var rot = "r" + res.rotation;
        image.transform(rot + "s0.1");
        image.animate({transform: rot + "s1"}, animationLength, 'linear');

        return {
            'coordinate': coordinate,
            'image': image
        };
    };

    this.removeCow = function (cow, animationLength) {
        cow.image.animate({transform: "s0.01"}, animationLength, 'linear', function () {
            cow.image.remove();
        });
    };

    this.renderCharacter = function() {
        character.render();
    };

    this.createGrid = function () {
        var grid = [];
        for (var i = 0; i < GRID_WIDTH; i++) {
            var row = [];
            for (var j = 0; j < GRID_HEIGHT; j++) {
                var x = i * GRID_SPACE_SIZE + PAPER_PADDING;
                var y = j * GRID_SPACE_SIZE + PAPER_PADDING;

                row.push(paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE));
            }
            grid.push(row);
        }
        return grid;
    };

    this.renderGrid = function (grid, currentTheme) {
        for (var i = 0; i < GRID_WIDTH; i++) {
            for (var j = 0; j < GRID_HEIGHT; j++) {
                grid[i][j].attr({
                    'stroke': currentTheme.border,
                    'fill': currentTheme.background,
                    'fill-opacity': 1
                });
            }
        }
    };

    this.clearPaper = function () {
        paper.clear();
    };

    this.renderMap = function (map) {
        this.renderBackground();
        this.renderRoad(map.nodes);
    };

    this.createImage = function (url, x, y, width, height) {
        return paper.image(url, x, y, width, height);
    };

    /****************/
    /** Animations **/
    /****************/

    this.transitionTrafficLight = function (lightID, endState, animationLength) {
        if (endState === ocargo.TrafficLight.GREEN) {
            lightImages[lightID][0].animate({opacity: 1}, animationLength / 2, 'linear');
            lightImages[lightID][1].animate({opacity: 0}, animationLength, 'linear');
        }
        else {
            lightImages[lightID][0].animate({opacity: 0}, animationLength / 2, 'linear');
            lightImages[lightID][1].animate({opacity: 1}, animationLength, 'linear');
        }
    };

    this.transitionDestination = function (destinationID, visited, duration) {
        var destinationRect = destinationImages[destinationID].rect;
        var colour = visited ? DESTINATION_VISITED_COLOUR : DESTINATION_NOT_VISITED_COLOUR;

        destinationRect.animate({'stroke': colour}, duration, 'linear');
    };

    this.scrollToShowCharacter = function() {
        character.scrollToShow();
    };

    this.moveForward = function (callback, scalingFactor) {
        return character.moveForward(callback, scalingFactor);
    };

    this.turnLeft = function (callback, scalingFactor) {
        return character.turnLeft(callback, scalingFactor);
    };

    this.turnRight = function (callback, scalingFactor) {
        return character.turnRight(callback, scalingFactor);
    };

    this.turnAround = function (direction) {
        return character.turnAround(direction);
    };

    this.wait = function (duration, callback) {
        character.wait(duration, callback);
    };

    this.deliver = function (destinationId, duration) {
        this.transitionDestination(destinationId, true, duration);
    };

    this.collisionWithCow = function (previousNode, currentNode, attemptedAction) {
        return character.collisionWithCow(previousNode, currentNode, attemptedAction)
    };

    this.crash = function (previousNode, currentNode, attemptedAction) {
        return character.crash(attemptedAction)
    };

    this.setCharacterManoeuvreDuration = function (speed) {
        character.setManoeuvreDuration(speed);
    };
};

/********************************/
/* Static methods and constants */
/********************************/

// Flips the y coordinate upside down to match the raphael coordinate system
ocargo.Drawing.translate = function (coordinate) {
    return new ocargo.Coordinate(coordinate.x, GRID_HEIGHT - 1 - coordinate.y);
};

/*
 This is the function that starts the pop-up.
 Buttons should be passed in separately to the function instead of concatenating
 to the message so as to keep the layout of the pop-up consistent.
 The following elements will be displayed vertically from top to bottom in this order:
 1. title (bolded)
 2. subtitle (same font size as title)
 3. message (smaller font size than title and subtitle)
 4. buttons (in one row)
 Mascot will be displayed on the right hand side of the popup
 */
ocargo.Drawing.startPopup = function (title, subtitle, message, mascot, buttons) {
    $('#myModal-title').html(title);
    $('#myModal-lead').html(subtitle);
    $('#myModal-mainText').html(message);

    if (mascot) {
        $('#modal-mascot').show();
    } else {
        $('#modal-mascot').hide();
    }

    if (buttons) {
        $('#modal-buttons').html(buttons);
    } else {
        $('#modal-buttons').html(ocargo.button.dismissButtonHtml('close_button', 'Close'));
    }


    $('#myModal').foundation('reveal', 'open', {
        animation: 'fadeAndPop',
        animation_speed: 200
    });
};

// This is the function that starts the pop-up with a yes and a no button
ocargo.Drawing.startYesNoPopup = function (title, subtitle, message, yesFunction, noFunction, mascot) {
    var buttonHtml = '<button id="modal-yesBtn" class="navigation_button long_button">Yes</button> <button id="modal-noBtn" class="navigation_button long_button">No</button>';
    ocargo.Drawing.startPopup(title, subtitle, message, mascot, buttonHtml);
    $('#modal-yesBtn').click(yesFunction);
    $('#modal-noBtn').click(noFunction);
};

// This is the function that starts the pop-up when there is no internet connection while playing the game
ocargo.Drawing.startInternetDownPopup = function () {
    ocargo.Drawing.startPopup(ocargo.messages.errorTitle, "", ocargo.messages.internetDown);
};

ocargo.Drawing.showButtonHelp = function () {
    $('#myModal-lead').html('');
    $('#myModal-mainText').html('<p>' + ocargo.messages.buttonHelp + '</p>' +
        '<p><button onclick="document.getElementById(' + "'close-modal'" +
        ').click()">Close</button></p>');
};

ocargo.Drawing.isMobile = function () {
    var mobileDetect = new MobileDetect(window.navigator.userAgent);
    return !!mobileDetect.mobile();
};

ocargo.Drawing.isChrome = function () {
    return navigator.userAgent.indexOf('Chrome') > -1;
};

ocargo.Drawing.renderCoins = function (coins) {
    var html = "<div>";
    var i;
    for (i = 0; i < coins.whole; i++) {
        html += "<img src='" + ocargo.Drawing.imageDir + "coins/coin_gold.svg' width='50'>";
    }
    if (coins.half) {
        html += "<img src='" + ocargo.Drawing.imageDir + "coins/coin_5050_dots.svg' width='50'>";
    }
    for (i = 0; i < coins.zero; i++) {
        html += "<img src='" + ocargo.Drawing.imageDir + "coins/coin_empty_dots.svg' width='50'>";
    }

    return html;
};


ocargo.Drawing.cowUrl = function(type){
    switch(type){
        case ocargo.Cow.WHITE:
            return ocargo.Drawing.whiteCowUrl;
        case ocargo.Cow.BROWN:
            return ocargo.Drawing.brownCowUrl;
        default:
            return ocargo.Drawing.whiteCowUrl;
    }
};


ocargo.Drawing.createAbsoluteRotationTransformation = function(degrees, rotationPointX, rotationPointY) {
    var transformation = '... R' + degrees;
    if (rotationPointX !== undefined && rotationPointY !== undefined) {
        transformation += ',' + rotationPointX;
        transformation += ',' + rotationPointY;
    }
    return transformation;
};

ocargo.Drawing.rotationTransformationAroundCentreOfGridSpace = function(degrees, x, y) {
    var rotationPointX = (x + 1 / 2) * GRID_SPACE_SIZE + PAPER_PADDING;
    var rotationPointY = (GRID_HEIGHT - (y + 1 / 2)) * GRID_SPACE_SIZE + PAPER_PADDING; //flipping y
    var result = ocargo.Drawing.createAbsoluteRotationTransformation(degrees, rotationPointX, rotationPointY);
    return result;
};

ocargo.Drawing.inLevelEditor = function() {
    return typeof CHARACTER_URL === 'undefined';
};

ocargo.Drawing.FRONT_VIEW = "front_view";
ocargo.Drawing.TOP_VIEW = "top_view";

ocargo.Drawing.whiteCowUrl = 'Clarice.svg';
ocargo.Drawing.brownCowUrl = 'Clarice_Jersey.svg';

ocargo.Drawing.imageDir = '/static/game/image/';
ocargo.Drawing.raphaelImageDir = '/static/game/raphael_image/';