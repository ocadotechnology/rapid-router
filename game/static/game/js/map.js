'use strict';

var ocargo = ocargo || {};

ocargo.Map = function(nodes, decor, destination, ui) {
	this.nodes = nodes;
	this.decor = decor;
	this.destination = destination;
	ui.renderMap(this);
};
