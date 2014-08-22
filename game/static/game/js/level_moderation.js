var levelID;

var CONFIRMATION_DATA = {
  'deleteLevel': {
      options: {
          title: 'Delete level',
      },
      html: "<p>This student's level will be permanently deleted. Are you sure?</p>",
      confirm: function() {
          $.ajax({
              url : '/game/level_moderation/delete/' + levelID,
              type : 'POST',
              dataType: 'json',
              data : {
                  csrfmiddlewaretoken : $.cookie('csrftoken'),
              },
              success: function(json) {
                  if(json.success) {
                      document.forms["levelModerationForm"].submit();
                  }
                  else {
                      console.debug("failure");
                  }
              },
              error : function(xhr,errmsg,err) {
                  console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
              }
          });
      },
  }
};

$(document).ready(function() {
	$(".delete").click(function() {
	  	levelID = this.getAttribute('value');
	  	openConfirmationBox('deleteLevel');
	});

	$('.play').click(function() {
		window.location.href = '/game/' + this.getAttribute('value');
	});
});
