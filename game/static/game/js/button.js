'use strict';

var ocargo = ocargo || {};

ocargo.button = {};

// Returns the html code for a button which closes the popup using handlebars precompiled templates
ocargo.button.dismissButtonHtml = function(id, label){
    return Handlebars.templates['button-dismiss']({label: label, id: id});
};

// Returns the html code for a button which redirects to location using handlebars precompiled templates
ocargo.button.redirectButtonHtml = function(id, location, label){
    return Handlebars.templates['button-redirect']({id: id, location: location, label: label});
};

// Returns the html code for a button which shows the try again message and closes the popup
ocargo.button.tryAgainButtonHtml = function(){
    return ocargo.button.dismissButtonHtml('try_again_button', gettext('Try again'));
};