'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(map) {
    this.nodes = map.nodes;
    this.destination = map.destination;
    this.optimalInstructions = [];
    this.optimalPath = null;
};

ocargo.PathFinder.prototype.getOptimalInstructions = function() {
    console.debug("Optimal path length", ocargo.level.pathFinder.optimalPath.length);
    ocargo.level.pathFinder.optimalInstructions = [];
    for (var i = 1; i < ocargo.level.pathFinder.optimalPath.length - 1; i++) {
        var previousNode = ocargo.level.pathFinder.optimalPath[i - 1];
        var node = ocargo.level.pathFinder.optimalPath[i];
        var nextNode = ocargo.level.pathFinder.optimalPath[i + 1];
        var instr = ocargo.level.pathFinder.recogniseIndividualInstruction(
            previousNode.coordinate, node.coordinate, nextNode.coordinate);
        ocargo.level.pathFinder.optimalInstructions.push(instr);
        console.debug(instr);
    }
};

ocargo.PathFinder.prototype.getScore = function(stack) {
    console.debug("Instructions: ", stack);
    var userSolutionLength = this.getLength(stack);
    console.debug("User instruction length ", userSolutionLength);
    var instrLengthScore = 100;
    var pathLenScore = 100;
    instrLengthScore = Math.min(100, Math.max(
        0, instrLengthScore - (userSolutionLength - this.optimalInstructions.length) * 10));
    console.debug("Instruction length score " + instrLengthScore + " = ");
    return instrLengthScore + pathLenScore;
};

ocargo.PathFinder.prototype.getOptimalPath = function() {
    ocargo.level.pathFinder.optimalPath = this.aStar();
};

ocargo.PathFinder.prototype.aStar = function() {
    var end = this.destination;     // Nodes already visited.
    var current;
    var start = this.nodes[0]
    var closedSet = [];                                 // The neightbours yet to be evaluated.
    var openSet = [start];
    start.parent = null;
    var came_from = [];                                 // The map of navigated nodes.
    var g_score = [0];
    var f_score = [0];
    var h_score = [0]
    var currentIndex = 0;
    var neighbourIndex = 0;

    while (openSet.length > 0) {
        current = openSet[openSet.length-1];
        currentIndex = this.nodes.indexOf(current);
        // End case.
        if (current === end) {
            var curr = current;
            var ret = [];
            while(curr !== start && curr !== null) {
                ret.push(curr);
                curr = curr.parent;
            }
            for(var i = 0; i < this.nodes.length; i++) {
            }
            ret.push(start);
            ret.reverse();
            for(var a = 0; a < ret.length; a++) {
                console.debug("Path", a, ret[a].coordinate);
            }
            return ret;
        }
        openSet.pop();
        closedSet.push(current);
        var neighbour;
        for (var i = 0; i < current.connectedNodes.length; i++) {
            neighbour = current.connectedNodes[i];
            neighbourIndex = this.nodes.indexOf(neighbour);
            if (closedSet.indexOf(neighbour) > 0) {
                continue;
            }

            var gScore = g_score[currentIndex] + 1;
            var gScoreIsBest = false;

            if (openSet.indexOf(current) === -1) {
                gScoreIsBest = true;
                h_score[neighbourIndex] = heuristic(neighbour, end);
                openSet.push(neighbour);
            } else if (gScore < g_score[neighbourIndex]) {
                gScoreIsBest = true;
            }

            if (gScoreIsBest) {
                console.debug(current.coordinate," <-> ", neighbour.coordinate);
                neighbour.parent = current;
                g_score[neighbourIndex] = gScore;
                f_score[neighbourIndex] = g_score[neighbourIndex] + h_score[neighbourIndex];
            }
        }
    }
    return [];

    function heuristic(node1, node2) {
        var d1 = Math.abs(node2.coordinate.x - node1.coordinate.x);
        var d2 = Math.abs(node2.coordinate.y - node1.coordinate.y);
        return d1 + d2;
    }
};

ocargo.PathFinder.prototype.getLength = function(stack) {
    var total = 0;
    var i;
    if (!stack) {
        return total;
    }
    for (i = 0; i < stack.length; i++) {
        if (stack[i].command === "While") {
            total += this.getLength(stack[i].block);
        }
        else if (stack[i].command === 'If') {
            total += this.getLength(stack[i].ifBlock);
            total += this.getLength(stack[i].elseBlock);
        }
        total++;
    }
    return total;
};

ocargo.PathFinder.prototype.recogniseIndividualInstruction = function(previous, point1, point2) {
    if (isHorizontal(point1, point2) &&
        (previous === null || isHorizontal(previous, point1))) {
        return 'Forward';

    } else if (isVertical(point1, point2) &&
        (previous === null || isVertical(previous, point1))) {
        return 'Forward';
    }
    if (isProgressive(previous.x, point1.x)) {
        return nextPointAbove(point1, point2) ? 'Left' : 'Right';
    }
    if (isProgressive(point1.x, previous.x)) {
        return nextPointAbove(point1, point2) ? 'Right' : 'Left';
    }
    if (isProgressive(previous.y, point1.y)) {
        return nextPointFurther(point1, point2) ? 'Right' : 'Left';
    }
    if (isProgressive(point1.y, previous.y)) {
        return nextPointFurther(point1, point2) ? 'Left' : 'Right';
    }
};
