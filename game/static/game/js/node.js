'use strict';

var ocargo = ocargo || {};

ocargo.Node = function (coordinate) {
    this.coordinate = coordinate;
    this.connectedNodes = [];
    this.trafficLights = [];
    this.parent = null;
};

ocargo.Node.prototype.addConnectedNode = function(node) {
	this.connectedNodes.push(node);
};

ocargo.Node.prototype.addConnectedNodeWithBacklink = function(node) {
	this.addConnectedNode(node);
	node.addConnectedNode(this);
};

ocargo.Node.prototype.removeDoublyConnectedNode = function(node) {
    var index = this.connectedNodes.indexOf(node);
    if (index > -1) {
        this.connectedNodes.splice(index, 1);
    }
    index = node.connectedNodes.indexOf(this);
    if (index > -1) {
        node.connectedNodes.splice(index, 1);
    }
};

ocargo.Node.prototype.addTrafficLight = function(trafficLight) {
	this.trafficLights.push(trafficLight);
};

ocargo.Node.parsePathData = function(nodeData) {
    var nodes = [];

    // Create nodes with coords
    for (var i = 0; i < nodeData.length; i++) {
        var coordinate = new ocargo.Coordinate(nodeData[i]['coordinate'][0], nodeData[i]['coordinate'][1]);
        nodes.push(new ocargo.Node(coordinate));
    }

    // Link nodes (must be done in second loop so that linked nodes have definitely been created)
    for (var i = 0; i < nodeData.length; i++) {
        var node = nodes[i];
        var connectedNodes = nodeData[i]['connectedNodes'];
        for (var j = 0; j < connectedNodes.length; j++) {
            node.addConnectedNode(nodes[connectedNodes[j]]);
        }
    }
    
    return nodes;
};

// Helper m ethod that returns a node matching the given coordinate
ocargo.Node.findNodeByCoordinate = function(coordinate, nodes) {
    for (var i = 0; i < nodes.length; i++) {
        var coord = nodes[i].coordinate;
        if (coord.x === coordinate[0] && coord.y === coordinate[1]) {
            return nodes[i];
        }
    }
    return null;
}


ocargo.calculateNodeAngle = function(nodeA, nodeB) {
    var coordinateA = nodeA.coordinate;
    var coordinateB = nodeB.coordinate;

    return Math.atan2(coordinateB.y - coordinateA.y, coordinateB.x - coordinateA.x);
};

ocargo.calculateClockwiseNodeAngle = function(nodeA, nodeB, nodeC) {
    var angleAB = ocargo.calculateNodeAngle(nodeA, nodeB);
    var angleBC = ocargo.calculateNodeAngle(nodeB, nodeC);
    var angle = (Math.PI + angleAB - angleBC) % (2 * Math.PI);
    return angle < 0 ? angle + 2 * Math.PI : angle;
};
