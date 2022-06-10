var ocargo = ocargo || {};

ocargo.Saving = function () {};

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
    else {
        callback("Not logged in and no local storage available");
    }
};

ocargo.Saving.prototype.deleteWorkspace = function (id, callback) {
    csrftoken = Cookies.get('csrftoken');
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
    } else {
        callback("Not logged in and no local storage available");
    }
};

ocargo.Saving.prototype.saveWorkspace = function (workspace, id, callback) {
    csrftoken = Cookies.get('csrftoken');
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
    else {
        callback("Not logged in and no local storage available");
    }
};


/****************************/
/* Levels (level_editor.js) */
/****************************/

ocargo.Saving.prototype._retrieveLevels = function (url, callback, errorCallback) {
    csrftoken = Cookies.get('csrftoken');
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
    csrftoken = Cookies.get('csrftoken');
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

ocargo.Saving.prototype.loadSolution = function (levelID, callback) {
    $.ajax({
        url: Urls.load_workspace_solution(levelID),
        type: 'GET',
        dataType: 'json',
        success: function (json) {
            callback(null, json);
        },
        error: function (xhr, errmsg, err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.retrieveRandomLevel = function (data, callback) {
    csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url: Urls.generate_random_map_for_editor(),
        type: "POST",
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
    csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url: Urls.delete_level_for_editor(id),
        type: 'POST',
        dataType: 'json',
        data: {csrfmiddlewaretoken: Cookies.get('csrftoken')},
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
    csrftoken = Cookies.get('csrftoken');
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
    csrftoken = Cookies.get('csrftoken');
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

