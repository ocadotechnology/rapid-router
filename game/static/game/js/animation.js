/*
Code for Life

Copyright (C) 2016, Ocado Innovation Limited

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

ADDITIONAL TERMS – Section 7 GNU General Public Licence

This licence does not grant any right, title or interest in any “Ocado” logos,
trade names or the trademark “Ocado” or any other trademarks or domain names
owned by Ocado Innovation Limited or the Ocado group of companies or any other
distinctive brand features of “Ocado” as may be secured from time to time. You
must not distribute any modification of this program using the trademark
“Ocado” or claim any affiliation or association with Ocado or its employees.

You are not authorised to use the name Ocado (or any of its trade names) or
the names of any author or contributor in advertising or for publicity purposes
pertaining to the distribution of this program, without the prior written
authorisation of Ocado.

Any propagation, distribution or conveyance of this program must include this
copyright notice and these terms. You must not misrepresent the origins of this
program; modified versions of the program must be marked as such and not
identified as the original program.
*/
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
    this.drawing.renderDecor(this.decor);
    this.drawing.renderOrigin(this.model.map.startingPosition());
    this.drawing.renderDestinations(this.model.map.getDestinations());
    this.drawing.renderTrafficLights(this.model.trafficLights);
	this.drawing.renderCharacter();

     this._updateFuelGauge(100);
};

ocargo.Animation.prototype.isFinished = function() {
	return this.finished;
};

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
				//Special case for crashing into cow as the van travel less before crashing
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
							buttons += ocargo.button.redirectButtonHtml('next_level_button', NEXT_LEVEL_URL, gettext('Next Level'));
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
				buttons += '<button class="navigation_button long_button" id="hintPopupBtn"><span>' + gettext('Are you stuck? Do you need help?') + '</span></button>';
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
		case 'cow':
            this.numberOfCowsOnMap++;
			var activeCow = this.drawing.renderCow(animation.id, animation.coordinate, animation.node, duration, animation.cowType);
			this.activeCows.push(activeCow);
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
        if (cow.coordinate == coordinate) {
            this.activeCows.splice(i, 1);   // remove cow from array
            return cow;
        }
    }
};

ocargo.Animation.prototype._updateFuelIfPresent = function(animation) {
	if (typeof animation.fuel != 'undefined') {
		this._updateFuelGauge(animation.fuel);
	}
};

ocargo.Animation.prototype._updateFuelGauge = function(fuelPercentage) {
    var degrees = ((fuelPercentage / 100) * 240) - 120;
    var rotation = 'rotate(' + degrees + 'deg)';
    document.getElementById('fuelGaugePointer').style.transform = rotation;
    document.getElementById('fuelGaugePointer').style.webkitTransform = rotation;
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