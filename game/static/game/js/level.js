'use strict';

var ocargo = ocargo || {};

ocargo.Level = function(map, vans, ui, nextLevel, nextEpisode) {
    this.levelId = null;
    this.map = map;
    this.ui = ui;
    this.correct = 0;
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

ocargo.Level.prototype.play = function(program) {

    this.attemptData = {};

    var threadStacks = [];
    var procedureStack = {};

    if (ocargo.level.blockLimit &&
            ocargo.blocklyControl.getBlocksCount() > ocargo.level.blockLimit) {
        enableDirectControl();
        startPopup("Oh no!", "", ocargo.messages.tooManyBlocks);
        sendAttempt(0);
        return;
    }

    this.initAttemptData(program);

    for (var i = 0; i < program.threads.length; i++) {
        program.threads[i].startBlock.selectWithConnected();
    }

    this.program = program;
    stepProgram(this);
};

ocargo.Level.prototype.initAttemptData = function(program) {
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

function stepProgram(level) {
    var terminationDelay = 1000;
    try {
        if (level.program.canStep()) {
            level.correct++;
            level.program.step(level);

            var animationLength = 0;
            for (var i = 0; i < THREADS; i++) {
                var action = level.program.threads[i].currentAction;
                level.handleAction(action, level.program.threads[i], level.vans[i]);

                if (action.animationLength > animationLength) {
                    animationLength = action.animationLength;
                }
            }

            setTimeout(function () {stepProgram(level)}, animationLength);
        } 
        else if (level.hasWon()) {
            setTimeout(function () {programTerminated(level, true)}, terminationDelay);
        } 
        else if (level.program.isTerminated) {
            setTimeout(function () {programTerminated(level, false, ocargo.messages.terminated)}, terminationDelay);
            $("#myModal > .title").text(ocargo.messages.stoppingTitle);
        } 
        else {
            setTimeout(function () {programTerminated(level, false, ocargo.messages.outOfInstructions)}, terminationDelay);
            level.program.terminate();
        }
    } 
    catch (error) {
        level.fail(ocargo.messages.crashed);
        level.program.terminate();
        enableDirectControl();
        throw error;
    }
}

ocargo.Level.prototype.hasWon = function() {
    for (var i = 0; i < THREADS; i++) {
        if (this.vans[i].currentNode !== this.map.destination) {
            return false;
        }
    }
    return true;    
}

ocargo.Level.prototype.handleAction = function(action, thread, van) {
    console.debug('Calculating next node for action ' + action.name);

    if (action === ocargo.EMPTY_ACTION) {
        return;
    }

    var prevNode = van.previousNode;
    var currNode = van.currentNode;
    var nextNode = action.getNextNode(prevNode, currNode);
    if (!nextNode) {
        var n = this.correct - 1;
        ocargo.blocklyControl.blink();
        this.fail(ocargo.messages.xcorrect(n) + ocargo.messages.tryagain);

        thread.terminate();
        return; //TODO: animate the crash
    } else if (nextNode !== currNode && directedThroughRedTrafficLight(prevNode, currNode, nextNode)){
        this.fail(ocargo.messages.throughRedTrafficLight);
        thread.terminate();
        return; //TODO: play police siren sound
    }
    
    if (van.fuel === 0) {
        this.fail(ocargo.messages.nofuel);
        thread.terminate();
        return;
    }

    van.move(nextNode, action);
};
 
function programTerminated(level, result, msg) {
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
        if(tl.sourceNode == previousNode && tl.state == tl.RED){
            return true;
        }
    }
    return false;
}
