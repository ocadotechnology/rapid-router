'use strict';

var ocargo = ocargo || {};

var ANIMATION_LENGTH = 500;

ocargo.Animation = function(model, decor, numVans) {
	this.model = model;
	this.decor = decor;
	this.numVans = numVans;

	// timer identifier for pausing
	this.playTimer = -1;

	this.resetAnimation();
};

ocargo.Animation.prototype.isFinished = function() {
	return this.finished;
};

ocargo.Animation.prototype.wasJustReset = function() {
	return (!this.isFinished() && this.animationQueue.length == 1 && this.animationQueue[0].length == 1 && this.animationQueue[0][0].length == 0);
};

ocargo.Animation.prototype.resetAnimation = function() {
	this.animationQueue = [[[]]];

	this.timestamp = 0;
	this.subTimestamp = 0;
	this.lastTimestamp = 0;
	this.lastSubTimestamp = 0;
	this.isPlaying = false;
	this.currentlyAnimating = false;
	this.finished = false;

	ocargo.drawing.clearPaper();
	ocargo.drawing.renderMap(this.model.map);
	ocargo.drawing.renderDecor(this.decor);
	ocargo.drawing.renderVans(this.model.map.getStartingPosition(), this.numVans);
	ocargo.drawing.renderOrigin(this.model.map.getStartingPosition());
	ocargo.drawing.renderDestinations(this.model.map.getDestinations());
	ocargo.drawing.renderTrafficLights(this.model.trafficLights);
};

ocargo.Animation.prototype.stepAnimation = function(callback) {
	if (this.currentlyAnimating) {
		return;
	}

	this.currentlyAnimating = true;

	var maxDelay = ANIMATION_LENGTH;

	var timestampQueue = this.animationQueue[this.timestamp];

	if (timestampQueue) {
		// Perform all events for this subTimestamp
		var subTimestampQueue = timestampQueue[this.subTimestamp];
		if (subTimestampQueue) {
			while (subTimestampQueue.length > 0) {
				var delay = this.performAnimation(subTimestampQueue.shift());
				maxDelay = Math.max(maxDelay, delay);
			}
		}

		// And move onto the next subTimestamp
		this.subTimestamp += 1;
	}

	// Go to the next timestamp if there are no events for this one
	// or if we've performed them all already
	if (!timestampQueue || this.subTimestamp >= timestampQueue.length) {
		this.timestamp += 1;
		this.subTimestamp = 0;
	}

	// Check if we've performed all events we have
	if (this.timestamp >= this.animationQueue.length) {
		this.isPlaying = false;
		this.finished = true;
	}

	// Call this function again after the events have finished
	var self = this;
	setTimeout(function() {
		if (callback) {
			callback();
		}
		self.currentlyAnimating = false;
		if (self.isPlaying) {
			self.stepAnimation();
		}
	}, maxDelay);
};

ocargo.Animation.prototype.playAnimation = function() {
	if (!this.currentlyAnimating && !this.isPlaying && this.animationQueue.length > 0) {
		this.isPlaying = true;
		this.stepAnimation();
	}
};

ocargo.Animation.prototype.pauseAnimation = function() {
	this.isPlaying = false;
};

ocargo.Animation.prototype.queueAnimation = function(a) {
	if (a.timestamp && a.subTimestamp) {
		if (!this.animationQueue[a.timestamp]) {
			this.animationQueue[a.timestamp] = [];
		}
		if (!this.animationQueue[a.timestamp][a.subTimestamp]) {
			this.animationQueue[a.timestamp][a.subTimestamp] = [];
		}
		this.animationQueue[a.timestamp][a.subTimestamp].push(a);

		this.lastTimestamp = Math.max(this.lastTimestamp, a.timestamp);
		this.lastSubTimestamp = Math.max(this.lastSubTimestamp, a.subTimestamp);
	}
	// Remove duplicate animations... or make any animations that could potentially appear twice idempotent... Undecided...
};

ocargo.Animation.prototype.queueAnimations = function(as) {
	for (var i = 0; i < as.length; i++) {
		this.queueAnimation(as[i]);
	}
};

ocargo.Animation.prototype.appendAnimation = function(a) {
	this.animationQueue[this.lastTimestamp][this.lastSubTimestamp].push(a);
};

ocargo.Animation.prototype.startNewSubTimestamp = function() {
	this.lastSubTimestamp += 1;

	this.animationQueue[this.lastTimestamp][this.lastSubTimestamp] = [];
};

ocargo.Animation.prototype.startNewTimestamp = function() {
	this.lastTimestamp += 1;
	this.lastSubTimestamp = 0;

	this.animationQueue[this.lastTimestamp] = [[]];
};

ocargo.Animation.prototype.performAnimation = function(a) {
	// animation length is either default or may be custom set
	var animationLength = a.animationLength || ANIMATION_LENGTH;

	switch (a.type) {
		case 'callable':
			animationLength = a.animationLength || 0;
			a.functionCall();
			break;
		case 'van':
			// Set all current animations to the final position, so we don't get out of sync
			var vanID = a.id;
			ocargo.drawing.skipOutstandingVanAnimationsToEnd(vanID);
            ocargo.drawing.scrollToShowVan(vanID);

            // move van
            switch (a.vanAction) {
            	case 'FORWARD':
            		ocargo.drawing.moveForward(vanID, animationLength);
            		break;
            	case 'TURN_LEFT':
            		ocargo.drawing.moveLeft(vanID, animationLength);
            		break;
            	case 'TURN_RIGHT':
            		ocargo.drawing.moveRight(vanID, animationLength);
            		break;
            	case 'TURN_AROUND':
            		animationLength *= 3;
            		ocargo.drawing.turnAround(vanID, animationLength);
            		break;
            	case 'WAIT':
            		ocargo.drawing.wait(vanID, animationLength);
            		break;
            	case 'CRASH':
            		ocargo.drawing.crash(vanID, animationLength, a.previousNode, a.currentNode, a.attemptedAction, a.startNode);
            		break;
            	case 'DELIVER':
            		ocargo.drawing.deliver(vanID, animationLength, a.destinationID);
            	case 'OBSERVE':
            		break;
            }
            // Check if fuel update present
            if (typeof a.fuel != 'undefined') {
            	// update fuel gauge
            	var rotation = 'rotate(' + (((a.fuel/100)*240)-120) + 'deg)';
				document.getElementById('fuelGaugePointer').style.transform=rotation;
				document.getElementById('fuelGaugePointer').style.webkitTransform=rotation;
            }
			break;
		case 'popup':
			var title = "";
			var leadMsg = a.popupMessage;
			var delay;
			// sort popup...
			switch (a.popupType) {
				case 'WIN':
					title = ocargo.messages.winTitle;
					var levelMsg = "";
					if (NEXT_LEVEL) {
				        levelMsg = '<br><br>' + ocargo.messages.nextLevelButton(NEXT_LEVEL);
				    } 
				    else {
				        if (NEXT_EPISODE) {
				            levelMsg = '<br><br>' + ocargo.messages.nextEpisodeButton(NEXT_EPISODE);
				        } else {
				            levelMsg = ocargo.messages.lastLevel;
				        }
				    }
				    leadMsg = leadMsg + levelMsg;
				    delay = 1000;
					break;
				case 'FAIL':
					title = ocargo.messages.failTitle;
					leadMsg = leadMsg + ocargo.messages.closebutton(ocargo.messages.tryagainLabel);
					if(a.failSubtype == "CRASH") {
						delay = 3000;
					}
					else {
						delay = 1000;
					}
					break;
				case 'WARNING':
					title = ocargo.messages.ohNo;
					leadMsg = leadMsg + ocargo.messages.closebutton(ocargo.messages.tryagainLabel);
					delay = 1000;
					break;
			}
			var otherMsg = "";
			if (a.popupHint) {
				var hintBtns = $("#hintPopupBtn");
		        if (hintBtns.length === null || hintBtns.length === 0) {
		            otherMsg = '<p id="hintBtnPara">' +
		                '<button id="hintPopupBtn">' + ocargo.messages.needHint + '</button>' + 
		                '</p><p id="hintText">' + HINT + '</p>';
		            $("#myModal > .mainText").append('<p id="hintBtnPara">' +
		                '<button id="hintPopupBtn">' + ocargo.messages.needHint + '</button>' + 
		                '</p><p id="hintText">' + HINT + '</p>');
    			}
			}
			ocargo.Drawing.startPopup(title, leadMsg, otherMsg, delay);
			if (a.popupHint) {
				if(level.hintOpened){
	                $("#hintBtnPara").hide();
	            } else {
	                $("#hintText" ).hide();
	                $("#hintPopupBtn").click( function(){
	                    $("#hintText").show(500);
	                    $("#hintBtnPara").hide();
	                    level.hintOpened = true;
	                });
	            }
	        }
			break;
		case 'trafficlight':
			ocargo.drawing.transitionTrafficLight(a.id, a.colour, animationLength/2);
			break;
		case 'console':
			ocargo.consoleOutput.text(ocargo.consoleOutput.text() + a.text);
			break;
	}

	return animationLength;
};
