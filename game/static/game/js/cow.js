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
        var node = ocargo.Node.findNodeByCoordinate(coordinate, nodes)
        this.potentialNodes.push(ocargo.Node.findNodeByCoordinate(coordinate, nodes));
        var coordinate_str = JSON.stringify(node.coordinate)
        this.activeNodes[coordinate_str] = ocargo.Cow.ACTIVE
    }
};
ocargo.Cow.prototype.reset = function() {

    for (var jsonCoordinate in this.activeNodes) {
        this.activeNodes[jsonCoordinate] = ocargo.Cow.READY;
    }
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

ocargo.Cow.prototype.setActive = function(model, node) {
    var jsonCoordinate = JSON.stringify(node.coordinate); //get node coordinates
    this.activeNodes[jsonCoordinate] = ocargo.Cow.ACTIVE; //set cow state to active
    this.triggerEvent = true;
    this.queueAnimation(model, node);
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
