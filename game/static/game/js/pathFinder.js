'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(map) {
    this.nodes = map.nodes;
    this.destination = map.destination;
    this.optimalInstructions = [];
    this.optimalPath = null;
    this.max = 0;
};

ocargo.PathFinder.prototype.getOptimalInstructions = function() {

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

    var userSolutionLength = this.getLength(stack);
    var instrLengthScore = 100;
    var fuelScore = 100;
    var usedFuel = ocargo.level.van.maxFuel - ocargo.level.van.fuel;
    console.debug(ocargo.level.van.maxFuel, ocargo.level.van.fuel, usedFuel, this.optimalPath.length - 2);
    this.max = instrLengthScore + fuelScore;
    instrLengthScore = Math.min(100, Math.max(
        0, instrLengthScore - (userSolutionLength - this.optimalInstructions.length) * 10));
    fuelScore = Math.max(0, fuelScore - (usedFuel - (this.optimalPath.length - 2)) * 10);
    return instrLengthScore + fuelScore;
};

ocargo.PathFinder.prototype.getOptimalPath = function() {
    ocargo.level.pathFinder.optimalPath = this.aStar();
};

ocargo.PathFinder.prototype.aStar = function() {

    var end = this.destination;     // Nodes already visited.
    var current;
    var start = this.nodes[0]
    var closedSet = [];             // The neightbours yet to be evaluated.
    var openSet = [start];          // All 3 lists are indexed the same way original nodes are.
    var costFromStart = [0];        // Costs from the starting point.
    var reversePriority = [0];      // The lower the value, the higher priority of the node.
    var heuristics = [0]            // Stores results of heuristic().
    var currentIndex = 0;
    var neighbourIndex = 0;

    initialiseParents();

    while (openSet.length > 0) {
        current = openSet[openSet.length-1];
        currentIndex = this.nodes.indexOf(current);

        // End case.
        if (current === end) {
            return getNodeList(current);
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

            var gScore = costFromStart[currentIndex] + 1;
            var gScoreIsBest = false;

            if (openSet.indexOf(current) === -1) {
                gScoreIsBest = true;
                heuristics[neighbourIndex] = heuristic(neighbour, end);
                openSet.push(neighbour);
            } else if (gScore < costFromStart[neighbourIndex]) {
                gScoreIsBest = true;
            }

            if (gScoreIsBest) {
                neighbour.parent = current;
                costFromStart[neighbourIndex] = gScore;
                reversePriority[neighbourIndex] =
                    costFromStart[neighbourIndex] + heuristics[neighbourIndex];
            }
        }
    }
    return [];

    function heuristic(node1, node2) {

        var d1 = Math.abs(node2.coordinate.x - node1.coordinate.x);
        var d2 = Math.abs(node2.coordinate.y - node1.coordinate.y);
        return d1 + d2;
    }

    function initialiseParents() {

        for(var i = 0; i < ocargo.level.pathFinder.nodes.length; i++) {
            ocargo.level.pathFinder.nodes[i].parent = null;
        }
    }

    function getNodeList(current) {

        var curr = current;
        var ret = [];
        while(curr !== start && curr !== null) {
            ret.push(curr);
            curr = curr.parent;
        }
        ret.push(start);
        ret.reverse();
        return ret;
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
