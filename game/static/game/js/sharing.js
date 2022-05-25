var ocargo = ocargo || {};

ocargo.Sharing = function () {};

/**
 * Setup the teachers/classes radio buttons for the teacher panel
 * @param {*} currentClassID The current class ID
 * @param {*} fellowTeachers The fellow teachers
 * @param {*} saving The Saving object
 * @param {*} levelId The level ID
 * @param {*} canShare Whether or not the user can share a level
 */
ocargo.Sharing.prototype.setupRadioButtonsForTeacherPanel = function (
  currentClassID,
  fellowTeachers,
  saving,
  levelId,
  canShare
) {
  var sharing = this;
  $("#share_type_select").change(function () {
    if (this.value == "classes") {
      $("#class_selection").css("display", "block");
      $("#class_select").val(currentClassID);
      $("#class_select").change();
    } else {
      $("#class_selection").css("display", "none");
      sharing.populateSharingTable(fellowTeachers, saving, levelId, canShare);
    }
  });
};

/**
 * Setup the select all button
 * @param {*} saving The Saving object
 * @param {*} levelId The level ID
 * @param {*} canShare Whether or not the user can share a level
 * @param {*} shareLevelCallback A function to be called after the level is shared
 */
ocargo.Sharing.prototype.setupSelectAllButton = function (
  saving,
  levelId,
  canShare,
  shareLevelCallback
) {
  $("#shareWithAll").click(function () {
    if (!canShare) {
      return;
    }

    var actionDesired = allShared ? "unshare" : "share";

    var recipientIDs = [];
    $("#shareLevelTable tr[value]").each(function () {
      recipientIDs.push(this.getAttribute("value"));
    });

    var recipientData = { recipientIDs: recipientIDs, action: actionDesired };

    saving.shareLevel(levelId, recipientData, shareLevelCallback);
  });
};

/**
 * Populate the sharing table
 * @param {*} recipients The recipients
 * @param {*} saving The Saving object
 * @param {*} levelId The level ID
 * @param {*} canShare Whether or not the user can share a level
 */
ocargo.Sharing.prototype.populateSharingTable = function (
  recipients,
  saving,
  levelId,
  canShare
) {
  // Remove click listeners to avoid memory leak and remove all rows
  var table = $("#shareLevelTable tbody");
  $("#shareLevelTable tr").off("click");
  table.empty();

  // Order them alphabetically
  recipients.sort(function (a, b) {
    if (a.name < b.name) {
      return -1;
    } else if (a.name > b.name) {
      return 1;
    }
    return 0;
  });

  allShared = true;
  // Add a row to the table for each workspace saved in the database
  for (var i = 0; i < recipients.length; i++) {
    var recipient = recipients[i];
    var status = recipient.shared ? "shared" : "unshared";

    if (recipient.shared) {
      status = "shared";
    } else {
      status = "unshared";
      allShared = false;
    }
    table.append(
      '<tr value="' +
        recipient.id +
        '" status="' +
        status +
        '"><td>' +
        $("<div>").text(recipient.name).html() +
        '</td><td class="share_cell">' +
        text[status] +
        "</td></tr>"
    );
  }

  // Update the shareWithAll button
  if (allShared) {
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
    if (canShare) {
      var status = this.getAttribute("status");

      var recipientData = {
        recipientIDs: [this.getAttribute("value")],
        action: status === "shared" ? "unshare" : "share",
      };

      saving.shareLevel(levelId, recipientData, processSharingInformation);
    }
  });

  // update column widths
  for (var i = 0; i < 2; i++) {
    var td = $("#shareLevelTable td:eq(" + i + ")");
    var td2 = $("#shareLevelTableHeader th:eq(" + i + ")");
    td2.width(td.width());
  }
};
