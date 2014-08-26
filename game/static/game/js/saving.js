var ocargo = ocargo || {};

ocargo.Saving = function() {};

/************************/
/* Workspaces (game.js) */
/************************/

ocargo.Saving.prototype.retrieveListOfWorkspaces = function(callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
	        url: '/rapidrouter/workspace',
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
	  	callback(null, results);
	} else {
		callback("Not logged in and no local storage available");
	}
};

ocargo.Saving.prototype.retrieveWorkspace = function(id, callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
            url: '/rapidrouter/workspace/' + id,
            type: 'GET',
            dataType: 'json',
            success: function(json) {
                callback(null, json.workspace);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	} else if (localStorage) {
		var json = JSON.parse(localStorage.getItem('blocklySavedWorkspaceXml-' + id));
		callback(null, json.workspace);
	} else {
		callback("Not logged in and no local storage available");
	}
};

ocargo.Saving.prototype.deleteWorkspace = function(id, callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
            url: '/rapidrouter/workspace/' + id,
            type: 'DELETE',
            success: function() {
                callback(null);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	} else if (localStorage) {
		localStorage.removeItem('blocklySavedWorkspaceXml-' + id);
		callback(null);
	} else {
		callback("Not logged in and no local storage available");
	}
};

ocargo.Saving.prototype.createNewWorkspace = function(name, workspace, callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
            url: '/rapidrouter/workspace',
            type: 'POST',
            contentType:"application/json; charset=utf-8",
            data: {
                name: name,
                workspace: workspace
            },
            success: function() {
                callback(null);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	} else if (localStorage) {
		// Need to generate a unique integer, for our purposes this should do
		var id = new Date().getTime();

		localStorage.setItem('blocklySavedWorkspaceXml-' + id, JSON.stringify({
			name: name,
			workspace: workspace
		}));

		callback(null);
	} else {
		callback("Not logged in and no local storage available");
	}
};

/****************************/
/* Levels (level_editor.js) */
/****************************/

ocargo.Saving.prototype.retrieveListOfLevels = function(callback) {
	$.ajax({
        url: '/rapidrouter/level_editor/level/get_all',
        type: 'GET',
        dataType: 'json',
        success: function(json) {
        	callback(null, json.ownedLevels, json.sharedLevels);
        },
        error: function(xhr, errmsg, err) {
        	callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.retrieveLevel = function(id, callback) {
	$.ajax({
        url: '/rapidrouter/level_editor/level/get/' + id,
        type: 'GET',
        dataType: 'json',
        success: function(json) {
            callback(null, json.level, json.owned);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.retrieveRandomLevel = function(data, callback) {
    $.ajax({
        url: "/rapidrouter/level_editor/level/random",
        type: "GET",
        dataType: 'json',
        data: data,
        success: function(json) {
            callback(null, json);
        },
        error: function(xhr, errmsg, err) {
           callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

 ocargo.Saving.prototype.deleteLevel = function(id, callback) {
	$.ajax({
        url: '/rapidrouter/level_editor/level/delete/' + id,
        type: 'POST',
        dataType: 'json',
        data: {csrfmiddlewaretoken : $.cookie('csrftoken')},
        success: function() {
            callback(null);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.saveLevel = function(level, id, callback) {
    level.csrfmiddlewaretoken = $.cookie('csrftoken');
	$.ajax({
        url: '/rapidrouter/level_editor/level/save' + (id ? '/' + id : ''),
        type: 'POST',
        dataType: 'json',
        data: level,
        success: function(json) {
            callback(null, json.levelID, json.ownedLevels, json.sharedLevels);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
    delete level.csrfmiddlewaretoken;
};

ocargo.Saving.prototype.getSharingInformation = function(levelID, callback) {
    $.ajax({
        url: '/rapidrouter/level_editor/level/get_sharing_information/' + levelID,
        type: 'GET',
        dataType: 'json',
        success: function(json) {
            callback(null, json.validRecipients, json.role);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
};

ocargo.Saving.prototype.shareLevel = function(levelID, recipientData, callback) {
    recipientData.csrfmiddlewaretoken = $.cookie('csrftoken'),
    $.ajax({
        url: '/rapidrouter/level_editor/level/share/' + levelID,
        type: 'POST',
        contentType:"application/json; charset=utf-8",
        dataType: 'json',
        data: recipientData,
        success: function(json) {
            callback(null, json.validRecipients, json.role);
        },
        error: function(xhr,errmsg,err) {
            callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
        }
    });
    delete recipientData.csrfmiddlewaretoken;
};