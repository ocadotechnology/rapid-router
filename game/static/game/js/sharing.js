var ocargo = ocargo || {};

/**
 *
 * @param {*} getLevelId A function to get the level ID
 * @param {*} validationFunction A function validating whether or not the user can share a level
 */
ocargo.Sharing = function (getLevelId, validationFunction) {
  this.text = [];
  this.text.shared = gettext("Yes");
  this.text.admin = gettext("Yes");
  this.text.unshared = gettext("No");

  this.classesTaught = [];
  this.fellowTeachers = [];
  this.currentClassID = null;
  this.allShared = false;

  this.getLevelId = getLevelId;
  this.validationFunction = validationFunction;
};

/**
 * Setup the teacher panel
 */
ocargo.Sharing.prototype.setupTeacherPanel = function () {
  let sharing = this;

  // Setup the teachers/classes radio buttons for the teacher panel
  $("#share_type_select").change(function () {
    if (this.value == "classes") {
      $("#class_selection").css("display", "block");
      $("#class_select").val(sharing.currentClassID);
      $("#class_select").change();
    } else {
      $("#class_selection").css("display", "none");
      sharing.populateSharingTable(sharing.fellowTeachers);
    }
  });

  // Setup the class dropdown menu for the teacher panel
  $("#class_select").change(function () {
    let classID = $("#class_select").val();

    for (let i = 0; i < sharing.classesTaught.length; i++) {
      if (sharing.classesTaught[i].id == classID) {
        sharing.populateSharingTable(sharing.classesTaught[i].students);
        sharing.currentClassID = sharing.classesTaught[i].id;
        break;
      }
    }
  });
};

/**
 * Setup the select all button
 */
ocargo.Sharing.prototype.setupSelectAllButton = function () {
  $("#shareWithAll").click(
    function () {
      if (!this.validationFunction()) {
        return;
      }

      let levelId = this.getLevelId();
      let actionDesired = this.allShared ? "unshare" : "share";

      let recipientIDs = [];
      $("#shareLevelTable tr[value]").each(function () {
        recipientIDs.push(this.getAttribute("value"));
      });

      let recipientData = { recipientIDs: recipientIDs, action: actionDesired };

      this.shareLevel(levelId, recipientData);
    }.bind(this)
  );
};

/**
 * Populate the sharing table
 * @param {*} recipients The recipients
 */
ocargo.Sharing.prototype.populateSharingTable = function (recipients) {
  let sharing = this;
  let levelId = this.getLevelId();
  // Remove click listeners to avoid memory leak and remove all rows
  let table = $("#shareLevelTable tbody");
  $("#shareLevelTable tr").off("click");
  table.empty();

  // sort by admins first
  recipients.sort(function (a, b) {
    if (a.admin && !b.admin) {
      return -1
    } else if (b.admin && !a.admin) {
      return 1
    }
    return 0;
  });

  this.allShared = true;
  // Add a row to the table for each recipient
  for (let i = 0; i < recipients.length; i++) {
    let recipient = recipients[i];
    let status = recipient.shared ? "shared" || "admin" : "unshared";

    if (recipient.shared) {
      status = "shared";

      if (recipient.admin) {
        status = "admin"
      }

    } else {
      status = "unshared";
      this.allShared = false;
    }

    let name_text = recipient.name

    if (recipient.admin) {
      name_text += (" (Admin)")
    }

    table.append(
      '<tr value="' +
        recipient.id +
        '" status="' +
        status +
        '"><td class="share_name">' +
        $("<div>").text(name_text).html() +
        '</td><td class="share_cell">' +
        this.text[status] +
        "</td></tr>"
    );
  }

  // Update the shareWithAll button
  if (this.allShared) {
    $("#shareWithAll span").html(gettext("Unshare with all"));
    $("#shareWithAll img").attr(
      "src",
      ocargo.Drawing.imageDir + "icons/quit.svg"
    );
  } else {
    $("#shareWithAll span").html(gettext("Share with all"));
    $("#shareWithAll img").attr(
      "src",
      ocargo.Drawing.imageDir + "icons/share.svg"
    );
  }

  // update click listeners in the new rows
  $("#shareLevelTable tr[value]").on("click", function (event) {
    if (sharing.validationFunction()) {
      let status = this.getAttribute("status");

      let recipientData = {
        recipientIDs: [this.getAttribute("value")],
        action: status === "shared" ? "unshare" : "share",
      };

      sharing.shareLevel(levelId, recipientData);
    }
  });

  // update column widths
  for (let i = 0; i < 2; i++) {
    let td = $("#shareLevelTable td:eq(" + i + ")");
    let td2 = $("#shareLevelTableHeader th:eq(" + i + ")");
    td2.width(td.width());
  }
};

/**
 * Method to call when we get an update on the level's sharing information
 * @param {*} error The error
 * @param {*} validRecipients The valid recipients
 */
ocargo.Sharing.prototype.processSharingInformation = function (
  error,
  validRecipients
) {
  if (error !== null) {
    console.error(error);
    ocargo.Drawing.startInternetDownPopup();
    return;
  }

  if (USER_STATUS === "SCHOOL_STUDENT") {
    let classmates = validRecipients.classmates;

    this.populateSharingTable(classmates);
  } else if (USER_STATUS === "TEACHER") {
    this.classesTaught = validRecipients.classes;
    this.fellowTeachers = validRecipients.teachers;

    $("#class_select").empty();
    for (let i = 0; i < this.classesTaught.length; i++) {
      let option = $("<option>");
      option.attr({
        value: this.classesTaught[i].id,
      });
      option.text(this.classesTaught[i].name);
      $("#class_select").append(option);
    }

    if ($("#share_type_select").val() === "teachers") {
      this.populateSharingTable(validRecipients.teachers);
    } else {
      let found = false;
      $("#class_select option").each(function () {
        if (this.value == this.currentClassID) {
          $("#class_select").val(this.currentClassID);
          $("#class_select").change();
          found = true;
        }
      });

      if (!found) {
        $("#class_select").change();
      }
    }
  }
};

/**
 * Share a level
 * @param {*} levelID The level ID
 * @param {*} recipientData The recipient data
 */
ocargo.Sharing.prototype.shareLevel = function (levelID, recipientData) {
  let sharing = this;
  csrftoken = Cookies.get("csrftoken");
  $.ajax({
    url: Urls.share_level_for_editor(levelID),
    type: "POST",
    dataType: "json",
    data: recipientData,
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    },
    success: function (json) {
      sharing.processSharingInformation(null, json);
    },
    error: function (xhr, errmsg, err) {
      sharing.processSharingInformation(
        xhr.status + ": " + errmsg + " " + err + " " + xhr.responseText
      );
    },
  });
  delete recipientData.csrfmiddlewaretoken;
};
