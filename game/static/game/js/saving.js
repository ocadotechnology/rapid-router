var ocargo = ocargo || {};

ocargo.Saving = function() {
    this.getListOfWorkspacesFromLocalStorage = function() {
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

ocargo.Saving.prototype.retrieveListOfWorkspaces = function(callback) {
	if (USER_STATUS === 'TEACHER' ||  USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'SOLO_STUDENT') {
		$.ajax({
	        url: '/rapidrouter/workspace/load_list/',
	        type: 'GET',
	        dataType: 'json',
	        success: function(json) {
	        	callback(null, json);
	        },
	        error: function(xhr,errmsg,err) {
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

ocargo.Saving.prototype.retrieveWorkspace = function(id, callback) {
	if (USER_STATUS === 'TEACHER' ||  USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'SOLO_STUDENT') {
		$.ajax({
            url: '/rapidrouter/workspace/load/' + id + '/',
            type: 'GET',
            dataType: 'json',
            success: function(json) {
                callback(null, json);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	}
    //setTimeout is used here in order to ensure that these lines of code are executed after the correct tab is selected
    else if (localStorage) {
        setTimeout(function(){
            var json = JSON.parse(localStorage.getItem('blocklySavedWorkspaceXml-' + id));
            callback(null, json);
        }, 0)
	}
    else {
		callback("Not logged in and no local storage available");
	}
};

ocargo.Saving.prototype.deleteWorkspace = function(id, callback) {
    csrftoken = $.cookie('csrftoken');
	if (USER_STATUS === 'TEACHER' ||  USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'SOLO_STUDENT') {
		$.ajax({
            url: '/rapidrouter/workspace/delete/' + id + '/',
            type: 'POST',
            dataType: 'json',
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function(json) {
                callback(null, json);
            },
            error: function(xhr,errmsg,err) {
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

ocargo.Saving.prototype.saveWorkspace = function(workspace, id, callback) {
    csrftoken = $.cookie('csrftoken');
	if (USER_STATUS === 'TEACHER' ||  USER_STATUS === 'SCHOOL_STUDENT' || USER_STATUS === 'SOLO_STUDENT') {
		$.ajax({
            url: '/rapidrouter/workspace/save/' + (id ? (id + '/') : ''),
            type: 'POST',
            dataType: 'json',
            data: workspace,
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            success: function(json) {
                callback(null, json);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	} 
    else if (localStorage) {
		if(!id) {
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

ocargo.Saving.prototype.retrieveListOfLevels = function(callback) {
    csrftoken = $.cookie('csrftoken');
	$.ajax({
        url: '/rapidrouter/level_editor/level/get_all/',
        type: 'GET',
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(json) {
        	callback(null, json.ownedLevels, json.sharedLevels);
        },
        error: function(xhr, errmsg, err) {
        	callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.retrieveLevel = function(id, callback) {
    csrftoken = $.cookie('csrftoken');
	$.ajax({
        url: '/rapidrouter/level_editor/level/get/' + id + '/',
        type: 'GET',
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(json) {
            callback(null, json.level, json.owned);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.retrieveRandomLevel = function(data, callback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: "/rapidrouter/level_editor/level/random/",
        type: "GET",
        dataType: 'json',
        data: data,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(json) {
            callback(null, json);
        },
        error: function(xhr, errmsg, err) {
           callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

 ocargo.Saving.prototype.deleteLevel = function(id, callback) {
    csrftoken = $.cookie('csrftoken');
	$.ajax({
        url: '/rapidrouter/level_editor/level/delete/' + id + '/',
        type: 'POST',
        dataType: 'json',
        data: {csrfmiddlewaretoken : $.cookie('csrftoken')},
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(json) {
            callback(null, json.ownedLevels, json.sharedLevels);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.saveLevel = function(level, id, anonymous, callback) {
    csrftoken = $.cookie('csrftoken');
    level.anonymous = anonymous;
	$.ajax({
        url: '/rapidrouter/level_editor/level/save/' + (id ? (id + '/') : ''),
        type: 'POST',
        dataType: 'json',
        data: {data: JSON.stringify(level)},
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(json) {
            callback(null, json.levelID, json.ownedLevels, json.sharedLevels);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
    delete level.anonymous;
};

ocargo.Saving.prototype.getSharingInformation = function(levelID, callback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: '/rapidrouter/level_editor/level/get_sharing_information/' + levelID + '/',
        type: 'GET',
        dataType: 'json',
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(json) {
            callback(null, json);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.shareLevel = function(levelID, recipientData, callback) {
    csrftoken = $.cookie('csrftoken');
    $.ajax({
        url: '/rapidrouter/level_editor/level/share/' + levelID + '/',
        type: 'POST',
        dataType: 'json',
        data: recipientData,
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        success: function(json) {
            callback(null, json);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
    delete recipientData.csrfmiddlewaretoken;
};
