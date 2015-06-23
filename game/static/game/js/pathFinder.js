'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(model) {
    this.van = model.van;
    this.nodes = model.map.nodes;
    this.destinations = model.map.destinations;
    
    this.pathScoreDisabled = DISABLE_ROUTE_SCORE;
    this.modelSolution = MODEL_SOLUTION;

    this.maxScoreForPathLength = 10;
    this.maxScoreForNumberOfInstructions = 10;

    this.maxScore = this.maxScoreForPathLength + this.maxScoreForNumberOfInstructions;
    
    this.optimalPath = getOptimalPath(this.nodes, this.destinations);
};

ocargo.PathFinder.prototype.getScore = function() {
    var message = "";
    var button = "";

    var pathLengthScore = 0;
    if(!this.pathScoreDisabled){
        pathLengthScore = Math.max(0, this.getTravelledPathScore());
        message = ocargo.messages.pathScore + this.renderCoins(pathLengthScore, this.maxScoreForPathLength);
    }

    var totalScore = pathLengthScore;

    if (this.modelSolution.length > 0) {
        // Then we're on a default level
        var initInstrScore = this.getScoreForNumberOfInstructions();
        var instrScore = Math.max(0, initInstrScore);

        if (initInstrScore >= 2 * this.maxScoreForNumberOfInstructions) {
            instrScore = 0;
        } else if (initInstrScore > this.maxScoreForNumberOfInstructions) {
            instrScore = this.maxScoreForNumberOfInstructions - initInstrScore % this.maxScoreForNumberOfInstructions;
        }
        instrScore = Math.max(0, instrScore);

        message +=  ocargo.messages.algorithmScore +
                    this.renderCoins(instrScore, this.maxScoreForNumberOfInstructions) + "<br>";
        totalScore += instrScore;
    }


    message += ocargo.messages.totalScore(totalScore, this.maxScore);

    if (pathLengthScore < this.maxScoreForPathLength) {
        message += "<br>" + ocargo.messages.pathLonger;
        button += ocargo.button.getTryAgainButtonHtml();
    }
    else if (initInstrScore > this.maxScoreForNumberOfInstructions) {
        message += "<br>" + ocargo.messages.algorithmShorter;
        button += ocargo.button.getTryAgainButtonHtml();
    }
    else if (initInstrScore < this.maxScoreForNumberOfInstructions) {
        message += "<br>" + ocargo.messages.algorithmLonger;
        button += ocargo.button.getTryAgainButtonHtml();
    }
    else  if (totalScore === this.maxScore) {
        message += "<br>" + ocargo.messages.scorePerfect;
    }

    return [totalScore, message, button];
};


// Renders the gained score in coins.
ocargo.PathFinder.prototype.renderCoins = function(score, maxScore) {
    var coins = "<div>";
    var i;
    for (i = 0; i < Math.floor(score); i++) {
        coins += "<img src='" + ocargo.Drawing.imageDir + "coins/coin_gold.svg' width='50'>";
    }
    if (score - Math.floor(score) > 0) {
        coins += "<img src='" + ocargo.Drawing.imageDir + "coins/coin_5050_dots.svg' width='50'>";
    }
    for (i = Math.ceil(score); i < maxScore; i++) {
        coins += "<img src='" + ocargo.Drawing.imageDir + "coins/coin_empty_dots.svg' width='50'>";
    }
    coins += "      " + score + "/" + maxScore;
    coins += "</div>";

    return coins;
};

ocargo.PathFinder.prototype.getTravelledPathScore = function() {
    var travelled = this.van.travelled;
    return this.maxScoreForPathLength - (travelled - this.optimalPath.length + 2);
};

ocargo.PathFinder.prototype.getScoreForNumberOfInstructions = function() {
    var blocksUsed = ocargo.blocklyControl.getActiveBlocksCount();
    var algorithmScore = 0;
    var difference = this.maxScoreForNumberOfInstructions;
    for (var i = 0; i < this.modelSolution.length; i++) {
        var currDifference = blocksUsed - this.modelSolution[i];
        if (Math.abs(currDifference) < difference) {
            difference = Math.abs(currDifference);
            algorithmScore = this.maxScoreForNumberOfInstructions - currDifference;
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
    // Brute force Travelling Salesman implementation, using A* to determine the connection lengths
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
    function permute(array, data) {
        var current;
        var currentPermutation = data || [];

        for (var i = 0; i < array.length; i++) {
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
