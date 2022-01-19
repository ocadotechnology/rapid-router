/* global showPopupConfirmation */

var levelID;
var classID;
var students;

var saving = new ocargo.Saving();

function deleteLevel() {
  saving.deleteLevel(
    levelID,
    function () {
      document.forms["moderateForm"].submit();
    },
    console.error
  );
}

function confirmDelete() {
  let title = "Delete level";
  let text = `
    <div class='popup-text'>
      <p>This student's level will be permanently deleted. Are you sure?</p>
    </div>`;
  let confirmHandler = "deleteLevel()";

  showPopupConfirmation(title, text, confirmHandler);
}

$(document).ready(function () {
  $(".delete").click(function () {
    levelID = this.getAttribute("value");
    confirmDelete();
  });

  $(".play").click(function () {
    window.location.href = Urls.play_custom_level(this.getAttribute("value"));
  });

  $("#clear-classes").on("click", () => {
    $('[id^="id_classes_"],#select-all-classes').prop("checked", false);
  });

  $("#select-all-classes").on("click", () => {
    $('[id^="id_classes_"]').prop(
      "checked",
      $("#select-all-classes").is(":checked")
    );
  });

  // Checks the select all checkboxes on page load if all their sub boxes are already checked
  $("#select-all-classes").prop(
    "checked",
    $('[id^="id_classes_"]:checked').length === $('[id^="id_classes_"]').length
  );

  // Prevents reloading the page by submitting the form by pressing the Enter key
  $(window).on("keydown", function (event) {
    if (event.keyCode === 13) {
      event.preventDefault();
      return false;
    }
  });

  // Stops closing the dropdowns when selecting items within it or when pressing the confirmation buttons
  $(document).on("click", ".dropdown .dropdown-menu", function (e) {
    e.stopPropagation();
  });

  const moderateTable = $("#moderateTable").DataTable({
    deferRender: true,
    paging: true,
    pageLength: 5,
    columnDefs: [
      {
        orderable: false,
        searchable: false,
        targets: [-1, -2], // Play and Delete columns
      },
    ],
  });

  $("#moderateSearch").on("keyup", function () {
    moderateTable.search(this.value).draw();
  });

  $("#moderateTable_next").append(" >");
  $(".next").removeClass("paginate_button");

  moderateTable.on("draw", () => {
    $("#moderateTable_next").append(" >");
    $("#moderateTable_previous").prepend("< ");
    $(".next").removeClass("paginate_button");
    $(".previous").removeClass("paginate_button");
  });
});
