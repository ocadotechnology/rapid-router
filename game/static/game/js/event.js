'use strict';

var ocargo = ocargo || {};

ocargo.Event = function() {};

ocargo.Event.prototype.sendEvent = function(eventType, details) {
};

$(document).ready(function() {
  ocargo.event = new ocargo.Event();
});

// The play button seems to have very complicated implementation
// therefore, retriggerring the current event when click run code
const runCode = () => {
  $("#play_radio").click()
}
