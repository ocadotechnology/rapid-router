/*
Code for Life

Copyright (C) 2016, Ocado Innovation Limited

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
var ocargo = ocargo || {};

// Object containing helper js objects (buttons etc).
ocargo.jsElements = {
    image: function(url, class_) {
        return "<img src='" + url + "'class='" + class_ + "'>";
    }
};


//FIXME: actually use Django's internationalisation framework.
ocargo.messages = {

    tooManyBlocks: "Whoops. You used too many blocks.",
    ohNo: "Oh no!",
    terminated: "Program terminated.",
    crashed: "Your program crashed.",
    stoppingTitle: "Stopping...",

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
    noRoadSubtitle: "You forgot to create a road. ",
    noRoad: "In " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/map.svg', 'popupIcon') +
        "<b>Map</b> menu, click on  " +
	ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/add_road.svg', 'popupIcon') +
	"<b>Add road</b>. Draw a road by clicking on a square then dragging to another square.", 
    noStartEndRouteSubtitle: "There is no way to get from the start to the destination.",
    noStartEndRoute: "Edit your level to allow the driver to get to the end.",
    noBlocksSubtitle: "You haven't selected any blocks to use in your level.",
    noBlocks: "Go to " +
        ocargo.jsElements.image(ocargo.Drawing.imageDir + 'icons/blockly.svg', 'popupIcon') +
        "<b>Code</b> and select some to use. Remember to include the move and turn commands!",
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
        "can only be placed on dead ends. You need a road first before adding a starting point.<br> Make sure you use " +
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
            " levels. You can log on <a href='"+Urls.play()+"'>here</a>.";
    },
    independentStudentSharing:  "Sorry but as an independent student you'll need to join a school or club to " +
        "share your levels with others.",
    notSaved: "Please save your level before continuing!",
    notOwned: "You do not own this level. If you would like to share it you will first have to " +
        "save your own copy! ",
    changesSinceLastSave: "Please save your latest changes! ",
    saveOverwriteWarning: function(newName) {
        return "Level '" + newName + "' already exists. Are you sure you want to overwrite it?";
    },
    shareSuccessful: "Your level has been successfully shared! ",

    addNewLine: function(arr){
        var html = '';
        for(var i = 0 ; i < arr.length ; i++ ){
            html += arr[i] + '<br>';
        }
        return html;
    }
};
