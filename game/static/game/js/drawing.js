'use strict';

var PAPER_WIDTH = 1000;
var PAPER_HEIGHT = 800;
var GRID_WIDTH = 10;
var GRID_HEIGHT = 8;
var GRID_SPACE_SIZE = 100;

var ANIMATION_FRAME = 500;

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

var DASH = '10';

var paper = new Raphael('paper', PAPER_WIDTH, PAPER_HEIGHT);

var vanImages = {};
var lightImages = {};

var animationQueue = []
var isAnimating = false;
var animationTimestamp = 0;

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
    previous = transformY(previous);
    node1 = transformY(node1);
    node2 = transformY(node2);

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

function transformY(coord) {
    return new ocargo.Coordinate(coord.x, GRID_HEIGHT - 1 - coord.y);
}

function drawDeadEndRoad(node) {
    var previousNode = node.connectedNodes[0];

    var nextNode = {};
    nextNode.coordinate = new ocargo.Coordinate(
            node.coordinate.x + (node.coordinate.x - previousNode.coordinate.x),
            node.coordinate.y + (node.coordinate.y - previousNode.coordinate.y));

    var roadLetters = getRoadLetters(previousNode.coordinate, node.coordinate, nextNode.coordinate);

    var prevFlipped = transformY(previousNode.coordinate);
    var flipped = transformY(node.coordinate);

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

    var flipped = transformY(node.coordinate);
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

    var flipped = transformY(node.coordinate);
    var flipped1 = transformY(node1.coordinate);
    var flipped2 = transformY(node2.coordinate);
    var flipped3 = transformY(node3.coordinate);

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
    var flipped = transformY(node.coordinate);
    
    var road = paper.image('/static/game/image/roadTile_crossRoads.svg',
        flipped.x * GRID_SPACE_SIZE, flipped.y * GRID_SPACE_SIZE, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
}

function createRoad(nodes) {
    $.each(nodes, function(i, node) {
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
    });
}

function isMobile() {
    var mobileDetect = new MobileDetect(window.navigator.userAgent);
    return !!mobileDetect.mobile();
}

function drawBackground(paper) {
    if (!isMobile()) {
        paper.rect(0, 0, PAPER_WIDTH, PAPER_HEIGHT)
            .attr({fill: 'url(/static/game/image/grassTile1.svg)',
                'stroke': 'none'});
    }
}

function drawDecor(decor) {
    for (var i = 0; i < decor.length; i++) {
        var obj = decor[i];
        var coord = obj['coordinate'];
        paper.image(obj['url'], coord.x, PAPER_HEIGHT - coord.y - DECOR_SIZE, 
            DECOR_SIZE, DECOR_SIZE);
    }
}

function createCFC(paper, previousNode, startNode) {
    var initialX = calculateInitialX(startNode);
    var initialY = calculateInitialY(startNode);

    var cfc = paper.image('/static/game/image/OcadoCFC_no_road.svg', initialX - 95, initialY - 25, 100, 107);

    var rotation = calculateInitialRotation(previousNode, startNode);
    rotateElementAroundCentreOfGridSpace(cfc, rotation, startNode.coordinate.x, startNode.coordinate.y);

    cfc.transform('... r90');
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

function createDestination(destination) {
    var variation = getHousePosition(destination);

    paper.rect(destination.coordinate.x * GRID_SPACE_SIZE, PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - 100,
            100, 100).attr({'stroke': 'yellow'});

    paper.image('/static/game/image/house1_noGreen.svg',
        destination.coordinate.x * GRID_SPACE_SIZE + variation[0],
        PAPER_HEIGHT - (destination.coordinate.y * GRID_SPACE_SIZE) - variation[1],
        50, 50).transform('r' + variation[2]);
}

function renderTheMap(map) {
    paper.clear();
    drawBackground(paper);
    createRoad(map.nodes);
    createDestination(map.destination);
    var previousNode = map.nodes[0];
    var startNode = map.nodes[0].connectedNodes[0];
    createCFC(paper, previousNode, startNode);
    drawDecor(map.decor);
    createTrafficLights(map.trafficLights, false);
}

function renderTheVans(vans) {
    for (var i = 0; i < vans.length; i++) {
        var vanImage = createVanImage(paper, vans[i]);
        scrollToShowVanImage(vanImage);
    }
}

function translate(coordinate) {
    return new ocargo.Coordinate(coordinate.x, GRID_HEIGHT - 1 - coordinate.y);
}

function createTrafficLights(trafficLights, draggable) {
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
        trafficLight.greenLightEl = paper.image('/static/game/image/trafficLight_green.svg', drawX,
            drawY, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT).transform('r' + rotation + 's-1,1');
        trafficLight.redLightEl = paper.image('/static/game/image/trafficLight_red.svg', drawX,
            drawY, TRAFFIC_LIGHT_WIDTH, TRAFFIC_LIGHT_HEIGHT).transform('r' + rotation + 's-1,1');

        if (draggable) {
            var id = trafficLight.id;
            trafficLight.greenLightEl.draggableLights(translate(controlledNode.coordinate), id);
            trafficLight.redLightEl.draggableLights(translate(controlledNode.coordinate), id);
            trafficLight.redLightEl.node.ondblclick = function() {
                console.debug("id", trafficLight.id);
                var image = trafficLight.redLightEl;
                return image.transform('...r90');
            };

            trafficLight.greenLightEl.node.ondblclick = function() {
                console.debug("id", id);
                var image = trafficLight.greenLightEl;
                return image.transform('...r90');
            };
        }

        lightImages[trafficLight.id] = [trafficLight.greenLightEl, trafficLight.redLightEl];
		
		//hide light which isn't the starting state
		if(trafficLight.startingState === ocargo.TrafficLight.RED){
			trafficLight.greenLightEl.attr({'opacity': 0});
		} else {
			trafficLight.redLightEl.attr({'opacity': 0});
		}
		
	}
}

// This is the function that starts the pop-up.
function startPopup(title, subtitle, message) {
    $('#myModal').foundation('reveal', 'open');
    $('#myModal-title').html(title);
    $('#myModal-lead').html(subtitle);
    $('#myModal-mainText').html(message);
}


/*****************/
/** Van methods **/
/*****************/

function scrollToShowVanImage(vanImage) {
    var point = getVanImagePosition(vanImage);
    var element = document.getElementById('paper');

    element.scrollLeft = point[0] - element.offsetWidth/2;
    element.scrollTop = point[1] - element.offsetHeight/2;
}

function moveForward(van, callback) {
    var moveDistance = -MOVE_DISTANCE;
    var transformation = "... t 0, " + moveDistance;
    moveVanImage({
        transform: transformation
    }, van, callback);
}

function moveLeft(van, callback) {
    var vanImage = vanImages[van.id];
    var rotationPointX = vanImage.attrs.x - TURN_DISTANCE + ROTATION_OFFSET_X;
    var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(-90, rotationPointX, rotationPointY);
    moveVanImage({
        transform: transformation
    }, van, callback);
}

function moveRight(van, callback) {
    var vanImage = vanImages[van.id];
    var rotationPointX = vanImage.attrs.x + TURN_DISTANCE + ROTATION_OFFSET_X;
    var rotationPointY = vanImage.attrs.y + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(90, rotationPointX, rotationPointY);
    moveVanImage({
        transform: transformation
    }, van, callback);
}

function turnAround(van, callback) {
    var moveDistance = -GRID_SPACE_SIZE / 2;
    var moveTransformation = "... t 0, " + moveDistance;
    var vanImage = vanImages[van.id];
    var timePerState = (ANIMATION_FRAME - 50) / 3;

    function moveForward() {
        moveVanImage({
            transform: moveTransformation
        }, van, rotate, timePerState);
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

function wait(van, callback) {
    //no movement for now
    moveVanImage({
        transform: '... t 0,0'
    }, van, callback);
}

function createVanImage(paper, van) {
    var initialX = calculateInitialX(van.currentNode);
    var initialY = calculateInitialY(van.currentNode);

    var imageStr = (van.id % 2 == 0) ? '/static/game/image/van_small.svg' : '/static/game/image/van_small2.svg';
    var vanImage = paper.image(imageStr, initialX, initialY, VAN_HEIGHT, VAN_WIDTH);

    var rotation = calculateInitialRotation(van.previousNode, van.currentNode);
    rotateElementAroundCentreOfGridSpace(vanImage, rotation, van.currentNode.coordinate.x, van.currentNode.coordinate.y);

    vanImages[van.id] = vanImage;

    return vanImage.transform('... r90');
}

function resetVanImage(previousNode, startNode, van) {
    var vanImage = vanImages[van.id];
    
    vanImage.transform('r0');

    var rotation = calculateInitialRotation(previousNode, startNode);
    rotateElementAroundCentreOfGridSpace(vanImage, rotation, startNode.coordinate.x, startNode.coordinate.y);

    var initialX = calculateInitialX(startNode);
    var initialY = calculateInitialY(startNode);
    vanImage.attr({
        x: initialX,
        y: initialY
    });

    vanImage.transform('... r90');
    scrollToShowVanImage(vanImage);
}

function getVanImagePosition(vanImage) {
    var box = vanImage.getBBox();
    return [box.x, box.y];
}

/***********************/
/** Animation methods **/
/***********************/

function resetAnimation() {
    isAnimating = false;
    animationQueue = [];
    animationTimestamp = 0;
}

function startAnimation() {
    if (!isAnimating && animationQueue.length > 0) {
        isAnimating = true;

        while (animationQueue.length > 0 && animationQueue[0].timestamp <= animationTimestamp) {
            var a = animationQueue.splice(0, 1)[0];

            if (a.type == 'van') {
                // Set all current animations to the final position, so we don't get out of sync
                var anims = vanImages[a.id].status();
                for (var i = 0, ii = anims.length; i < ii; i++) {
                    vanImages[a.id].status(anims[i].anim, 1);
                }

                scrollToShowVanImage(vanImages[a.id]);
                vanImages[a.id].animate(a.attr, a.animationLength, a.animationType, a.callback);
            }
            else if (a.type == 'trafficLight') {
                if (a.colour == ocargo.TrafficLight.GREEN) {
                    lightImages[a.id][0].animate({ opacity : 1 }, ANIMATION_FRAME/4, 'linear', a.callback);
                    lightImages[a.id][1].animate({ opacity : 0 }, ANIMATION_FRAME/2, 'linear', a.callback);
                }
                else {
                    lightImages[a.id][0].animate({ opacity : 0 }, ANIMATION_FRAME/2, 'linear', a.callback);
                    lightImages[a.id][1].animate({ opacity : 1 }, ANIMATION_FRAME/4, 'linear', a.callback);
                }
            }
            else if (a.type == 'highlightLine') {
                var line = a.line;
                $('.CodeMirror-code')[0].children[line].style.background = a.highlight;
                setTimeout(function() {$('.CodeMirror-code')[0].children[line].style.background = "";}, 400);
            }
        }
        
        setTimeout(function() {
            animationTimestamp++;
            isAnimating = false;
            startAnimation();
        }, ANIMATION_FRAME);
    }
}

function moveVanImage(attr, van, callback, animationLength) {
    animationLength = animationLength || ANIMATION_FRAME;

    animationQueue.push({type: 'van', timestamp: ocargo.time.timestamp, id: van.id, attr: attr, animationLength: animationLength, animationType: 'linear', callback: callback});

    if (!isAnimating) {
        startAnimation();
    }
}

function changeTrafficLight(id, colour) {
    animationQueue.push({type: 'trafficLight', timestamp: ocargo.time.timestamp, id: id, colour: colour});

    if (!isAnimating) {
        startAnimation();
    }
}

function resetTrafficLightAnimation(id, colour) {
    if (colour == ocargo.TrafficLight.GREEN) {
        lightImages[id][0].attr({ opacity : 1 });
        lightImages[id][1].attr({ opacity : 0 });
    }
    else {
        lightImages[id][0].attr({ opacity : 0 });
        lightImages[id][1].attr({ opacity : 1 });
    }

    resetAnimation();
}

function highlightLine(lineIndex) {
    animationQueue.push({type: 'highlightLine', timestamp: ocargo.time.timestamp, line: lineIndex, highlight: "yellowgreen"});

    if (!isAnimating) {
        startAnimation();
    }
}
