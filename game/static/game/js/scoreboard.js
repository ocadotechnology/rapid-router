$(document).ready(function () {
  // Check all episodes if none of the checkboxes were ticked (load all by default)
  if($('[id^="id_episodes_"]:checked').length === 0) {
    $("#select-all-levels").prop("checked", true);
    $('[id^="id_episodes_"]').prop("checked", true);
  }

  $("#clear-classes").on("click", () => {
    $('[id^="id_classes_"],#select-all-classes').prop("checked", false);
  });

  $("#select-all-classes").on("click", () => {
    $('[id^="id_classes_"]').prop("checked", $("#select-all-classes").is(":checked"));
  });

  $("#clear-levels").on("click", () => {
    $('[id^="id_episodes_"],#select-all-levels').prop("checked", false);
  });

  $("#select-all-levels").on("click", () => {
    $('[id^="id_episodes_"]').prop("checked", $("#select-all-levels").is(":checked"));
  });

  // Checks the select all checkboxes on page load if all their sub boxes are already checked
  $("#select-all-classes").prop("checked",
      $('[id^="id_classes_"]:checked').length === $('[id^="id_classes_"]').length);

  $("#select-all-levels").prop("checked",
      $('[id^="id_episodes_"]:checked').length === $('[id^="id_episodes_"]').length);

  let scoreboardPresent = document.getElementById("scoreboardTable") !== null;
  let improvementPresent = document.getElementById("improvementTable") !== null;

  if (scoreboardPresent) {
    // Setup main scoreboard table
    let table = $("#scoreboardTable").DataTable({
      scrollY: false,
      scrollX: true,
      scrollCollapse: false,
      paging: true,
      deferRender: true,
      language: {
        emptyTable: "No data available in table",
        loadingRecords: "Loading...",
        processing: "Processing...",
        search: "Search:",
        zeroRecords: "No matching records found"
      },
      columnDefs: [
        {
          orderable: false,
          targets: "no-sort"
        }
      ]
    });

    new $.fn.dataTable.FixedColumns(table, {
      leftColumns: 2,
      rightColumns: 1
    });

    $("#scoreboardTable_next").append(" >");
    $(".next").removeClass("paginate_button");

    table.on("draw", () => {
      $("#scoreboardTable_next").append(" >");
      $("#scoreboardTable_previous").prepend("< ");
      $(".next").removeClass("paginate_button");
      $(".previous").removeClass("paginate_button");
    });

    $("#scoreboardSearch").on("keyup", function () {
      table.search(this.value).draw();
    });

    $(window).on("load", function () {
      table.columns.adjust();
    });
  }

  // Prevents reloading the page by submitting the form by pressing the Enter key
  $(window).on("keydown", function(event) {
    if(event.keyCode === 13) {
      event.preventDefault();
      return false;
    }
  });

  // Stops closing the dropdowns when selecting items within it or when pressing the confirmation buttons
  $(document).on("click", ".dropdown .dropdown-menu", function (e) {
    e.stopPropagation();
  });

  if (improvementPresent) {
    const impTable = $("#improvementTable").DataTable({
      pageLength: 5
    });

    $("#scoreboardSearch").on("keyup", function () {
      impTable.search(this.value).draw();
    });

    $("#improvementTable_next").append(" >");
    $(".next").removeClass("paginate_button");

    impTable.on("draw", () => {
      $("#improvementTable_next").append(" >");
      $("#improvementTable_previous").prepend("< ");
      $(".next").removeClass("paginate_button");
      $(".previous").removeClass("paginate_button");
    });
  }
});
