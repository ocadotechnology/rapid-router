'use strict';

var ocargo = ocargo || {};

ocargo.Animation = function(model, decor, numVans) {
    this.model = model;
    this.decor = decor;
    this.numVans = numVans;

    this.DEFAULT_ANIMATION_LENGTH = 500;

    // timer identifier for pausing
    this.playTimer = -1;

    ocargo.drawing.clearPaper();
    ocargo.drawing.renderMap(this.model.map);
    ocargo.drawing.renderDecor(this.decor);
    ocargo.drawing.renderVans(this.model.map.getStartingPosition(), this.numVans);
    ocargo.drawing.renderOrigin(this.model.map.getStartingPosition());
    ocargo.drawing.renderDestinations(this.model.map.getDestinations());
    ocargo.drawing.renderTrafficLights(this.model.trafficLights);

     this.updateFuelGauge(100);
};

ocargo.Animation.prototype.isFinished = function() {
	return this.finished;
};

ocargo.Animation.prototype.resetAnimation = function() {
	this.animationQueue = [[]];

	this.timestamp = 0;
	this.lastTimestamp = 0;
	this.isPlaying = false;
	this.currentlyAnimating = false;
	this.finished = false;

	// Reset the display
	for(var i = 0; i < this.model.trafficLights.length; i++) {
		var tl = this.model.trafficLights[i];
		ocargo.drawing.transitionTrafficLight(tl.id, tl.state, 0);
	}

	for(var i = 0; i < this.model.map.destinations.length; i++) {
		var destination = this.model.map.destinations[i];
		ocargo.drawing.transitionDestination(destination.id, false, 0);
	}

	for(var i = 0; i < THREADS; i++) {
		ocargo.drawing.skipOutstandingVanAnimationsToEnd(i);
		ocargo.drawing.setVanImagePosition(this.model.map.getStartingPosition(), i);
	}

	ocargo.drawing.removeWreckageImages();
};

ocargo.Animation.prototype.stepAnimation = function(callback, generalAnimationLength) {
	if (this.currentlyAnimating) {
		return;
	}

	this.currentlyAnimating = true;

	var timestampDelay = this.DEFAULT_ANIMATION_LENGTH;

	var timestampQueue = this.animationQueue[this.timestamp];

	if (timestampQueue) {
		// Perform all events for this timestamp
		while (timestampQueue.length > 0) {
			timestampDelay = this.performAnimation(timestampQueue.shift(), generalAnimationLength);
		}
		// And move onto the next timestamp
		this.timestamp += 1;
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
			self.stepAnimation(undefined, generalAnimationLength);
		}
	}, timestampDelay);
};

ocargo.Animation.prototype.playAnimation = function(generalAnimationLength) {
	if (!this.currentlyAnimating && !this.isPlaying && this.animationQueue.length > 0) {
		this.isPlaying = true;
		this.stepAnimation(undefined, generalAnimationLength);
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

ocargo.Animation.prototype.performAnimation = function(a, generalAnimationLength) {
	// animation length is either custom set (for each element), general (for the whole animation) or default
	var animationLength = a.animationLength || generalAnimationLength || this.DEFAULT_ANIMATION_LENGTH;
	//console.log("Type: " + a.type + " Description: " + a.description);
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
            	case 'TURN_AROUND_FORWARD':
            		animationLength *= 3;
            		ocargo.drawing.turnAround(vanID, 'FORWARD', animationLength);
            		break;
            	case 'TURN_AROUND_RIGHT':
            		animationLength *= 3;
            		ocargo.drawing.turnAround(vanID, 'RIGHT', animationLength);
            		break;
            	case 'TURN_AROUND_LEFT':
            		animationLength *= 3;
            		ocargo.drawing.turnAround(vanID, 'LEFT', animationLength);
            		break;
            	case 'WAIT':
            		ocargo.drawing.wait(vanID, animationLength);
            		break;
            	case 'CRASH':
            		ocargo.drawing.crash(vanID, animationLength, a.previousNode, a.currentNode,
            			a.attemptedAction, a.startNode);
                    animationLength += 100;
            		break;
            	case 'DELIVER':
            		ocargo.drawing.deliver(a.destinationID, animationLength);
            	case 'OBSERVE':
            		break;
            }
            // Check if fuel update present
            if (typeof a.fuel != 'undefined') {
                this.updateFuelGauge(a.fuel);
            }
			break;
		case 'popup':
			var title = "";
			var leadMsg = a.popupMessage;
			var buttons = '';

			// sort popup...
			switch (a.popupType) {
				case 'WIN':
					title = ocargo.messages.winTitle;
					var levelMsg = [];

					if (!a.pathScoreDisabled) {
						levelMsg.push(ocargo.messages.pathScore + ocargo.Drawing.renderCoins(a.routeCoins) + a.pathLengthScore + "/" + a.maxScoreForPathLength);
					}

					if (a.maxScoreForNumberOfInstructions != 0){
						levelMsg.push(ocargo.messages.algorithmScore +
							ocargo.Drawing.renderCoins(a.instrCoins) + a.instrScore + "/" + a.maxScoreForNumberOfInstructions);
					}

					levelMsg.push(ocargo.messages.totalScore(a.totalScore, a.maxScore));

					levelMsg.push(leadMsg);

					if(a.performance != "scorePerfect"){
						buttons += ocargo.button.getTryAgainButtonHtml();
					}

					if (BLOCKLY_ENABLED && PYTHON_ENABLED && ocargo.game.currentTabSelected == ocargo.game.tabs.blockly) {
						levelMsg.push(ocargo.messages.nowTryPython);
						buttons += ocargo.button.addDismissButtonHtml('Close');
					}
					else {
						// If there exists next level, add a button which redirects the user to that
						if (NEXT_LEVEL) {
							buttons += ocargo.button.getRedirectButtonHtml("'/rapidrouter/" + NEXT_LEVEL + "/'",
					        								     		'Next Level');
					    }
					    else {
							/*
							 This is the last level of the episode. If there exists a next episode, add button to
							 redirect user to it or level selection page.
							 If this is a default level and there isn't a next episode, user has reached the end of the
							 game. Add button to encourage users to create their own levels or redirect to level
							 selection page.
							 */

					        if (NEXT_EPISODE) {
					            levelMsg.push(ocargo.messages.nextEpisode(NEXT_EPISODE, RANDOM));
								buttons += ocargo.jsElements.nextEpisodeButton(NEXT_EPISODE, RANDOM);
					        }
					        else if(DEFAULT_LEVEL) {
					            levelMsg.push(ocargo.messages.lastLevel);
								buttons += ocargo.button.getRedirectButtonHtml("'/rapidrouter/level_editor/'", "Create your own map!");
								buttons += ocargo.button.getRedirectButtonHtml("'/rapidrouter/'", "Home");
					        }
					    }
					}
					leadMsg = ocargo.messages.addNewLine(levelMsg);
					break;
				case 'FAIL':
					title = ocargo.messages.failTitle;
					buttons = ocargo.button.getTryAgainButtonHtml();
					break;
				case 'WARNING':
					buttons = ocargo.button.getTryAgainButtonHtml();
					break;
			}
			var otherMsg = "";
			if (a.popupHint) {
				buttons += '<button class="navigation_button long_button" id="hintPopupBtn"><span>' + ocargo.messages.needHint + '</span></button>';
				otherMsg = '<div id="hintBtnPara">' + '</div><div id="hintText">' + HINT + '</div>';
			}
			ocargo.Drawing.startPopup(title, leadMsg, otherMsg, true, buttons);
			if (a.popupHint) {
				$("#hintPopupBtn").click( function(){
	                    $("#hintText").show(500);
	                    $("#hintBtnPara").hide();
	                    $("#hintPopupBtn").hide();
	                });
	        }
			break;
		case 'trafficlight':
			ocargo.drawing.transitionTrafficLight(a.id, a.colour, animationLength/2);
			break;
		case 'console':
			ocargo.pythonControl.appendToConsole(a.text);
			break;
	}

	return animationLength;
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
        webkit.messageHandlers.handler.postMessage(json);
    }
	return json;
}