'use strict';

function SimpleUi() {
    this.update = function(nextNode) {
        console.debug('Moving to coordinate ' + JSON.stringify(nextNode.coordinate));
    };
}

var ui = new SimpleUi();