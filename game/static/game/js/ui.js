'use strict';

var ocargo = ocargo || {};

ocargo.SimpleUi = function() {
};

ocargo.SimpleUi.prototype.setVanToFront = function() {
    resetVan();
};

ocargo.SimpleUi.prototype.renderMap = function(map) {
    renderTheMap(map);
};
