$(function() {
    'use strict';

    var origin = new Coordinate(0, 0);
    var vanStart = new Coordinate(1, 0);
    var destination = new Coordinate(1, 1);

    var originNode = new Node(origin);
    var vanStartNode = new Node(vanStart);
    var destinationNode = new Node(destination);

    originNode.addConnectedNodeWithBacklink(vanStartNode);
    vanStartNode.addConnectedNodeWithBacklink(destinationNode);

    var map = new Map();
    var van = new Van(originNode, vanStartNode);
    var level = new Level(map, van, destinationNode);

    var program = new Program([TURN_LEFT]);

    level.play(program);
});