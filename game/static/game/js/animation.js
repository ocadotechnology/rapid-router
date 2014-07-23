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
	return (this.animationQueue.length == 0);
};

ocargo.Animation.prototype.getLastTimestamp = function() {
	return this.latestTimestamp;
};

ocargo.Animation.prototype.resetAnimation = function() {
	this.animationQueue = [];
	this.animationTimestamp = 0;
	this.latestTimestamp = 0;
	this.isPlaying = false;
	this.currentlyAnimating = false;

	clearPaper();
	renderMap(this.model.map);
	renderDecor(this.decor);
	renderTrafficLights(this.model.trafficLights);
	renderVans(this.model.map.getStartingPosition(), this.numVans);
};

ocargo.Animation.prototype.stepAnimation = function(callback) {
	if (this.currentlyAnimating) {
		return;
	}

	this.currentlyAnimating = true;

	var maxDelay = ANIMATION_LENGTH;

	// do all things in this timestep
	while (this.animationQueue.length > 0 && this.animationQueue[0].timestamp <= this.animationTimestamp) {
		var a = this.animationQueue.shift();

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
                var anims = vanImages[vanID].status();
                for (var i = 0, ii = anims.length; i < ii; i++) {
                    vanImages[vanID].status(anims[i].anim, 1);
                }

                scrollToShowVanImage(vanImages[vanID]);

                // move van
                switch (a.vanAction) {
                	case 'FORWARD':
                		moveForward(vanID, animationLength);
                		break;
                	case 'TURN_LEFT':
                		moveLeft(vanID, animationLength);
                		break;
                	case 'TURN_RIGHT':
                		moveRight(vanID, animationLength);
                		break;
                	case 'TURN_AROUND':
                		animationLength *= 3;
                		turnAround(vanID, animationLength);
                		break;
                	case 'WAIT':
                		wait(vanID, animationLength);
                		break;
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
						break;
					case 'FAIL':
						title = ocargo.messages.failTitle;
						leadMsg = leadMsg + ocargo.messages.closebutton(ocargo.messages.tryagainLabel);
						break;
					case 'WARNING':
						title = ocargo.messages.ohNo;
						leadMsg = leadMsg + ocargo.messages.closebutton(ocargo.messages.tryagainLabel);
						break;
				}
				var otherMsg = "";
				if (a.popupHint) {
					var hintBtns = $("#hintPopupBtn");
			        if (hintBtns.length === null || hintBtns.length === 0) {
			            otherMsg = '<p id="hintBtnPara">' +
			                '<button id="hintPopupBtn">' + ocargo.messages.needHint + '</button>' + 
			                '</p><p id="hintText">' + HINT + '</p>'
			            $("#myModal > .mainText").append('<p id="hintBtnPara">' +
			                '<button id="hintPopupBtn">' + ocargo.messages.needHint + '</button>' + 
			                '</p><p id="hintText">' + HINT + '</p>');
        			}
				}
				startPopup(title, leadMsg, otherMsg);
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
				var lightID = a.id;
				if (a.colour == ocargo.TrafficLight.GREEN) {
                    lightImages[lightID][0].animate({ opacity : 1 }, animationLength/4, 'linear');
                    lightImages[lightID][1].animate({ opacity : 0 }, animationLength/2, 'linear');
                }
                else {
                    lightImages[lightID][0].animate({ opacity : 0 }, animationLength/2, 'linear');
                    lightImages[lightID][1].animate({ opacity : 1 }, animationLength/4, 'linear');
                }
				break;
			case 'console':
				ocargo.consoleOutput.text(ocargo.consoleOutput.text() + a.text);
				break;
		}
		// Calculate maximum animation length
		if (animationLength > maxDelay) {
			maxDelay = animationLength;
		}
	}

	if (this.animationQueue.length == 0) {
		// finished animation, stop playing
		this.isPlaying = false;
	}

	this.animationTimestamp ++;

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
	// Find correct position to insert into animation queue in time ascending order
	// (backwards linear search likely to be better for one van setup at least...)
	var found = false;
	var index = this.animationQueue.length;
	while (!found && index > 0) {
		if (this.animationQueue[index - 1].timestamp > a.timestamp) {
			index --;
		}
		else {
			found = true;
		}
	}
	this.animationQueue.splice(index, 0, a);

	if (this.latestTimestamp < a.timestamp) {
		this.latestTimestamp = a.timestamp;
	}

	// Remove duplicate animations... or make any animations that could potentially appear twice idempotent... Undecided...
};

ocargo.Animation.prototype.queueAnimations = function(as) {
	for (var i = 0; i < as.length; i++) {
		this.queueAnimation(as[i]);
	}
};
