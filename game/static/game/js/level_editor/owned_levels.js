'use strict';

var ocargo = ocargo || {};

ocargo.OwnedLevels = function(saveState) {
    this.listeners = [];
    this.levels = [];
    this.saveState = saveState;
    this.saving = new ocargo.Saving();
};

ocargo.OwnedLevels.prototype.addListener = function(listener) {
    this.listeners.push(listener);
};

ocargo.OwnedLevels.prototype._updateListeners = function() {
    this.listeners.forEach(function (listener) {
        listener(this.levels);
    }.bind(this))
};

ocargo.OwnedLevels.prototype._updateLevels = function(levels) {
    this.levels = levels;
    this._updateListeners();
};

ocargo.OwnedLevels.prototype.update = function() {
    function processError(error) {
        console.error(error);
        ocargo.Drawing.startInternetDownPopup();
    }

    this.saving.retrieveOwnedLevels(this._updateLevels.bind(this), processError);
};

ocargo.OwnedLevels.prototype.save = function(level, id, finishedCallback) {
    function handleError(error) {
        console.error(error);
        ocargo.Drawing.startInternetDownPopup();
    }

    this.saving.saveLevel(level, id, false, function(newId) {
        delete level.name;

        this.saveState.saved(level, newId);

        this.update();

        if (finishedCallback) {
            finishedCallback();
        }
        window.location.replace("/rapidrouter/level_editor/" + newId +"/");
    }.bind(this), handleError.bind(this));
};

ocargo.OwnedLevels.prototype.deleteLevel = function(levelId) {
    function handleError(error) {
        console.error(error);
        ocargo.Drawing.startInternetDownPopup();
    }

    this.saving.deleteLevel(levelId, function () {
        this.saveState.deleted(levelId);

        this.update();
    }.bind(this), handleError.bind(this));
};
