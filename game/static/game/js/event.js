'use strict';

var ocargo = ocargo || {};

ocargo.Event = function() {};

ocargo.Event.prototype.sendEvent = function(eventType, details) {
};

$(document).ready(function() {
  ocargo.event = new ocargo.Event();
});
