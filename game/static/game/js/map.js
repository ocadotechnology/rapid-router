'use strict';

var ocargo = ocargo || {};

ocargo.Map = function(nodes, decor, trafficLights, destination, ui) {
	this.nodes = nodes;
	this.decor = decor;
	this.trafficLights = trafficLights;
	this.destination = destination;
	ui.renderMap(this);
};
