'use strict';

function Map(nodes) {
	this.nodes = nodes;
	console.debug('Before');
	this.instructions = getThePath(nodes);
	console.debug('After');
	ui.renderMap(this)
}

function getThePath(nodes) {
	var instructions = {};
	var prevCoord = null;
	var twoBack = null;

	for (var i = 0; i < nodes.length; i++) {
		var node = nodes[i];
		var coord = node.coordinate;

		if (prevCoord) {

			if (isHorizontal(prevCoord, coord) && (twoBack == null || isHorizontal(twoBack, prevCoord))) {
				pushInstruction(instructions, coord, 'H');
					console.debug(prevCoord.x + " "+prevCoord.y + " next "+ coord.x + " "+ coord.y + "HORIZONTAL")

			} else if (isVertical(prevCoord, coord) && (twoBack == null || isVertical(twoBack, prevCoord))) {
				pushInstruction(instructions, coord, 'V');
					console.debug(prevCoord.x + " "+prevCoord.y + " next "+ coord.x + " "+ coord.y + "verticaal")

			// Handle turns.
			} else if (isHorizontal(twoBack, prevCoord)) {
				if (isProgressive(twoBack.x, prevCoord.x)) {
					pushInstruction(instructions, coord, nextPointAbove(prevCoord, coord) ? 'DR' : 'DL');
				} else {
					pushInstruction(instructions, coord, nextPointAbove(prevCoord, coord) ? 'UL' : 'UR');
				}
			} else {
				if (isProgressive(twoBack.y, prevCoord.y)) {
					pushInstruction(instructions, coord, nextPointAbove(prevCoord, coord) ? 'UR' : 'UL');
				} else {
					pushInstruction(instructions, coord, nextPointAbove(prevCoord, coord) ? 'DL' : 'DR');
				}
			}

			twoBack = prevCoord;
			prevCoord = coord;

		} else {
			prevCoord = node.coordinate;
		}

	}
	return instructions;
}

function pushInstruction(json, coord, instruction) {
	var y = coord.x.toString();
	var x = coord.y.toString();
	if (!json.hasOwnProperty(x)) {
		json[x] = {};
	}
	json[x][y] = instruction;
}

function isHorizontal(prev, next) {
	return prev.y == next.y && prev.x != next.x;
}

function isVertical(prev, next) {
	return prev.x == next.x && prev.y != next.y;
}

function checkTurn(prev, next) {
	return next.x + next.y - prev.x - prev.y;
}

function nextPointAbove(curr, next) {
	return curr.y < next.y;
}

function nextPointBelow(curr, next) {
	return curr.y > next.y;
}

function isProgressive(coord1, coord2) {
	return coord1 < coord2;
}
