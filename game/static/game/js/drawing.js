'use strict';

var PAPER_WIDTH = 1000;
var PAPER_HEIGHT = 800;
var GRID_WIDTH = 10;
var GRID_HEIGHT = 8;
var GRID_SPACE_SIZE = 100;

var VAN_WIDTH = 40;
var VAN_HEIGHT = 20;

var TRAFFIC_LIGHT_WIDTH = 60;
var TRAFFIC_LIGHT_HEIGHT = 22;

var MOVE_DISTANCE = GRID_SPACE_SIZE;
var TURN_DISTANCE = MOVE_DISTANCE / 2;
var INITIAL_OFFSET_X = 10;
var INITIAL_OFFSET_Y = 82;
var ROTATION_OFFSET_X = 22;
var ROTATION_OFFSET_Y = VAN_WIDTH - 20;

var DECOR_SIZE = 100;

var ROAD_WIDTH = GRID_SPACE_SIZE * 0.7;
var EDGE_GAP = (GRID_SPACE_SIZE - ROAD_WIDTH) / 2;
var ROAD_COLOUR = '#222';
var ROAD_ATTR = {
    fill: ROAD_COLOUR,      
    'stroke': '#aaa'
};

var ROAD_ATTR_JUNCTION = {
    fill: ROAD_COLOUR,
    'stroke': 'none'
};

var ROAD_MARKER_ATTR = {
    'stroke': 'white'
};

var DESTINATION_NOT_VISITED_COLOUR = 'yellow';
var DESTINATION_VISITED_COLOUR = 'green';

var DASH = '10';

var paper = new Raphael('paper', PAPER_WIDTH, PAPER_HEIGHT);

var vanImages = {};
var lightImages = {};
var destinationImages = {};

function createRotationTransformation(degrees, rotationPointX, rotationPointY) {
    var transformation = '... r' + degrees;
    if (rotationPointX !== undefined && rotationPointY !== undefined) {
        transformation += ',' + rotationPointX;
        transformation += ',' + rotationPointY;
    }
    return transformation;
}

function rotateElement(element, degrees, rotationPointX, rotationPointY) {
    var transformation = createRotationTransformation(degrees, rotationPointX, rotationPointY);
    element.transform(transformation);
}

function rotateElementAroundCentreOfGridSpace(element, degrees, x, y) {
    var rotationPointX = (x + 1 / 2) * GRID_SPACE_SIZE;
    var rotationPointY = (GRID_HEIGHT - (y + 1/2)) * GRID_SPACE_SIZE;
    rotateElement(element, degrees, rotationPointX, rotationPointY);
}

function calculateInitialX(startNode) {
    return startNode.coordinate.x * GRID_SPACE_SIZE - INITIAL_OFFSET_X;
}

function calculateInitialY(startNode) {
    return (GRID_HEIGHT - startNode.coordinate.y) * GRID_SPACE_SIZE - INITIAL_OFFSET_Y;
}

function calculateInitialRotation(previousNode, startNode) {
    var nodeAngleRadians = ocargo.calculateNodeAngle(previousNode, startNode);
    var nodeAngleDegrees = nodeAngleRadians * (180 / Math.PI);
    return -nodeAngleDegrees; // Calculation is counterclockwise, transformations are clockwise
}

function getRoadLetters(previous, node1, node2) {
    previous = translate(previous);
    node1 = translate(node1);
    node2 = translate(node2);

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

function translate(coordinate) {
    return new ocargo.Coordinate(coordinate.x, GRID_HEIGHT - 1 - coordinate.y);
}

function isMobile() {
    var mobileDetect = new MobileDetect(window.navigator.userAgent);
    return !!mobileDetect.mobile();
}

// This is the function that starts the pop-up.
// This is the function that starts the pop-up.
function startPopup(title, subtitle, message, delay) {
    $('#myModal-title').html(title);
    $('#myModal-lead').html(subtitle);
    $('#myModal-mainText').html(message);
    setTimeout( function() { $('#myModal').foundation('reveal', 'open'); }, delay);
}

function clearPaper() {
    paper.clear();
}

function renderMap(map) {
    drawBackground();
    createRoad(map.nodes);
}

function renderEndpoints(map) {
    renderDestinations(map.destinations);
    createCFC(map.getStartingPosition());
}

function drawBackground() {
    if (!isMobile()) {
        paper.rect(0, 0, PAPER_WIDTH, PAPER_HEIGHT)
            .attr({fill: 'url(' + BACKGROUND_URL + ')',
                'stroke': 'none'});
    }
}

function createCFC(position) {
    var initialX = calculateInitialX(position.currentNode);
    var initialY = calculateInitialY(position.currentNode);

    var cfc = paper.image('/static/game/image/OcadoCFC_no_road.svg', initialX - 95, initialY - 25, 100, 107);

    var rotation = calculateInitialRotation(position.previousNode, position.currentNode);
    rotateElementAroundCentreOfGridSpace(cfc, rotation, position.currentNode.coordinate.x, position.currentNode.coordinate.y);

    cfc.transform('... r90');
}

function renderDecor(decor) {
    for (var i = 0; i < decor.length; i++) {
        var obj = JSON.parse(decor[i]);
        var coord = obj['coordinate'];
        paper.image(obj['url'], coord.x, PAPER_HEIGHT - coord.y - DECOR_SIZE, 
            DECOR_SIZE, DECOR_SIZE);
    }
}

/*****************************/
/** Traffic light rendering **/
/*****************************/

function renderTrafficLights(trafficLights, draggable) {
    for (var i = 0; i < trafficLights.length; i++) {
        var trafficLight = trafficLights[i];
        var controlledNode = trafficLight.controlledNode;
        var sourceNode = trafficLight.sourceNode;
        
        //get position based on nodes
        var x = (controlledNode.coordinate.x + sourceNode.coordinate.x) / 2.0;
        var y = (controlledNode.coordinate.y + sourceNode.coordinate.y) / 2.0;
        
        //get rotation based on nodes (should face source)
        var rotation = calculateInitialRotation(sourceNode, controlledNode) + 90;
        
        //draw red and green lights, keep reference to both
        var drawX = x * GRID_SPACE_SIZE + TRAFFIC_LIGHT_HEIGHT;
        var drawY = PAPER_HEIGHT - (y * GRID_SPACE_SIZE) - TRAFFIC_LIGHT_WIDTH;
        if (trafficLight.startingState === "RED") {
            trafficLight.greenLightEl = paper.image('/static/game/image/trafficLight_green.svg',
                drawX, drawY, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
                    .transform('r' + rotation + 's-1,1');
            trafficLight.redLightEl = paper.image('/static/game/image/trafficLight_red.svg', drawX,
                drawY, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
                    .transform('r' + rotation + 's-1,1');
        } else {
            trafficLight.redLightEl = paper.image('/static/game/image/trafficLight_red.svg', drawX,
                drawY, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
                    .transform('r' + rotation + 's-1,1');
            trafficLight.greenLightEl = paper.image('/static/game/image/trafficLight_green.svg',
                drawX, drawY, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT)
                    .transform('r' + rotation + 's-1,1');
        }
        

        lightImages[trafficLight.id] = [trafficLight.greenLightEl, trafficLight.redLightEl];

        if (draggable) {
            var id = trafficLight.id;
            if (trafficLight.startingState === "RED") {
                trafficLight.redLightEl.draggableLights(translate(controlledNode.coordinate), id, true);
            } else {
                trafficLight.greenLightEl.draggableLights(translate(controlledNode.coordinate), id, false);
            }

            if (trafficLight.startingState === "RED") {
                trafficLight.redLightEl.node.ondblclick = function() {
                    var traffic = trafficLight;
                    console.debug("id", traffic.id);
                    var image = traffic.redLightEl;
                    return image.transform('...r90');
                };
            } else {
                trafficLight.greenLightEl.node.ondblclick = function() {
                    var traffic = trafficLight;
                    console.debug("id", traffic.id);
                    var image = traffic.greenLightEl;
                    return image.transform('...r90');
                };
            }
        }

		
		//hide light which isn't the starting state
		if(trafficLight.startingState === ocargo.TrafficLight.RED){
			trafficLight.greenLightEl.attr({'opacity': 0});
		} else {
			trafficLight.redLightEl.attr({'opacity': 0});
		}
	}
}



/***************************/
/** Destination rendering **/
/***************************/

function renderDestinations(destinations) {
    for(var i = 0; i < destinations.length; i++) {
        var destination = destinations[i].node;
        var variation = getHousePosition(destination);

        var destinationRect = paper.rect(destination.coordinate.x * GRID_SPACE_SIZE, 
                                PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - 100,
                                100, 100).attr({'stroke': DESTINATION_NOT_VISITED_COLOUR});

        var destinationHouse = paper.image('/static/game/image/house1_noGreen.svg',
                                destination.coordinate.x * GRID_SPACE_SIZE + variation[0],
                                PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - variation[1],
                                50, 50).transform('r' + variation[2]);

        destinationImages[destinations[i].id] = {rect: destinationRect, 
                                                house: destinationHouse};
    }
}

//find a side of the road
function getHousePosition(destination) {
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
    var variation = [25,25,90];

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



/********************/
/** Road rendering **/
/********************/

function createRoad(nodes) {
    for (var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        switch (node.connectedNodes.length) {
            case 1:
                drawDeadEndRoad(node);
                break;
            
            case 2:
                drawSingleRoadSegment(node.connectedNodes[0], node, node.connectedNodes[1]);
                break;
            
            case 3:
                drawTJunction(node);
                break;
            
            case 4:
                drawCrossRoads(node);
                break;

            default:
                break;
        }
    }
}

function drawDeadEndRoad(node) {
    var previousNode = node.connectedNodes[0];

    var nextNode = {};
    nextNode.coordinate = new ocargo.Coordinate(
            node.coordinate.x + (node.coordinate.x - previousNode.coordinate.x),
            node.coordinate.y + (node.coordinate.y - previousNode.coordinate.y));

    var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

    var prevFlipped = translate(previousNode.coordinate);
    var flipped = translate(node.coordinate);

    var road = paper.image('/static/game/image/roadTile_deadEnd.svg',
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
}

function drawSingleRoadSegment(previousNode, node, nextNode) {
    var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

    var flipped = translate(node.coordinate);
    var road;
    if (roadLetters === 'H') {
        road = paper.image('/static/game/image/roadTile_straight.svg',
            flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
        road.rotate(90);
    }
    else if (roadLetters === 'V') {
        road = paper.image('/static/game/image/roadTile_straight.svg',
            flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
    }
    else {
        road = paper.image('/static/game/image/roadTile_turn.svg',
            flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);

        if (roadLetters === 'UL') {
            road.rotate(90, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
        }
        else if (roadLetters === 'UR') {
            road.rotate(180, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
        }
        else if (roadLetters === 'DR') {
            road.rotate(270, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
        }
    }
}

function drawTJunction(node) {
    var node1 = node.connectedNodes[0];
    var node2 = node.connectedNodes[1];
    var node3 = node.connectedNodes[2];

    var flipped = translate(node.coordinate);
    var flipped1 = translate(node1.coordinate);
    var flipped2 = translate(node2.coordinate);
    var flipped3 = translate(node3.coordinate);

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

    var road = paper.image('/static/game/image/roadTile_TJunction.svg',
        flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
    road.rotate(rotation, flipped.x * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2, flipped.y * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2);
}

function drawCrossRoads(node) {
    var flipped = translate(node.coordinate);
    
    var road = paper.image('/static/game/image/roadTile_crossRoads.svg',
        flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
}


/*********************************/
/** Van rendering and animation **/
/*********************************/

function renderVans(position, numVans) {
    for (var i = 0; i < numVans; i++) {
        vanImages[i] = createVanImage(position, i);
    }
    scrollToShowVanImage(vanImages[0]);
}

function createVanImage(position, vanId) {
    var initialX = calculateInitialX(position.currentNode);
    var initialY = calculateInitialY(position.currentNode);

    var imageStr = (vanId % 2 == 0) ? '/static/game/image/van_small.svg' : '/static/game/image/van_small2.svg';
    var vanImage = paper.image(imageStr, initialX, initialY, VAN_HEIGHT, VAN_WIDTH);

    var rotation = calculateInitialRotation(position.previousNode, position.currentNode);
    rotateElementAroundCentreOfGridSpace(vanImage, rotation, position.currentNode.coordinate.x, position.currentNode.coordinate.y);

    vanImage.transform('... r90');

    return vanImage;
}

function getVanImagePosition(vanImage) {
    var box = vanImage.getBBox();
    return [box.x, box.y];
}

function scrollToShowVanImage(vanImage) {
    var point = getVanImagePosition(vanImage);
    var element = document.getElementById('paper');

    element.scrollLeft = point[0] - element.offsetWidth/2;
    element.scrollTop = point[1] - element.offsetHeight/2;
}

function moveForward(vanId, animationLength, callback) {
    var moveDistance = -MOVE_DISTANCE;
    var transformation = "... t 0, " + moveDistance;
    moveVanImage({
        transform: transformation
    }, vanId, animationLength, callback);
}

function moveLeft(vanId, animationLength,callback) {
    var vanImage = vanImages[vanId];
    var rotationPointX = vanImage.attrs.x - TURN_DISTANCE + ROTATION_OFFSET_X;
    var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(-90, rotationPointX, rotationPointY);
    moveVanImage({
        transform: transformation
    }, vanId, animationLength, callback);
}

function moveRight(vanId, animationLength, callback) {
    var vanImage = vanImages[vanId];
    var rotationPointX = vanImage.attrs.x + TURN_DISTANCE + ROTATION_OFFSET_X;
    var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(90, rotationPointX, rotationPointY);
    moveVanImage({
        transform: transformation
    }, vanId, animationLength, callback);
}

function turnAround(vanId, animationLength, callback) {
    var moveDistance = -GRID_SPACE_SIZE / 2;
    var moveTransformation = "... t 0, " + moveDistance;
    var vanImage = vanImages[vanId];
    var timePerState = (animationLength - 50) / 3;

    function moveForward() {
        moveVanImage({
            transform: moveTransformation
        }, vanId, timePerState, rotate);
    }

    function rotate() {
        var rotationPointX = vanImage.attrs.x + 22;
        var rotationPointY = vanImage.attrs.y + 20;

        vanImage.animate({
            transform: createRotationTransformation(180, rotationPointX, rotationPointY)
        }, timePerState, 'easeIn', moveBack);
    }

    function moveBack() {
        vanImage.animate({
            transform: moveTransformation
        }, timePerState, 'easeIn', callback);
    }
    
    moveForward();
}

function wait(vanId, animationLength, callback) {
    //no movement for now
    moveVanImage({
        transform: '... t 0,0'
    }, vanId, animationLength, callback);
}

function deliver(vanID, animationLength, destinationID, callback) {
    var destinationRect = destinationImages[destinationID].rect;
    destinationRect.animate({'stroke': DESTINATION_VISITED_COLOUR}, animationLength, 'linear', callback);
}

function moveVanImage(attr, vanId, animationLength, callback) {
    vanImages[vanId].animate(attr, animationLength, 'linear', callback);
}

/**********************/
/** Crash animations **/
/**********************/

function crash(vanID, animationLength, previousNode, currentNode, attemptedAction,  startNode) {
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
    else if(attemptedAction == "TURN_LEFT") {
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
        var transformation = createRotationTransformation(-rotationAngle, rotationPointX, rotationPointY);
    }
    else if(attemptedAction == "TURN_RIGHT") {
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
        var transformation = createRotationTransformation(rotationAngle, rotationPointX, rotationPointY);
    }

    moveVanImage({
        transform: transformation
    }, vanID, animationLength, animateExplosion);

    function animateExplosion() {
        
        var bbox = vanImage.getBBox();

        var x = bbox.x + bbox.width/2;
        var y = bbox.y + bbox.height/2;

        var width = 20;
        var height = 20;

        var maxSize = 20;
        var minSize = 10;

        var explosionParts = 20;

        var initialX = calculateInitialX(startNode);
        var initialY = calculateInitialY(startNode);

        var wreckageImage = paper.image('/static/game/image/van_wreckage.svg', initialX, initialY, VAN_HEIGHT, VAN_WIDTH);
        wreckageImage.transform(vanImage.transform());
        wreckageImage.attr({"opacity":0});

        setTimeout(function() {
            wreckageImage.animate({opacity: 1}, 1000);
            vanImage.animate({opacity: 0}, 1000);
            for(var i = 0; i < explosionParts; i++) {
                setTimeout(function() {
                    var size = minSize + Math.random()*(maxSize-minSize);
                    var xco = x + width*(Math.random()-0.5) - 0.5*size;
                    var yco = y + height*(Math.random()-0.5) - 0.5*size;
                    var imageStr = '/static/game/image/' + (Math.random() < 0.5 ? 'smoke' : 'fire') + '.svg'; 
                    var img = paper.image(imageStr, xco, yco, size, size);
                    img.animate({opacity: 0, transform: 's2'}, 1000, function () {});
                },(i < 5 ? 0 :(i-5)*50));
            }
        }, 100);
    }
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