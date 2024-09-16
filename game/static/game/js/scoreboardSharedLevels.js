$(document).ready(function () {
  let scoreboardPresent = document.getElementById("scoreboardTable") !== null;

  if (scoreboardPresent) {
    // Setup shared levels table
    let sharedLevelsTable = $("#sharedLevelsTable").DataTable({
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

    new $.fn.dataTable.FixedColumns(sharedLevelsTable, {
      leftColumns: 2,
    });

    $("#sharedLevelsTable_next").append(" >");

    sharedLevelsTable.on("draw", () => {
      $("#sharedLevelsTable_next").append(" >");
      $("#sharedLevelsTable_previous").prepend("< ");
      $(".next").removeClass("paginate_button");
      $(".previous").removeClass("paginate_button");
    });

    $("#scoreboardSearch").on("keyup", function () {
      sharedLevelsTable.search(this.value).draw();
    });

    $(window).on("load", function () {
      sharedLevelsTable.columns.adjust();
    });
  }
});
