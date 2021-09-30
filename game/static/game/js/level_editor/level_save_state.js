'use strict';


var ocargo = ocargo || {};

ocargo.LevelSaveState = function() {
    this.savedState = null;
    this.owned = null;
    this.id = -1;
};

ocargo.LevelSaveState.prototype.loaded = function(owned, level, id) {
    this.owned = owned;
    this.savedState = JSON.stringify(level);
    this.id = id;
};

ocargo.LevelSaveState.prototype.saved = function(level, id) {
    this.owned = true;
    this.savedState = JSON.stringify(level);
    this.id = id;
};

ocargo.LevelSaveState.prototype.deleted = function (id) {
    if (id == this.id) {
        this.id = -1;
        this.savedState = null;
        this.owned = false;
    }
};

ocargo.LevelSaveState.prototype.isOwned = function () {
    return this.owned;
};

ocargo.LevelSaveState.prototype.isCurrentLevel = function (levelId) {
    return levelId == this.id;
};

ocargo.LevelSaveState.prototype.isSaved = function () {
    return this.savedState;
};

ocargo.LevelSaveState.prototype.hasChanged = function (currentState) {
    return currentState !== this.savedState;
};
