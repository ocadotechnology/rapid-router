'use strict';

function Map(nodes, ui) {
	this.nodes = nodes;
	this.instructions = this.getThePath();
	ui.renderMap(this);
}

Map.prototype.getThePath = function() {
	var instructions = {};
	var prevCoord = null;
	var twoBack = null;
	var node = null;

	if(this.nodes.length == 0) {
		return instructions;
	}

	for (var i = 0; i <= this.nodes.length; i++) {
		node = i < this.nodes.length ? this.nodes[i] : node;
		var coord = transformY(node.coordinate);

		if (prevCoord) {

			if (isHorizontal(prevCoord, coord) 
				&& (twoBack == null || isHorizontal(twoBack, prevCoord))) {
				pushInstruction(instructions, prevCoord, 'H');

			} else if (isVertical(prevCoord, coord) 
				&& (twoBack == null || isVertical(twoBack, prevCoord))) {
				pushInstruction(instructions, prevCoord, 'V');

			// Handle turns.
			} else { 
				if(isProgressive(twoBack.x, prevCoord.x)) {
					pushInstruction(instructions, prevCoord, 
						nextPointAbove(prevCoord, coord) ? 'DL' : 'UL');
				}
				if(isProgressive(prevCoord.x, twoBack.x)) {
					pushInstruction(instructions, prevCoord,
						nextPointAbove(prevCoord, coord) ? 'DR' : 'UR');
				}
				if(isProgressive(twoBack.y, prevCoord.y)) {
					pushInstruction(instructions, prevCoord,
						nextPointFurther(prevCoord, coord) ? 'UR' : 'UL');
				}
				if(isProgressive(prevCoord.y, twoBack.y)) {
					pushInstruction(instructions, prevCoord,
						nextPointFurther(prevCoord, coord) ? 'DR' : 'DL');
				}
			}
			twoBack = prevCoord;
			prevCoord = coord;

		} else {
			prevCoord = coord;
		}
	}
	return instructions;


	// Helper methods for generating the path.
	function transformY(coord) {
	    return new Coordinate(coord.x, 4 - coord.y);
	}

	function pushInstruction(json, coord, instruction) {
		var x = coord.x.toString();
		var y = coord.y.toString();
		if (!json.hasOwnProperty(x)) {
			json[x] = {};
		}
		json[x][y] = instruction;
	}

	function isHorizontal(prev, next) {
		return prev.y == next.y;
	}

	function isVertical(prev, next) {
		return prev.x == next.x;
	}

	function checkTurn(prev, next) {
		return next.x + next.y - prev.x - prev.y;
	}

	function nextPointAbove(curr, next) {
		return curr.y < next.y;
	}

	function nextPointFurther(curr, next) {
		return curr.x < next.x;
	}

	function isProgressive(coord1, coord2) {
		return coord1 < coord2;
	}
};
