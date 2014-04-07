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

var VAN_WIDTH = 37;
var VAN_HEIGHT = 50;

var MOVE_DISTANCE = GRID_SPACE_WIDTH;
var TURN_DISTANCE = MOVE_DISTANCE / 2;
var INITIAL_X = -25;
var INITIAL_Y = 410;
var ROTATION_OFFSET_X = 0;
var ROTATION_OFFSET_Y = 25;

var ROAD_WIDTH = GRID_SPACE_WIDTH / 2;
var EDGE_GAP_X = (GRID_SPACE_WIDTH - ROAD_WIDTH) / 2;
var EDGE_GAP_Y = (GRID_SPACE_HEIGHT - ROAD_WIDTH) / 2;
var ROAD_COLOUR = '#222';
var ROAD_ATTR = {
    fill: ROAD_COLOUR
};

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
};

function createHorizontalRoad(paper, i, j) {
    var x = i * GRID_SPACE_WIDTH;
    var y = j * GRID_SPACE_HEIGHT + (GRID_SPACE_HEIGHT - ROAD_WIDTH) / 2;
    var road = paper.rect(x, y, GRID_SPACE_WIDTH, ROAD_WIDTH);
    road.attr(ROAD_ATTR);
    return road;
};

function createVerticalRoad(paper, i, j) {
    var road = createHorizontalRoad(paper, i, j);
    road.attr({
        transform: 'r90'
    });
    return road;
};

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
    
    var rotation = 'r0';
    switch (direction) {
        case 'UR':
            rotation = 'r90';
            break;
        case 'DR':
            rotation = 'r180';
            break;
        case 'DL':
            rotation = 'r270';
            break;
    }
    
    var rotationPointX = baseX + ROAD_WIDTH;
    var rotationPointY = baseY + ROAD_WIDTH;
    return turn.attr({
        transform: rotation + ',' + rotationPointX + ',' + rotationPointY
    });
};

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
};

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
};

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
};

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
    };
    
    return createRoad(paper, roadDefinition);
};

var van;
var vanMoving = false;

function moveVan(attr, callback) {
    van.animate(attr, 500, 'easeIn', callback);
};

function moveForward(callback) {
    moveVan({
        x: van.attrs.x + MOVE_DISTANCE
    }, callback);
};

function moveLeft(callback) {
    var centerX = van.attrs.x + ROTATION_OFFSET_X;
    var centerY = van.attrs.y - TURN_DISTANCE + ROTATION_OFFSET_Y;
    moveVan({
        transform: '... r-90,' + centerX + ',' + centerY
    }, callback);
};

function moveRight(callback) {
    var centerX = van.attrs.x + ROTATION_OFFSET_X;
    var centerY = van.attrs.y + TURN_DISTANCE + ROTATION_OFFSET_Y;
    moveVan({
        transform: '... r90,' + centerX + ',' + centerY
    }, callback);
};

function resetVan() {
    van.attr({
        x: INITIAL_X,
        y: INITIAL_Y,
        transform: 'r0'
    });
    van.toFront();
    vanMoving = false;
};

window.onload = function() {
    var paper = new Raphael('paper', PAPER_WIDTH, PAPER_HEIGHT);
    
    createGrid(paper);
    
    var roadElements = createDefaultRoad(paper);
    
    van = paper.image('/static/game/image/van.png', INITIAL_X, INITIAL_Y, VAN_HEIGHT, VAN_WIDTH);

    function moveCompleteCallback() {
        vanMoving = false;
    };

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

    function clearRoad() {
        for (var i = 0; i < roadElements.length; i++) {
            roadElements[i].remove();
        }
        roadElements = [];
    };
    
    window.reset = function() {
        clearRoad();
        roadElements = createDefaultRoad(paper);
        resetVan();
    };
    
    window.randomRoad = function() {
        clearRoad();
        roadElements = createRandomRoad(paper);
        resetVan();
    };
};
