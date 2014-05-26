'use strict';

var PAPER_WIDTH = 1000;
var PAPER_HEIGHT = 800;
var GRID_WIDTH = 10;
var GRID_HEIGHT = 8;
var GRID_SPACE_SIZE = 100;

var VAN_WIDTH = 40;
var VAN_HEIGHT = 20;

var MOVE_DISTANCE = GRID_SPACE_SIZE;
var TURN_DISTANCE = MOVE_DISTANCE / 2;
var INITIAL_OFFSET_X = 10;
var INITIAL_OFFSET_Y = 32;
var INITIAL_X = GRID_SPACE_SIZE - INITIAL_OFFSET_X;
var INITIAL_Y = 450 - INITIAL_OFFSET_Y;
var ROTATION_OFFSET_X = 25;
var ROTATION_OFFSET_Y = VAN_WIDTH - 20;

var ROAD_WIDTH = GRID_SPACE_SIZE / 2;
var EDGE_GAP_X = (GRID_SPACE_SIZE - ROAD_WIDTH) / 2;
var EDGE_GAP_Y = (GRID_SPACE_SIZE - ROAD_WIDTH) / 2;
var ROAD_COLOUR = '#222';
var ROAD_ATTR = {
    fill: ROAD_COLOUR
};

var ROAD_MARKER_ATTR = {
    fill: '#FFF',
    stroke: 'none'
};

var WEIGHT_POINT_ATTR = {
    fill: '#FFF',
    'fill-opacity': 0,
    stroke: 'none'
};

var paper = new Raphael('paper', PAPER_WIDTH, PAPER_HEIGHT);

function createRotationTransformation(degrees, rotationPointX, rotationPointY) {
    var transformation = '... r' + degrees;
    if (rotationPointX !== undefined && rotationPointY !== undefined) {
        transformation += ',' + rotationPointX;
        transformation += ',' + rotationPointY;
    }
    return transformation;
}

function createVan(paper) {
    return paper.image(
        '/static/game/image/ocadoVan_big.svg', INITIAL_X, INITIAL_Y, VAN_HEIGHT, VAN_WIDTH)
        .transform('r90');
}

function getGridSpace(x, y) {
    return [Math.floor((x + GRID_SPACE_SIZE / 2) / GRID_SPACE_SIZE),
        Math.floor((y + GRID_SPACE_SIZE / 2) / GRID_SPACE_SIZE)];
}

function identifyInstruction(roadSet) {
    var weightPointBox = roadSet[2].getBBox();
    var roadBox = roadSet[0].getBBox();
    var diffX = Math.abs(weightPointBox.x - roadBox.x);
    var diffY = Math.abs(weightPointBox.y - roadBox.y);
    var instruction = '';

    if (diffX === 0 && diffY === 0)
        instruction = 'UL';
    if (diffX === 0 && diffY == EDGE_GAP_Y)
        instruction = 'DL';
    if (diffX == EDGE_GAP_X && diffY == EDGE_GAP_Y)
        instruction = 'DR';
    if (diffX == EDGE_GAP_X && diffY === 0)
        instruction = 'UR';
    if (roadBox.width == 50 && roadBox.height == 100)
        instruction = 'V';
    if (roadBox.width == 100 && roadBox.height == 50)
        instruction = 'H';

    return instruction;
}

function createHorizontalRoad(paper, i, j) {
    var x = i * GRID_SPACE_SIZE;
    var y = j * GRID_SPACE_SIZE + (GRID_SPACE_SIZE - ROAD_WIDTH) / 2;

    var road = paper.rect(x, y, GRID_SPACE_SIZE, ROAD_WIDTH);
    road.attr(ROAD_ATTR);

    var entryMarker = paper.rect(x, j * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 - 1,
            GRID_SPACE_SIZE / 8, 2);
    entryMarker.attr(ROAD_MARKER_ATTR);

    var middleMarker = paper.rect(x + 3 * GRID_SPACE_SIZE / 8,
            j * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 - 1, GRID_SPACE_SIZE / 4, 2);
    middleMarker.attr(ROAD_MARKER_ATTR);

    var lastMarker = paper.rect(x + 7 * GRID_SPACE_SIZE / 8,
            j * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 - 1, GRID_SPACE_SIZE / 8, 2);
    lastMarker.attr(ROAD_MARKER_ATTR);

    var weightPoint = paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
    weightPoint.attr(WEIGHT_POINT_ATTR);

    var markerSet = paper.set();
    markerSet.push(entryMarker, middleMarker, lastMarker);

    var roadSet = paper.set();
    roadSet.push(road, markerSet, weightPoint);

    return roadSet;
}

function createVerticalRoad(paper, i, j) {
    var x = i * GRID_SPACE_SIZE + (GRID_SPACE_SIZE - ROAD_WIDTH) / 2;
    var y = j * GRID_SPACE_SIZE;

    var road = paper.rect(x, y, ROAD_WIDTH, GRID_SPACE_SIZE);
    road.attr(ROAD_ATTR);

    var entryMarker = paper.rect(i * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 - 1, y,
        2, GRID_SPACE_SIZE / 8);
    entryMarker.attr(ROAD_MARKER_ATTR);

    var middleMarker = paper.rect(i * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 - 1,
            y + 3 * GRID_SPACE_SIZE / 8, 2, GRID_SPACE_SIZE / 4);
    middleMarker.attr(ROAD_MARKER_ATTR);

    var lastMarker = paper.rect(i * GRID_SPACE_SIZE + GRID_SPACE_SIZE / 2 - 1,
            y + 7 * GRID_SPACE_SIZE / 8, 2, GRID_SPACE_SIZE / 8);
    lastMarker.attr(ROAD_MARKER_ATTR);

    var weightPoint = paper.rect(x, y, GRID_SPACE_SIZE, GRID_SPACE_SIZE);
    weightPoint.attr(WEIGHT_POINT_ATTR);

    var markerSet = paper.set();
    markerSet.push(entryMarker, middleMarker, lastMarker);

    var roadSet = paper.set();
    roadSet.push(road, markerSet, weightPoint);

    return roadSet;
}

function createTurn(paper, i, j, direction) {
    var baseX = i * GRID_SPACE_SIZE;
    var baseY = j * GRID_SPACE_SIZE;
    var turnAndMarker = [];

    switch (direction) {
        case 'UL':
            turnAndMarker = createTurnUL(baseX, baseY);
            break;

        case 'UR':
            turnAndMarker = createTurnUR(baseX, baseY);
            break;

        case 'DR':
            turnAndMarker = createTurnDR(baseX, baseY);
            break;

        case 'DL':
            turnAndMarker = createTurnDL(baseX, baseY);
            break;
    }

    var turn = turnAndMarker[0];
    var marker = turnAndMarker[1];
    var weightPoint = paper.rect(baseX, baseY, GRID_SPACE_SIZE, GRID_SPACE_SIZE);

    turn.attr(ROAD_ATTR);
    marker.attr(ROAD_MARKER_ATTR);
    weightPoint.attr(WEIGHT_POINT_ATTR);

    var roadSet = paper.set();
    roadSet.push(turn, marker, weightPoint);

    return roadSet;
}

function createTurnUL(baseX, baseY) {

    var turn = paper.path([
        'M', baseX, baseY + EDGE_GAP_Y,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y, baseX + EDGE_GAP_X, baseY,
        'H', baseX + EDGE_GAP_X + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y + ROAD_WIDTH, baseX,
            baseY + EDGE_GAP_Y + ROAD_WIDTH
    ]);

    var marker = paper.path([
        'M', baseX, baseY + GRID_SPACE_SIZE / 2 - 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 - 1, baseY + GRID_SPACE_SIZE / 2 - 1,
            baseX + GRID_SPACE_SIZE / 2 - 1, baseY + 1,
        'H', baseX + GRID_SPACE_SIZE / 2 + 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 + 1, baseY + GRID_SPACE_SIZE / 2 + 1, baseX ,
            baseY + GRID_SPACE_SIZE / 2 + 1
    ]);

    return [turn, marker];
}

function createTurnDL(baseX, baseY) {

    var turn = paper.path([
        'M', baseX, baseY + EDGE_GAP_Y + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y + ROAD_WIDTH, baseX + EDGE_GAP_X,
            baseY + GRID_SPACE_SIZE,
        'H', baseX + EDGE_GAP_X + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y, baseX, baseY + EDGE_GAP_Y
    ]);

    var marker = paper.path([
        'M', baseX, baseY + GRID_SPACE_SIZE / 2 - 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 + 1, baseY + GRID_SPACE_SIZE / 2 - 1,
            baseX + GRID_SPACE_SIZE / 2 + 1, baseY + GRID_SPACE_SIZE + 1,
        'H', baseX + GRID_SPACE_SIZE / 2 - 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 - 1, baseY + GRID_SPACE_SIZE / 2 + 1,
        baseX, baseY + GRID_SPACE_SIZE / 2 + 1
    ]);

    return [turn, marker];
}

function createTurnDR(baseX, baseY) {

    var turn = paper.path([
        'M', baseX + GRID_SPACE_SIZE, baseY + EDGE_GAP_Y,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y, baseX + EDGE_GAP_X, baseY + GRID_SPACE_SIZE,
        'H', baseX + EDGE_GAP_X + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y + ROAD_WIDTH,
            baseX + GRID_SPACE_SIZE, baseY + EDGE_GAP_Y + ROAD_WIDTH
    ]);

    var marker = paper.path([
        'M', baseX + GRID_SPACE_SIZE / 2 - 1, baseY + GRID_SPACE_SIZE + 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 + 1, baseY + GRID_SPACE_SIZE / 2 - 1,
            baseX + GRID_SPACE_SIZE + 1, baseY + GRID_SPACE_SIZE / 2 - 1,
        'V', baseY + GRID_SPACE_SIZE / 2 + 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 + 1, baseY + GRID_SPACE_SIZE / 2 + 1,
            baseX + GRID_SPACE_SIZE / 2 + 1, baseY + GRID_SPACE_SIZE + 1
    ]);

    return [turn, marker];
}

function createTurnUR(baseX, baseY) {

    var turn = paper.path([
        'M', baseX + EDGE_GAP_X, baseY,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y + ROAD_WIDTH, baseX + GRID_SPACE_SIZE, baseY +
            EDGE_GAP_Y + ROAD_WIDTH,
        'V', baseY + EDGE_GAP_Y,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y, baseX + EDGE_GAP_X + 
            ROAD_WIDTH, baseY
    ]);

    var marker = paper.path([
        'M', baseX + GRID_SPACE_SIZE + 1, baseY + GRID_SPACE_SIZE / 2 - 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 + 1, baseY + GRID_SPACE_SIZE / 2 - 1,
            baseX + GRID_SPACE_SIZE / 2 + 1, baseY,
        'H', baseX + GRID_SPACE_SIZE / 2 - 1,
        'Q', baseX + GRID_SPACE_SIZE / 2 - 1, baseY + GRID_SPACE_SIZE / 2 + 1,
            baseX + GRID_SPACE_SIZE + 1, baseY + GRID_SPACE_SIZE / 2 + 1
    ]);

    return [turn, marker];
}

function createRoad(paper, roadDefinition) {
    var roadElements = [];

    $.each(roadDefinition, function(i, roadSlice) {
        $.each(roadSlice, function(j, roadType) {
            if (roadType) {
                switch (roadType) {
                    case 'H':
                        roadElements.push(createHorizontalRoad(paper, i, j));
                        break;
                    case 'V':
                        roadElements.push(createVerticalRoad(paper, i, j));
                        break;
                    default:
                        roadElements.push(createTurn(paper, i, j, roadType));
                        break;
                }
            }
        });
    });

    return roadElements;
}

var van;

function scrollToShowVan() {
    var point = getVanPosition();
    var element = document.getElementById('paper');

    if (point[0] > Math.floor(PAPER_WIDTH / 2)) {
        element.scrollLeft = PAPER_WIDTH / 2;
    } else {
        element.scrollLeft = 0;
    }

    if (point[1] > Math.floor(PAPER_HEIGHT / 2)) {
        element.scrollTop = PAPER_HEIGHT / 2;
    } else {
        element.scrollTop = 0;
    }
}

function moveVan(attr, callback) {
    var combinedCallback = function () {
        scrollToShowVan();
        callback();
    };

    van.animate(attr, 500, 'easeIn', combinedCallback);
}

function moveForward(callback) {
    var moveDistance = -MOVE_DISTANCE;
    var transformation = "... t 0, " + moveDistance;
    moveVan({
        transform: transformation
    }, callback);
}

function moveLeft(callback) {
    var rotationPointX = van.attrs.x - TURN_DISTANCE + ROTATION_OFFSET_X;
    var rotationPointY = van.attrs.y + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(-90, rotationPointX, rotationPointY);
    moveVan({
        transform: transformation
    }, callback);
}

function moveRight(callback) {
    var rotationPointX = van.attrs.x + TURN_DISTANCE + ROTATION_OFFSET_X;
    var rotationPointY = van.attrs.y + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(90, rotationPointX, rotationPointY);
    moveVan({
        transform: transformation
    }, callback);
}

function resetVan() {
    van.attr({
        x: INITIAL_X,
        y: INITIAL_Y,
        transform: 'r90'
    });
    van.toFront();
    scrollToShowVan();
}

function getVanPosition() {
    var box = van.getBBox();
    return [box.x, box.y];
}

function turnAround(callback) {
    var moveDistance = -GRID_SPACE_SIZE / 2;
    var moveTransformation = "... t 0, " + moveDistance;

    function moveBack() {
        moveVan({
            transform: moveTransformation
        }, callback);
    }

    function rotate() {
        var rotationPointX = van.attrs.x + 22;
        var rotationPointY = van.attrs.y + 20;

        moveVan({
            transform: createRotationTransformation(180, rotationPointX, rotationPointY)
        }, moveBack);
    }

    function moveForward() {
        moveVan({
            transform: moveTransformation
        }, rotate);
    }

    moveForward();
}

function isMobile() {
    var mobileDetect = new MobileDetect(window.navigator.userAgent);
    return !!mobileDetect.mobile();
}

function drawBackground(paper){
    if (!isMobile()) {
        paper.rect(0, 0, PAPER_WIDTH, PAPER_HEIGHT)
            .attr({fill: 'url(/static/game/image/grassTile1.svg)'});
    }
}

function createCFC(){
	paper.image('/static/game/image/OcadoCFC.svg', INITIAL_X - 90, INITIAL_Y - 40, 100, 100)
        .transform('r90');
}

function createDestination(destination){
	console.log(destination);
	paper.image('/static/game/image/house1_noGreen.svg',
		destination.x * GRID_SPACE_SIZE, PAPER_HEIGHT - (destination.y * GRID_SPACE_SIZE) - 25,
        100, 100).transform('r90');
}

function renderTheMap(map) {
    paper.clear();
    drawBackground(paper);
    createRoad(paper, map.instructions);
    createCFC(paper);
    createDestination(map.destination.coordinate);
    van = createVan(paper);
    scrollToShowVan();
}


function closePopup(){
    $('#myModal').foundation('reveal', 'close');
}

//This is the function that starts the pop-up
function startPopup(title, subtitle, message){
    $('#myModal').foundation('reveal', 'open');
    $('.title').html(title);
    $('.lead').html(subtitle);
    $('.mainText').html(message);
}
