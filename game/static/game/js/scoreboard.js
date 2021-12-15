$('#clear-classes').on('click', () => {
    $('[id^="id_classes_"]').prop('checked', false)
})

$('#clear-levels').on('click', () => {
    $('[id^="id_episodes_"]').prop('checked', false)
})
