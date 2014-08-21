
var ocargo = ocargo || {};


// Object containing helper js objects (buttons etc).
ocargo.jsElements = {
    redirectButton: function(location, label) {
        return '<button onclick="window.location.href=' + location + '">' + label + '</button>';
    },
    closebutton: function(label) {
        return '<br><br> <button onclick="document.getElementById(' + "'close-modal'" +
        ').click()">' + label +'</button>';
    },
    buttonHelpButton: '<button onclick="ocargo.Drawing.showButtonHelp();">Button help</button>',
};


//FIXME: actually use Django's internationalisation framework.
ocargo.messages = {
    nextEpisode: function(episode) {
        return "Well done, you've completed the episode! <br> Are you ready for the next " + 
            "challenge? <br><br>" + 
            ocargo.jsElements.redirectButton("'/game/episode/" + episode + "'", 'Next episode') + " " +
            ocargo.jsElements.redirectButton("'/game/'", "Home");
    },

    lastLevel: "Congratulations, you’ve completed the game! Carry on the fun by creating your " +
        "own map. <br><br>" +
        ocargo.jsElements.redirectButton("'/game/level_editor'", "Create your own map!") + " " +
        ocargo.jsElements.redirectButton("'/game/'", "Home"),

    tooManyBlocks: "Whoops! You used too many blocks.",
    ohNo: "Oh no!",
    winTitle: "You win!",
    failTitle: "Oh dear! ",
    tryagainLabel: "Try again",
    needHint: "Are you stuck? Need a hint?",
    terminated: "Program terminated!",
    crashed: "Your program crashed!",
    compilationError: "Your program doesn't look quite right...",
    stoppingTitle: "Stopping...",

    outOfFuel : "You ran out of fuel! Try to find a shorter path to the destination.",
    outOfInstructions: "The van ran out of instructions before it reached the house.",
    throughRedLight: "Uh oh, you just sent the van through a red light! Stick to the Highway " +
        "Code - the van must wait for green.",
    offRoad : function(correctSteps){
        if (correctSteps === 1) {
            return "Your first move worked.";
        }
        else {
            return "Your first " + correctSteps + " moves worked.";
        }
    },

    // Level editor.
    noStartOrEndSubtitle: "You forgot to mark the start and end points.",
    noStartOrEnd: "Click on the 'Mark Start' or 'Mark End' then select the road of the segment " +
        "you want to serve as the starting or ending point.",
    somethingWrong: "Something is wrong...", 
    noStartEndRouteSubtitle: "There is no way to get from the starting point to the destination.",
    noStartEndRoute: "Edit your level to allow the driver to get to the end.",
    levelEditorMobileSubtitle: "Click on the point you want this part of the road to start and, " +
        "while holding it, click on the square you want it to end.",
    levelEditorPCSubtitle: "Click on the point you want this part of the road to start then " +
        "click where you would like it to end.",
    levelEditorHelpText: "Click on the 'Mark Start' or 'Mark End' then select the road of the " +
        "segment you want to serve as the starting or ending point. <br><br>" +
        "To delete a part of the road, click on the 'Delete Mode' button and remove it the same " +
        "way you added it.<br><br>" +
        "To add bushes or trees, click their image and one will be added in the top left corner " +
        "of the map, from there you can drag it wherever you like!<br><br>" +
        "Don't forget to choose a name and fuel limit for your level! It will " +
        "make sharing it with others much easier for you.",
    levelEditorTitle: "Welcome to the Level Editor!",
    notLoggedIn: "Unfortunately you need to be logged in to share levels.",
    internetDown: "Could not connect to server. Your internet might not be working properly.",
    notSaved: "Please save your level before continuing!",
    notOwned: "You do not own this level. If you would like to share it you will first have to save your own copy!",
    changesSinceLastSave: "Please save your latest changes!",
    saveOverwriteWarning: function(newName, onNoFunction, onYesFunction) {
        return "Level " + newName + " already exists. Are you sure you want to overwrite it? THIS DOESN'T WORK" + 
        "<br><br>" + 
        '<button onclick="onYesFunction(); document.getElementById(' + '"close-modal"' +').click();">Yes</button>' +
        '<button onclick=document.getElementById(' + '"close-modal"' +').click();">No</button>';
    },
    shareSuccessful: "Your level has been successfully shared!",

    // Scoring.
    totalScore: function(score, maxScore) {
        return "Your total score: " + score + "/" + maxScore;
    },
    pathScore: "Route score: ",
    pathLonger: "Try finding a shorter path to the destination.",
    algorithmScore: "Algorithm score: ",
    algorithmLonger: "Try creating a simpler program.",
    algorithmShorter: "That solution isn't quite right. Read the level instructions and hints " +
        "for clues.",
    scorePerfect: "Congratulations! You've aced it.",

    // Malormed program.
    whileConditionError: "Perhaps try looking at your 'repeat' blocks?",
    whileBodyError: "Perhaps try looking at your 'repeat' blocks?",
    ifConditionError: "Perhaps try looking at your 'if' blocks?",
    procMissingNameError: "Perhaps try looking at your 'define' blocks?",
    procMissingBodyError: "Perhaps try looking at your 'define' blocks?",
    procDupNameError: "Perhaps try checking the names of your 'define' blocks?",
    procCallNameError: "Perhaps try checking the names in your 'call' blocks?",
};
