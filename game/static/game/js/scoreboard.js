$("#clear-classes").on("click", () => {
  $('[id^="id_classes_"],#select-all-classes').prop("checked", false);
});

$("#select-all-classes").on("click", () => {
  $('[id^="id_classes_"]').prop(
    "checked",
    $("#select-all-classes").is(":checked")
  );
});

$("#clear-levels").on("click", () => {
  $('[id^="id_episodes_"],#select-all-levels').prop("checked", false);
});

$("#select-all-levels").on("click", () => {
  $('[id^="id_episodes_"]').prop(
    "checked",
    $("#select-all-levels").is(":checked")
  );
});
