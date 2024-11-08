'use strict';

var ocargo = ocargo || {};

ocargo.Animation = function(model, decor, drawing) {
    this.model = model;
    this.decor = decor;
	this.drawing = drawing;
	this.activeCows = []; // cows currently displayed on map
	this.scalingModifier = [];
	this.crashed = false;
	this.speedUp = false;

	this.FAST_ANIMATION_DURATION = 125;
	this.REGULAR_ANIMATION_DURATION = 500;

	this.setAnimationDuration(this.REGULAR_ANIMATION_DURATION);

	// timer identifier for pausing
	this.playTimer = -1;

	this.drawing.clearPaper();
	this.drawing.renderMap(this.model.map);
	this.drawing.renderCharacter();
	this.drawing.renderDecor(this.decor);
	this.drawing.renderOrigin(this.model.map.startingPosition());
	this.drawing.renderDestinations(this.model.map.getDestinations());
	this.drawing.renderTrafficLights(this.model.trafficLights);

	this.addCows();

	this._updateFuelGauge(100);
};

ocargo.Animation.prototype.isFinished = function() {
	return this.finished;
};

ocargo.Animation.prototype.addCows = function() {
	let cows = this.model.cows;
	
	for (let i = 0 ; i < cows.length ; i++){
		let cow = cows[i];
		for (let j = 0; j < cow.coordinates.length; j++) {
			const cowImage = this.drawing.renderCow(cow.id, cow.coordinates[j], cow.potentialNodes[j], 0, cow.type);
			this.numberOfCowsOnMap++;
			this.activeCows.push(cowImage);
		}
	}
}

ocargo.Animation.prototype.removeCows = function() {
	for (var i = 0; i < this.activeCows.length; i++) {
		this.drawing.removeCow(this.activeCows[i]);
	}
	this.activeCows = [];
};

ocargo.Animation.prototype.resetAnimation = function() {
	this.animationQueue = [[]];

	this.timestamp = 0;
	this.lastTimestamp = 0;
	this.isPlaying = false;
	this.currentlyAnimating = false;
	this.finished = false;
	this.numberOfCowsOnMap = 0;
	this.crashed = false;
	this.scalingModifier = [];

	// Reset the display
	for(var i = 0; i < this.model.trafficLights.length; i++) {
		var tl = this.model.trafficLights[i];
		this.drawing.transitionTrafficLight(tl.id, tl.state, 0);
	}

	this.removeCows();
	this.addCows();

	for(var i = 0; i < this.model.map.destinations.length; i++) {
		var destination = this.model.map.destinations[i];
		this.drawing.transitionDestination(destination.id, false, 0);
	}

	this.drawing.reset();
};

ocargo.Animation.prototype.setRegularSpeed = function() {
	this.setAnimationDuration(this.REGULAR_ANIMATION_DURATION);
	this.speedUp = false;
};

ocargo.Animation.prototype.setHighSpeed = function(){
	this.setAnimationDuration(this.FAST_ANIMATION_DURATION);
	this.speedUp = true;
};

ocargo.Animation.prototype.baseAnimationDuration = function(){
	return this.speedUp ? this.FAST_ANIMATION_DURATION : this.REGULAR_ANIMATION_DURATION;
};

ocargo.Animation.prototype.stepAnimation = function(callback) {
	function removeBlockSelection () {
		Blockly.mainWorkspace.getAllBlocks().forEach(
			function (block) {
				if(block.keepHighlighting){
					delete (block.keepHighlighting);
				}
			}
		);
	}

	if (this.currentlyAnimating) {
		return;
	}

	removeBlockSelection();

	this.currentlyAnimating = true;

	var maxDelay = 0;

	var timestampQueue = this.animationQueue[this.timestamp];

	if (timestampQueue) {
		// Perform all events for this timestamp
		while (timestampQueue.length > 0) {
			var animation = timestampQueue.shift();
            var delay = this.performAnimation(animation);
			if (this.crashed && delay != 0) {
				// Special case for crashing into cow as the van travel less before crashing
				maxDelay = delay;
			} else {
				maxDelay = Math.max(maxDelay, delay);
			}
		}
		// And move onto the next timestamp
		this.timestamp += 1;
		// Update defaultAnimationLength at every increment to prevent sudden stop in animation
		if (!this.crashed && this.numberOfCowsOnMap > 0) {
			this.setAnimationDuration(this.baseAnimationDuration() * 1.5);
		} else {
			this.setAnimationDuration(this.baseAnimationDuration());
		}
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
			self.stepAnimation(undefined);
		}
	}, maxDelay);
};

ocargo.Animation.prototype.playAnimation = function() {
	if (!this.currentlyAnimating && !this.isPlaying && this.animationQueue.length > 0) {
		this.isPlaying = true;
		this.stepAnimation(undefined);

		let gauge_text = document.getElementById("Text_percentage");
		let gauge_text_value = document.getElementById("Text_percentage_value");
		let gauge_charge_circle = document.getElementById("f");
		let gauge_emptying_circle = document.getElementById("emptying_circle");

		gauge_text.setAttribute("transform", "translate(42.3 48.2)");
		gauge_text.setAttribute("fill", "#4ba0dd");
		gauge_text_value.textContent = "100%";
		gauge_charge_circle.setAttribute("fill", "#4ba0dd");
		gauge_emptying_circle.setAttribute("stroke-dashoffset", 273.18);
		gauge_emptying_circle.setAttribute("transform", "rotate(90, 59.79, 59.79)");
	}
};

ocargo.Animation.prototype.pauseAnimation = function() {
	this.isPlaying = false;
};

ocargo.Animation.prototype.appendAnimation = function(a) {
	this.animationQueue[this.lastTimestamp].push(a);
};

ocargo.Animation.prototype.startNewTimestamp = function() {
	this.lastTimestamp += 1;

	this.animationQueue[this.lastTimestamp] = [];
};

ocargo.Animation.prototype._addPause = function(duration) {
	return duration + (this.animationDuration * 0.8);
};

ocargo.Animation.prototype.performAnimation = function(animation) {
	// Duration is either custom set (for each element) or generic
	var duration = animation.animationLength || this.animationDuration;

    switch (animation.type) {
		case 'callable':
			duration = animation.animationLength || 0;
			animation.functionCall();
			break;
		case 'crashSound':
			duration = 0;
			animation.functionCall(this.animationDuration / 2);
			break;
		case 'van':
			this.drawing.scrollToShowCharacter();

			// move van
			switch (animation.vanAction) {
				case 'FORWARD':
					duration = this.drawing.moveForward(null, this.scalingModifier.shift());
					break;
				case 'TURN_LEFT':
					duration = this.drawing.turnLeft(null, this.scalingModifier.shift());
					break;
				case 'TURN_RIGHT':
					duration = this.drawing.turnRight(null, this.scalingModifier.shift());
					break;
				case 'TURN_AROUND_FORWARD':
					duration = this.drawing.turnAround('FORWARD');
					break;
				case 'TURN_AROUND_RIGHT':
					duration = this.drawing.turnAround('RIGHT');
					break;
				case 'TURN_AROUND_LEFT':
					duration = this.drawing.turnAround('LEFT');
					break;
				case 'WAIT':
            		this.drawing.wait();
            		break;
				case 'SOUND_HORN':
					this.drawing.wait();
					break;
				case 'PUFFUP':
					this.scalingModifier.push(2);
					break;
                case 'REMAINPUFFUP':
                    this.scalingModifier.unshift(1);
                    break;
                case 'PUFFDOWN':
					this.scalingModifier.push(0.5);
                    break;
            	case 'CRASH':
					this.crashed = true;
            		duration = this.drawing.crash(animation.previousNode, animation.currentNode,
            			animation.attemptedAction, animation.startNode);
            		break;
				case 'COLLISION_WITH_COW':
					this.crashed = true;
					//Update animationLength with time van moves before crashing
					duration = this.drawing.collisionWithCow(animation.previousNode, animation.currentNode,
						animation.attemptedAction, animation.startNode);
					break;
            	case 'DELIVER':
            		this.drawing.deliver(animation.destinationID, duration);
					break;
            	case 'OBSERVE':
            		break;
			}

			if (animation.pause) {
				duration = this._addPause(duration);
			}

			this._updateFuelIfPresent(animation);

			break;
		case 'popup':
			var title = "";
			var leadMsg = animation.popupMessage;
			var buttons = '';

			// sort popup...
			switch (animation.popupType) {
				case 'WIN':
					title = gettext('You win!');
					var levelMsg = [];

					if (!animation.pathScoreDisabled) {
						levelMsg.push(gettext('Route score: ') + ocargo.Drawing.renderCoins(animation.routeCoins)
							+ "<span id=\"routeScore\">" + animation.pathLengthScore + "/" + animation.maxScoreForPathLength + "</span>");
					}

					if (animation.maxScoreForNumberOfInstructions != 0){
						levelMsg.push(gettext('Algorithm score: ') +
							ocargo.Drawing.renderCoins(animation.instrCoins)
                            + "<span id=\"algorithmScore\">" + animation.instrScore + "/" + animation.maxScoreForNumberOfInstructions + "</span>");
					}

					levelMsg.push(interpolate(
						gettext('Your total score: %(totalScore)s/%(maxScore)s'),
						{totalScore: animation.totalScore, maxScore: animation.maxScore},
						true
					));

					levelMsg.push(leadMsg);

					if (animation.performance != "scorePerfect") {
						buttons += ocargo.button.tryAgainButtonHtml();
					}

					if (BLOCKLY_ENABLED && PYTHON_ENABLED && ocargo.game.isInBlocklyWorkspace()) {
						levelMsg.push(gettext(
							'Looks like you\'ve got a route sorted using Blockly.<br><br>Now go to the Python tab and see if you can do the same in Python! '
						));
						buttons += ocargo.button.dismissButtonHtml('close_button', gettext('Close'));
					} else {
						// If there exists next level, add animation button which redirects the user to that
						if (NEXT_LEVEL_URL) {
							if (NEXT_LEVEL_URL == "/pythonden/") {
								buttons += ocargo.button.episodeRedirectButtonHtml('next_level_button', NEXT_LEVEL_URL, gettext('Next episode'), NEXT_EPISODE)
							} else {
								buttons += ocargo.button.redirectButtonHtml('next_level_button', NEXT_LEVEL_URL, gettext('Next level'))
							}
						}
						else if (PREV_LEVEL_URL) {
							buttons += ocargo.button.redirectButtonHtml('prev_level_button', PREV_LEVEL_URL, gettext('Previous level'));
						} else {
							/*
							 This is the last level of the episode. If there exists animation next episode, add button to
							 redirect user to it or level selection page.
							 If this is animation default level and there isn't animation next episode, user has reached the end of the
							 game. Add button to encourage users to create their own levels or redirect to level
							 selection page.
							 */

							if (NEXT_EPISODE) {
								var nextEpisodeMessages = [gettext('Well done, you\'ve completed the episode! <br> Are you ready for the next challenge? ')];
								if (RANDOM) {
									nextEpisodeMessages.push(gettext('Or try one of this episode\'s random levels!'));
								}
								levelMsg.push(nextEpisodeMessages.join(' '));
								buttons += ocargo.button.redirectButtonHtml('next_episode_button', Urls.start_episode(NEXT_EPISODE), gettext('Next episode'));
								if (RANDOM) {
									buttons += ocargo.button.redirectButtonHtml('random_level_button', Urls.random_level_for_episode(NEXT_EPISODE-1), gettext('Random level'));
								}
								buttons += ocargo.button.redirectButtonHtml('home_button', Urls.levels(), gettext('Home'));
					        } else if(DEFAULT_LEVEL) {
					            levelMsg.push(gettext('That\'s all we\'ve got for you right now. Carry on the fun by creating your own challenges.'));
								buttons += ocargo.button.redirectButtonHtml('next_level_button', Urls.level_editor(), gettext('Create your own map!'));
								buttons += ocargo.button.redirectButtonHtml('home_button', Urls.levels(), gettext('Home'));
					        } else if (IS_RANDOM_LEVEL) {
					            levelMsg.push(gettext('Do you want to try another random level?'));
								buttons += ocargo.button.redirectButtonHtml('retry_button', window.location.href, gettext('Have more fun!'));
								buttons += ocargo.button.redirectButtonHtml('home_button', Urls.levels(), gettext('Home'));
							}
					    }
					}
					leadMsg = levelMsg.join('<br>') + '<br>';
					break;
				case 'FAIL':
					title = gettext('Oh dear!');
					buttons = ocargo.button.tryAgainButtonHtml();
					break;
				case 'WARNING':
					buttons = ocargo.button.tryAgainButtonHtml();
					break;
			}
			var otherMsg = "";
			if (animation.popupHint) {
				buttons += '<button class="navigation_button long_button" id="hintPopupBtn"><span>' + gettext('Show hint') + '</span></button>';
				otherMsg = '<div id="hintBtnPara">' + '</div><div id="hintText">' + HINT + '</div>';
			}
			ocargo.Drawing.startPopup(title, leadMsg, otherMsg, true, buttons);
			if (animation.popupHint) {
				$("#hintPopupBtn").click( function(){
	                    $("#hintText").show(500);
	                    $("#hintBtnPara").hide();
	                    $("#hintPopupBtn").hide();
	                });
	        }
			break;
		case 'trafficlight':
			this.drawing.transitionTrafficLight(animation.id, animation.colour, duration/2);
			break;
        case 'cow_leave':
					this.numberOfCowsOnMap--;
					var cow = this._extractCowAt(animation.coordinate);
					this.drawing.removeCow(cow, duration);  // remove it from drawing
			break;
		case 'console':
			ocargo.pythonControl.appendToConsole(animation.text);
			break;
	}
	return duration;
};

ocargo.Animation.prototype._extractCowAt = function(coordinate) {
    for (var i = 0; i < this.activeCows.length; i++) {
        var cow = this.activeCows[i];
        if (coordinate.equals(cow.coordinate)) {
            this.activeCows.splice(i, 1);   // remove cow from array
            return cow;
        }
    }
};

ocargo.Animation.prototype._updateFuelIfPresent = function(animation) {
	if (typeof animation.fuel != 'undefined' && animation.fuel >= 0) {
		this._updateFuelGauge(animation.fuel);
	}
};

ocargo.Animation.prototype._updateFuelGauge = function(fuelPercentage) {
    if (CHARACTER_NAME == "Electric van") {
			let gaugeCircumference = 273.18;
			let baseRotation = 270;

			let offset = gaugeCircumference * (fuelPercentage / 100);
			let rotation = 36 * (fuelPercentage / 10) - baseRotation;

			let color = (fuelPercentage > 30) ? "#4ba0dd" : ((fuelPercentage > 10) ? "#ff7300" : "#ff3131");
			let text_x = (fuelPercentage == 100) ? 42.3 : ((fuelPercentage >= 10) ? 45 : 50);

			let gauge_text = document.getElementById("Text_percentage");
			let gauge_text_value = document.getElementById("Text_percentage_value");
			let gauge_charge_circle = document.getElementById("f");
			let gauge_emptying_circle = document.getElementById("emptying_circle");

			gauge_text.setAttribute("transform", "translate(" + text_x + " 48.2)");
			gauge_text.setAttribute("fill", color);
			gauge_text_value.textContent = fuelPercentage + "%";
			gauge_charge_circle.setAttribute("fill", color);
			gauge_emptying_circle.setAttribute("stroke-dashoffset", offset);
			gauge_emptying_circle.setAttribute("transform", "rotate(" + rotation + ", 59.79, 59.79)");
		} else {
			var degrees = ((fuelPercentage / 100) * 240) - 120;
			var rotation = 'rotate(' + degrees + 'deg)';
			document.getElementById('fuelGaugePointer').style.transform = rotation;
			document.getElementById('fuelGaugePointer').style.webkitTransform = rotation;
		}
};

ocargo.Animation.prototype.serializeAnimationQueue = function(blocks){
    var replacer = function (key, val) {
        function clone(obj) {
			var target = {};
			for (var i in obj) {
				if (obj.hasOwnProperty(i)) {
					target[i] = obj[i];
				}
			}
			return target;
		}

		if (key == "previousNode" || key == "currentNode"){
			// Replaces array of nodes to array of coordinates as nodes have circular reference
			var result = [];
			var modifiedVal = clone(val); // val has to be cloned to avoid modifying the original nodes
			for(var i = 0 ; i < modifiedVal.connectedNodes.length ; i++){
				result.push({coordinate: modifiedVal.connectedNodes[i].coordinate});
			}
			modifiedVal.connectedNodes = result;
			return modifiedVal;
		}
		if (val instanceof ocargo.Node){
			return val.coordinate;
		}
		return val;
	};

	/* Use for calculating algorithm score as blocks used by mobile are not added to Blockly workspace */
	ocargo.game.mobileBlocks = blocks.length;
	ocargo.game.runProgramAndPrepareAnimation(blocks);

	var result = ocargo.animation.animationQueue;
	/* Replaces type with functionType if the animation is callable as api cannot pass function to mobile app */
	for (var i = 0 ; i < result.length ; i ++ ){
		for (var j = 0 ; j < result[i].length ; j++){
			if(result[i][j].functionType){
				result[i][j]["type"] = result[i][j].functionType;
				delete result[i][j]["functionType"];
			}
		}
	}

	var json = JSON.stringify(result, replacer);
	if(ocargo.utils.isIOSMode()){
		console.log(json);
        webkit.messageHandlers.handler.postMessage(json);
    }
	return json;
};

ocargo.Animation.prototype.setAnimationDuration = function(duration) {
	this.animationDuration = duration;
	this.drawing.setCharacterManoeuvreDuration(this.animationDuration);
};
