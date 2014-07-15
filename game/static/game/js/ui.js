'use strict';

var ocargo = ocargo || {};

ocargo.SimpleUi = function() {};

ocargo.SimpleUi.prototype.setVanToFront = function(previousNode, startNode, van) {
    resetVanImage(previousNode, startNode, van);
};

ocargo.SimpleUi.prototype.renderMap = function(map) {
    renderTheMap(map);
};

ocargo.SimpleUi.prototype.renderVans = function(vans) {
	renderTheVans(vans);
}
