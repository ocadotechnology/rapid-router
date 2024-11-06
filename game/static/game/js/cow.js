'use strict';

var ocargo = ocargo || {};

ocargo.Cow = function(id, data, nodes) {
    this.id = id;
    this.nodes = nodes;
    this.type = data.type;
    this.potentialNodes = [];    // Potential nodes at which a cow could appear
    this.activeNodes = {};       // Actual nodes at which cows will appear during a run.
    this.coordinates = [];       // coordinates of the cows, some cows may have null nodes that denotes they are outside of road

    for(var i = 0; i < data.potentialCoordinates.length; i++) {
        var coordinate = new ocargo.Coordinate(data.potentialCoordinates[i].x, data.potentialCoordinates[i].y);
        var node = ocargo.Node.findNodeByCoordinate(coordinate, nodes);
        this.potentialNodes.push(node);
        var coordinate_str = JSON.stringify(coordinate);
        this.activeNodes[coordinate_str] = ocargo.Cow.ACTIVE;
        this.coordinates.push(coordinate);
    }
};
ocargo.Cow.prototype.reset = function() {

    for (var jsonCoordinate in this.activeNodes) {
        this.activeNodes[jsonCoordinate] = ocargo.Cow.READY;
    }
};

ocargo.Cow.prototype.queueLeaveAnimation = function(model, node) {
    ocargo.animation.appendAnimation({
        type: 'callable',
        functionCall: this.type == ocargo.Cow.PIGEON ? ocargo.sound.pigeon : ocargo.sound.cow,
        description: 'animal sound'
    });
    ocargo.animation.appendAnimation({
        type: 'cow_leave',
        id: this.id,
        coordinate: node.coordinate,
        description: 'animal leaving'
    });
};

ocargo.Cow.prototype.setInactive = function(model, node) {
    var jsonCoordinate = JSON.stringify(node.coordinate); //get node coordinates
    this.activeNodes[jsonCoordinate] = ocargo.Cow.INACTIVE; //set cow state to inactive
    this.triggerEvent = true;
    this.queueLeaveAnimation(model, node);
};

ocargo.Cow.READY = 'READY';
ocargo.Cow.ACTIVE = 'ACTIVE';
ocargo.Cow.INACTIVE = 'INACTIVE';
ocargo.Cow.WHITE = 'WHITE';
ocargo.Cow.BROWN = 'BROWN';
ocargo.Cow.PIGEON = 'PIGEON';
