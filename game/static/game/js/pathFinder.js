'use strict';

var ocargo = ocargo || {};

ocargo.PathFinder = function(map) {
	this.nodes = map.nodes;
	this.destination = map.destination;
	this.optimalInstructions = [];
	this.optimalPath = null;
};

ocargo.PathFinder.prototype.getOptimalInstructions = function() {
// TODO: actually develop an algotirhm that finds the shortest path.
	ocargo.level.pathFinder.optimalInstructions = [];
	console.debug("Here?");
	$.each(ocargo.level.pathFinder.nodes, function(i, node) {
		console.debug("each node ");
		for (i = 0; i < node.connectedNodes.length; i++) {
			var previousNode = node.connectedNodes[i];
			console.debug("each connected node");
			for (var j = i + 1; j < node.connectedNodes.length; j++) {
				console.debug("nodes following the connected node");
				var nextNode = node.connectedNodes[j];
				var instr = ocargo.level.pathFinder.recogniseIndividualInstruction(
					previousNode.coordinate, node.coordinate, nextNode.coordinate);
				ocargo.level.pathFinder.optimalInstructions.push(instr);
			}
		}
	});
};

ocargo.PathFinder.prototype.getScore = function(stack) {
	console.debug(stack);
	var userSolutionLength = this.getLength(stack);
	var instrLengthScore = 100;
	var pathLenScore = 100;
	instrLengthScore = Math.min(100, Math.max(
		0, instrLengthScore - (this.optimalInstructions.length - userSolutionLength) * 10));
	return instrLengthScore + pathLenScore ;
};

ocargo.PathFinder.prototype.getOptimalPath = function() {
};

ocargo.PathFinder.prototype.getLength = function(stack) {
	var total = 0;
	var i;
	if (!stack) {
		return total;
	}
	console.debug(stack.length);
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
	console.debug(total);
	return total;
};

ocargo.PathFinder.prototype.recogniseIndividualInstruction = function(previous, point1, point2) {
	console.debug("before recognition ", point1, point2);
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
