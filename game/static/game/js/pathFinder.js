'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(model) {
    this.van = model.van;
    this.nodes = model.map.nodes;
    this.destination = model.map.destination;
    this.optimalPath = this.getOptimalPath();
    this.maxDistanceScore = 10;
    this.maxInstrLengthScore = 10;
    this.maxScore = this.maxDistanceScore + this.maxInstrLengthScore;
    this.modelLength = MODEL_SOLUTION;
};

ocargo.PathFinder.prototype.getScore = function() {

    var pathLengthScore = this.getTravelledPathScore();
    var initInstrScore = this.getInstrLengthScore();
    var instrScore = initInstrScore <= this.maxInstrLengthScore ? initInstrScore :
        this.maxInstrLengthScore - initInstrScore % this.maxInstrLengthScore;

    var totalScore = pathLengthScore + instrScore;

    var message = ocargo.messages.totalScore(totalScore, this.maxScore) +
                "<br>" + ocargo.messages.pathScore(pathLengthScore, this.maxDistanceScore) +
                "<br>" + ocargo.messages.algorithmScore(instrScore, this.maxInstrLengthScore);

    if (initInstrScore > this.maxInstrLengthScore) {
        message += "<br><br>" + ocargo.messages.algorithmShorter;
    }
    if (initInstrScore < this.maxInstrLengthScore) {
        message += "<br><br>" + ocargo.messages.algorithmLonger;
    }
    if (pathLengthScore < this.maxDistanceScore) {
        message += "<br><br>" + ocargo.messages.pathLonger;
    }
    if (totalScore === this.maxScore) {
        message += "<br><br>" + ocargo.messages.scorePerfect;
    }
    return [totalScore, message];
};

ocargo.PathFinder.prototype.getTravelledPathScore = function() {
    var travelled = this.van.travelled;
    var travelledScore = this.maxDistanceScore -
        (travelled - this.optimalPath.length + 2);
    
    return travelledScore;
};

ocargo.PathFinder.prototype.getInstrLengthScore = function() {
    var userLength = ocargo.blocklyControl.getBlocksCount();
    var algorithmScore = this.maxInstrLengthScore - (userLength - 1 - this.modelLength);

    return algorithmScore;
};

ocargo.PathFinder.prototype.getOptimalPath = function() {
    return aStar(this.nodes, this.destination);
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
