/*
Code for Life

Copyright (C) 2015, Ocado Limited

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

ocargo.Animation = function(model, decor) {
    this.model = model;
    this.decor = decor;
	this.activeCows = []; // cows currently displayed on map
	this.scalingModifier = [];
	this.crashed = false;
	this.speedUp = false;

	this.FAST_ANIMATION_DURATION = 125;
	this.REGULAR_ANIMATION_DURATION = 500;

	this.setAnimationDuration(this.REGULAR_ANIMATION_DURATION);

    // timer identifier for pausing
    this.playTimer = -1;

    ocargo.drawing.clearPaper();
    ocargo.drawing.renderMap(this.model.map);
    ocargo.drawing.renderDecor(this.decor);
    ocargo.drawing.renderOrigin(this.model.map.startingPosition());
    ocargo.drawing.renderDestinations(this.model.map.getDestinations());
    ocargo.drawing.renderTrafficLights(this.model.trafficLights);
	ocargo.drawing.renderCharacter();

     this.updateFuelGauge(100);
};

ocargo.Animation.prototype.isFinished = function() {
	return this.finished;
};

ocargo.Animation.prototype.removeCows = function() {
	for (var i = 0; i < this.activeCows.length; i++) {
		ocargo.drawing.removeCow(this.activeCows[i]);
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
		ocargo.drawing.transitionTrafficLight(tl.id, tl.state, 0);
	}

	this.removeCows();

	for(var i = 0; i < this.model.map.destinations.length; i++) {
		var destination = this.model.map.destinations[i];
		ocargo.drawing.transitionDestination(destination.id, false, 0);
	}

	ocargo.drawing.reset();
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
	return duration + this.animationDuration;
};

ocargo.Animation.prototype.performAnimation = function(animation) {
	// animation length is either custom set (for each element) or generic
	var animationDuration = animation.animationLength || this.animationDuration;
	//console.log("Type: " + animation.type + " Description: " + animation.description);

    switch (animation.type) {
		case 'callable':
			animationDuration = animation.animationLength || 0;
			animation.functionCall();
			break;
		case 'crashSound':
			animationDuration = 0;
			animation.functionCall(this.animationDuration / 2);
			break;
		case 'van':
            ocargo.drawing.scrollToShowCharacter();

            // move van
            switch (animation.vanAction) {
            	case 'FORWARD':
            		animationDuration = ocargo.drawing.moveForward(null, this.scalingModifier.shift());
					animationDuration = this._addPause(animationDuration);
					break;
            	case 'TURN_LEFT':
					animationDuration = ocargo.drawing.turnLeft(null, this.scalingModifier.shift());
					animationDuration = this._addPause(animationDuration);
            		break;
            	case 'TURN_RIGHT':
					animationDuration = ocargo.drawing.turnRight(null, this.scalingModifier.shift());
					animationDuration = this._addPause(animationDuration);
            		break;
            	case 'TURN_AROUND_FORWARD':
            		animationDuration = ocargo.drawing.turnAround('FORWARD');
					animationDuration = this._addPause(animationDuration);
            		break;
            	case 'TURN_AROUND_RIGHT':
					animationDuration = ocargo.drawing.turnAround('RIGHT');
					animationDuration = this._addPause(animationDuration);
            		break;
            	case 'TURN_AROUND_LEFT':
            		animationDuration = ocargo.drawing.turnAround('LEFT');
					animationDuration = this._addPause(animationDuration);
            		break;
            	case 'WAIT':
            		ocargo.drawing.wait(animationDuration);
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
            		animationDuration = ocargo.drawing.crash(animation.previousNode, animation.currentNode,
            			animation.attemptedAction, animation.startNode);
            		break;
				case 'COLLISION_WITH_COW':
					this.crashed = true;
					//Update animationLength with time van moves before crashing
					animationDuration = ocargo.drawing.collisionWithCow(animation.previousNode, animation.currentNode,
						animation.attemptedAction, animation.startNode);
					break;
            	case 'DELIVER':
            		ocargo.drawing.deliver(animation.destinationID, animationDuration);
					break;
            	case 'OBSERVE':
            		break;
            }
            // Check if fuel update present
            if (typeof animation.fuel != 'undefined') {
                this.updateFuelGauge(animation.fuel);
            }
			break;
		case 'popup':
			var title = "";
			var leadMsg = animation.popupMessage;
			var buttons = '';

			// sort popup...
			switch (animation.popupType) {
				case 'WIN':
					title = ocargo.messages.winTitle;
					var levelMsg = [];

					if (!animation.pathScoreDisabled) {
						levelMsg.push(ocargo.messages.pathScore + ocargo.Drawing.renderCoins(animation.routeCoins)
							+ "<span id=\"routeScore\">" + animation.pathLengthScore + "/" + animation.maxScoreForPathLength + "</span>");
					}

					if (animation.maxScoreForNumberOfInstructions != 0){
						levelMsg.push(ocargo.messages.algorithmScore +
							ocargo.Drawing.renderCoins(animation.instrCoins)
                            + "<span id=\"algorithmScore\">" + animation.instrScore + "/" + animation.maxScoreForNumberOfInstructions + "</span>");
					}

					levelMsg.push(ocargo.messages.totalScore(animation.totalScore, animation.maxScore));

					levelMsg.push(leadMsg);

					if (animation.performance != "scorePerfect") {
						buttons += ocargo.button.tryAgainButtonHtml();
					}

					if (BLOCKLY_ENABLED && PYTHON_ENABLED && ocargo.game.currentTabSelected == ocargo.game.tabs.blockly) {
						levelMsg.push(ocargo.messages.nowTryPython);
						buttons += ocargo.button.addDismissButtonHtml('Close');
					} else {
						// If there exists next level, add animation button which redirects the user to that
						if (NEXT_LEVEL_URL) {
							buttons += ocargo.button.redirectButtonHtml('next_level_button', NEXT_LEVEL_URL, 'Next Level');
						} else {
							/*
							 This is the last level of the episode. If there exists animation next episode, add button to
							 redirect user to it or level selection page.
							 If this is animation default level and there isn't animation next episode, user has reached the end of the
							 game. Add button to encourage users to create their own levels or redirect to level
							 selection page.
							 */

							if (NEXT_EPISODE) {
								levelMsg.push(ocargo.messages.nextEpisode(NEXT_EPISODE, RANDOM));
								buttons += ocargo.jsElements.nextEpisodeButton(NEXT_EPISODE, RANDOM);
					        } else if(DEFAULT_LEVEL) {
					            levelMsg.push(ocargo.messages.lastLevel);
								buttons += ocargo.button.redirectButtonHtml('next_level_button', "/rapidrouter/level_editor/", "Create your own map!");
								buttons += ocargo.button.redirectButtonHtml('home_button', "/rapidrouter/", "Home");
					        } else if (IS_RANDOM_LEVEL) {
					            levelMsg.push(ocargo.messages.anotherRandomLevel);
								buttons += ocargo.button.redirectButtonHtml('retry_button', window.location.href, 'Have more fun!');
								buttons += ocargo.button.redirectButtonHtml('home_button', "/rapidrouter/", "Home");
							}
					    }
					}
					leadMsg = ocargo.messages.addNewLine(levelMsg);
					break;
				case 'FAIL':
					title = ocargo.messages.failTitle;
					buttons = ocargo.button.tryAgainButtonHtml();
					break;
				case 'WARNING':
					buttons = ocargo.button.tryAgainButtonHtml();
					break;
			}
			var otherMsg = "";
			if (animation.popupHint) {
				buttons += '<button class="navigation_button long_button" id="hintPopupBtn"><span>' + ocargo.messages.needHint + '</span></button>';
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
			ocargo.drawing.transitionTrafficLight(animation.id, animation.colour, animationDuration/2);
			break;
		case 'cow':
            this.numberOfCowsOnMap++;
			var activeCow = ocargo.drawing.renderCow(animation.id, animation.coordinate, animation.node, animationDuration, animation.cowType);
			this.activeCows.push(activeCow);
			break;
        case 'cow_leave':
            this.numberOfCowsOnMap--;
			var cow = this._extractCowAt(animation.coordinate);
            ocargo.drawing.removeCow(cow, animationDuration);  // remove it from drawing
			break;
		case 'console':
			ocargo.pythonControl.appendToConsole(animation.text);
			break;
	}
	return animationDuration;
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

ocargo.Animation.prototype.updateFuelGauge = function(fuelPercentage) {
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
    var movementSpeed = GRID_SPACE_SIZE / this.animationDuration;
	ocargo.drawing.setMovementSpeed(movementSpeed);
}