'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(model) {
    this.van = model.van;
    this.nodes = model.map.nodes;
    this.destinations = model.map.destinations;
    this.maxDistanceScore = 10;
    this.maxInstrLengthScore = 10;
    this.maxScore = this.maxDistanceScore + this.maxInstrLengthScore;
    this.modelLength = MODEL_SOLUTION;

    this.optimalPath = getOptimalPath(this.nodes, this.destinations);
};

ocargo.PathFinder.prototype.getScore = function() {

    var pathLengthScore = this.getTravelledPathScore();
    var initInstrScore = this.getInstrLengthScore();
    var instrScore = initInstrScore;

    if (initInstrScore >= 2 * this.maxInstrLengthScore) {
        instrScore = 0;
    } else if (initInstrScore > this.maxInstrLengthScore) {
        instrScore = this.maxInstrLengthScore - initInstrScore % this.maxInstrLengthScore;
    }

    var totalScore = pathLengthScore + instrScore;

    var message = ocargo.messages.pathScore + 
                    this.renderCoins(pathLengthScore, this.maxDistanceScore) + "<br>" +
                    ocargo.messages.algorithmScore + 
                    this.renderCoins(instrScore, this.maxInstrLengthScore) + "<br>" +
                    ocargo.messages.totalScore(totalScore, this.maxScore);


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


// Renders the gained score in coins.
ocargo.PathFinder.prototype.renderCoins = function(score, maxScore) {
    var coins = "<div>";
    var i;
    for (i = 0; i < Math.floor(score); i++) {
        coins += "<img src='/static/game/image/coins/coin_gold.svg' width='50'>";
    }
    if (score - Math.floor(score) > 0) {
        coins += "<img src='/static/game/image/coins/coin_5050_transparent.svg' width='50'>";
    }
    for (i = Math.ceil(score); i < maxScore; i++) {
        coins += "<img src='/static/game/image/coins/coin_empty_transparent.svg' width='50'>";
    }
    coins += "      " + score + "/" + maxScore;
    coins += "</div>";

    return coins;
};

ocargo.PathFinder.prototype.getTravelledPathScore = function() {
    var travelled = this.van.travelled;
    var travelledScore = this.maxDistanceScore -
        (travelled - this.optimalPath.length + 2);
    
    return travelledScore;
};

ocargo.PathFinder.prototype.getInstrLengthScore = function() {
    var userLength = ocargo.blocklyControl.getActiveBlocksCount();
    console.log(userLength);
    var algorithmScore = 0;
    var difference = this.maxInstrLengthScore;
    for (var i = 0; i < this.modelLength.length; i++) {
        var currDifference = userLength - this.modelLength[i];
        if (Math.abs(currDifference) < difference) {
            difference = Math.abs(currDifference);
            algorithmScore = this.maxInstrLengthScore - currDifference;
        }
    }
    return algorithmScore;
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



function getOptimalPath(nodes, destinations) {
    // Brute force Travelling Salesman implementation, using A* to determinee the connection lengths
    // If the map size increases or lots of destinations are required, it may need to be rethought
    var hash = {};
    function getPathBetweenNodes(node1, node2) {
        var key = '(' + node1.coordinate.x + ',' + node1.coordinate.y + '),(' + node2.coordinate.x +
                    ',' + node2.coordinate.y + ')';
        var solution;
        if (key in hash) {
            solution = hash[key];
        }
        else {
            solution = aStar(node1, node2, nodes);
            hash[key] = solution;
        }
        return solution;
    }

    function getPermutationPath(start, permutation) {
        var fragPath = [getPathBetweenNodes(start, permutation[0], nodes)];
        for (var i = 1; i < permutation.length; i++) {
            fragPath.push(getPathBetweenNodes(permutation[i-1], permutation[i], nodes));
        }

        var fullPath = [start];
        for (var i = 0; i < fragPath.length; i++) {
            if (!fragPath[i]) {
                return null;
            } 
            else {
                fullPath = fullPath.concat(fragPath[i].slice(1));
            }
        }
        return fullPath;
    }

    var permutations = [];
    function permute(array, data) 
    {
        var current;
        var currentPermutation = data || [];

        for (var i = 0; i < array.length; i++) 
        {
            // Take node out
            current = array.splice(i, 1)[0];
            // Then the current permutation is complete so add it
            if (array.length === 0) {
                permutations.push(currentPermutation.concat([current]));
            }
            //Recurse over the remaining array
            permute(array.slice(), currentPermutation.concat([current]));
            // Add node back in
            array.splice(i, 0, current);
        }
    }
    
    var start = nodes[0];
    var bestScore = Number.POSITIVE_INFINITY;
    var bestPermutationPath = null;
    var destinationNodes = [];

    for (var i = 0; i < destinations.length; i++) {
        destinationNodes.push(destinations[i].node);
    }
    permute(destinationNodes);
    
    for (var i = 0; i < permutations.length; i++) {
        var permutation = permutations[i];
        var permutationPath = getPermutationPath(start, permutation, nodes);

        if (permutationPath && permutationPath.length < bestScore) {
            bestScore = permutationPath.length;
            bestPermutationPath = permutationPath;
        }
    }

    return bestPermutationPath;
}

function aStar(origin, destination, nodes) {

    var end = destination;          // Nodes already visited.
    var current;
    var start = origin;
    var closedSet = [];             // The neightbours yet to be evaluated.
    var openSet = [start];          // All 3 lists are indexed the same way original nodes are.
    var costFromStart = [0];        // Costs from the starting point.
    var reversePriority = [0];      // The lower the value, the higher priority of the node.
    var heuristics = [0];            // Stores results of heuristic().
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
    // Failed to find a path
    return null;

    function heuristic(node1, node2) {

        var d1 = Math.abs(node2.coordinate.x - node1.coordinate.x);
        var d2 = Math.abs(node2.coordinate.y - node1.coordinate.y);
        return d1 + d2;
    }

    function initialiseParents(nodes) {

        for (var i = 0; i < nodes.length; i++) {
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
