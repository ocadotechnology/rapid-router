'use strict';

var ocargo = ocargo || {};

ocargo.Map = function(nodes, destination, ui) {
	this.nodes = nodes;
	this.destination = destination;
	ui.renderMap(this);
};

