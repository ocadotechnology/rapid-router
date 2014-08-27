
var ocargo = ocargo || {};


// Object containing helper js objects (buttons etc).
ocargo.jsElements = {
    image: function(url, width) {
        return "<img src='" + url + "'width='" + width + "'>";
    },
    redirectButton: function(location, label) {
        return '<button onclick="window.location.href=' + location + '">' + label + '</button>';
    },
    closebutton: function(label) {
        return '<br><br> <button onclick="document.getElementById(' + "'close-modal'" +
        ').click()">' + label +'</button>';
    },
    buttonHelpButton: '<button onclick="ocargo.Drawing.showButtonHelp();">Button help</button>'
};


//FIXME: actually use Django's internationalisation framework.
ocargo.messages = {
    nextEpisode: function(episode) {
        return "Well done, you've completed the episode! <br> Are you ready for the next " + 
            "challenge? <br><br>" + 
            ocargo.jsElements.redirectButton("'/rapidrouter/episode/" + episode + "'",
                                             'Next episode') + " " +
            ocargo.jsElements.redirectButton("'/rapidrouter/'", "Home");
    },

    loggedOutWarning: "You are not logged in. Your progress won't be saved.",

    lastLevel: "That's all we've got for you right now. Carry on the fun by creating your own " +
        "challenges. <br><br>" +
        ocargo.jsElements.redirectButton("'/rapidrouter/level_editor'", "Create your own map!") + 
        " " + ocargo.jsElements.redirectButton("'/rapidrouter/'", "Home"),

    tooManyBlocks: "Whoops! You used too many blocks.",
    ohNo: "Oh no!",
    winTitle: "You win!",
    failTitle: "Oh dear! ",
    tryagainLabel: "Try again",
    needHint: "Are you stuck? Do you need help?",
    terminated: "Program terminated!",
    crashed: "Your program crashed!",
    compilationError: "Your program doesn't look quite right...",
    stoppingTitle: "Stopping...",

    outOfFuel : "You ran out of fuel! Try to find a shorter route to the destination.",
    outOfInstructions: "The van ran out of instructions before it reached a destination.",
    throughRedLight: "Uh oh, you just sent the van through a red light! Stick to the Highway " +
        "Code - the van must wait for green.",
    offRoad : function(correctSteps){
        if (correctSteps === 1) {
            return "Your first move was right. What went wrong after that?";
        }
        else {
            return "Your first " + correctSteps + " moves worked. What went wrong after that?";
        }
    },

    // Level editor.
    levelEditorTitle: "Welcome to the Level editor! ",
    levelEditorSubtitle: "Click  " +
        ocargo.jsElements.image('/static/game/image/icons/help.svg', 20) +
        "Help for clues on getting started. ",
    noStartOrEndSubtitle: "You forgot to mark the start and end points.",
    noStartOrEnd: "Click on Mark start or Mark end then select the square where you want the " +
        "road to start or end.",
    somethingWrong: "Something is wrong...", 
    noStartEndRouteSubtitle: "There is no way to get from the start to the destination.",
    noStartEndRoute: "Edit your level to allow the driver to get to the end.",
    levelEditorMobileSubtitle: "To draw a road, place two fingers on the " +
        "square you want the road to start from. Then, keeping one finger in place, drag the the " +
        "other to the square you want the road to end on. <br><br> Do this as many times as you " +
        "like to add new sections of road.",
    levelEditorPCSubtitle: "To draw a road, click on the square you want the " +
        "road to start from. Then, without letting go of the mouse button, drag to the square " +
        "you'd like the road to end on. <br><br> Do this as many times as you like to add new " +
        "sections of road.",
    trafficLightsWarning: "You should not use traffic lights unless you already have covered " +
        "them in your classroom activities or played the levels from the Traffic Lights episode. ",
    levelEditorHelpText: "In <b>Map</b> menu, click <b>Mark start</b> and select a square for " +
        "your road to start from. Make sure you use <b>Mark end</b> to select a final " +
        "destination. <br><br> To remove road, click the <b>Delete road</b> button and select a " +
        "section to get rid of. <br><br> Select <b>Scenery</b> and choose trees, bushes and more " +
        "to place around your road. These will show in the top left corner - drag them into " +
        "place. <br><br> Choose a character to play with from the <b>Character</b> menu. <br><br>" +
        "Select which blocks you want to use to create a route from the <b>Blocks</b> menu. " +
        "<br><br> When you're ready click <b>Play</b>. <br><br> You can also save your road or " +
        "share it with a friend. <br><br> Don't forget you can set a fuel limit for your level! ", 
    notLoggedIn: function(activity) {
        return "Unfortunately you need to be logged in to " + activity + " levels. You can log on <a href='/play/'>here</a>."
    },
    internetDown: "Could not connect to server. Your internet might not be working properly.",
    notSaved: "Please save your level before continuing!",
    notOwned: "You do not own this level. If you would like to share it you will first have to " +
        "save your own copy!",
    changesSinceLastSave: "Please save your latest changes!",
    saveOverwriteWarning: function(newName, onNoFunction, onYesFunction) {
        return "Level " + newName + " already exists. Are you sure you want to overwrite it? " + 
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
    pathLonger: "Try finding a shorter route to the destination",
    algorithmScore: "Algorithm score: ",
    algorithmLonger: "Try creating a simpler program.",
    algorithmShorter: "That solution isn't quite right. Read the level instructions or click Help.",
    scorePerfect: "Congratulations! You've aced it.",

    // Malormed program.
    whileConditionError: "Perhaps try looking at your 'repeat' blocks?",
    whileBodyError: "Perhaps try looking at your 'repeat' blocks?",
    ifConditionError: "Perhaps try looking at your 'if' blocks?",
    procMissingNameError: "Perhaps try looking at your 'define' blocks?",
    procMissingBodyError: "Perhaps try looking at your 'define' blocks?",
    procDupNameError: "Perhaps try checking the names of your 'define' blocks?",
    procCallNameError: "Perhaps try checking the names in your 'call' blocks?"
};
