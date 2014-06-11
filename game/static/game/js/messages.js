var ocargo = ocargo || {};

ocargo.messages = {
	nofuel : "You ran out of fuel! Try to find a shorter path to the destination.",
	tryagain : "Click 'Clear Incorrect' to remove the incorrect blocks and try again!",
	xcorrect : function(x){
		return "Your first " + x + " execution steps were right. "
	}
}