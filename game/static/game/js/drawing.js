'use strict';

var KEY_CODE_UP = 38;
var KEY_CODE_LEFT = 37;
var KEY_CODE_RIGHT = 39;
var KEY_CODES = [KEY_CODE_UP, KEY_CODE_LEFT, KEY_CODE_RIGHT];

var PAPER_WIDTH = 1000;
var PAPER_HEIGHT = 800;
var GRID_WIDTH = 10;
var GRID_HEIGHT = 8;
var GRID_SPACE_WIDTH = PAPER_WIDTH / GRID_WIDTH;
var GRID_SPACE_HEIGHT = PAPER_HEIGHT / GRID_HEIGHT;

var VAN_WIDTH = 37.5;
var VAN_HEIGHT = 17.5;

var MOVE_DISTANCE = GRID_SPACE_WIDTH;
var TURN_DISTANCE = MOVE_DISTANCE / 2;
var INITIAL_X = GRID_SPACE_HEIGHT - VAN_WIDTH / 2;
var INITIAL_Y = 430;
var ROTATION_OFFSET_X = VAN_WIDTH / 2;
var ROTATION_OFFSET_Y = 20;

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
    var rotationPointX = (i + 1/2) * GRID_SPACE_WIDTH;
    var rotationPointY = (j + 1/2) * GRID_SPACE_HEIGHT;
    rotateElement(element, degrees, rotationPointX, rotationPointY);
}

function createGrid(paper) {
    for (var i = 0; i < GRID_WIDTH; i++) {
        for (var j = 0; j < GRID_HEIGHT; j++) {
            var x = i * GRID_SPACE_WIDTH;
            var y = j * GRID_SPACE_HEIGHT;
            var gridSpace = paper.rect(x, y, GRID_SPACE_WIDTH, GRID_SPACE_HEIGHT);
            gridSpace.attr({
                stroke: '#777'
            });
        }
    }
}

function createHorizontalRoad(paper, i, j) {
    var x = i * GRID_SPACE_WIDTH;
    var y = j * GRID_SPACE_HEIGHT + (GRID_SPACE_HEIGHT - ROAD_WIDTH) / 2;

    var road = paper.rect(x, y, GRID_SPACE_WIDTH, ROAD_WIDTH);
    road.attr(ROAD_ATTR);

    var entryMarker = paper.rect(x, j * GRID_SPACE_WIDTH + GRID_SPACE_WIDTH / 2 - 1, GRID_SPACE_WIDTH / 8, 2);
    entryMarker.attr(ROAD_MARKER_ATTR);

    var middleMarker = paper.rect(x + 3 * GRID_SPACE_WIDTH / 8, j * GRID_SPACE_HEIGHT + GRID_SPACE_HEIGHT / 2 - 1, GRID_SPACE_WIDTH / 8, 2);
    middleMarker.attr(ROAD_MARKER_ATTR);

    var markerSet = paper.set();
    markerSet.push(entryMarker, middleMarker);

    var rotatedMarkerSet = markerSet.clone();
    rotateElementAroundCentreOfGridSpace(rotatedMarkerSet, 180, i, j);

    var roadSet = paper.set();
    roadSet.push(road, markerSet, rotatedMarkerSet);

    return roadSet;
}

function createVerticalRoad(paper, i, j) {
    var road = createHorizontalRoad(paper, i, j);
    rotateElementAroundCentreOfGridSpace(road, 90, i, j);
    return road;
}

function createTurn(paper, i, j, direction) {
    var baseX = i * GRID_SPACE_WIDTH;
    var baseY = j * GRID_SPACE_HEIGHT;

    var turn = paper.path([
        'M', baseX, baseY + EDGE_GAP_Y,
        'Q', baseX + EDGE_GAP_X, baseY + EDGE_GAP_Y, baseX + EDGE_GAP_X, baseY,
        'H', baseX + EDGE_GAP_X + ROAD_WIDTH,
        'Q', baseX + EDGE_GAP_X + ROAD_WIDTH, baseY + EDGE_GAP_Y + ROAD_WIDTH, baseX, baseY + EDGE_GAP_Y + ROAD_WIDTH
    ]);
    turn.attr(ROAD_ATTR);

    var marker = paper.path([
        'M', baseX, baseY + GRID_SPACE_HEIGHT / 2 - 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 - 1, baseY + GRID_SPACE_HEIGHT / 2 - 1, baseX + GRID_SPACE_WIDTH / 2 - 1, baseY,
        'H', baseX + GRID_SPACE_WIDTH / 2 + 1,
        'Q', baseX + GRID_SPACE_WIDTH / 2 + 1, baseY + GRID_SPACE_HEIGHT / 2 + 1, baseX, baseY + GRID_SPACE_HEIGHT / 2 + 1
    ]);
    marker.attr(ROAD_MARKER_ATTR);

    var rotation = 0;
    switch (direction) {
        case 'UR':
            rotation = 90;
            break;
        case 'DR':
            rotation = 180;
            break;
        case 'DL':
            rotation = 270;
            break;
    }

    var roadSet = paper.set();
    roadSet.push(turn, marker);
    rotateElementAroundCentreOfGridSpace(roadSet, rotation, i, j);

    return roadSet;
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

function createDefaultRoad(paper) {
    var defaultRoad = {
        0: {
            4: 'H'
        },
        1: {
            2: 'DR',
            3: 'V',
            4: 'UL'
        },
        2: {
            2: 'H'
        },
        3: {
            0: 'DR',
            1: 'V',
            2: 'UL'
        },
        4: {
            0: 'H'
        },
        5: {
            0: 'DL',
            1: 'V',
            2: 'UR'
        },
        6: {
            2: 'H'
        },
        7: {
            2: 'H'
        },
        8: {
            2: 'H'
        },
        9: {
            2: 'H'
        }
    };
    return createRoad(paper, defaultRoad);
}

function onGrid(i, j) {
    return i >= 0 && i < GRID_WIDTH && j >= 0 && j < GRID_HEIGHT;
}

function gridPositionUndefined(roadDefinition, i, j) {
    var roadSlice = roadDefinition[i];
    return !(roadSlice && roadSlice[j]);
}

function randomElement(array) {
    var randomIndex = Math.floor(Math.random() * array.length);
    return array[randomIndex];
}

function createRandomRoad(paper) {
    var roadDefinition = {};

    var nextElementsAndOrientations = {
        'U': [['DL', 'L', -1, 0], ['V', 'U', 0, -1], ['DR', 'R', 1, 0]],
        'R': [['UL', 'U', 0, -1], ['H', 'R', 1, 0], ['DL', 'D', 0, 1]],
        'D': [['UL', 'L', -1, 0], ['V', 'D', 0, 1], ['UR', 'R', 1, 0]],
        'L': [['DR', 'D', 0, 1], ['H', 'L', -1, 0], ['UR', 'U', 0, -1]]
    };

    var orientation = 'R';
    var i = 0;
    var j = 4;
    while (onGrid(i, j) && gridPositionUndefined(roadDefinition, i, j)) {
        var possibleNext = nextElementsAndOrientations[orientation];
        var next = randomElement(possibleNext);
        var element = next[0];
        var nextOrientation = next[1];
        var iChange = next[2];
        var jChange = next[3];

        var roadSlice = roadDefinition[i];
        if (!roadSlice) {
            roadSlice = {};
            roadDefinition[i] = roadSlice;
        }
        roadSlice[j] = element;

        orientation = nextOrientation;
        i += iChange;
        j += jChange;
    }

    return createRoad(paper, roadDefinition);
}

var van;
var vanMoving = false;

function moveVan(attr, callback) {
    van.animate(attr, 500, 'easeIn', callback);
}

function moveForward(callback) {
    moveVan({
        x: van.attrs.x + MOVE_DISTANCE
    }, callback);
}

function moveLeft(callback) {
    var rotationPointX = van.attrs.x + ROTATION_OFFSET_X;
    var rotationPointY = van.attrs.y - TURN_DISTANCE + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(-90, rotationPointX, rotationPointY);
    moveVan({
        transform: transformation
    }, callback);
}

function moveRight(callback) {
    var rotationPointX = van.attrs.x + ROTATION_OFFSET_X;
    var rotationPointY = van.attrs.y + TURN_DISTANCE + ROTATION_OFFSET_Y;
    var transformation = createRotationTransformation(90, rotationPointX, rotationPointY);
    moveVan({
        transform: transformation
    }, callback);
}

function resetVan() {
    van.attr({
        x: INITIAL_X,
        y: INITIAL_Y,
        transform: 'r0'
    });
    van.toFront();
    vanMoving = false;
}

function renderTheMap(map) {

    paper.clear();

    createGrid(paper);

    var roadElements = createRoad(paper, map.instructions);

    van = paper.image('/static/game/image/van.svg', INITIAL_X, INITIAL_Y, VAN_WIDTH, VAN_HEIGHT);

    function moveCompleteCallback() {
        vanMoving = false;
    }

    window.onkeyup = function(event) {
        var keyCode = event.keyCode;
        if (vanMoving || KEY_CODES.indexOf(keyCode) === -1) {
            return;
        }

        vanMoving = true;

        switch (keyCode) {
            case KEY_CODE_UP:
                moveForward(moveCompleteCallback);
                break;
            case KEY_CODE_LEFT:
                moveLeft(moveCompleteCallback);
                break;
            case KEY_CODE_RIGHT:
                moveRight(moveCompleteCallback);
                break;
        }
    };
}
