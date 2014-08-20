var ocargo = ocargo || {};

//FIXME: actually use Django's internationalisation framework.
//FIXME: remove functionality (buttons, JS) from messages.
ocargo.messages = {
    tryagain : "Either remove the incorrect blocks or click clear and try again!",
    closebutton: function(label) {
        return '<br><br> <button onclick="document.getElementById(' + "'close-modal'" +
        ').click()">' + label +'</button>';
    },
    nextLevelButton: function(level) {
        return '<button onclick="window.location.href=' + "'/game/" + level + "'" + 
            '">Next Level</button>';
    },
    buttonHelpButton: '<button onclick="ocargo.Drawing.showButtonHelp();">Button help</button>',
    nextEpisodeButton: function(episode) {
        return "Well done, you've completed the episode!<br>" +
           "Are you ready for the next challenge? <br><br> " +
           '<button onclick="window.location.href=' + "'/game/episode/" + episode +
            "'" + '"">Next episode</button> </center>' + '<button onclick="window.location.href=' +
            "'/home/'" + '"">Home</button>';
    },
    lastLevel: "Congratulations, that's all we've got for you for now! <br>" +
        "Why not try creating your own road? <br><br> <button onclick=" +
        '"window.location.href=' + "'/game/level_editor'" + 
        '"">Create your own map!</button> </center>' + '<button onclick="window.location.href=' +
        "'/home/'" + '"">Home</button>',

    tooManyBlocks: "You used too many blocks!",
    ohNo: "Oh no!",
    winTitle: "You win!",
    failTitle: "Oh dear! :(",
    tryagainLabel: "Try again",
    needHint: "Are you stuck? Need a hint?",
    terminated: "Program terminated!",
    crashed: "Your program crashed!",
    compilationError: "Your program doesn't look quite right!",
    stoppingTitle: "Stopping...",

    outOfFuel : "You ran out of fuel! Try to find a shorter path to the destination.",
    outOfInstructions: "You ran out of instructions without reaching your destination!",
    throughRedLight: "You just directed the van through a red traffic light! Stick to the " +
        "highway code!",
    offRoad : function(correctSteps){
        if (correctSteps === 1) {
            return "Your first move worked.";
        }
        else {
            return "Your first " + correctSteps + " moves worked.";
        }
    },

    /* Level editor */
    noStartOrEndSubtitle: "You forgot to mark the start and end points.",
    noStartOrEnd: "Click on the 'Mark Start' or 'Mark End' then select the road of the segment " +
        "you want to serve as the starting or ending point.",
    somethingWrong: "Something is wrong.", 
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
    shareSuccessful: "Your level has been succesfully shared!",

    /* Scoring */
    totalScore: function(score, maxScore) {
        return "Your total score: " + score + "/" + maxScore;
    },
    pathScore: "Travelled path score: ",
    pathLonger: "Try finding a shorter path to reach the destination.",
    algorithmScore: "Algorithm score: ",
    algorithmLonger: "Try creating a smaller program to improve the score",
    algorithmShorter: "That's not exactly the solution we wanted you to come up with. Read the " +
        "level instructions for more information.",
    scorePerfect: "Congratulations! You've aced it.",
    
    /* Malformed program */
    whileConditionError: "Perhaps try looking at your 'repeat' blocks?",
    whileBodyError: "Perhaps try looking at your 'repeat' blocks?",
    ifConditionError: "Perhaps try looking at your 'if' blocks?",
    procMissingNameError: "Perhaps try looking at your 'define' blocks?",
    procMissingBodyError: "Perhaps try looking at your 'define' blocks?",
    procDupNameError: "Perhaps try checking the names of your 'define' blocks?",
    procCallNameError: "Perhaps try checking the names in your 'call' blocks?",

    buttonHelp: '<div id="buttonHelp">\
                    <p><img src="/static/game/image/buttons/menu/play.svg" alt="Play" /> Plays your program</p>\
                    <p><img src="/static/game/image/buttons/menu/pause.svg" alt="Pause" /> Pauses your program</p>\
                    <p><img src="/static/game/image/buttons/menu/stop.svg" alt="Stop" /> Stops your program</p>\
                    <p><img src="/static/game/image/buttons/menu/step.svg" alt="Step" /> Steps to the next command in your program</p>\
                    <p><img src="/static/game/image/buttons/menu/save.svg" alt="Save" /> Saves your program</p>\
                    <p><img src="/static/game/image/buttons/menu/load.svg" alt="Load" /> Loads your program</p>\
                    <p><img src="/static/game/image/buttons/menu/clear.svg" alt="Clear" /> Clears your program, removing all instructions</p>\
                    <p><img src="/static/game/image/buttons/menu/toggle_console.svg" alt="Toggle Console" /> Switches between Blockly and Python</p>\
                    <p><img src="/static/game/image/buttons/menu/big_code_mode.svg" alt="Big Code Mode" /> Makes Blockly blocks bigger</p>\
                    <p><img src="/static/game/image/buttons/menu/help.svg" alt="Show Help" /> Shows level hints and button help</p>\
                    <p><img src="/static/game/image/buttons/menu/muted.svg" alt="Muted / Unmute" /> Shows that the game is muted (click to unmute)</p>\
                    <p><img src="/static/game/image/buttons/menu/unmuted.svg" alt="Unmuted / Mute" /> Shows that the game is unmuted (click to mute)</p>\
                    <p><img src="/static/game/image/buttons/menu/quit.svg" alt="Quit" /> Quits the level, returning to the level selection page</p>\
                  </div>',
};
