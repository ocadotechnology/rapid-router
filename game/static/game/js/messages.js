var ocargo = ocargo || {};

ocargo.messages = {
	nofuel : "You ran out of fuel! Try to find a shorter path to the destination.",
	tryagain : "Click 'Clear Incorrect' to remove the incorrect blocks and try again!",
	closebutton: function(label) {
		return '<br><br> <button onclick="document.getElementById(' + "'close-modal'" +
		').click()">' + label +'</button>';
	},
	xcorrect : function(x){
		return "Your first " + x + " execution steps were right. ";
	},
	nextLevelButton: function(level) {
		return '<button onclick="window.location.href=' + "'/game/" + level + "'" + 
			'">Next Level</button>';
	},
        nextEpisodeButton: function(episode) {
                var episodeUri = "/game/episode/" + ocargo.level.nextEpisode;
                return "Well done, you've completed the episode!<br>" +
                       "Are you ready for the next challenge? <br><br> " +
                       '<button onclick="window.location.href=' + 
                       "'" + episodeUri + "'" +
                       '"">Next episode</button> </center>' +
                       '<button onclick="window.location.href=' + "'/home/'" + '"">Home</button>';
        },
	lastLevel: "Congratulations, that's all we've got for you for now! <br>" +
		"Wny not try creating your own road? <br><br> <button onclick=" +
		'"window.location.href=' + "'/game/level_editor'" + 
		'"">Create your own map!</button> </center>' + '<button onclick="window.location.href=' +
		"'/home/'" + '"">Home</button>',
	tooManyBlocks: "You used too many blocks!",
}

