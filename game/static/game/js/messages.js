
var ocargo = ocargo || {};

// Object containing helper js objects (buttons etc).
ocargo.jsElements = {
    image: function(url, class_) {
        return "<img src='" + url + "'class='" + class_ + "'>";
    },
    nextEpisodeButton: function(episode, random){
        return ocargo.button.getRedirectButtonHtml("'/rapidrouter/episode/" + episode + "/'",
                'Next episode') + (random ? ocargo.button.getRedirectButtonHtml("'/rapidrouter/levels/random/" + (episode-1) + "/'",
            'Random level') : "") +
            ocargo.button.getRedirectButtonHtml("'/rapidrouter/'", "Home");
    },

    buttonHelpButton: '<button onclick="ocargo.Drawing.showButtonHelp();">Button help</button>'
};


//FIXME: actually use Django's internationalisation framework.
ocargo.messages = {
    nextEpisode: function(episode, random) {
        return "Well done, you've completed the episode! <br> Are you ready for the next " + 
            "challenge? " + (random ? "Or try one of this episode's random levels!" : "") ;
    },

    loggedOutWarning: "You are not logged in. Your progress won't be saved.",
    nowTryPython: "Looks like you've got a route sorted using Blockly.<br><br>" +
        "Now go to the Python tab and see if you can do the same in Python! ",
    lastLevel: "That's all we've got for you right now. Carry on the fun by creating your own challenges.",

    illegalBlocks: "Sorry, this workspace has blocks in it that aren't allowed in this level!",
    tooManyBlocks: "Whoops! You used too many blocks.",
    ohNo: "Oh no!",
    winTitle: "You win!",
    failTitle: "Oh dear! ",
    tryagainLabel: "Try again",
    needHint: "Are you stuck? Do you need help?",
    terminated: "Program terminated!",
    crashed: "Your program crashed!",
    queryInfiniteLoop: "It looks as though your program's been running a while. Check your repeat loops are okay.",
    compilationError: "Your program doesn't look quite right...",
    stoppingTitle: "Stopping...",
    errorTitle: "Error",

    outOfFuel : "You ran out of fuel! Try to find a shorter route to the destination.",
    outOfInstructions: "The van ran out of instructions before it reached a destination.",
    throughRedLight: "Uh oh, you just sent the van through a red light! Stick to the Highway " +
        "Code - the van must wait for green.",
    alreadyDelivered: "You have already delivered to that destination! You must only deliver " +
        "once to each destination.",
    undeliveredDestinations: "There are destinations that have not been delivered to! " + 
        "Ensure you visit all destinations and use the deliver command at each one.",
    offRoad : function(correctSteps){
        if (correctSteps === 0) {
            return "Your first move was a crash. What went wrong?";
        }
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
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/help.svg', 'popupHelp') +
        "<b>Help</b> for clues on getting started. ",
    noStartOrEndSubtitle: "You forgot to mark the start and end points. ",
    noStartOrEnd: "In " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/map.svg', 'popupIcon') +
        "<b>Map</b> menu, click on  " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/origin.svg', 'popupIcon') + 
        "<b>Mark start</b> or " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/destination.svg', 'popupIcon') + 
        "<b>Mark end</b> then select the square where you want the road to start or end.",
    somethingWrong: "Something is wrong...", 
    noStartEndRouteSubtitle: "There is no way to get from the start to the destination.",
    noStartEndRoute: "Edit your level to allow the driver to get to the end.",
    noBlocksSubtitle: "You haven't selected any blocks to use in your level.",
    noBlocks: "Go to " + 
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/blockly.svg', 'popupIcon') +
        "<b>Blocks</b> and select some to use. Remember to include the move and turn commands!",
    levelEditorPCSubtitle: "To get started, draw a road. <br><br> Click on the square you want " +
        "the road to start from. Then, without letting go of the mouse button, drag to the " +
        "square you’d like the road to end on. <br> Do this as many times as you like to add " +
        "new sections of road. ",
    trafficLightsWarning: "You need to complete level 44 before using a traffic light. ",
    levelEditorHelpText: "In " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/map.svg', 'popupIcon') +
        "<b>Map</b> menu, click " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/origin.svg', 'popupIcon') + 
        "<b>Mark start</b> and select a square for your road to start from. The starting point " +
        "can only be placed on dead ends. <br> Make sure you use " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/destination.svg', 'popupIcon') + 
        "<b>Mark end</b> to select a final destination. <br><br> To remove road, click the " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/delete_road.svg', 'popupIcon') + 
        "<b>Delete road</b> button and select a section to get rid of. <br><br> Click " + 
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/random.svg', 'popupIcon') +
        "<b>Random</b> if you want the computer to create a random route for you.<br><br> Select " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/decor.svg', 'popupIcon') +
        "<b>Scenery</b> and choose trees, bushes and more to place around your road. These will " +
        "show in the top left corner - drag them into place. Delete items by dragging them into " + 
        "the bin in the bottom right. <br> To rotate a traffic light, " +
        "simply double click on it. <i>Remember, using the traffic lights is not covered until " +
        "level 44.</i><br><br> Choose a character to play with from the " + 
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/character.svg', 'popupIcon') +
        "<b>Character</b> menu. <br><br> Select which blocks of code you want to be used to " +
        "create a route for your character from the " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/blockly.svg', 'popupIcon') +
        "<b>Blocks</b> menu. <br><br> Setting a fuel level means the route will need to be short " +
        "enough for the fuel not to run out. When you're ready click " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/play.svg', 'popupIcon') +
        "<b>Play</b>, or " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/save.svg', 'popupIcon') +
        "<b>Save</b> your road or " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/share.svg', 'popupIcon') +
        "<b>Share</b> it with a friend. Don't forget to choose a good name for it! <br><br> " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/quit.svg', 'popupIcon') +
        "<b>Quit</b> will take you back to the Rapid Router homepage.",
    notLoggedIn: function(activity) {
        return "Unfortunately you need to be logged in to " + activity +
            " levels. You can log on <a href='/play/'>here</a>.";
    },
    soloSharing:  "Sorry but as an independent student you'll need to join a school or club to " +
        "share your levels with others.",
    internetDown: "Could not connect to server. Your internet might not be working properly.",
    notSaved: "Please save your level before continuing!",
    notOwned: "You do not own this level. If you would like to share it you will first have to " +
        "save your own copy! ",
    changesSinceLastSave: "Please save your latest changes! ",
    saveOverwriteWarning: function(newName) {
        return "Level '" + newName + "' already exists. Are you sure you want to overwrite it?";
    },
    shareSuccessful: "Your level has been successfully shared! ",

    // Scoring.
    totalScore: function(score, maxScore) {
        return "Your total score: " + score + "/" + maxScore;
    },
    pathScore: "Route score: ",
    pathLonger: "Try finding a shorter route to the destination. ",
    algorithmScore: "Algorithm score: ",
    algorithmLonger: "Try creating a simpler program. ",
    algorithmShorter: "That solution isn't quite right. Read the level instructions or click Help.",
    scorePerfect: "Congratulations! You've aced it. ",

    // Malormed program.
    whileConditionError: "Perhaps try looking at your 'repeat' blocks? ",
    whileBodyError: "Perhaps try looking at your 'repeat' blocks? ",
    ifConditionError: "Perhaps try looking at your 'if' blocks? ",
    procMissingNameError: "Perhaps try looking at your 'define' blocks? ",
    procMissingBodyError: "Perhaps try looking at your 'define' blocks? ",
    procDupNameError: "Perhaps try checking the names of your 'define' blocks? ",
    procCallNameError: "Perhaps try checking the names in your 'call' blocks? ",
    
    pythonCommands: "<p>Run the following commands on the van object v, e.g. v.move_forwards()</p>" +
        	"<div class=\"row\">" +
            "<div class=\"large-4 columns\">" +
                  "<p><b>Movement</b>" +
                  "<br>v.move_forwards()" +
                  "<br>v.turn_left()" +
                  "<br>v.turn_right()" +
                  "<br>v.turn_around()" +
                  "<br>v.wait()</p>" +
                "</div>" +
                "<div class=\"large-4 columns\">" +
                  "<p><b>Position</b>" +
                  "<br>v.at_dead_end()" +
                  "<br>v.at_destination()" +
                  "<br>v.at_red_traffic_light()" +
                  "<br>v.at_green_traffic_light()" +
                  "<br>v.at_traffic_light(c)" +
                  "<br><i>where c is 'RED' or 'GREEN'</i></p>" +
                "</div>" +
                "<div class=\"large-4 columns\">" +
                  "<p>" +
                  "<br>v.is_road_forward()" +
                  "<br>v.is_road_left()" +
                  "<br>v.is_road_right()" +
                  "<br>v.is_road(d)" +
                  "<br><i>where d is 'FORWARD'," +
                  "<br>'LEFT', or 'RIGHT'</i></p>" +
                "</div>" +
              "</div>"
};
