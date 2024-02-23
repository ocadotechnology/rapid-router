'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(model) {
    this.van = model.van;
    this.nodes = model.map.nodes;
    this.destinations = model.map.destinations;

    this.pathScoreDisabled = DISABLE_ROUTE_SCORE;
    this.algorithmScoreDisabled = DISABLE_ALGORITHM_SCORE;
    this.modelSolution = MODEL_SOLUTION;

    const tooSimpleToGetAlgorithmScore = (LEVEL_ID < 13);

    if (!this.pathScoreDisabled) {
        if (tooSimpleToGetAlgorithmScore) {
            this.maxScoreForPathLength = 20;
        } else {
            this.maxScoreForPathLength = 10;
        }
    } else {
        this.maxScoreForPathLength = 0;
    }

    this.maxScoreForNumberOfInstructions = 0;

    if (!this.algorithmScoreDisabled) {
        this.maxScoreForNumberOfInstructions = 10;
    }

    this.maxScore = this.maxScoreForPathLength + this.maxScoreForNumberOfInstructions;
    this.optimalPath = getOptimalPath(this.nodes, this.destinations);
};

ocargo.PathFinder.prototype.getScore = function() {
    let routeCoins = {};
    let instrCoins = {};
    let performance= "";

    let pathLengthScore = 0;
    if (!this.pathScoreDisabled) {
        pathLengthScore = Math.max(0, this.getTravelledPathScore());
        routeCoins = this.getNumCoins(pathLengthScore, this.maxScoreForPathLength);
    }

    let totalScore = pathLengthScore;

    if (!this.algorithmScoreDisabled) {
        var initInstrScore = this.getScoreForNumberOfInstructions();
        var instrScore = Math.max(0, initInstrScore);

        if (initInstrScore >= 2 * this.maxScoreForNumberOfInstructions) {
            instrScore = 0;
        } else if (initInstrScore > this.maxScoreForNumberOfInstructions) {
            instrScore = this.maxScoreForNumberOfInstructions - initInstrScore % this.maxScoreForNumberOfInstructions;
        }
        instrScore = Math.max(0, instrScore);

        totalScore += instrScore;
        instrCoins = this.getNumCoins(instrScore, this.maxScoreForNumberOfInstructions);
    }

    if (pathLengthScore < this.maxScoreForPathLength) {
        performance = "pathLonger";
    }
    else if (initInstrScore > this.maxScoreForNumberOfInstructions) {
        performance = "algorithmShorter";
    }
    else if (initInstrScore < this.maxScoreForNumberOfInstructions) {
        performance = "algorithmLonger";
    }
    else if (totalScore === this.maxScore) {
        performance = "scorePerfect";
    }

    const endLevelMsg = function(performance) {
        switch (performance){
            case 'pathLonger':
                return gettext('Try finding a shorter route to the destination.');
            case 'algorithmLonger':
                return gettext('Try creating a simpler program.');
            case 'algorithmShorter':
                return gettext('That solution isn\'t quite right. Read the level instructions or click Help.');
            case 'scorePerfect':
                return gettext('Congratulations! You\'ve aced it.');
            default:
                return '';
        }
    };

    return {totalScore: totalScore,
            routeCoins: routeCoins,
            instrCoins: instrCoins,
            maxScore: this.maxScore,
            performance: performance,
            pathLengthScore: pathLengthScore,
            pathScoreDisabled: this.pathScoreDisabled,
            algorithmScoreDisabled: this.algorithmScoreDisabled,
            maxScoreForPathLength: this.maxScoreForPathLength,
            instrScore: instrScore,
            maxScoreForNumberOfInstructions: this.maxScoreForNumberOfInstructions,
            popupMessage: endLevelMsg(performance)};
};

/* Return number of coins for each type*/
ocargo.PathFinder.prototype.getNumCoins = function(score, maxScore) {
    return {whole: Math.floor(score), half: score - Math.floor(score) > 0 ? 1 : 0, zero: maxScore - Math.ceil(score)};
};

ocargo.PathFinder.prototype.getTravelledPathScore = function() {
    const travelled = this.van.getDistanceTravelled();
    const START_AND_END_BLOCKS = 2;
    return this.maxScoreForPathLength - (travelled + START_AND_END_BLOCKS - this.optimalPath.length);
};

ocargo.PathFinder.prototype.getScoreForNumberOfInstructions = function() {
    const blocksUsed = ocargo.utils.isIOSMode() ? ocargo.game.mobileBlocks : ocargo.blocklyControl.activeBlocksCount();
    let algorithmScore = 0;
    let difference = this.maxScoreForNumberOfInstructions;
    for (let i = 0; i < this.modelSolution.length; i++) {
        let currDifference = blocksUsed - this.modelSolution[i];
        if (Math.abs(currDifference) < difference) {
            difference = Math.abs(currDifference);
            algorithmScore = this.maxScoreForNumberOfInstructions - currDifference;
        }
    }
    return algorithmScore;
};

ocargo.PathFinder.prototype.getLength = function(stack) {
    let total = 0;
    if (!stack) {
        return total;
    }
    for (let i = 0; i < stack.length; i++) {
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
    let hash = {};
    function getPathBetweenNodes(node1, node2) {
        const key = '(' + node1.coordinate.x + ',' + node1.coordinate.y + '),(' + node2.coordinate.x +
                    ',' + node2.coordinate.y + ')';
        let solution;
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
        let fragPath = [getPathBetweenNodes(start, permutation[0], nodes)];
        for (let i = 1; i < permutation.length; i++) {
            fragPath.push(getPathBetweenNodes(permutation[i-1], permutation[i], nodes));
        }

        let fullPath = [start];
        for (let i = 0; i < fragPath.length; i++) {
            if (!fragPath[i]) {
                return null;
            }
            else {
                fullPath = fullPath.concat(fragPath[i].slice(1));
            }
        }
        return fullPath;
    }

    let permutations = [];
    function permute(array, data) {
        let current;
        let currentPermutation = data || [];

        for (let i = 0; i < array.length; i++) {
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

    let start = nodes[0];
    let bestScore = Number.POSITIVE_INFINITY;
    let bestPermutationPath = null;
    let destinationNodes = [];

    for (let i = 0; i < destinations.length; i++) {
        destinationNodes.push(destinations[i].node);
    }
    permute(destinationNodes);

    for (let i = 0; i < permutations.length; i++) {
        let permutation = permutations[i];
        const permutationPath = getPermutationPath(start, permutation, nodes);

        if (permutationPath && permutationPath.length < bestScore) {
            bestScore = permutationPath.length;
            bestPermutationPath = permutationPath;
        }
    }
    return bestPermutationPath;
}

function QueueLink(node, score) {
  this.node = node;
  this.score = score;
  this.next = null;
}

function PriorityQueue() {
  this.push = function(node, score) {
    if (this.head == null) {
      this.head = new QueueLink(node, score);
    } else if (this.head.score > score) {
      let tmp = this.head;
      this.head = new QueueLink(node, score);
      this.head.next = tmp;
    } else {
      let i = this.head;
      let found = false;
      while (i.next != null && !found) {
        if (i.next.score > score) {
          let tmp = i.next;
          i.next = new QueueLink(node, score);
          i.next.next = tmp;
          found = true;
        }
        i = i.next;
      }
      if (!found) {
        i.next = new QueueLink(node, score);
      }
    }
  };

  this.pop = function() {
    if (this.head == null) {
      return null;
    } else {
      const result = this.head.node;
      this.head = this.head.next;
      return result;
    }
  };

  this.isEmpty = function () {
    return this.head == null;
  }
}

function aStar(origin, destination, nodes) {
    const end = destination;          // Nodes already visited.
    let current;
    const start = origin;
    let closedSet = {};             // The neighbours yet to be evaluated.
    let openSet = new PriorityQueue();
    openSet.push(start, 0);

    initialiseParents(nodes);
    closedSet[start.id] = true;

    while (!openSet.isEmpty()) {
        current = openSet.pop();

        // End case.
        if (current === end) {
            return getNodeList(current);
        }
        for (let i = 0; i < current.connectedNodes.length; i++) {
            let neighbour = current.connectedNodes[i];
            if (Object.prototype.hasOwnProperty.call(closedSet, neighbour.id)) {
                continue;
            }
            closedSet[neighbour.id] = true;
            neighbour.parent = current;
            const score = distanceFromStart(neighbour) + heuristic(destination, neighbour);
            openSet.push(neighbour, score);
        }
    }
    // Failed to find a path
    return null;

    function heuristic(node1, node2) {
        const d1 = Math.abs(node2.coordinate.x - node1.coordinate.x);
        const d2 = Math.abs(node2.coordinate.y - node1.coordinate.y);
        return d1 + d2;
    }

    function initialiseParents(nodes) {
        for (let i = 0; i < nodes.length; i++) {
            nodes[i].parent = null;
            nodes[i].id = i;
        }
    }

    function distanceFromStart(current) {
      let count = 0;
      let i = current;
      while (i.parent != null) {
        count = count + 1;
        i = i.parent;
      }
      return count;
    }

    function getNodeList(current) {
        let curr = current;
        let ret = [];
        while (curr !== start && curr !== null) {
            ret.push(curr);
            curr = curr.parent;
        }
        ret.push(start);
        ret.reverse();
        return ret;
    }
}

function areDestinationsReachable(start, destinations, nodes) {
  for (let i = 0; i < destinations.length; i++) {
    if (aStar(start, destinations[i], nodes) == null) {
      return false;
    }
  }
  return true;
}
