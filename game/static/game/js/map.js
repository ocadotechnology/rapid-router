'use strict';

var ocargo = ocargo || {};

ocargo.Map = function(nodes, destination, ui) {
	this.nodes = nodes;
	this.destination = destination;
	this.instructions = this.getThePath();
	ui.renderMap(this);
};

ocargo.Map.prototype.getThePath = function() {
	var instructions = {};
	var current = null;
	var previous = null;
	var node = null;

	if(this.nodes.length == 0) {
		return instructions;
	}

	for (var i = 0; i <= this.nodes.length; i++) {
		node = i < this.nodes.length ? this.nodes[i] : node;
		var next = transformY(node.coordinate);

		if (current) {

			if (isHorizontal(current, next) 
				&& (previous == null || isHorizontal(previous, current))) {
				pushInstruction(instructions, current, 'H');

			} else if (isVertical(current, next) 
				&& (previous == null || isVertical(previous, current))) {
				pushInstruction(instructions, current, 'V');

			// Handle turns.
			} else { 
				if (isProgressive(previous.x, current.x)) {
					pushInstruction(instructions, current, 
						nextPointAbove(current, next) ? 'DL' : 'UL');
				}
				if (isProgressive(current.x, previous.x)) {
					pushInstruction(instructions, current,
						nextPointAbove(current, next) ? 'DR' : 'UR');
				}
				if (isProgressive(previous.y, current.y)) {
					pushInstruction(instructions, current,
						nextPointFurther(current, next) ? 'UR' : 'UL');
				}
				if (isProgressive(current.y, previous.y)) {
					pushInstruction(instructions, current,
						nextPointFurther(current, next) ? 'DR' : 'DL');
				}
			}
			previous = current;
			current = next;

		} else {
			current = next;
		}
	}
	return instructions;


	// Helper methods for generating the path.
	function transformY(coord) {
	    return new ocargo.Coordinate(coord.x, GRID_HEIGHT - 1 - coord.y);
	}

	function isHorizontal(prev, next) {
		return prev.y == next.y;
	}

	function isVertical(prev, next) {
		return prev.x == next.x;
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

function pushInstruction(json, coord, instruction) {
	var x = coord.x.toString();
	var y = coord.y.toString();
	if (!json.hasOwnProperty(x)) {
		json[x] = {};
	}
	json[x][y] = instruction;
}
