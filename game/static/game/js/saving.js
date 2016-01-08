/*
 Code for Life

 Copyright (C) 2015, Ocado Innovation Limited

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

ocargo.Saving = function () {
    this.getListOfWorkspacesFromLocalStorage = function () {
        var query = /blocklySavedWorkspaceXml-([0-9]+)$/;
        var i, results = [];
        for (i in localStorage) {
            if (localStorage.hasOwnProperty(i)) {
                var matches = query.exec(i);
                if (matches) {
                    var json = JSON.parse(localStorage.getItem(i));
                    results.push({
                        id: matches[1],
                        name: json.name,
                        workspace: json.workspace
                    });
                }
            }
        }
        return results;
    };
};

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

/************************/
/* Workspaces (game.js) */
/************************/

ocargo.Saving.prototype.retrieveListOfWorkspaces = function (callback) {
    if (USER_STATUS === 'TEACHER' || USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'INDEPENDENT_STUDENT') {
        $.ajax({
            url: Urls.load_list_of_workspaces(),
            type: 'GET',
            dataType: 'json',
            success: function (json) {
                callback(null, json);
            },
                  error: function (xhr, errmsg, err) {
          callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    }
    else if (localStorage) {
        var results = this.getListOfWorkspacesFromLocalStorage();
        callback(null, results);
    }
    else {
        callback("Not logged in and no local storage available");
    }
};

ocargo.Saving.prototype.retrieveWorkspace = function (id, callback) {
    if (USER_STATUS === 'TEACHER' || USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'INDEPENDENT_STUDENT') {
        $.ajax({
            url: Urls.load_workspace(id),
            type: 'GET',
            dataType: 'json',
            success: function (json) {
                callback(null, json);
            },
            error: function (xhr, errmsg, err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    }
    //setTimeout is used here in order to ensure that these lines of code are executed after the correct tab is selected
    else if (localStorage) {
        setTimeout(function () {
            var json = JSON.parse(localStorage.getItem('blocklySavedWorkspaceXml-' + id));
            callback(null, json);
        }, 0)
    }
    else {
        callback("Not logged in and no local storage available");
    }
};

ocargo.Saving.prototype.deleteWorkspace = function (id, callback) {
    csrftoken = $.cookie('csrftoken');
    if (USER_STATUS === 'TEACHER' || USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'INDEPENDENT_STUDENT') {
        $.ajax({
            url: Urls.delete_workspace(id),
            type: 'POST',
            dataType: 'json',
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function (json) {
                callback(null, json);
            },
            error: function (xhr, errmsg, err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    } else if (localStorage) {
        localStorage.removeItem('blocklySavedWorkspaceXml-' + id);
        var results = this.getListOfWorkspacesFromLocalStorage();
        callback(null, results);
    } else {
        callback("Not logged in and no local storage available");
    }
};

ocargo.Saving.prototype.saveWorkspace = function (workspace, id, callback) {
    csrftoken = $.cookie('csrftoken');
    if (USER_STATUS === 'TEACHER' || USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'INDEPENDENT_STUDENT') {
        $.ajax({
            url: (id ? Urls.save_workspace(id) : Urls.save_workspace()),
            type: 'POST',
            dataType: 'json',
            data: workspace,
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function (json) {
                callback(null, json);
            },
            error: function (xhr, errmsg, err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
    }
    else if (localStorage) {
        if (!id) {
            // Need to generate a unique integer, for our purposes this should do
            id = new Date().getTime();
        }

        localStorage.setItem('blocklySavedWorkspaceXml-' + id, JSON.stringify(workspace));

        var results = this.getListOfWorkspacesFromLocalStorage();
        callback(null, results);
    }
    else {
        callback("Not logged in and no local storage available");
    }
};


/****************************/
/* Levels (level_editor.js) */
/****************************/

ocargo.Saving.prototype._retrieveLevels = function (url, callback, errorCallback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: url,
        type: 'GET',
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (json) {
            callback(json);
        },
        error: function (xhr, errmsg, err) {
            errorCallback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.retrieveOwnedLevels = function (callback, errorCallback) {
    this._retrieveLevels(Urls.owned_levels(), callback, errorCallback);
};

ocargo.Saving.prototype.retrieveSharedLevels = function (callback, errorCallback) {
    this._retrieveLevels(Urls.shared_levels(), callback, errorCallback);
};

ocargo.Saving.prototype.retrieveLevel = function (id, callback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: Urls.load_level_for_editor(id),
        type: 'GET',
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (json) {
            callback(null, json.level, json.owned);
        },
        error: function (xhr, errmsg, err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.retrieveRandomLevel = function (data, callback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: Urls.generate_random_map_for_editor(),
        type: "GET",
        dataType: 'json',
        data: data,
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (json) {
            callback(null, json);
        },
        error: function (xhr, errmsg, err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.deleteLevel = function (id, callback, errorCallback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: Urls.delete_level_for_editor(id),
        type: 'POST',
        dataType: 'json',
        data: {csrfmiddlewaretoken: $.cookie('csrftoken')},
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (json) {
            callback();
        },
        error: function (xhr, errmsg, err) {
            errorCallback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.saveLevel = function (level, id, anonymous, callback, errorCallback) {
    csrftoken = $.cookie('csrftoken');
    level.anonymous = anonymous;
    $.ajax({
        url: (id ? Urls.save_level_for_editor(id) : Urls.save_level_for_editor()),
        type: 'POST',
        dataType: 'json',
        data: {data: JSON.stringify(level)},
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (json) {
            callback(json.id);
        },
        error: function (xhr, errmsg, err) {
            errorCallback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
    delete level.anonymous;
};

ocargo.Saving.prototype.getSharingInformation = function (levelID, callback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: Urls.get_sharing_information_for_editor(levelID),
        type: 'GET',
        dataType: 'json',
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (json) {
            callback(null, json);
        },
        error: function (xhr, errmsg, err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.shareLevel = function (levelID, recipientData, callback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: Urls.share_level_for_editor(levelID),
        type: 'POST',
        dataType: 'json',
        data: recipientData,
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function (json) {
            callback(null, json);
        },
        error: function (xhr, errmsg, err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
    delete recipientData.csrfmiddlewaretoken;
};
