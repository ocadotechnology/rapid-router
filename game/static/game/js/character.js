/*
 Code for Life

 Copyright (C) 2015, Ocado Limited

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

var MOVE_DISTANCE = GRID_SPACE_SIZE;

var DISTANCE_BETWEEN_THE_EDGE_AND_MIDDLE_OF_LEFT_LANE = 38;

var TURN_LEFT_RADIUS = -38;
var TURN_RIGHT_RADIUS = 62;
var TURN_AROUND_RADIUS = 12;

ocargo.Character = function (paper, imageUrl, wreckageImageUrl, width, height, startingPosition, nightMode) {
    this.currentScale = 1;

    this.imageUrl = imageUrl;
    this.wreckageImageUrl = wreckageImageUrl;

    this.image = undefined;
    this.wreckageImage = undefined;

    this.paper = paper;
    this.width = width;
    this.height = height;
    this.startingPosition = startingPosition;
    this.nightMode = nightMode;

    this.initialOffsetX = -this.height / 2;
    this.initialOffsetY = DISTANCE_BETWEEN_THE_EDGE_AND_MIDDLE_OF_LEFT_LANE - (this.width / 2);
};

ocargo.Character.prototype.createCharacterImage = function() {
    return this.paper.image(ocargo.Drawing.raphaelImageDir + this.imageUrl, 0, 0,
        this.height, this.width);
};

ocargo.Character.prototype.render = function () {
    this.image = this.createCharacterImage();
    this.resetPosition();
    this.scrollToShow();
};

ocargo.Character.prototype.setPosition = function (position) {
    var initialPosition = this.calculateCharactersInitialPosition(position.currentNode);
    this.image.transform('t' + initialPosition.x + ',' + initialPosition.y);

    var rotation = this.calculateInitialRotation(position.previousNode, position.currentNode);
    var transformation = ocargo.Drawing.rotationTransformationAroundCentreOfGridSpace(
        rotation,
        position.currentNode.coordinate.x,
        position.currentNode.coordinate.y);
    this.image.transform(transformation);
    this.image.transform('... r90'); // all characters face up by default
    this.image.attr({opacity: 1});
};

ocargo.Character.prototype.resetPosition = function () {
    this.setPosition(this.startingPosition);
};

ocargo.Character.prototype.calculateCharactersInitialPosition = function (startNode) {
    var coord = ocargo.Drawing.translate(startNode.coordinate);
    var result = {
        x: coord.x * GRID_SPACE_SIZE + this.initialOffsetX + PAPER_PADDING,
        y: coord.y * GRID_SPACE_SIZE + this.initialOffsetY + PAPER_PADDING
    };
    return result
};

ocargo.Character.prototype.calculateInitialRotation = function (previousNode, startNode) {
    var nodeAngleRadians = ocargo.calculateNodeAngle(previousNode, startNode);
    var nodeAngleDegrees = nodeAngleRadians * (180 / Math.PI);
    return -nodeAngleDegrees; // Calculation is counterclockwise, transformations are clockwise
};

ocargo.Character.prototype.imagePosition = function () {
    var box = this.image.getBBox();
    return [box.x, box.y];
};

ocargo.Character.prototype.scrollToShow = function () {
    this.skipOutstandingAnimations();
    var point = this.imagePosition();
    var element = document.getElementById('paper');

    element.scrollLeft = point[0] - element.offsetWidth / 2;
    element.scrollTop = point[1] - element.offsetHeight / 2;
};


ocargo.Character.prototype.skipOutstandingAnimations = function () {
    if (!this.image) {
        return;
    }
    var anims = this.image.status();
    for (var i = 0, ii = anims.length; i < ii; i++) {
        this.image.status(anims[i].anim, 1);
    }
};

ocargo.Character.prototype.rotationPointX = function (radius) {
    var centreX = this.height / 2;    // x coordinate of the canvas of the character svg
    return centreX + (radius / this.currentScale);
};

ocargo.Character.prototype.rotationPointXForLeftTurn = function () {
    return this.rotationPointX(TURN_LEFT_RADIUS);
};

ocargo.Character.prototype.rotationPointXForRightTurn = function () {
    return this.rotationPointX(TURN_RIGHT_RADIUS);
};

ocargo.Character.prototype.rotationPointXForTurnAround = function () {
    return this.rotationPointX(TURN_AROUND_RADIUS);
};

// Returns the y coordinate of the centre of rotation
ocargo.Character.prototype.rotationPointY = function () {
    var centreY = this.width / 2;     // y coordinate of the centre of the character svg
    return centreY;
};

ocargo.Character.prototype.moveForward = function (animationLength, callback, scalingFactor) {

    var moveDistance = -MOVE_DISTANCE / this.currentScale;
    var transformation = "..." + "t 0, " + moveDistance;

    if (scalingFactor) {
        this.currentScale *= scalingFactor;
        transformation += "s" + scalingFactor;
    }

    this.moveVanImage({
        transform: transformation
    }, animationLength, callback);
};

ocargo.Character.prototype.moveLeft = function (animationLength, callback, scalingFactor) {
    var transformation = this.turnLeftTransformation(90, scalingFactor);
    this.moveVanImage({
        transform: transformation
    }, animationLength, callback);
    if (scalingFactor) {
        this.currentScale *= scalingFactor;
    }
};

ocargo.Character.prototype.moveRight = function (animationLength, callback, scalingFactor) {
    var transformation = this.turnRightTransformation(90, scalingFactor);
    this.moveVanImage({
        transform: transformation
    }, animationLength, callback);
    if (scalingFactor) {
        this.currentScale *= scalingFactor;
    }
};

ocargo.Character.prototype.turnAround = function (direction, animationLength) {
    var that = this;
    var timePerState = (animationLength - 50) / 3;

    var actions = [];
    var index = 0;

    switch (direction) {
        case 'FORWARD':
            actions = [moveForward('easeIn'), rotate('linear'), moveForward('easeOut')];
            break;
        case 'RIGHT':
            actions = [turnRight('easeIn'), rotate('linear'), turnLeft('easeOut')];
            break;
        case 'LEFT':
            actions = [turnLeft('easeIn'), rotate('linear'), turnRight('easeOut')];
            break;
    }

    performNextAction();

    function performNextAction() {
        if (index < actions.length) {
            actions[index]();
            index++;
        }
    }

    function moveForward(easing) {
        return function () {
            var moveDistance = -GRID_SPACE_SIZE / 2;
            var moveTransformation = "... t 0, " + moveDistance;
            that.image.animate({
                transform: moveTransformation
            }, timePerState, easing, performNextAction);
        }
    }

    function rotate(easing) {
        return function () {
            var transformation = that.turnAroundTransformation();
            that.image.animate({
                transform: transformation
            }, timePerState, easing, performNextAction);
        }
    }

    function turnLeft(easing) {
        return function () {
            var transformation = that.turnLeftTransformation(45);
            that.image.animate({
                transform: transformation
            }, timePerState, easing, performNextAction);
        }
    }

    function turnRight(easing) {
        return function () {
            var transformation = that.turnRightTransformation(45);
            that.image.animate({
                transform: transformation
            }, timePerState, easing, performNextAction);
        }
    }
};

ocargo.Character.prototype.wait = function (animationLength, callback) {
    //no movement for now
    this.moveVanImage({
        transform: '... t 0,0'
    }, animationLength, callback);
};

ocargo.Character.prototype.moveVanImage = function (attr, animationLength, callback) {
    // Compress all current transformations into one
    this.image.transform(this.image.matrix.toTransformString());

    // Perform the next animation
    this.image.animate(attr, animationLength, 'linear', callback);
};

ocargo.Character.prototype.collisionImage = function (withFire) {
    if (withFire) {
        return Math.random() < 0.5 ? 'smoke.svg' : 'fire.svg';
    } else {
        return 'smoke.svg';
    }
};

ocargo.Character.prototype.animateCollision = function (withFire) {
    var that = this;
    if (CHARACTER_NAME !== "Van") {
        return;
    }
    var bbox = this.image.getBBox();

    var x = bbox.x + bbox.width / 2;
    var y = bbox.y + bbox.height / 2;

    var width = 20;
    var height = 20;

    var maxSize = 20;
    var minSize = 10;

    var explosionParts = 20;

    this.wreckageImage = this.paper.image(ocargo.Drawing.raphaelImageDir + this.wreckageImageUrl, 0, 0,
        this.height, this.width);
    this.wreckageImage.transform(this.image.transform());
    this.wreckageImage.attr({"opacity": 0});

    setTimeout(function () {
        that.wreckageImage.animate({opacity: 1}, 1000);
        if (!this.nightMode) {
            that.image.animate({opacity: 0}, 1000);
        }

        for (var i = 0; i < explosionParts; i++) {
            setTimeout(function () {
                var size = minSize + Math.random() * (maxSize - minSize);
                var xco = x + width * (Math.random() - 0.5) - 0.5 * size;
                var yco = y + height * (Math.random() - 0.5) - 0.5 * size;
                var imageUrl = ocargo.Drawing.raphaelImageDir + that.collisionImage(withFire);
                var img = that.paper.image(imageUrl, xco, yco, size, size);
                img.animate({opacity: 0, transform: 's2'}, 1000, function () {
                    img.remove()
                });
            }, (i < 5 ? 0 : (i - 5) * 50));
        }
    }, 100);
};

ocargo.Character.prototype.animateCollisionWithFire = function() {
    var that = this;
    return function() {
        that.animateCollision(true);
    }
};

ocargo.Character.prototype.animateCollisionNoFire = function() {
    var that = this;
    return function() {
        that.animateCollision(false);
    }
};

ocargo.Character.prototype.turnLeftTransformation = function (rotationAngle, scalingFactor) {
    var rotationPointX = this.rotationPointXForLeftTurn();
    var rotationPointY = this.rotationPointY();
    var transformation = this.createRotationTransformation(-rotationAngle, rotationPointX, rotationPointY, scalingFactor);
    return transformation;
};

ocargo.Character.prototype.turnRightTransformation = function (rotationAngle, scalingFactor) {
    var rotationPointX = this.rotationPointXForRightTurn();
    var rotationPointY = this.rotationPointY();
    var transformation = this.createRotationTransformation(rotationAngle, rotationPointX, rotationPointY, scalingFactor);
    return transformation;
};

ocargo.Character.prototype.turnAroundTransformation = function () {
    var rotationPointX = this.rotationPointXForTurnAround();
    var rotationPointY = this.rotationPointY();
    var transformation = this.createRotationTransformation(180, rotationPointX, rotationPointY);
    return transformation;
};

ocargo.Character.prototype.crash = function (animationLength, previousNode, currentNode, attemptedAction) {
    if (attemptedAction === "FORWARD") {
        var distanceForwards;
        distanceForwards = 0.8 * GRID_SPACE_SIZE;

        var transformation = "... t 0, " + (-distanceForwards);
    } else if (attemptedAction === "TURN_LEFT") {
        var transformation = this.turnLeftTransformation(75);
    } else if (attemptedAction === "TURN_RIGHT") {
        var transformation = this.turnRightTransformation(75);
    }

    this.moveVanImage({
        transform: transformation
    }, animationLength, this.animateCollisionWithFire());
};

ocargo.Character.prototype.collisionWithCow = function (animationLength, previousNode, currentNode, attemptedAction) {
    if (attemptedAction === "FORWARD") {
        var distanceForwards = (0.5 * GRID_SPACE_SIZE - 0.5 * ROAD_WIDTH) / this.currentScale;
        var transformation = "... t 0, " + (-distanceForwards);
    } else if (attemptedAction === "TURN_LEFT") {
        var transformation = this.turnLeftTransformation(15);
    } else if (attemptedAction === "TURN_RIGHT") {
        var transformation = this.turnRightTransformation(15);
    }

    var newAnimationLength = animationLength * ((GRID_SPACE_SIZE - ROAD_WIDTH) / (GRID_SPACE_SIZE + ROAD_WIDTH));
    this.moveVanImage({
        transform: transformation
    }, newAnimationLength, this.animateCollisionNoFire());

    return newAnimationLength;
};

ocargo.Character.prototype.createRotationTransformation = function (degrees, rotationPointX, rotationPointY, scalingFactor) {
    var transformation = "..." + "r" + degrees;
    if (rotationPointX !== undefined && rotationPointY !== undefined) {
        transformation += ',' + rotationPointX;
        transformation += ',' + rotationPointY;
    }
    if (scalingFactor) {
        // extra scaling is done after rotation as scaling was taken into acocunt in getRotationPoints
        transformation += "s" + scalingFactor;
    }
    return transformation;
};

ocargo.Character.prototype.removeWreckage = function () {
    if (this.wreckageImage) {
        this.wreckageImage.remove();
    }
};

ocargo.Character.prototype.reset = function () {
    this.skipOutstandingAnimations();
    this.resetPosition();
    this.removeWreckage();
    this.currentScale = 1;
};
