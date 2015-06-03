'use strict';

var ocargo = ocargo || {};

ocargo.button = {};

// Returns the html code for a button which closes the popup using handlebars precompiled templates
ocargo.button.getDismissButtonHtml = function(label){
    return Handlebars.templates['button-dismiss']({label: label});
}

// Returns the html code for a button which redirects to location using handlebars precompiled templates
ocargo.button.getRedirectButtonHtml = function(location, label){
    return Handlebars.templates['button-redirect']({location: location, label: label});
}

// Returns the html code for a button which shows the try again message and closes the popup
ocargo.button.getTryAgainButtonHtml = function(){
    return ocargo.button.getDismissButtonHtml(ocargo.messages.tryagainLabel)
}