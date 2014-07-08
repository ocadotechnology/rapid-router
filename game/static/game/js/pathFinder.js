'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(map) {
    this.nodes = map.nodes;
    this.destination = map.destination;
    this.optimalInstructions = [];
    this.optimalPath = null;
    this.maxFuelScore = 100;
		this.maxInstrLengthScore = 100;
		this.maxScore = this.maxFuelScore + this.maxInstrLengthScore;
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
    // [[[instructions], startIndex]],
    var suffixArray = buildSuffixArray(sequentialInstructions);
    // [[startIndex, endIndex, loopBody]]
    //var loopDic = getLoops(suffixArray);
    ocargo.level.pathFinder.optimalInstructions = sequentialInstructions;

    function getLoops(suffixArray) {
        var loopDic = [];
        var index = 0;
        var loopBlock = null;
        var previous = null;
        var prevIndex;
        var currentInstr, currentIndex;
        var count = 0;
        var start = -1;
        var currLen, prevLen, loopLen;
        var ascending, descending, indexNotCovered;

        while (index < suffixArray.length) {
            currentInstr = suffixArray[index][0];
            currentIndex = suffixArray[index][1];

            if (previous !== null) {

                prevLen = previous.length;
                currLen = currentInstr.length;
                loopLen = loopBlock.length;

                ascending = compare(currentInstr, currLen - prevLen, currLen, previous, 0, prevLen);
                descending = compare(previous, prevLen - currLen, prevLen, currentInstr, 0, currLen);
                indexNotCovered = checkIndex(currentIndex, loopDic);

                if (loopBlock !== null) {
                    // If we were inversigating a loop and it is not continued on current line.
                    if (count > 1 && (indexNotCovered && 
                        !((ascending && compare(currentInstr, 0, loopLen, loopBlock, 0, loopLen) &&
                            (prevLen + loopLen === currLen))) ||
                          (descending && compare(previous, 0, loopLen, loopBlock, 0, loopLen) &&
                            (currLen + loopLen === prevLen)))) {
                        
                        count++;
                        loopDic.push([start, start + count * loopLen - 1, loopBlock]);
                        loopBlock = currentInstr;
                        count = 0;
                        start = currentIndex;
                    } 
                    // If current still classifies as the ongoing loop and was not rolled in before.
                    if (indexNotCovered && ascending &&
                        compare(currentInstr, 0, loopLen, loopBlock, 0, loopLen)) {
                        
                        start = currentIndex;
                        // Loop ends with the program end.
                        if (index === suffixArray.length - 1 && count > 0) {
                            count++;
                            loopDic.push([start, start + count * loopLen - 1, loopBlock]);
                            count = 1;
                        } else {
                            loopBlock = currentInstr.slice(0, currLen - prevLen);
                            count++;
                        }

                    } else if (indexNotCovered && descending &&
                        compare(previous, 0, loopLen, loopBlock, 0, loopLen)) {
                        
                        // Loop ends with the program end.
                        if (index === suffixArray.length - 1 && count > 0) {
                            count++;
                            loopDic.push([start, start + count * loopLen - 1, loopBlock]);
                            count = 1;
                        } else {
                            loopBlock = previous.slice(0, prevLen - currLen);
                            count++;
                        }
                    }
                }
            } else {
                loopBlock = currentInstr;
                count = 1;
            }
            previous = currentInstr;
            index++;
        }
        return loopDic;
    }

    // Check if you have to cover this part of the loop.
    function checkIndex(index, dictionary) {
        for (var i = 0; i < dictionary.length; i++) {
            if (dictionary[i][0] <= index && index <= dictionary[i][1]) {
                return false;
            }
        }
        return true;
    }

    // Checks if two arrays slices defined by start and end indices are identical.
    function compare(arr1, start1, end1, arr2, start2, end2) {
        if(end1 - start1 !== end2 - start2) {
            return false;
        }
        for(var i = 0; i < end1 - start1; i++) {
            if(arr1[start1 + i] !== arr2[start2 + i]) {
                return false;
            }
        }
        return true;
    }

    function buildSuffixArray(instructions) {
        var suffixArray = [];
        for (var i = 0; i < instructions.length; i++) {
            suffixArray.push([instructions.slice(i, instructions.length), i]);
        }
        suffixArray.sort();
        return suffixArray;
    }
};

ocargo.PathFinder.prototype.getScore = function(stack) {

    var fuelScore = ocargo.PathFinder.prototype.getFuelScore(stack);
		var instrLengthScore = ocargo.PathFinder.prototype.getInstrLengthScore(stack);

    return instrLengthScore + fuelScore;
};

ocargo.PathFinder.prototype.getFuelScore = function(stack) {

    var usedFuel = ocargo.level.van.maxFuel - ocargo.level.van.fuel;
    var fuelScore = Math.max(0, ocargo.level.pathFinder.maxFuelScore - (usedFuel - (ocargo.level.pathFinder.optimalPath.length - 2)) * 10);
    
		return fuelScore;
};

ocargo.PathFinder.prototype.getInstrLengthScore = function(stack) {

    var userSolutionLength = this.getLength(stack);
    var instrLengthScore = Math.max(0, ocargo.level.pathFinder.maxInstrLengthScore - (userSolutionLength - ocargo.level.pathFinder.optimalInstructions.length) * 10);
    
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
