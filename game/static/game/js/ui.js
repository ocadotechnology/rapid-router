'use strict';

function SimpleUi() {
    this.update = function(nextNode) {
        console.log('Moving to coordinate ' + JSON.stringify(nextNode.coordinate));
    };
}

var ui = new SimpleUi();