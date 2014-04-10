'use strict';

function SimpleUi() {
    this.update = function(nextNode) {
        console.debug('Moving to coordinate ' + JSON.stringify(nextNode.coordinate));
    };

    this.renderMap = function(map) {
    	console.debug('Updating the map' + JSON.stringify(map.instructions));
    }
}

var ui = new SimpleUi();
