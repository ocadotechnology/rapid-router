'use strict';

var ocargo = ocargo || {};

ocargo.Cow = function(id, data, nodes) {
    this.id = id;
    this.nodes = nodes;
    this.type = data.type;
    this.potentialNodes = [];    // Potential nodes at which a cow could appear
    this.activeNodes = {};       // Actual nodes at which cows will appear during a run.
    for(var i = 0; i < data.potentialCoordinates.length; i++) {
        var coordinate = new ocargo.Coordinate(data.potentialCoordinates[i].x, data.potentialCoordinates[i].y);
        this.potentialNodes.push(ocargo.Node.findNodeByCoordinate(coordinate, nodes));
    }

    if ('minCows' in data) {
        this.minCows = data.minCows; // Minimum number of cows to appear on the potential nodes during a run
    }

    if ('maxCows' in data) {
        this.maxCows = data.maxCows; // Maximum number of cows to appear on the potential nodes during a run
    }

    this.chooseNewCowPositions(); // init simulation fields
};

ocargo.Cow.prototype.pickRandom = function (count, arr) {
    var out = [], i, pick, clone = arr.slice(0, arr.length);
    for (i = 0; i < count; i ++) {
        pick = Math.floor(Math.random() * clone.length);
        if (clone[pick] !== undefined) {
            out.push(clone[pick]);
            clone.splice(pick, 1);
        }
    }
    return out;
};

ocargo.Cow.prototype.reset = function() {
    this.activeNodeTimers = {};     // Stores time of appearance of cows on each activeNode.

    for (var jsonCoordinate in this.activeNodes) {
        this.activeNodes[jsonCoordinate] = ocargo.Cow.READY;
        this.activeNodeTimers[jsonCoordinate] = 0;
    }
};

function arraysIdentical(a, b) {
    var i = a.length;
    if (i != b.length) return false;
    while (i--) {
        if (a[i] !== b[i]) return false;
    }
    return true;
}

ocargo.Cow.prototype.chooseNewCowPositions = function() {
    var numCows = Math.round(this.minCows+Math.random()*(this.maxCows-this.minCows));

    var previousActiveNodes = [];   // Actual nodes during last run
    for (var jsonCoordinate in this.activeNodes) {
        var node = ocargo.Node.findNodeByCoordinate(JSON.parse(jsonCoordinate), this.nodes);
        previousActiveNodes.push(node);
    }

    this.activeNodes = {};

    // at least one node in the new active nodes should be a different one from previous run
    // (Unless minCows is equal to the number of potential nodes)
    var activeNodesArray;
    // No previous run
    if(previousActiveNodes.length == 0) {
        activeNodesArray = this.pickRandom(numCows, this.potentialNodes);
        // New run, choose different nodes if possible
    } else {
        activeNodesArray = previousActiveNodes;
        while (this.minCows < this.potentialNodes.length && arraysIdentical(previousActiveNodes, activeNodesArray)) {
            activeNodesArray = this.pickRandom(numCows, this.potentialNodes);
        }
    }

    for (var i = 0; i < activeNodesArray.length; i++) {
        var jsonCoordinate = JSON.stringify(activeNodesArray[i].coordinate);
        this.activeNodes[jsonCoordinate] = ocargo.Cow.READY;
    }

    this.reset();
};

ocargo.Cow.prototype.queueAnimation = function(model, node) {
    ocargo.animation.appendAnimation({
        type: 'cow',
        id: this.id,
        node: node,
        cowType: this.type,
        coordinate: node.coordinate,
        description: 'Cow'
    });
};

ocargo.Cow.prototype.queueLeaveAnimation = function(model, node) {
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: ocargo.sound.cow,
        description: 'cow sound'
    });
    ocargo.animation.appendAnimation({
        type: 'cow_leave',
        id: this.id,
        coordinate: node.coordinate,
        description: 'Cow leaving'
    });
};

ocargo.Cow.prototype.incrementTime = function(model) {
    // Do not hide cow(s) if van has crashed
    if(model.van.crashStatus === 'CRASHED') {
        return;
    }
    // check if any active cows should be removed (if van has taken any action to scare them away)
    for (var jsonCoordinate in this.activeNodes) {
        if (this.activeNodes[jsonCoordinate] == ocargo.Cow.ACTIVE) {
            var coordinate = JSON.parse(jsonCoordinate);
            var cowTimestamp = this.activeNodeTimers[jsonCoordinate];
            if (this.scaredAwayByHorn(model, cowTimestamp, coordinate) || this.scaredAwayByPuffUp(model, cowTimestamp, coordinate)) {
                // Deactivate and remove cow from map
                this.activeNodes[jsonCoordinate] = ocargo.Cow.INACTIVE;
                this.activeNodeTimers[jsonCoordinate] = 0;
                var node = ocargo.Node.findNodeByCoordinate(coordinate, this.nodes);
                this.queueLeaveAnimation(model, node);
            }
        }
    }
};

// White cows are scared away if horn was sounded after the cow appeared and within hearing distance
ocargo.Cow.prototype.scaredAwayByHorn = function(model, coordinateTime, coordinate){
    if(jQuery.isEmptyObject(model.soundedHorn)){
        return false;
    }
    return this.type == ocargo.Cow.WHITE && coordinateTime < model.soundedHorn.timestamp && this.withinRadius(coordinate, model.soundedHorn.coordinates) ;

};

// Brown cows are scared away if the van was puffed up at the time of checking
ocargo.Cow.prototype.scaredAwayByPuffUp = function(model, coordinateTime, coordinate){
    if(jQuery.isEmptyObject(model.puffedUp)){
        return false;
    }
    return this.type == ocargo.Cow.BROWN && this.withinRadius(coordinate, model.puffedUp.coordinates) ;

};

ocargo.Cow.prototype.withinRadius = function(coordinate1, coordinate2){
    return Math.abs(coordinate1.x-coordinate2.x)+ Math.abs(coordinate1.y-coordinate2.y) <= 2;
};

ocargo.Cow.prototype.setActive = function(model, node) {
    var jsonCoordinate = JSON.stringify(node.coordinate); //get node coordinates
    this.activeNodes[jsonCoordinate] = ocargo.Cow.ACTIVE; //set cow state to active
    this.activeNodeTimers[jsonCoordinate] = model.movementTimestamp; //initialize cow timer.
    this.triggerEvent = true;
    this.queueAnimation(model, node);
};

ocargo.Cow.READY = 'READY';
ocargo.Cow.ACTIVE = 'ACTIVE';
ocargo.Cow.INACTIVE = 'INACTIVE';
ocargo.Cow.WHITE = 'WHITE';
ocargo.Cow.BROWN = 'BROWN';