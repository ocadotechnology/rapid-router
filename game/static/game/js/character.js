'use strict';

var ocargo = ocargo || {};

ocargo.circumference = function (radius) {
    return 2 * Math.PI * radius;
};

var MOVE_DISTANCE = GRID_SPACE_SIZE;

var DISTANCE_BETWEEN_THE_EDGE_AND_MIDDLE_OF_LEFT_LANE = 38;

var TURN_LEFT_RADIUS = 38;
var TURN_RIGHT_RADIUS = 62;
var TURN_AROUND_RADIUS = 12;

var TURN_LEFT_DISTANCE = ocargo.circumference(TURN_LEFT_RADIUS) / 4;
var TURN_RIGHT_DISTANCE = ocargo.circumference(TURN_RIGHT_RADIUS) / 4;

var FULL_TURN_ANGLE = 90;
var CRASH_TURN_ANGLE = 75;
var TURN_AROUND_TURN_ANGLE = 45;
var CRASH_INTO_COW_TURN_ANGLE = 15;

ocargo.fractionOfTurnLeftDistance = function (angle) {
    return TURN_LEFT_DISTANCE * (angle / FULL_TURN_ANGLE);
};

ocargo.fractionOfTurnRightDistance = function (angle) {
    return TURN_RIGHT_DISTANCE * (angle / FULL_TURN_ANGLE);
};

var TURN_AROUND_TURN_LEFT_DISTANCE = ocargo.fractionOfTurnLeftDistance(TURN_AROUND_TURN_ANGLE);
var TURN_AROUND_TURN_RIGHT_DISTANCE = ocargo.fractionOfTurnRightDistance(TURN_AROUND_TURN_ANGLE);
var TURN_AROUND_MOVE_FORWARD_DISTANCE = MOVE_DISTANCE / 2;
var TURN_AROUND_TURN_AROUND_DISTANCE = ocargo.circumference(TURN_AROUND_RADIUS) / 2;

var CRASH_MOVE_FORWARD_DISTANCE = 0.8 * MOVE_DISTANCE;

var CRASH_INTO_COW_MOVE_FORWARDS_DISTANCE = (MOVE_DISTANCE - ROAD_WIDTH) / 2;

var VEIL_OF_NIGHT_WIDTH = 4240;
var VEIL_OF_NIGHT_HEIGHT = 3440;

var VEIL_OF_NIGHT_URL = 'characters/top_view/VeilOfNight.svg';

ocargo.Character = function (paper, imageUrl, wreckageImageUrl, width, height, startingPosition, nightMode, isVeilOfNight) {
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
    this.isVeilOfNight = isVeilOfNight;

    if (this.nightMode) {
        this.veilOfNight = new ocargo.Character(paper, VEIL_OF_NIGHT_URL, null,
            VEIL_OF_NIGHT_WIDTH, VEIL_OF_NIGHT_HEIGHT, startingPosition, false, true);
    }

    this.initialOffsetX = -this.height / 2;
    this.initialOffsetY = DISTANCE_BETWEEN_THE_EDGE_AND_MIDDLE_OF_LEFT_LANE - (this.width / 2);
};

ocargo.Character.prototype._createCharacterImage = function () {
    return this.paper.image(ocargo.Drawing.raphaelImageDir + this.imageUrl, 0, 0,
        this.height, this.width);
};

ocargo.Character.prototype._createWreckageImage = function () {
    var wreckageImage = this.paper.image(ocargo.Drawing.raphaelImageDir + this.wreckageImageUrl, 0, 0, this.height, this.width);
    wreckageImage.attr({"opacity": 0});
    return wreckageImage;

};

ocargo.Character.prototype.render = function () {
    this.image = this._createCharacterImage();
    this._resetPosition();
    if (!this.isVeilOfNight) {
        this.wreckageImage = this._createWreckageImage();
        this.scrollToShow();
    }
    if (this.nightMode) {
        this.veilOfNight.render();
    }
};

ocargo.Character.prototype._setPosition = function (position) {
    var initialPosition = this._calculateCharactersInitialPosition(position.currentNode);
    this.image.transform('t' + initialPosition.x + ',' + initialPosition.y);

    var rotation = this._calculateInitialRotation(position.previousNode, position.currentNode);
    var transformation = ocargo.Drawing.rotationTransformationAroundCentreOfGridSpace(
        rotation,
        position.currentNode.coordinate.x,
        position.currentNode.coordinate.y);
    this.image.transform(transformation);
    this.image.transform('... r90'); // all characters face up by default
    this.image.attr({opacity: 1});
};

ocargo.Character.prototype._resetPosition = function () {
    this._setPosition(this.startingPosition);
};

ocargo.Character.prototype._calculateCharactersInitialPosition = function (startNode) {
    var coord = ocargo.Drawing.translate(startNode.coordinate);
    var result = {
        x: coord.x * GRID_SPACE_SIZE + this.initialOffsetX + PAPER_PADDING,
        y: coord.y * GRID_SPACE_SIZE + this.initialOffsetY + PAPER_PADDING
    };
    return result
};

ocargo.Character.prototype._calculateInitialRotation = function (previousNode, startNode) {
    var nodeAngleRadians = ocargo.calculateNodeAngle(previousNode, startNode);
    var nodeAngleDegrees = nodeAngleRadians * (180 / Math.PI);
    return -nodeAngleDegrees; // Calculation is counterclockwise, transformations are clockwise
};

ocargo.Character.prototype._imagePosition = function () {
    var box = this.image.getBBox();
    return [box.x, box.y];
};

ocargo.Character.prototype.scrollToShow = function () {
    var dx = 150;
    var dy = 150;

    this.skipOutstandingAnimations();
    var point = this._imagePosition();
    var element = document.getElementById('paper');

    var characterPositionX = point[0];
    var characterPositionY = point[1];
    var top = element.scrollTop;
    var left = element.scrollLeft;
    var width = element.offsetWidth;
    var height = element.offsetHeight;

    function closeToTheEdge(characterPositionCoordinate, delta, lowBoundary, size) {
        var highBoundary = lowBoundary + size;
        var closeToOrBelowLowBoundary = characterPositionCoordinate - delta < lowBoundary;
        var closeToAboveHighBoundary = characterPositionCoordinate + delta > highBoundary;

        return closeToOrBelowLowBoundary || closeToAboveHighBoundary;
    }

    function centerPosition(characterPositionCoordinate, size) {
        return characterPositionCoordinate - (size / 2);
    }

    function scrollHorizontally(dx) {
        if (closeToTheEdge(characterPositionX, dx, left, width)) {
            element.scrollLeft = centerPosition(characterPositionX, width);
            return true;
        }
        return false;
    }

    function scrollVertically(dy) {
        if (closeToTheEdge(characterPositionY, dy, top, height)) {
            element.scrollTop = centerPosition(characterPositionY, height);
            return true;
        }
        return false;
    }

    if (scrollHorizontally(dx)) {
        scrollVertically(dy * 3);
    }

    if (scrollVertically(dy)) {
        scrollHorizontally(dx * 3);
    }

};


ocargo.Character.prototype.skipOutstandingAnimations = function () {
    if (!this.image) {
        return;
    }
    var anims = this.image.status();
    for (var i = 0, ii = anims.length; i < ii; i++) {
        this.image.status(anims[i].anim, 1);
    }

    if (this.veilOfNight) {
        this.veilOfNight.skipOutstandingAnimations();
    }
};

ocargo.Character.prototype._rotationPointX = function (radius) {
    var centreX = this.height / 2;    // x coordinate of the canvas of the character svg
    return centreX + (radius / this.currentScale);
};

ocargo.Character.prototype._rotationPointXForLeftTurn = function () {
    return this._rotationPointX(-TURN_LEFT_RADIUS);
};

ocargo.Character.prototype._rotationPointXForRightTurn = function () {
    return this._rotationPointX(TURN_RIGHT_RADIUS);
};

ocargo.Character.prototype._rotationPointXForTurnAround = function () {
    return this._rotationPointX(TURN_AROUND_RADIUS);
};

// Returns the y coordinate of the centre of rotation
ocargo.Character.prototype._rotationPointY = function () {
    var centreY = this.width / 2;     // y coordinate of the centre of the character svg
    return centreY;
};

ocargo.Character.prototype.moveForward = function (callback, scalingFactor) {
    var moveDistance = -MOVE_DISTANCE / this.currentScale;
    var transformation = "..." + "t 0, " + moveDistance;

    if (scalingFactor) {
        this.currentScale *= scalingFactor;
        transformation += "s" + scalingFactor;
    }

    this._moveImage({
        transform: transformation
    }, this.manoeuvreDuration, callback);

    if (this.veilOfNight) {
        this.veilOfNight.moveForward(null, scalingFactor);
    }
    return this.manoeuvreDuration;
};

ocargo.Character.prototype.turnLeft = function (callback, scalingFactor) {
    var transformation = this._turnLeftTransformation(FULL_TURN_ANGLE, scalingFactor);

    this._moveImage({
        transform: transformation
    }, this.manoeuvreDuration, callback);

    if (scalingFactor) {
        this.currentScale *= scalingFactor;
    }

    if (this.veilOfNight) {
        this.veilOfNight.turnLeft(null, scalingFactor);
    }

    return this.manoeuvreDuration;
};

ocargo.Character.prototype.turnRight = function (callback, scalingFactor) {
    var transformation = this._turnRightTransformation(FULL_TURN_ANGLE, scalingFactor);

    this._moveImage({
        transform: transformation
    }, this.manoeuvreDuration, callback);
    if (scalingFactor) {
        this.currentScale *= scalingFactor;
    }

    if (this.veilOfNight) {
        this.veilOfNight.turnRight(null, scalingFactor);
    }

    return this.manoeuvreDuration;
};

ocargo.Character.prototype.turnAround = function (direction) {
    var that = this;

    var actions = [];
    var index = 0;

    switch (direction) {
        case 'FORWARD':
            actions = [moveForward('easeIn'), rotate(), moveForward('linear')];
            break;
        case 'RIGHT':
            actions = [turnRight('easeIn'), rotate(), turnLeft('linear')];
            break;
        case 'LEFT':
            actions = [turnLeft('easeIn'), rotate(), turnRight('linear')];
            break;
    }


    var duration = 0.0;
    actions.forEach(function(action) {
        duration += action.duration;
    });

    var functions = actions.map(function (action) {
        return action.function;
    });

    performNextAction();

    function performNextAction() {
        if (index < functions.length) {
            functions[index]();
            index++;
        }
    }

    function moveForward(easing) {
        var moveDistance = TURN_AROUND_MOVE_FORWARD_DISTANCE;
        var moveTransformation = "... t 0, -" + moveDistance;

        var duration = that._durationOf(moveDistance);

        var animate = function () {
            that.image.animate({
                transform: moveTransformation
            }, duration, easing, performNextAction);
        };

        return {
            duration: duration,
            function: animate
        };
    }

    function rotate() {
        var transformation = that._turnAroundTransformation();

        var duration = that._durationOf(TURN_AROUND_TURN_AROUND_DISTANCE);
        duration *= 2;

        var animate = function () {
            that.image.animate({
                transform: transformation
            }, duration, 'linear', performNextAction);
        };

        return {
            duration: duration,
            function: animate
        };
    }
    function turnLeft(easing) {
        var transformation = that._turnLeftTransformation(TURN_AROUND_TURN_ANGLE);

        var duration = that._durationOf(TURN_AROUND_TURN_LEFT_DISTANCE);

        var animate = function () {
            that.image.animate({
                transform: transformation
            }, duration, easing, performNextAction);
        };

        return {
            duration: duration,
            function: animate
        };
    }

    function turnRight(easing) {
        var transformation = that._turnRightTransformation(TURN_AROUND_TURN_ANGLE);

        var duration = that._durationOf(TURN_AROUND_TURN_RIGHT_DISTANCE);

        var animate = function () {
            that.image.animate({
                transform: transformation
            }, duration, easing, performNextAction);
        };

        return {
            duration: duration,
            function: animate
        };
    }

    if (this.veilOfNight) {
        this.veilOfNight.turnAround(direction);
    }

    return duration;
};

ocargo.Character.prototype.wait = function (callback) {
    //no movement for now
    this._moveImage({
        transform: '... t 0,0'
    }, this._moveForwardsDuration(), callback);
};

ocargo.Character.prototype._moveImage = function (attr, animationLength, callback) {
    // Compress all current transformations into one
    this.image.transform(this.image.matrix.toTransformString());

    // Perform the next animation
    this.image.animate(attr, animationLength, 'easeInOut', callback);
};

ocargo.Character.prototype._collisionImage = function (withFire) {
    if (withFire) {
        return Math.random() < 0.5 ? 'smoke.svg' : 'fire.svg';
    } else {
        return 'smoke.svg';
    }
};

ocargo.Character.prototype._animateCollision = function (withFire) {
    if (this.isVeilOfNight) {
        return function () {
        };
    }

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

    this.wreckageImage.transform(this.image.transform());

    setTimeout(function () {
        var duration = that._collisionDuration();
        that.wreckageImage.animate({opacity: 1}, duration);
        if (!this.nightMode) {
            that.image.animate({opacity: 0}, duration);
        }

        for (var i = 0; i < explosionParts; i++) {
            setTimeout(function () {
                var size = minSize + Math.random() * (maxSize - minSize);
                var xco = x + width * (Math.random() - 0.5) - 0.5 * size;
                var yco = y + height * (Math.random() - 0.5) - 0.5 * size;
                var imageUrl = ocargo.Drawing.raphaelImageDir + that._collisionImage(withFire);
                var img = that.paper.image(imageUrl, xco, yco, size, size);
                img.animate({opacity: 0, transform: 's2'}, duration, function () {
                    img.remove()
                });
            }, (i < 5 ? 0 : (i - 5) * (duration / 20)));
        }
    }, that._collisionDelay());
};

ocargo.Character.prototype._animateCollisionWithFire = function () {
    var that = this;

    return function () {
        that._animateCollision(true);
    }
};

ocargo.Character.prototype._animateCollisionNoFire = function () {
    var that = this;
    return function () {
        that._animateCollision(false);
    }
};

ocargo.Character.prototype._turnLeftTransformation = function (rotationAngle, scalingFactor) {
    var rotationPointX = this._rotationPointXForLeftTurn();
    var rotationPointY = this._rotationPointY();
    var transformation = this._createRotationTransformation(-rotationAngle, rotationPointX, rotationPointY, scalingFactor);
    return transformation;
};

ocargo.Character.prototype._turnRightTransformation = function (rotationAngle, scalingFactor) {
    var rotationPointX = this._rotationPointXForRightTurn();
    var rotationPointY = this._rotationPointY();
    var transformation = this._createRotationTransformation(rotationAngle, rotationPointX, rotationPointY, scalingFactor);
    return transformation;
};

ocargo.Character.prototype._turnAroundTransformation = function () {
    var rotationPointX = this._rotationPointXForTurnAround();
    var rotationPointY = this._rotationPointY();
    var transformation = this._createRotationTransformation(180, rotationPointX, rotationPointY);
    return transformation;
};

ocargo.Character.prototype.crash = function (attemptedAction) {
    if (attemptedAction === "FORWARD") {
        var transformation = "... t 0, " + (-CRASH_MOVE_FORWARD_DISTANCE);
    } else if (attemptedAction === "TURN_LEFT") {
        var transformation = this._turnLeftTransformation(CRASH_TURN_ANGLE);
    } else if (attemptedAction === "TURN_RIGHT") {
        var transformation = this._turnRightTransformation(CRASH_TURN_ANGLE);
    }

    this._moveImage({
        transform: transformation
    }, this.manoeuvreDuration, this._animateCollisionWithFire());

    if (this.veilOfNight) {
        this.veilOfNight.crash(attemptedAction);
    }

    return this.manoeuvreDuration + this._collisionDuration() + this._collisionDelay();
};

ocargo.Character.prototype.collisionWithCow = function (previousNode, currentNode, attemptedAction) {
     var distance = 0;
    if (attemptedAction === "FORWARD") {
        distance = CRASH_INTO_COW_MOVE_FORWARDS_DISTANCE;
        var scaledDistance = distance / this.currentScale;
        var transformation = "... t 0, " + (-scaledDistance);
    } else if (attemptedAction === "TURN_LEFT") {
        var transformation = this._turnLeftTransformation(CRASH_INTO_COW_TURN_ANGLE);
    } else if (attemptedAction === "TURN_RIGHT") {
        var transformation = this._turnRightTransformation(CRASH_INTO_COW_TURN_ANGLE);
    }

    this._moveImage({
        transform: transformation
    }, this.manoeuvreDuration, this._animateCollisionNoFire());

    if (this.veilOfNight) {
        this.veilOfNight.collisionWithCow(previousNode, currentNode, attemptedAction);
    }

    return this.manoeuvreDuration + this._collisionDuration() + this._collisionDelay();
};

ocargo.Character.prototype._moveForwardsDuration = function () {
    return this._durationOf(MOVE_DISTANCE);
};

ocargo.Character.prototype._collisionDuration = function () {
    return this._moveForwardsDuration() * 2;
};

ocargo.Character.prototype._collisionDelay = function () {
    return this._moveForwardsDuration() / 5;
};

ocargo.Character.prototype._createRotationTransformation = function (degrees, rotationPointX, rotationPointY, scalingFactor) {
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

ocargo.Character.prototype._removeWreckage = function () {
    this.wreckageImage.attr({"opacity": 0});
};

ocargo.Character.prototype.reset = function () {
    this.skipOutstandingAnimations();
    this._resetPosition();
    if (!this.isVeilOfNight) {
        this._removeWreckage();
        this.currentScale = 1;
        this.scrollToShow();
    }

    if (this.veilOfNight) {
        this.veilOfNight.reset();
    }
};

ocargo.Character.prototype.setManoeuvreDuration = function (duration) {
    this.manoeuvreDuration = duration;
};

ocargo.Character.prototype._speed = function () {
    return MOVE_DISTANCE / this.manoeuvreDuration
};

ocargo.Character.prototype._durationOf = function (distance) {
    return distance / this._speed();
};