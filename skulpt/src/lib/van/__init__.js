//
// Controller for a van
//
function VanController() {
    this.initialize();
};
VanController.prototype.initialize = function () {

};
VanController.prototype.highlightLineCallable = function(lineIndex, colour) {
    var lines = $('.CodeMirror-code')[0].children;
    // unhighlight all lines
    var i;
    for (i = 0; i < lines.length; i++) {
        lines[i].style.background = "";
    }
    // highlight desired line
    lines[lineIndex].style.background = colour;
};
VanController.prototype.queueHighlight = function(colour) {
    var self = this;
    var lineIndex = Sk.currLineNo - 1;
    ocargo.animation.queueAnimation({
        timestamp: ocargo.model.timestamp,
        type: 'callable',
        functionCall: function () { self.highlightLineCallable(lineIndex, colour); },
    });
};
//
// Movement and condition functions delegated appropriately
//
VanController.prototype.move_forwards = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellowgreen");
    }
    Sk.failed = Sk.failed || !ocargo.model.moveForwards();
};
VanController.prototype.turn_left = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellowgreen");
    }
    Sk.failed |= Sk.failed || !ocargo.model.turnLeft();
};
VanController.prototype.turn_right = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellowgreen");
    }
    Sk.failed = Sk.failed || !ocargo.model.turnRight();
};
VanController.prototype.turn_around = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellowgreen");
    }
    Sk.failed = Sk.failed || !ocargo.model.turnAround();
};
VanController.prototype.wait = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellowgreen");
    }
    Sk.failed = Sk.failed || !ocargo.model.wait();
};
VanController.prototype.at_dead_end = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellow");
    }
    return ocargo.model.isDeadEnd();
};
VanController.prototype.at_destination = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellow");
    }
    return ocargo.model.isAtDestination();
};
VanController.prototype.at_traffic_light = function (c) {
    switch(c) {
    case "GREEN":
        return this.at_green_traffic_light();
        break;
    case "RED":
        return this.at_red_traffic_light();
        break;
    default:
        return false;
    }
};
VanController.prototype.at_red_traffic_light = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellow");
    }
    return ocargo.model.isTrafficLightRed();
};
VanController.prototype.at_green_traffic_light = function () {
    if (!Sk.failed) {
        this.queueHighlight("yellow");
    }
    return ocargo.model.isTrafficLightGreen();
};
VanController.prototype.is_road = function (d) {
    switch(d) {
    case "FORWARD":
        return this.is_road_forward();
        break;
    case "LEFT":
        return this.is_road_left();
        break;
    case "RIGHT":
        return this.is_road_right();
        break;
    default:
        return false;
    }
}
VanController.prototype.is_road_forward = function () {
    this.queueHighlight("yellow");
    return ocargo.model.isRoadForward();

};
VanController.prototype.is_road_left = function () {
    this.queueHighlight("yellow");
    return ocargo.model.isRoadLeft();
};
VanController.prototype.is_road_right = function () {
    this.queueHighlight("yellow");
    return ocargo.model.isRoadRight();
};

var $builtinmodule = function (name) {
    'use strict';
    var mod = {},
        checkArgs = function (expected, actual, func) {
            if (actual !== expected) {
                throw new Sk.builtin.TypeError(func + ' takes exactly ' + expected + ' positional argument (' + actual + ' given)');
            }
        },
        van = function ($gbl, $loc) {
            $loc.__init__ = new Sk.builtin.func(function (self) {
                self.theVan = new VanController();
            });
            //
            // Van Motion
            //
            $loc.move_forwards = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'move_forwards()');
                self.theVan.move_forwards();
            });
            $loc.turn_left = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'turn_left()');
                self.theVan.turn_left();
            });
            $loc.turn_right = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'turn_right()');
                self.theVan.turn_right();
            });
            $loc.turn_around = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'turn_around()');
                self.theVan.turn_around();
            });
            $loc.wait = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'wait()');
                self.theVan.wait();
            });
            //
            // Van state
            //
            $loc.at_dead_end = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'at_dead_end()');
                return Sk.builtin.bool(self.theVan.at_dead_end());
            });
            $loc.at_destination = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'at_destination()');
                return Sk.builtin.bool(self.theVan.at_destination());
            });
            $loc.at_traffic_light = new Sk.builtin.func(function (self, c) {
                checkArgs(2, arguments.length, 'at_traffic_light()');
                return Sk.builtin.bool(self.theVan.at_traffic_light(new Sk.builtin.str(c).v));
            });
            $loc.at_red_traffic_light = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'at_red_traffic_light()');
                return Sk.builtin.bool(self.theVan.at_red_traffic_light());
            });
            $loc.at_green_traffic_light = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'at_green_traffic_light()');
                return Sk.builtin.bool(self.theVan.at_green_traffic_light());
            });
            $loc.is_road = new Sk.builtin.func(function (self, d) {
                checkArgs(2, arguments.length, 'is_road()');
                return Sk.builtin.bool(self.theVan.is_road(new Sk.builtin.str(d).v));
            });
            $loc.is_road_forward = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'is_road_forward()');
                return Sk.builtin.bool(self.theVan.is_road_forward());
            });
            $loc.is_road_left = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'is_road_left()');
                return Sk.builtin.bool(self.theVan.is_road_left());
            });
            $loc.is_road_right = new Sk.builtin.func(function (self) {
                checkArgs(1, arguments.length, 'is_road_right()');
                return Sk.builtin.bool(self.theVan.is_road_right());
            });
        };

    mod.Van = Sk.misceval.buildClass(mod, van, 'Van', []);

    return mod;
};