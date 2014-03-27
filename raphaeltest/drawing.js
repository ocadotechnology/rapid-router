'use strict';

var KEY_CODE_UP = 38;
var KEY_CODE_LEFT = 37;
var KEY_CODE_RIGHT = 39;
var KEY_CODES = [KEY_CODE_UP, KEY_CODE_LEFT, KEY_CODE_RIGHT];

var MOVE_DISTANCE = 50;
var INITIAL_X = 50;
var INITIAL_Y = 400;
var ROTATION_OFFSET_X = 0;
var ROTATION_OFFSET_Y = 30;

window.onload = function() {
    var paper = new Raphael('paper', 500, 500);

    var van = paper.image('van.png', INITIAL_X, INITIAL_Y, 69, 52);
    van.attr({
        fill: '#B35B36'
    });

    var vanMoving = false;

    function moveCompleteCallback() {
        vanMoving = false;
    };

    function moveVan(attr) {
        van.animate(attr, 500, 'easeIn', moveCompleteCallback);
    };

    function moveForward() {
        moveVan({
            x: van.attrs.x + MOVE_DISTANCE
        });
    };

    function moveLeft() {
        var centerX = van.attrs.x + ROTATION_OFFSET_X;
        var centerY = van.attrs.y - MOVE_DISTANCE + ROTATION_OFFSET_Y;
        moveVan({
            transform: '... r-90,' + centerX + ',' + centerY
        });
    };

    function moveRight() {
        var centerX = van.attrs.x + ROTATION_OFFSET_X;
        var centerY = van.attrs.y + MOVE_DISTANCE + ROTATION_OFFSET_Y;
        moveVan({
            transform: '... r90,' + centerX + ',' + centerY
        });
    };

    window.onkeyup = function(event) {
        var keyCode = event.keyCode;
        if (vanMoving || KEY_CODES.indexOf(keyCode) === -1) {
            return;
        }

        vanMoving = true;

        switch (keyCode) {
            case KEY_CODE_UP:
                moveForward();
                break;
            case KEY_CODE_LEFT:
                moveLeft();
                break;
            case KEY_CODE_RIGHT:
                moveRight();
                break;
        }
    };

    window.reset = function() {
        van.attr({
            x: INITIAL_X,
            y: INITIAL_Y,
            transform: 'r0'
        });
        vanMoving = false;
    };
};