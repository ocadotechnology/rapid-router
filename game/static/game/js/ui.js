'use strict';

function SimpleUi() {
    this.queue_ = [];

    // HACK to start with, just pass in the instruction and call the function in drawing.js
    // At the end of the day we need to animate along same bezier curve as road creates
    // see source of http://raphaeljs.com/gear.html for way of doing this
}

SimpleUi.prototype.queueUpdate = function(van, nextNode, instruction) {
    console.debug('Moving to coordinate ' + JSON.stringify(nextNode.coordinate));
    this.queue_.push(instruction);
}

SimpleUi.prototype.animateUpdates = function() {
    var self = this;

    var animate = function() {
        var ins = self.queue_.shift();
        if (!ins) {
            return;
        }

        if (ins == FORWARD) {
            moveForward(animate);
        } else if (ins == TURN_LEFT) {
            moveLeft(animate);
        } else if (ins == TURN_RIGHT) {
            moveRight(animate);
        }
    }

    animate();
}

SimpleUi.prototype.renderMap = function(map) {
    console.debug('Updating the map: ' + JSON.stringify(map.instructions));
    renderTheMap(map);
}
