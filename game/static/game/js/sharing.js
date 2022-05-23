var ocargo = ocargo || {};

ocargo.Sharing = function () {};

//Method to call when we get an update on the level's sharing information
ocargo.Sharing.prototype.processSharingInformation = function (
  error,
  validRecipients,
  currentClassID
) {
  if (error !== null) {
    console.error(error);
    ocargo.Drawing.startInternetDownPopup();
    return;
  }

  if (USER_STATUS === "SCHOOL_STUDENT") {
    var classmates = validRecipients.classmates;
    var teacher = validRecipients.teacher;

    populateSharingTable(classmates);
  } else if (USER_STATUS === "TEACHER") {
    classesTaught = validRecipients.classes;
    fellowTeachers = validRecipients.teachers;

    $("#class_select").empty();
    for (var i = 0; i < classesTaught.length; i++) {
      var option = $("<option>");
      option.attr({
        value: classesTaught[i].id,
      });
      option.text(classesTaught[i].name);
      $("#class_select").append(option);
    }

    if ($("#share_type_select").val() === "teachers") {
      populateSharingTable(validRecipients.teachers);
    } else {
      var found = false;
      $("#class_select option").each(function () {
        if (this.value == currentClassID) {
          $("#class_select").val(currentClassID);
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
