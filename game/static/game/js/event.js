'use strict';

var ocargo = ocargo || {};

ocargo.Event = function() {};

ocargo.Event.prototype.sendEvent = function(eventType, details) {
  //var csrftoken = $.cookie('csrftoken');
  //$.ajax({
  //   url: '/reports/event',
  //   type: 'POST',
  //   async: true,
  //   dataType: 'json',
  //   beforeSend: function(xhr, settings) {
  //     xhr.setRequestHeader("X-CSRFToken", csrftoken);
  //   },
  //   data: JSON.stringify({ app: "RapidRouter", eventType: eventType, details: details }),
  // });
}

$(document).ready(function() {
  ocargo.event = new ocargo.Event();
});
