'use strict';

var PAPER_WIDTH = 1000;
var PAPER_HEIGHT = 800;
var GRID_WIDTH = 10;
var GRID_HEIGHT = 8;
var GRID_SPACE_WIDTH = PAPER_WIDTH / GRID_WIDTH;
var GRID_SPACE_HEIGHT = PAPER_HEIGHT / GRID_HEIGHT;

var VAN_WIDTH = 40;
var VAN_HEIGHT = 20;

var MOVE_DISTANCE = GRID_SPACE_WIDTH;
var TURN_DISTANCE = MOVE_DISTANCE / 2;
var INITIAL_OFFSET_X = 10;
var INITIAL_OFFSET_Y = 32;
var INITIAL_X = GRID_SPACE_HEIGHT - INITIAL_OFFSET_X;
var INITIAL_Y = 450 - INITIAL_OFFSET_Y;
var ROTATION_OFFSET_X = 25;
var ROTATION_OFFSET_Y = VAN_WIDTH - 20;

var ROAD_WIDTH = GRID_SPACE_WIDTH / 2;
var EDGE_GAP_X = (GRID_SPACE_WIDTH - ROAD_WIDTH) / 2;
var EDGE_GAP_Y = (GRID_SPACE_HEIGHT - ROAD_WIDTH) / 2;
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

function rotateElement(element, degrees, rotationPointX, rotationPointY) {
    var transformation = createRotationTransformation(degrees, rotationPointX, rotationPointY);
    element.transform(transformation);
}

function rotateElementAroundCentreOfGridSpace(element, degrees, i, j) {
    var rotationPointX = (i + 1 / 2) * GRID_SPACE_WIDTH;
    var rotationPointY = (j + 1 / 2) * GRID_SPACE_HEIGHT;
    rotateElement(element, degrees, rotationPointX, rotationPointY);
}

function createVan(paper) {
    return paper.image('/static/game/image/ocadoVan_big.svg', INITIAL_X, INITIAL_Y, VAN_HEIGHT, VAN_WIDTH)
        .transform('r90');
}

function getGridSpace(x, y) {
    return [Math.floor((x + GRID_SPACE_WIDTH / 2) / GRID_SPACE_WIDTH),
        Math.floor((y + GRID_SPACE_HEIGHT / 2) / GRID_SPACE_HEIGHT)];
}

function identifyInstruction(roadSet) {
    var weightPointBox = roadSet[2].getBBox();
    var roadBox = roadSet[0].getBBox();
    var diffX = Math.abs(weightPointBox.x - roadBox.x);
    var diffY = Math.abs(weightPointBox.y - roadBox.y);
    var width = roadBox.width;
    var instruction = '';
    if (diffX == 0 && diffY == 0)
        instruction = 'UL';
    if (diffX == 0 && diffY == EDGE_GAP_Y)
        instruction = 'DL';
    if (diffX == EDGE_GAP_X && diffY == EDGE_GAP_Y)
        instruction = 'DR';
    if (diffX == EDGE_GAP_X && diffY == 0)
        instruction = 'UR';
    if (roadBox.width == 50 && roadBox.height == 100)
        instruction = 'V';
    if (roadBox.width == 100 && roadBox.height == 50)
        instruction = 'H';
    return instruction;
}

function createHorizontalRoad(paper, i, j) {
    var x = i * GRID_SPACE_WIDTH;
    var y = j * GRID_SPACE_HEIGHT + (GRID_SPACE_HEIGHT - ROAD_WIDTH) / 2;

    var road = paper.rect(x, y, GRID_SPACE_WIDTH, ROAD_WIDTH);
    road.attr(ROAD_ATTR);

    var entryMarker = paper.rect(x, j * GRID_SPACE_WIDTH + GRID_SPACE_WIDTH / 2 - 1,
            GRID_SPACE_WIDTH / 8, 2);
    entryMarker.attr(ROAD_MARKER_ATTR);

    var middleMarker = paper.rect(x + 3 * GRID_SPACE_WIDTH / 8,
            j * GRID_SPACE_HEIGHT + GRID_SPACE_HEIGHT / 2 - 1, GRID_SPACE_WIDTH / 4, 2);
    middleMarker.attr(ROAD_MARKER_ATTR);

    var lastMarker = paper.rect(x + 7 * GRID_SPACE_WIDTH / 8,
            j * GRID_SPACE_HEIGHT + GRID_SPACE_HEIGHT / 2 - 1, GRID_SPACE_WIDTH / 8, 2);
    lastMarker.attr(ROAD_MARKER_ATTR);

    var weightPoint = paper.rect(x, y, GRID_SPACE_WIDTH, GRID_SPACE_HEIGHT);
    weightPoint.attr(WEIGHT_POINT_ATTR);

    var markerSet = paper.set();
    markerSet.push(entryMarker, middleMarker, lastMarker);

    var roadSet = paper.set();
    roadSet.push(road, markerSet, weightPoint);

    return roadSet;
}

function createVerticalRoad(paper, i, j) {
    var x = i * GRID_SPACE_WIDTH + (GRID_SPACE_HEIGHT - ROAD_WIDTH) / 2;
    var y = j * GRID_SPACE_HEIGHT;

    var road = paper.rect(x, y, ROAD_WIDTH, GRID_SPACE_HEIGHT);
    road.attr(ROAD_ATTR);

    var entryMarker = paper.rect(i * GRID_SPACE_WIDTH + GRID_SPACE_WIDTH / 2 - 1, y,
        2, GRID_SPACE_WIDTH / 8);
    entryMarker.attr(ROAD_MARKER_ATTR);

    var middleMarker = paper.rect(i * GRID_SPACE_WIDTH + GRID_SPACE_WIDTH / 2 - 1,
            y + 3 * GRID_SPACE_HEIGHT / 8, 2, GRID_SPACE_WIDTH / 4);
    middleMarker.attr(ROAD_MARKER_ATTR);

    var lastMarker = paper.rect(i * GRID_SPACE_WIDTH + GRID_SPACE_WIDTH / 2 - 1,
            y + 7 * GRID_SPACE_HEIGHT / 8, 2, GRID_SPACE_WIDTH / 8);
    lastMarker.attr(ROAD_MARKER_ATTR);

    var weightPoint = paper.rect(x, y, GRID_SPACE_WIDTH, GRID_SPACE_HEIGHT);
    weightPoint.attr(WEIGHT_POINT_ATTR);

    var markerSet = paper.set();
    markerSet.push(entryMarker, middleMarker, lastMarker);

    var roadSet = paper.set();
    roadSet.push(road, markerSet, weightPoint);

    return roadSet;
}

function createTurn(paper, i, j, direction) {
    var baseX = i * GRID_SPACE_WIDTH;
    var baseY = j * GRID_SPACE_HEIGHT;
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
    var weightPoint = paper.rect(baseX, baseY, GRID_SPACE_WIDTH, GRID_SPACE_HEIGHT);

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
        'M', baseX, baseY + GRID_SPACE_HEIGHT / 2 - 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 - 1, baseY + GRID_SPACE_HEIGHT / 2 - 1,
            baseX + GRID_SPACE_WIDTH / 2 - 1, baseY + 1,
        'H', baseX + GRID_SPACE_WIDTH / 2 + 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT / 2 + 1, baseX ,
            baseY + GRID_SPACE_HEIGHT / 2 + 1
    ]);

    return [turn, marker];
}

function createTurnDL(baseX, baseY) {

    var turn = paper.path([
        'M', baseX, baseY + EDGE_GAP_Y + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y + ROAD_WIDTH, baseX + EDGE_GAP_X,
            baseY + GRID_SPACE_HEIGHT,
        'H', baseX + EDGE_GAP_X + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y, baseX, baseY + EDGE_GAP_Y
    ]);

    var marker = paper.path([
        'M', baseX, baseY + GRID_SPACE_HEIGHT / 2 - 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT / 2 - 1,
            baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT + 1,
        'H', baseX + GRID_SPACE_WIDTH / 2 - 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 - 1, baseY + GRID_SPACE_HEIGHT / 2 + 1,
        baseX, baseY + GRID_SPACE_HEIGHT / 2 + 1
    ]);

    return [turn, marker];
}

function createTurnDR(baseX, baseY) {

    var turn = paper.path([
        'M', baseX + GRID_SPACE_WIDTH, baseY + EDGE_GAP_Y,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y, baseX + EDGE_GAP_X, baseY + GRID_SPACE_HEIGHT,
        'H', baseX + EDGE_GAP_X + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y + ROAD_WIDTH,
            baseX + GRID_SPACE_WIDTH, baseY + EDGE_GAP_Y + ROAD_WIDTH
    ]);

    var marker = paper.path([
        'M', baseX + GRID_SPACE_WIDTH / 2 - 1, baseY + GRID_SPACE_HEIGHT + 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT / 2 - 1,
            baseX + GRID_SPACE_WIDTH + 1, baseY + GRID_SPACE_HEIGHT / 2 - 1,
        'V', baseY + GRID_SPACE_HEIGHT / 2 + 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT / 2 + 1,
            baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT + 1
    ]);

    return [turn, marker];
}

function createTurnUR(baseX, baseY) {

    var turn = paper.path([
        'M', baseX + EDGE_GAP_X, baseY,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y + ROAD_WIDTH, baseX + GRID_SPACE_WIDTH, baseY + EDGE_GAP_Y + ROAD_WIDTH,
        'V', baseY + EDGE_GAP_Y,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y, baseX + EDGE_GAP_X + ROAD_WIDTH, baseY
    ]);

    var marker = paper.path([
        'M', baseX + GRID_SPACE_WIDTH + 1, baseY + GRID_SPACE_HEIGHT / 2 - 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT / 2 - 1,
            baseX + GRID_SPACE_WIDTH / 2 + 1, baseY,
        'H', baseX + GRID_SPACE_WIDTH / 2 - 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 - 1, baseY + GRID_SPACE_HEIGHT / 2 + 1,
            baseX + GRID_SPACE_WIDTH + 1, baseY + GRID_SPACE_HEIGHT / 2 + 1
    ]);

    return [turn, marker];
}

function createRoad(paper, roadDefinition) {
    var roadElements = [];
    for (var i = 0; i < GRID_WIDTH; i++) {
        var roadSlice = roadDefinition[i];
        if (roadSlice) {
            for (var j = 0; j < GRID_HEIGHT; j++) {
                var roadType = roadSlice[j];
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
            }
        }
    }
    return roadElements;
}

var van;

function moveVan(attr, callback) {
    van.animate(attr, 500, 'easeIn', callback);
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
}

function turnAround(callback) {
    var moveDistance = -GRID_SPACE_WIDTH / 2;
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

function drawBackground(paper){
	paper.rect(0, 0, PAPER_WIDTH, PAPER_HEIGHT).attr({fill: 'url(/static/game/image/grassTile1.svg)'})
}

function createCFC(){
	paper.image('/static/game/image/OcadoCFC.svg', INITIAL_X - 90, INITIAL_Y - 40, 100, 100).transform('r90');
}

function createDestination(destination){
	console.log(destination);
	paper.image('/static/game/image/house1_noGreen.svg',
			destination.x * GRID_SPACE_WIDTH, PAPER_HEIGHT - (destination.y * GRID_SPACE_HEIGHT) - 25, 100, 100)
			.transform('r90');
}

function renderTheMap(map) {
    paper.clear();
    drawBackground(paper);
    createRoad(paper, map.instructions);
    createCFC(paper);
    createDestination(map.destination.coordinate);
    van = createVan(paper);
}
