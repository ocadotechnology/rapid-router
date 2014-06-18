'use strict';

var ocargo = ocargo || {};

ocargo.SimpleUi = function() {
};

ocargo.SimpleUi.prototype.setVanToFront = function(previousNode, startNode) {
    resetVan(previousNode, startNode);
};

ocargo.SimpleUi.prototype.renderMap = function(map) {
    renderTheMap(map);
};
