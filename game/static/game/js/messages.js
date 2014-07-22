var ocargo = ocargo || {};

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
    nextEpisodeButton: function(episode) {
        return "Well done, you've completed the episode!<br>" +
           "Are you ready for the next challenge? <br><br> " +
           '<button onclick="window.location.href=' + "'/game/episode/" + ocargo.level.nextEpisode +
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
    levelEditorMainText: "Click on the 'Mark Start' or 'Mark End' then select the road of the " +
        "segment you want to serve as the starting or ending point. <br>" +
        "To delete a part of the road, click on the 'Delete Mode' button and remove it the same " +
        "way you added it.<br>" +
        "To add bushes or trees, click their image and one will be added in the top left corner " +
        "of the map, from there you can drag it wherever you like!<br>" +
        "Don't forget to choose a name and fuel limit for your level! It will " +
        "make sharing it with others much easier for you.",
    levelEditorTitle: "Welcome to the Level Editor!",

    /* Scoring */
    totalScore: function(score, maxScore) {
        return "Your total score: " + score + "/" + maxScore;
    },
    pathScore: function(score, maxScore) {
        return "Travelled path score: " + score + "/" + maxScore;
    },
    pathLonger: "Try finding a shorter path to reach the destination.",
    algorithmScore: function(score, maxScore) {
        return "Algorithm score: " + score + "/" + maxScore;
    },
    algorithmLonger: "Try creating a smaller program to improve the score",
    algorithmShorter: "That's not exactly the solution we wanted you to come up with. Read the " +
        "level instructions for more information.",
    scorePerfect: "Congratulations! You've aced it.",
    
    /* Malformed program */
    whileConditionError: "Perhaps try looking at your 'While' blocks?",
    whileBodyError: "Perhaps try looking at your 'While' blocks?",
    ifConditionError: "Perhaps try looking at your 'If' blocks?",
    procMissingNameError: "Perhaps try looking at your 'Proc' blocks?",
    procMissingBodyError: "Perhaps try looking at your 'Proc' blocks?",
    procDupNameError: "Perhaps try checking the names of your 'Proc' blocks?",
    procCallNameError: "Perhaps try checking the names in your 'Call' blocks?"
}
