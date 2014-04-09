'use strict';

function Node(coordinate) {
    this.coordinate = coordinate;
    this.connectedNodes = [];

    this.addConnectedNode = function(node) {
        this.connectedNodes.push(node);
    };

    this.addConnectedNodeWithBacklink = function(node) {
        this.addConnectedNode(node);
        node.addConnectedNode(this);
    };
}