'use strict';

var ocargo = ocargo || {};

var TERMINATION_DELAY = 1000;
var FAILS_BEFORE_HINT = 3;


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
    this.blockHandlers = [];
    for (var i = 0; i < THREADS; i++) {
        this.blockHandlers.push(new ocargo.BlocklyControl.BlockHandler(i));
    }

    console.debug(MODEL_SOLUTION);
};

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
    ocargo.blocklyControl.clearAllSelections();
    for (var i = 0; i < THREADS; i++) {
        this.blockHandlers[i].selectBlock(this.program.threads[i].startBlock);
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

    try {
        this.program.step(this);   
    }
    catch(error) {
        setTimeout(function () {programFinished(level, false, ocargo.messages.programCrashed)}, TERMINATION_DELAY);
        return;
    }

    var longestAnimation = 0;
    for (var i = 0; i < THREADS; i++) {
        this.blockHandlers[i].selectBlock(this.program.threads[i].currentBlock);

        var action = this.program.threads[i].currentAction;
        var successful = this.handleAction(action, this.program.threads[i], this.vans[i], callback);
        if (!successful) {
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

// Function to be used by python with support for animating/highlighlting correct line of code editor to follow...
ocargo.Level.prototype.handlePythonAction = function(action, thread, van) {
    console.info("Will do some action highlighting of line no. " + Sk.currLineNo);
    highlightLine(Sk.currLineNo - 1);
    return ocargo.level.handleAction(action, thread, van);
};

ocargo.Level.prototype.handleAction = function(action, thread, van, callback) {
    console.debug('Calculating next node for action ' + action.name);
    var level = this;

    if (action === ocargo.EMPTY_ACTION) {
        return true;
    }

    var nextNode = action.getNextNode(van.previousNode, van.currentNode);

    if (!nextNode) {
        var n = this.numStepsCorrect - 1;
        ocargo.blocklyControl.makeBlockBlink(thread.currentBlock);
         //TODO: animate the crash
        setTimeout(function () {programFinished(level, false, ocargo.messages.offRoad(level.numStepsCorrect))}, TERMINATION_DELAY);
        return false;
    } 
    else if (this.isVanGoingThroughRedLight(van, nextNode)){
        //TODO: play police siren sound
        setTimeout(function () {programFinished(level, false, ocargo.messages.throughRedLight)}, TERMINATION_DELAY);
        return false;
    }
    else if(van.fuel === 0) {
        //TODO: play empty tank noise
        setTimeout(function () {programFinished(level, false, ocargo.messages.outOfFuel)}, TERMINATION_DELAY);
        return false;
    }
    else {
        van.move(nextNode, action, callback);
        return true;
    }
};

ocargo.Level.prototype.getTrafficLightState = function(previousNode, currentNode) {
    for(var i = 0; i < currentNode.trafficLights.length; i++) {
        var tl = currentNode.trafficLights[i];
        if(tl.sourceNode == previousNode) {
            return tl.state;
        }
    }
}

/** Conditions **/

// Condition checker to be used by python with support for animating/highlighting correct line of code editor to follow...
ocargo.Level.prototype.checkAndHighlightPythonCondition = function(conditionFunction, van, action) {
    console.info("Will do some condition highlighting of line no. " + Sk.currLineNo);
    return conditionFunction(van, action);
}

ocargo.Level.prototype.isVanGoingThroughRedLight = function(van, nextNode){
    var previousNode = van.previousNode;
    var currentNode = van.currentNode;
    if(currentNode === nextNode) {
        return false;
    }
    else {
        // TODO fix creating a new traffic light object each time
        return this.isTrafficLightInState(previousNode, currentNode, ocargo.TrafficLight.RED);
    }
}

ocargo.Level.prototype.isTrafficLightInState = function(previousNode, currentNode, state) {
    return state === this.getTrafficLightState(previousNode, currentNode);
}

ocargo.Level.prototype.isVanAtRedLight = function(van) {
    return this.isTrafficLightInState(van.previousNode, van.currentNode, ocargo.TrafficLight.RED);
}

ocargo.Level.prototype.isVanAtGreenLight = function(van) {
    return this.isTrafficLightInState(van.previousNode, van.currentNode, ocargo.TrafficLight.GREEN);
}

ocargo.Level.prototype.isActionValidForVan = function(van, action) {
    return action.getNextNode(van.previousNode, van.currentNode);
}

ocargo.Level.prototype.isVanAtDeadEnd = function(van) {
    var actions = [ocargo.FORWARD_ACTION, ocargo.TURN_LEFT_ACTION, ocargo.TURN_RIGHT_ACTION];
    for (var i = 0; i < actions.length; i++) {
        var nextNode = actions[i].getNextNode(van.previousNode, van.currentNode);
        if (nextNode) {
            return false;
        }
    }
    return true;
}

ocargo.Level.prototype.isVanAtDestination = function(van) {
    return van.currentNode === ocargo.level.map.destination;
}



function programFinished(level, result, msg) {
    enableDirectControl();
    for (var i = 0; i < THREADS; i++) {
        level.blockHandlers[i].deselectCurrent();
    }

    if (result) {
        levelWon(level);
    }
    else {
        levelFailed(level,msg);
    }
}