'use strict';

var ocargo = ocargo || {};

var GRID_WIDTH = 10;
var GRID_HEIGHT = 8;
var GRID_SPACE_SIZE = 100;
var PAPER_WIDTH = GRID_SPACE_SIZE * GRID_WIDTH;
var PAPER_HEIGHT = GRID_SPACE_SIZE * GRID_HEIGHT;

var CHARACTER_WIDTH = 40;
var CHARACTER_HEIGHT = 20;

var ROAD_WIDTH = GRID_SPACE_SIZE * 0.7;

ocargo.Drawing = function() {

    /*************/
    /* Constants */
    /*************/

    var TRAFFIC_LIGHT_WIDTH = 60;
    var TRAFFIC_LIGHT_HEIGHT = 22;

    var MOVE_DISTANCE = GRID_SPACE_SIZE;
    var TURN_DISTANCE = MOVE_DISTANCE / 2;
    var INITIAL_OFFSET_X = 10;
    var INITIAL_OFFSET_Y = 82;
    var ROTATION_OFFSET_X = 22;
    var ROTATION_OFFSET_Y = CHARACTER_WIDTH - 20;
    
    var DESTINATION_NOT_VISITED_COLOUR = 'red';
    var DESTINATION_VISITED_COLOUR = 'green';

    /*********/
    /* State */
    /*********/

    var paper = new Raphael('paper', PAPER_WIDTH, PAPER_HEIGHT);
    var roadImages = [];

    var vanImages = {};
    var lightImages = {};
    var destinationImages = {};
    var wreckageImages = {};

    /*********************/
    /* Preloading images */
    /*********************/
    // Used by level editor to preload road tiles to prevent jittery drawing

    this.preloadRoadTiles = function() {
        var tiles = ['dead_end', 'crossroads', 'straight', 't_junction', 'turn'];
        var tileImages = [];
        var path = ocargo.Drawing.raphaelImageDir + 'road_tiles/';

        for(var i = 0; i < tiles.length; i++) {
            tileImages.push(paper.image(path + 'road/' + tiles[i] + '.svg', 0, 0, GRID_SPACE_SIZE, GRID_SPACE_SIZE));
            tileImages.push(paper.image(path + 'path/' + tiles[i] + '.svg', 0, 0, GRID_SPACE_SIZE, GRID_SPACE_SIZE));
        }
        
        for(var i = 0; i < tileImages.length; i++) {
            tileImages[i].remove()
        }
    };

    /***************************/
    /* Geometry helper methods */
    /***************************/

    function createRotationTransformation(degrees, rotationPointX, rotationPointY) {
        var transformation = '... r' + degrees;
        if (rotationPointX !== undefined && rotationPointY !== undefined) {
            transformation += ',' + rotationPointX;
            transformation += ',' + rotationPointY;
        }
        return transformation;
    }

    function createAbsoluteRotationTransformation(degrees, rotationPointX, rotationPointY) {
        var transformation = '... R' + degrees;
        if (rotationPointX !== undefined && rotationPointY !== undefined) {
            transformation += ',' + rotationPointX;
            transformation += ',' + rotationPointY;
        }
        return transformation;
    }

    function getRotationTransformationAroundCentreOfGridSpace(element, degrees, x, y) {
        var rotationPointX = (x + 1 / 2) * GRID_SPACE_SIZE;
        var rotationPointY = (GRID_HEIGHT - (y + 1/2)) * GRID_SPACE_SIZE;
        return createAbsoluteRotationTransformation(degrees, rotationPointX, rotationPointY);
    }

    function calculateInitialPosition(startNode) {
        var coord = ocargo.Drawing.translate(startNode.coordinate);
        return {x: coord.x * GRID_SPACE_SIZE - INITIAL_OFFSET_X,
                y: (coord.y + 1) * GRID_SPACE_SIZE - INITIAL_OFFSET_Y}
    }

    function calculateInitialRotation(previousNode, startNode) {
        var nodeAngleRadians = ocargo.calculateNodeAngle(previousNode, startNode);
        var nodeAngleDegrees = nodeAngleRadians * (180 / Math.PI);
        return -nodeAngleDegrees; // Calculation is counterclockwise, transformations are clockwise
    }

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

    /***************/
    /** Rendering **/
    /***************/

    this.renderDestinations = function(destinations) {
        for(var i = 0; i < destinations.length; i++) {
            var destination = destinations[i].node;
            var variation = getDestinationPosition(destination);

            var destinationRect = paper.rect(destination.coordinate.x * GRID_SPACE_SIZE, 
                                    PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - 100,
                                    100, 100).attr({'stroke': DESTINATION_NOT_VISITED_COLOUR});

            var destinationHouse = paper.image(ocargo.Drawing.raphaelImageDir + HOUSE_URL,
                                    destination.coordinate.x * GRID_SPACE_SIZE + variation[0],
                                    PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - variation[1],
                                    50, 50).transform('r' + variation[2]);

            destinationImages[destinations[i].id] = {rect: destinationRect, 
                                                    house: destinationHouse};
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
            if (roadLetters.indexOf('H') >= 0 ) {
                left = false;
                right = false;
                variation = [25,25,90];
            }
            if (roadLetters.indexOf('V') >= 0 ) {
                up = false;
                down = false;
                variation = [-25,75,180];
            }
            if (roadLetters.indexOf('UL') >= 0 ) {
                left = false;
                up = false;
                variation = [45,55,45];
            }
            if (roadLetters.indexOf('DL') >= 0 ) {
                left = false;
                down = false;
                variation = [45,95,315];
            }
            if (roadLetters.indexOf('UR') >= 0 ) {
                right = false;
                up = false;
                variation = [5,55,135];
            }
            if (roadLetters.indexOf('DR') >= 0 ) {
                right = false;
                down = false;
                variation = [5,95,225];
            }

            // Adapt for T-junctions and crossroads
            if (!(left || right || up || down)) {
                // 4-way junction, so hang it off to the bottom left
                variation = [-25,25,135];
            } else if (!(up || left || right)) {
                // T junction, road at bottom
                variation = [25,25,90];
            } else if (!(down || left || right)) {
                // T junction, road at top
                variation = [25,125,270];
            } else if (!(up || down || left)) {
                // T junction, road at right
                variation = [75,75,0];
            } else if (!(up || down || right)) {
                // T junction, road at left
                variation = [-25,75,180];
            }

            return variation;
        }
    };

    this.renderOrigin = function(position) {
        var initialPosition = calculateInitialPosition(position.currentNode);
        var cfc = paper.image(ocargo.Drawing.raphaelImageDir + CFC_URL, initialPosition.x - 95, initialPosition.y - 25, 100, 107);

        var rotation = calculateInitialRotation(position.previousNode, position.currentNode);
        var transformation = getRotationTransformationAroundCentreOfGridSpace(cfc,
                                                                              rotation, 
                                                                              position.currentNode.coordinate.x,
                                                                              position.currentNode.coordinate.y);
        cfc.transform(transformation);
        cfc.transform('... r90');
    };

    this.renderRoad = function(nodes) {
        for(var i = 0; i < roadImages.length; i++) {
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
                flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);

            if (roadLetters === 'H' && prevFlipped.x < flipped.x) {
                road.rotate(90, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
            }
            else if (roadLetters === 'H' && prevFlipped.x > flipped.x) {
                road.rotate(270, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
            }
            else if (roadLetters === 'V' && prevFlipped.y < flipped.y) {
                road.rotate(180, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
            }

            return road;
        }

        function drawSingleRoadSegment(previousNode, node, nextNode, path) {
            var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

            var flipped = ocargo.Drawing.translate(node.coordinate);
            var roadSrc = path + (roadLetters === 'H' || roadLetters ==='V' ? 'straight' : 'turn') + '.svg';
            var road = paper.image(roadSrc, flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);

            if (roadLetters === 'H') {
                road.rotate(90);
            }
            else if (roadLetters === 'UL') {
                road.rotate(90, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
            }
            else if (roadLetters === 'UR') {
                road.rotate(180, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
            }
            else if (roadLetters === 'DR') {
                road.rotate(270, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
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
            if      ((letters12 === 'V'  && (letters13 === 'UL' || letters13 === 'DL')) ||
                     (letters12 === 'UL' && (letters13 === 'DL' || letters13 === 'V' )) ||
                     (letters12 === 'DL' && (letters13 === 'UL' || letters13 === 'V' ))) {
                rotation = 0;
            }
            else if ((letters12 === 'H'  && (letters13 === 'UL' || letters13 === 'UR')) ||
                     (letters12 === 'UL' && (letters13 === 'UR' || letters13 === 'H' )) ||
                     (letters12 === 'UR' && (letters13 === 'UL' || letters13 === 'H' ))) {
                rotation = 90;
            }
            else if ((letters12 === 'V'  && (letters13 === 'UR' || letters13 === 'DR')) ||
                     (letters12 === 'UR' && (letters13 === 'DR' || letters13 === 'V' )) ||
                     (letters12 === 'DR' && (letters13 === 'UR' || letters13 === 'V' ))) {
                rotation = 180;
            }
            else if ((letters12 === 'H'  && (letters13 === 'DL' || letters13 === 'DR')) ||
                     (letters12 === 'DL' && (letters13 === 'DR' || letters13 === 'H' )) ||
                     (letters12 === 'DR' && (letters13 === 'DL' || letters13 === 'H' ))) {
                rotation = 270;
            }

            var road = paper.image(path + 't_junction.svg',
                flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
            road.rotate(rotation, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);

            return road;
        }

        function drawCrossRoads(node, path) {
            var flipped = ocargo.Drawing.translate(node.coordinate);

            return paper.image(path + 'crossroads.svg',
                    flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
        }
    };

    this.renderBackground = function() {
        if(!ocargo.Drawing.isMobile()) {
            paper.rect(0, 0, PAPER_WIDTH, PAPER_HEIGHT)
                .attr({fill: 'url(' + ocargo.Drawing.raphaelImageDir + BACKGROUND_URL + ')',
                    'stroke': 'none'});
        }
    };

    this.renderDecor = function(decors) {
        for (var i = 0; i < decors.length; i++) {
            var decor = decors[i];
            var src = ocargo.Drawing.raphaelImageDir + decor.url;
            var x = decor.x;
            var y = PAPER_HEIGHT - decor.y - decor.height;
            var width = decor.width;
            var height = decor.height;
            paper.image(src, x, y, width, height);
        }
    };

    this.createTrafficLightImage = function(url) {
        return paper.image(url, 0, 0, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT);
    };

    this.setTrafficLightImagePosition = function(sourceCoordinate, controlledCoordinate, image) {
        // get position based on nodes
        var x = (controlledCoordinate.x + sourceCoordinate.x) / 2.0;
        var y = (controlledCoordinate.y + sourceCoordinate.y) / 2.0;
        
        // get rotation based on nodes (should face source)
        var angle = sourceCoordinate.angleTo(controlledCoordinate) * (180 / Math.PI);
        var rotation = 90 - angle;

        // draw red and green lights, keep reference to both
        var drawX = x * GRID_SPACE_SIZE + TRAFFIC_LIGHT_HEIGHT;
        var drawY = PAPER_HEIGHT - (y * GRID_SPACE_SIZE) - TRAFFIC_LIGHT_WIDTH;

        image.transform('t' + drawX + ',' + drawY + ' r' + rotation + 's-1,1');
    };

    this.renderTrafficLights = function(trafficLights) {
        for (var i = 0; i < trafficLights.length; i++) {
            var trafficLight = trafficLights[i];
            var sourceCoordinate = trafficLight.sourceNode.coordinate;
            var controlledCoordinate = trafficLight.controlledNode.coordinate;

            trafficLight.greenLightEl = this.createTrafficLightImage(ocargo.Drawing.raphaelImageDir + 'trafficLight_green.svg');
            trafficLight.redLightEl = this.createTrafficLightImage(ocargo.Drawing.raphaelImageDir + 'trafficLight_red.svg');

            this.setTrafficLightImagePosition(sourceCoordinate, controlledCoordinate, trafficLight.greenLightEl);
            this.setTrafficLightImagePosition(sourceCoordinate, controlledCoordinate, trafficLight.redLightEl);
            
            // hide light which isn't the starting state
            if(trafficLight.startingState === ocargo.TrafficLight.RED) {
                trafficLight.greenLightEl.attr({'opacity': 0});
            } 
            else {
                trafficLight.redLightEl.attr({'opacity': 0});
            }

            lightImages[trafficLight.id] = [trafficLight.greenLightEl, trafficLight.redLightEl];
        }
    };

    this.setVanImagePosition = function(position, vanID) {
        var vanImage = vanImages[vanID];
        var initialPosition = calculateInitialPosition(position.currentNode);
        vanImage.transform('t' + initialPosition.x + ',' + initialPosition.y);

        var rotation = calculateInitialRotation(position.previousNode, position.currentNode);
        var transformation = getRotationTransformationAroundCentreOfGridSpace(vanImage,
                                                                              rotation, 
                                                                              position.currentNode.coordinate.x,
                                                                              position.currentNode.coordinate.y);
        vanImage.transform(transformation);
        vanImage.transform('... r90');
        vanImage.attr({opacity: 1});
    };    

    this.renderVans = function(position, numVans) {
        for (var i = 0; i < numVans; i++) {
            vanImages[i] = this.createVanImage();
            this.setVanImagePosition(position, i);
        }
        this.scrollToShowVan(0);
    };

    this.createVanImage = function() {
        return paper.image(ocargo.Drawing.raphaelImageDir + CHARACTER_URL, 0, 0, CHAR_HEIGHT, CHAR_WIDTH);
    };

    this.createGrid = function() {
        var grid = [];
        for (var i = 0; i < GRID_WIDTH; i++) {
            var row = [];
            for (var j = 0; j < GRID_HEIGHT; j++) {
                var x = i * GRID_SPACE_SIZE;
                var y = j * GRID_SPACE_SIZE;

                row.push(paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE));
            }
            grid.push(row);
        }
        return grid;
    };

    this.renderGrid = function(grid, currentTheme) {
        for (var i = 0; i < GRID_WIDTH; i++) {
            for (var j = 0; j < GRID_HEIGHT; j++) {
                grid[i][j].attr({'stroke': currentTheme.border,
                                 'fill': currentTheme.background,
                                 'fill-opacity': 1});
            }
        }
    };

    this.clearPaper = function() {
        paper.clear();
    };

    this.renderMap = function(map) {
        this.renderBackground();
        this.renderRoad(map.nodes);
    };

    this.createImage = function(url, x, y, width, height) {
        return paper.image(url, x, y, width, height);
    };

    /****************/
    /** Animations **/
    /****************/

    this.transitionTrafficLight = function(lightID, endState, animationLength) {
        if (endState === ocargo.TrafficLight.GREEN) {
            lightImages[lightID][0].animate({opacity : 1}, animationLength/2, 'linear');
            lightImages[lightID][1].animate({opacity : 0}, animationLength, 'linear');
        }
        else {
            lightImages[lightID][0].animate({opacity : 0}, animationLength/2, 'linear');
            lightImages[lightID][1].animate({opacity : 1}, animationLength, 'linear');
        }
    };

    this.transitionDestination = function(destinationID, visited, animationLength) {
        var destinationRect = destinationImages[destinationID].rect;
        var colour = visited ? DESTINATION_VISITED_COLOUR : DESTINATION_NOT_VISITED_COLOUR;

        destinationRect.animate({'stroke': colour}, animationLength, 'linear');
    };

    this.skipOutstandingVanAnimationsToEnd = function(vanID) {
        var anims = vanImages[vanID].status();
        for (var i = 0, ii = anims.length; i < ii; i++) {
            vanImages[vanID].status(anims[i].anim, 1);
        }
    };

    function getVanImagePosition(vanImage) {
        var box = vanImage.getBBox();
        return [box.x, box.y];
    }

    this.scrollToShowVan = function(vanID) {
        var vanImage = vanImages[vanID];
        var point = getVanImagePosition(vanImage);
        var element = document.getElementById('paper');

        element.scrollLeft = point[0] - element.offsetWidth/2;
        element.scrollTop = point[1] - element.offsetHeight/2;
    };

    this.moveForward = function(vanId, animationLength, callback) {
        var moveDistance = -MOVE_DISTANCE;
        var transformation = "... t 0, " + moveDistance;
        moveVanImage({
            transform: transformation
        }, vanId, animationLength, callback);
    };

    this.moveLeft = function(vanId, animationLength,callback) {
        var vanImage = vanImages[vanId];
        var rotationPointX = vanImage.attrs.x - TURN_DISTANCE + ROTATION_OFFSET_X;
        var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
        var transformation = createRotationTransformation(-90, rotationPointX, rotationPointY);
        moveVanImage({
            transform: transformation
        }, vanId, animationLength, callback);
    };

    this.moveRight = function(vanId, animationLength, callback) {
        var vanImage = vanImages[vanId];
        var rotationPointX = vanImage.attrs.x + TURN_DISTANCE + ROTATION_OFFSET_X;
        var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
        var transformation = createRotationTransformation(90, rotationPointX, rotationPointY);
        moveVanImage({
            transform: transformation
        }, vanId, animationLength, callback);
    };

    this.turnAround = function(vanId, direction, animationLength) {
        var vanImage = vanImages[vanId];
        var timePerState = (animationLength - 50) / 3;

        var actions = [];
        var index = 0;

        switch(direction) {
            case 'FORWARD':
                actions = [moveForward('easeIn'),   rotate('linear'), moveForward('easeOut')];
                break;
            case 'RIGHT':
                actions = [turnRight('easeIn'),     rotate('linear'), turnLeft('easeOut')];
                break;
            case 'LEFT':
                actions = [turnLeft('easeIn'),      rotate('linear'), turnRight('easeOut')];
                break;
        }

        performNextAction();

        function performNextAction() {
            if(index < actions.length) {
                actions[index]();
                index++;
            }
        }

        function moveForward(easing) {
            return function() {
                var moveDistance = -GRID_SPACE_SIZE / 2;
                var moveTransformation = "... t 0, " + moveDistance;
                vanImage.animate({
                    transform: moveTransformation
                }, timePerState, easing, performNextAction);
            }
        }

        function rotate(easing) {
            return function() {
                var rotationPointX = vanImage.attrs.x + 22;
                var rotationPointY = vanImage.attrs.y + 20;

                vanImage.animate({
                    transform: createRotationTransformation(180, rotationPointX, rotationPointY)
                }, timePerState, easing, performNextAction);
            }
        }

        function turnLeft(easing) {
            return function() {
                var vanImage = vanImages[vanId];
                var rotationPointX = vanImage.attrs.x - TURN_DISTANCE + ROTATION_OFFSET_X;
                var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
                var transformation = createRotationTransformation(-45, rotationPointX, rotationPointY);
                vanImage.animate({
                    transform: transformation
                }, timePerState, easing, performNextAction);
            }
        }

        function turnRight(easing) {
            return function() {
                var vanImage = vanImages[vanId];
                var rotationPointX = vanImage.attrs.x + TURN_DISTANCE + ROTATION_OFFSET_X;
                var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
                var transformation = createRotationTransformation(45, rotationPointX, rotationPointY);
                vanImage.animate({
                    transform: transformation
                }, timePerState, easing, performNextAction);
            }
        }
    };

    this.wait = function(vanId, animationLength, callback) {
        //no movement for now
        moveVanImage({
            transform: '... t 0,0'
        }, vanId, animationLength, callback);
    };

    this.deliver = function(destinationId, animationLength) {
        this.transitionDestination(destinationId, true, animationLength);
    };

    function moveVanImage(attr, vanId, animationLength, callback) {
        var vanImage = vanImages[vanId];

        // Compress all current transformations into one
        vanImage.transform(vanImage.matrix.toTransformString());

        // Perform the next animation
        vanImage.animate(attr, animationLength, 'linear', callback);
    }

    this.crash = function(vanID, animationLength, previousNode, currentNode, attemptedAction, startNode) {
        var road = getLeftRightForwardRoad(previousNode, currentNode);
        var roadLeft = road[0];
        var roadForward = road[1];
        var roadRight = road[2];
        var vanImage = vanImages[vanID];

        if(attemptedAction === "FORWARD") {
            var distanceForwards;
            if(roadLeft && roadRight) {
                distanceForwards = 0.5*GRID_SPACE_SIZE + 0.5*ROAD_WIDTH;
            }
            else if(roadLeft) {
                distanceForwards = 0.5*GRID_SPACE_SIZE + 0.3*ROAD_WIDTH;
            }
            else if(roadRight) {
                distanceForwards = 0.5*GRID_SPACE_SIZE + 0.2*ROAD_WIDTH;
            }
            else {
                distanceForwards = 0.5*GRID_SPACE_SIZE + 0.5*ROAD_WIDTH;
            }
            var transformation = "... t 0, " + (-distanceForwards);
        }
        else if(attemptedAction === "TURN_LEFT") {
            var rotationAngle;
            if(roadForward) {
                rotationAngle = 75;
            }
            else if(roadRight) {
                rotationAngle = 75;
            }
            else {
                rotationAngle = 75;
            }
            var rotationPointX = vanImage.attrs.x - TURN_DISTANCE + ROTATION_OFFSET_X;
            var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
            var transformation = createRotationTransformation(-rotationAngle, rotationPointX,
                                                              rotationPointY);
        }
        else if(attemptedAction === "TURN_RIGHT") {
            var rotationAngle;
            if(roadForward) {
                rotationAngle = 75;
            }
            else if(roadLeft) {
                rotationAngle = 75;
            }
            else {
                rotationAngle = 75;
            }
            var rotationPointX = vanImage.attrs.x + TURN_DISTANCE + ROTATION_OFFSET_X;
            var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
            var transformation = createRotationTransformation(rotationAngle, rotationPointX,
                                                              rotationPointY);
        }

        moveVanImage({
            transform: transformation
        }, vanID, animationLength, animateExplosion);

        function animateExplosion() {
            
            if (CHARACTER_NAME !== "Van") {
                return;
            }
            var bbox = vanImage.getBBox();

            var x = bbox.x + bbox.width/2;
            var y = bbox.y + bbox.height/2;

            var width = 20;
            var height = 20;

            var maxSize = 20;
            var minSize = 10;

            var explosionParts = 20;

            var wreckageImage = paper.image(ocargo.Drawing.raphaelImageDir + 'van_wreckage.svg', 0, 0, CHARACTER_HEIGHT, CHARACTER_WIDTH);
            wreckageImage.transform(vanImage.transform());
            wreckageImage.attr({"opacity":0});
            wreckageImages[vanID] = wreckageImage;

            setTimeout(function() {
                wreckageImage.animate({opacity: 1}, 1000);
                vanImage.animate({opacity: 0}, 1000);
                for(var i = 0; i < explosionParts; i++) {
                    setTimeout(function() {
                        var size = minSize + Math.random()*(maxSize-minSize);
                        var xco = x + width*(Math.random()-0.5) - 0.5*size;
                        var yco = y + height*(Math.random()-0.5) - 0.5*size;
                        var imageStr = ocargo.Drawing.raphaelImageDir + '' + (Math.random() < 0.5 ? 'smoke' : 'fire') + '.svg'; 
                        var img = paper.image(imageStr, xco, yco, size, size);
                        img.animate({opacity: 0, transform: 's2'}, 1000, function () {img.remove()});
                    },(i < 5 ? 0 :(i-5)*50));
                }
            }, 100);
        }

        function getLeftRightForwardRoad(previousNode, currentNode) {
            var N = 0;
            var E = 1;
            var S = 2;
            var W = 3;

            function getOrientation(n1,n2) {
                var c1 = n1.coordinate;
                var c2 = n2.coordinate;

                if(c1.y < c2.y) {
                    return N;
                }
                else if(c1.x < c2.x) {
                    return E;
                }
                else if(c1.y > c2.y) {
                    return S;
                }
                else {
                    return W;
                }
            }

            var neighbours = [null,null,null,null];
            for(var i = 0; i < currentNode.connectedNodes.length; i++) {
                var neighbour = currentNode.connectedNodes[i];
                neighbours[getOrientation(currentNode,neighbour)] = neighbour;
            }

            var vanOr = getOrientation(previousNode, currentNode);

            var roadLeft = neighbours[(W+vanOr)%4];
            var roadForward = neighbours[(N+vanOr)%4];
            var roadRight = neighbours[(E+vanOr)%4];

            return [roadLeft, roadForward, roadRight];
        }
    };

    this.removeWreckageImages = function() {
        for(var vanID in wreckageImages) {
            wreckageImages[vanID].remove();
        }
        wreckageImages = {};
    }
};

/********************************/
/* Static methods and constants */
/********************************/

ocargo.Drawing.translate = function(coordinate) {
    return new ocargo.Coordinate(coordinate.x, GRID_HEIGHT - 1 - coordinate.y);
};

// This is the function that starts the pop-up.
ocargo.Drawing.startPopup = function(title, subtitle, message, mascot, delay, buttons) {
    $('#myModal-title').html(title);
    $('#myModal-lead').html(subtitle);
    $('#myModal-mainText').html(message);

    if (mascot) {
        $('#modal-mascot').show();
    } else {
        $('#modal-mascot').hide();
    }
    
    if(buttons){
        $('#modal-buttons').html(buttons);
        $('#modal-buttons').show();
    } else {
        $('#modal-buttons').hide();
    }

    setTimeout( function() { $('#myModal').foundation('reveal', 'open'); }, delay);
};

// This is the function that starts the pop-up with a yes and a no button
ocargo.Drawing.startYesNoPopup = function(title, subtitle, message, yesFunction, noFunction, mascot, delay) {
    var buttonHtml = '<button id="modal-yesBtn" class="navigation_button long_button">Yes</button> <button id="modal-noBtn" class="navigation_button long_button">No</button>';
    ocargo.Drawing.startPopup(title, subtitle, message, mascot, delay, buttonHtml);
    $('#modal-yesBtn').click(yesFunction);
    $('#modal-noBtn').click(noFunction);
};

ocargo.Drawing.showButtonHelp = function(){
    $('#myModal-lead').html('');
    $('#myModal-mainText').html('<p>' + ocargo.messages.buttonHelp + '</p>' +
                                '<p><button onclick="document.getElementById(' + "'close-modal'" +
                                ').click()">Close</button></p>');
};

ocargo.Drawing.isMobile = function() {
    var mobileDetect = new MobileDetect(window.navigator.userAgent);
    return !!mobileDetect.mobile();
};

ocargo.Drawing.isChrome = function() {
    return navigator.userAgent.indexOf('Chrome') > -1;
};

ocargo.Drawing.imageDir = '/static/game/image/';
ocargo.Drawing.raphaelImageDir = '/static/game/raphael_image/';

ocargo.Drawing.FRONT_VIEW  = "front_view";
ocargo.Drawing.TOP_VIEW = "top_view";
