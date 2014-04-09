$(function() {
    'use strict';

    var points = [
        [0, 0],
        [1, 0],
        [1, 1],
        [1, 2],
        [2, 2],
        [3, 2],
        [3, 3],
        [3, 4],
        [4, 4],
        [5, 4],
        [5, 3],
        [5, 2],
        [6, 2],
        [7, 2],
        [8, 2],
        [9, 2]
    ];

    var previousNode = null;
    var nodes = [];
    for (var i = 0; i < points.length; i++) {
        var p = points[i];
        var coordinate = new Coordinate(p[0], p[1]);
        var node = new Node(coordinate);
        if (previousNode) {
            node.addConnectedNodeWithBacklink(previousNode);
        }
        previousNode = node;
        nodes.push(node);
    }

    var map = new Map();
    var van = new Van(nodes[0], nodes[1]);
    var level = new Level(map, van, nodes[nodes.length - 1]);

    var program = new Program(
            [TURN_LEFT,
                FORWARD,
                TURN_RIGHT,
                FORWARD,
                TURN_LEFT,
                FORWARD,
                TURN_RIGHT,
                FORWARD,
                TURN_RIGHT,
                FORWARD,
                TURN_LEFT,
                FORWARD,
                FORWARD,
                FORWARD
            ]);

    level.play(program);
});