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
    terminated: "Program terminated.",
    crashed: "Your program crashed.",
    stoppingTitle: "Stopping...",

    // Level editor.
    trafficLightsWarning: "You need to complete level 44 before using a traffic light. ",
    shareSuccessful: "Your level has been successfully shared! "
};
