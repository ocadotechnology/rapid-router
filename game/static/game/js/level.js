'use strict';

var ocargo = ocargo || {};

var TERMINATION_DELAY = 1000;

var ERRORS = {
  THROUGH_RED_LIGHT: "Through red light", 
  OFF_ROAD: "Off road", 
  OUT_OF_FUEL: "Out of fuel"
};


ocargo.Level = function(map, vans, ui, nextLevel, nextEpisode) {
    this.levelId = null;
    this.map = map;
    this.ui = ui;
    this.numStepsCorrect = 0;
    this.attemptData = {};
    this.pathFinder = new ocargo.PathFinder(map, MODEL_SOLUTION);
    this.fails = 0;
    this.hintOpened = false;
    this.nextLevel = nextLevel;
    this.nextEpisode = nextEpisode;
    this.vans = vans;
    console.debug(MODEL_SOLUTION);
};

ocargo.Level.prototype.failsBeforeHintBtn = 3;

ocargo.Level.prototype.playProgram = function(program) {

    if (ocargo.level.blockLimit &&
            ocargo.blocklyControl.getBlocksCount() > ocargo.level.blockLimit) {
        enableDirectControl();
        startPopup("Oh no!", "", ocargo.messages.tooManyBlocks);
        sendAttempt(0);
        return;
    }

    this.numStepsCorrect = 0;
    this.program = program;
    this.initAttemptData(program);

    this.selectStartBlocks();    

    playOutProgram(this);
};

ocargo.Level.prototype.selectStartBlocks = function() {
    for (var i = 0; i < this.program.threads.length; i++) {
        this.program.threads[i].startBlock.selectWithConnected();
    }
}

ocargo.Level.prototype.initAttemptData = function(program) {
    this.attemptData = {};
    this.attemptData.level = ocargo.level.levelId.toString();
    
    var parsedProcedures = [];
    for (var i = 0; i < program.procedures.length; i++) {
        parsedProcedures.push(program.procedures[i].parse());
    }

    var parsedThreads = [];
    for (var i = 0; i < program.threads.length; i++) {
        var parsedThread = [];
        for (var j = 0; j < program.threads[i].stack[0].length; j++) {
            parsedThread.push(program.threads[i].stack[0][j].parse());
        }
        parsedThreads.push(parsedThread);
    }   

    this.attemptData.commandStack = JSON.stringify(parsedThreads);
    this.attemptData.procedureStack = JSON.stringify(parsedProcedures);
}

function playOutProgram(level) {
    var animationLength = level.stepProgram();
    if (animationLength) {
        setTimeout(function () {playOutProgram(level)}, animationLength);
    }
}

ocargo.Level.prototype.stepProgram = function(callback) {

    var level = this;

    if (!this.program.canStep()) {
        this.program.terminate();
        setTimeout(function () {programFinished(level, false, ocargo.messages.outOfInstructions)}, TERMINATION_DELAY);
        return;
    }

    this.program.step(this);

    var longestAnimation = 0;
    for (var i = 0; i < THREADS; i++) {
        var action = this.program.threads[i].currentAction;

        try {
            this.handleAction(action, this.program.threads[i], this.vans[i], callback);
        }
        catch (error) {
            this.program.terminate();
            if (error === ERRORS.OFF_ROAD) {
                setTimeout(function () {programFinished(level, false, ocargo.messages.offRoad(level.numStepsCorrect))}, TERMINATION_DELAY);
            }
            else if (error === ERRORS.THROUGH_RED_LIGHT) {
                setTimeout(function () {programFinished(level, false, ocargo.messages.throughRedLight)}, TERMINATION_DELAY);
            }
            else if (error === ERRORS.OUT_OF_FUEL) {
                setTimeout(function () {programFinished(level, false, ocargo.messages.outOfFuel)}, TERMINATION_DELAY);
            }
            else {
                setTimeout(function () {programFinished(level, false, ocargo.messages.programCrashed)}, TERMINATION_DELAY);
                throw error;
            }
            return;
        }

        if (action.animationLength > longestAnimation) {
            longestAnimation = action.animationLength;
        }
    }    
    
    this.numStepsCorrect++;

    if (!this.program.canStep() && this.hasWon()) {
        setTimeout(function () {programFinished(level, true)}, TERMINATION_DELAY);
        return;
    }
    return longestAnimation;
}

ocargo.Level.prototype.hasWon = function() {
    for (var i = 0; i < THREADS; i++) {
        if (this.vans[i].currentNode !== this.map.destination) {
            return false;
        }
    }
    return true;    
}

ocargo.Level.prototype.handleAction = function(action, thread, van, callback) {
    console.debug('Calculating next node for action ' + action.name);

    if (action === ocargo.EMPTY_ACTION) {
        return;
    }

    var prevNode = van.previousNode;
    var currNode = van.currentNode;
    var nextNode = action.getNextNode(prevNode, currNode);
    if (!nextNode) {
        var n = this.numStepsCorrect - 1;
        ocargo.blocklyControl.blink();
         //TODO: animate the crash
        throw ERRORS.OFF_ROAD;
    } 
    if (nextNode !== currNode && directedThroughRedTrafficLight(prevNode, currNode, nextNode)){
        //TODO: play police siren sound
        throw ERRORS.THROUGH_RED_LIGHT;
    }
    if (van.fuel === 0) {
        throw ERRORS.OUT_OF_FUEL;
    }

    van.move(nextNode, action, callback);
};
 
function programFinished(level, result, msg) {
    if (result) {
        level.win();
    }
    else {
        level.fail(msg);
    }
}

ocargo.Level.prototype.win = function() {
    console.debug('You win!');

    var scoreArray = ocargo.level.pathFinder.getScore();

    sendAttempt(scoreArray[0]);
    ocargo.sound.win();

    var message = '';
    if (ocargo.level.nextLevel != null) {
      message = ocargo.messages.nextLevelButton(ocargo.level.nextLevel);
    } else {
        if (ocargo.level.nextEpisode != null && ocargo.level.nextEpisode !== "") {
            message = ocargo.messages.nextEpisodeButton(ocargo.level.nextEpisode);
        } else {
            message = ocargo.messages.lastLevel;
        }
    }

    enableDirectControl();

    startPopup("You win!", scoreArray[1], message);
};

ocargo.Level.prototype.fail = function(msg) {
    var title = 'Oh dear! :(';
    $('#play > span').css('background-image', 'url(/static/game/image/arrowBtns_v3.svg)');
    console.debug(title);
    enableDirectControl();
    ocargo.sound.failure();
    startPopup(title, '', msg + ocargo.messages.closebutton("Try again"));
    var level = this;
    level.fails++;
    if (level.fails >= level.failsBeforeHintBtn) {
        var hintBtns = $("#hintPopupBtn");
        if (hintBtns.length === null || hintBtns.length === 0) {
            $("#myModal > .mainText").append('<p id="hintBtnPara">' +
                '<button id="hintPopupBtn">' + ocargo.messages.needHint + '</button>' + 
                '</p><p id="hintText">' + HINT + '</p>');
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
    }
    
    sendAttempt(0);
};

function sendAttempt(score) {

    // Send out the submitted data.
    if (ocargo.level.levelId) {
        var attemptData = JSON.stringify(ocargo.level.attemptData);

        $.ajax({
            url : '/game/submit',
            type : 'POST',
            dataType: 'json',
            data : {
                attemptData : attemptData,
                csrfmiddlewaretoken :$( '#csrfmiddlewaretoken' ).val(),
                score : score,
                workspace : ocargo.blocklyControl.serialize()
            },
            success : function(json) {
            },
            error : function(xhr,errmsg,err) {
                console.debug(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    }
    return false;
}

function directedThroughRedTrafficLight(previousNode, currentNode, nextNode){
    for(var i = 0; i < currentNode.trafficLights.length; i++){
        var tl = currentNode.trafficLights[i];
        if(tl.sourceNode == currentNode && currentNode != nextNode && tl.state == tl.RED){
            return true;
        }
    }
    return false;
}
