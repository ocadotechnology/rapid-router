var ocargo = ocargo || {};

function loadAllSavedWorkspaces(callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
	        url: '/game/workspace',
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
	        			workspace: json.workspace,
	        		});
	      		}
	    	}
	  	}
	  	callback(null, results);
	}
	else {
		callback("Not logged in and no local storage available");
	}
}

function loadWorkspace(id, callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
            url: '/game/workspace/' + id,
            type: 'GET',
            dataType: 'json',
            success: function(json) {
                callback(null, json.workspace);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	}
	else if (localStorage) {
		var json = JSON.parse(localStorage.getItem('blocklySavedWorkspaceXml-' + id));
		callback(null, json.workspace);
	}
	else {
		callback("Not logged in and no local storage available");
	}
}

function overwriteWorkspace(id, workspace, callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
            url: '/game/workspace/' + id,
            type: 'PUT',
            data: {
                workspace: workspace,
            },
            success: function() {
                callback(null);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	}
	else if (localStorage) {
		var value = localStorage.getItem('blocklySavedWorkspaceXml-' + id);
		if (value && value != '') {
			var json = JSON.parse(value);
			json.workspace = workspace;
			localStorage.setItem('blocklySavedWorkspaceXml-' + id, JSON.stringify(json));
			callback(null);
		}
		else {
			callback("No workspace found with id=" + id + " to overwrite");
		}
	}
	else {
		callback("Not logged in and no local storage available");
	}	
}

function deleteWorkspace(id, callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
            url: '/game/workspace/' + id,
            type: 'DELETE',
            success: function() {
                callback(null);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	}
	else if (localStorage) {
		localStorage.removeItem('blocklySavedWorkspaceXml-' + id);
		callback(null);
	}
	else {
		callback("Not logged in and no local storage available");
	}
}

function createNewWorkspace(name, workspace, callback) {
	if (LOGGED_IN_AS_STUDENT) {
		$.ajax({
            url: '/game/workspace',
            type: 'POST',
            data: {
                name: name,
                workspace: workspace,
            },
            success: function() {
                callback(null);
            },
            error: function(xhr,errmsg,err) {
                callback(xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText);
            }
        });
	}
	else if (localStorage) {
		// Need to generate a unique integer, for our purposes this should do
		var id = new Date().getTime();

		localStorage.setItem('blocklySavedWorkspaceXml-' + id, JSON.stringify({
			name: name,
			workspace: workspace,
		}));

		callback(null);
	}
	else {
		callback("Not logged in and no local storage available");
	}
}