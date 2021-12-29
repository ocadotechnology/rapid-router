$(document).ready(function () {
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

  let scoreboardPresent = document.getElementById("scoreboardTable") !== null;
  let improvementPresent = document.getElementById("improvementTable") !== null;

  if (scoreboardPresent) {
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
      leftColumns: 3,
      rightColumns: 1
    });
    // document.getElementById("tableWrapper").scrollIntoView();

    $("#scoreboardSearch").on("keyup", function () {
      table.search(this.value).draw();
    });

    $("#scoreboardTable_next").append(" >");
    $(".next").removeClass("paginate_button");

    table.on("draw", () => {
      $("#scoreboardTable_next").append(" >");
      $("#scoreboardTable_previous").prepend("< ");
      $(".next").removeClass("paginate_button");
      $(".previous").removeClass("paginate_button");
    });

    $(window).on("load", function () {
      table.columns.adjust();
    });
  }

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

$(window).on('load', function () {
  tableText = $("#tableWrapper").html()
  firstClassName = $('label[for="id_classes_0"]').text().trimStart()

  if (tableText.includes(firstClassName)) {
    $("#id_classes_0").prop("checked", true);
  }

  if (tableText.includes("L1")) {
    $("#id_episodes_0").prop("checked", true);
  }
});
