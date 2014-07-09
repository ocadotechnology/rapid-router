'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(map) {
    this.nodes = map.nodes;
    this.destination = map.destination;
    this.optimalInstructions = [];
    this.optimalPath = null;
    this.maxDistanceScore = 100;
    this.maxInstrLengthScore = 100;
    this.maxScore = this.maxDistanceScore + this.maxInstrLengthScore;
};

ocargo.PathFinder.prototype.getOptimalInstructions = function() {

    ocargo.level.pathFinder.optimalInstructions = [];
    var sequentialInstructions = []
    for (var i = 1; i < ocargo.level.pathFinder.optimalPath.length - 1; i++) {
        var previousNode = ocargo.level.pathFinder.optimalPath[i - 1];
        var node = ocargo.level.pathFinder.optimalPath[i];
        var nextNode = ocargo.level.pathFinder.optimalPath[i + 1];
        var instr = ocargo.level.pathFinder.recogniseIndividualInstruction(
            previousNode.coordinate, node.coordinate, nextNode.coordinate);
        sequentialInstructions.push(instr);

    }
    ocargo.level.pathFinder.optimalInstructions = sequentialInstructions;

};

ocargo.PathFinder.prototype.getScore = function(stack) {

    var fuelScore = ocargo.PathFinder.prototype.getTravelledPathScore(stack);
    var instrLengthScore = ocargo.PathFinder.prototype.getInstrLengthScore(stack);

    console.debug("score: ", score, " out of ", ocargo.level.pathFinder.maxScore);

    return instrLengthScore + fuelScore;
};

ocargo.PathFinder.prototype.getTravelledPathScore = function(stack) {

    var travelled = ocargo.level.van.travelled;
    var travelledScore = Math.max(0, ocargo.level.pathFinder.maxDistanceScore -
        (travelled - (ocargo.level.pathFinder.optimalPath.length - 2)) * 10);
    
    console.debug("Travelled path score: ", travelledScore, " out of ",
            ocargo.level.pathFinder.maxDistanceScore);
    
    return travelledScore;
};

ocargo.PathFinder.prototype.getInstrLengthScore = function(stack) {

    var userSolutionLength = this.getLength(stack);
    var instrLengthScore = Math.max(0, ocargo.level.pathFinder.maxInstrLengthScore - (userSolutionLength - ocargo.level.pathFinder.optimalInstructions.length) * 10);
    
    console.debug("instr length score: ", instrLengthScore, " out of ", ocargo.level.pathFinder.maxInstrLengthScore);

    return instrLengthScore;
};

ocargo.PathFinder.prototype.getOptimalPath = function() {
    this.optimalPath = aStar(this.nodes, this.destination);
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

function aStar(nodes, destination) {

    var end = destination;          // Nodes already visited.
    var current;
    var start = nodes[0]
    var closedSet = [];             // The neightbours yet to be evaluated.
    var openSet = [start];          // All 3 lists are indexed the same way original nodes are.
    var costFromStart = [0];        // Costs from the starting point.
    var reversePriority = [0];      // The lower the value, the higher priority of the node.
    var heuristics = [0]            // Stores results of heuristic().
    var currentIndex = 0;
    var neighbourIndex = 0;

    initialiseParents(nodes);

    while (openSet.length > 0) {

        var smallestInOpen = 0;
        var smallestInReverse = 0;
        for (var i = 0; i < openSet.lenght; i++) {
            if (reversePriority[nodes.indexOf(openSet[i])] < reversePriority[smallestInReverse]) {
                smallestInOpen = i;
                smallestInReverse = nodes.indexOf(openSet[i]); 
            }
        }
        current = openSet[smallestInOpen];
        currentIndex = nodes.indexOf(current);

        // End case.
        if (current === end) {
            return getNodeList(current);
        }
        openSet.splice(smallestInOpen, 1);
        closedSet.push(current);
        var neighbour;
        for (var i = 0; i < current.connectedNodes.length; i++) {
            neighbour = current.connectedNodes[i];
            neighbourIndex = nodes.indexOf(neighbour);
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

    function initialiseParents(nodes) {

        for(var i = 0; i < nodes.length; i++) {
            nodes[i].parent = null;
        }
    }

    function getNodeList(current) {

        var curr = current;
        var ret = [];
        while (curr !== start && curr !== null) {
            ret.push(curr);
            curr = curr.parent;
        }
        ret.push(start);
        ret.reverse();
        return ret;
    }
}
