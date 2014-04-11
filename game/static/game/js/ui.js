'use strict';

function SimpleUi() {}

SimpleUi.prototype.update = function(nextNode) {
	console.debug('Moving to coordinate ' + JSON.stringify(nextNode.coordinate));
};

SimpleUi.prototype.renderMap = function(map) {
    console.debug('Updating the map: ' + JSON.stringify(map.instructions));
    renderTheMap(map);
}

var ui = new SimpleUi();
