/*
Code for Life

Copyright (C) 2015, Ocado Limited

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
'use strict';

var ocargo = ocargo || {};

ocargo.OwnedLevels = function(saveState) {
    this.listeners = [];
    this.levels = [];
    this.saveState = saveState;
};

ocargo.OwnedLevels.prototype.addListener = function(listener) {
    this.listeners.push(listener);
};

ocargo.OwnedLevels.prototype.updateListeners = function() {
    this.listeners.forEach(function (listener) {
        listener(this.levels);
    }.bind(this))
};

ocargo.OwnedLevels.prototype._updateLevels = function(levels) {
    this.levels = levels;
    this.updateListeners();
};

ocargo.OwnedLevels.prototype.update = function() {
    function processError(error) {
        console.error(error);
        ocargo.Drawing.startInternetDownPopup();
    }

    ocargo.saving.retrieveOwnedLevels(this._updateLevels.bind(this), processError);
};

ocargo.OwnedLevels.prototype.save = function(level, id, finishedCallback) {
    ocargo.saving.saveLevel(level, id, false, function(error, newId, ownedLevels, sharedLevels) {
        if (error !== null) {
            console.error(error);
            ocargo.Drawing.startInternetDownPopup();
            return;
        }

        delete level.name;

        this.saveState.saved(level, newId);

        this._updateLevels(ownedLevels);

        if (finishedCallback) {
            finishedCallback();
        }
    }.bind(this));
};

ocargo.OwnedLevels.prototype.deleteLevel = function(levelId) {
    ocargo.saving.deleteLevel(levelId, function (err, ownedLevels, sharedLevels) {
        if (err !== null) {
            console.error(err);
            ocargo.Drawing.startInternetDownPopup();
            return;
        }

        this.saveState.deleted(levelId);

        this._updateLevels(ownedLevels);
    }.bind(this));
};