$(':checkbox').on('change', function() {
    $(this).closest('li').toggleClass('checked', $(this).is(':checked'))
})

$('.all-class > label, .all-level').on('change', function() {
    var check = $(this).find('input').is(':checked')
    $(this).closest('ul').find(':checkbox').prop('checked', check).closest('li').toggleClass('checked', check)
})

$('.episode').on('change', function() {
    var check = $(this).find('input').is(':checked')
    var first = $(this).attr('data-first')
    var last = $(this).attr('data-last')
    for (var i = first; i <= last; i++) {
        $('.level-'+i).find(':checkbox').prop('checked', check).closest('li').toggleClass('checked', check)
    }
})

$('.expander').on('click', function() {
    var el = $(this).closest('li')
    var first = el.attr('data-first')
    var last = el.attr('data-last')
    if ($('.level-'+first).is(':visible')) {
        el.find('span').text('arrow_left')
    } else {
        el.find('span').text('arrow_drop_down')
    }
    for (var i = first; i <= last; i++) {
        $('.level-'+i).toggle('blind')
    }
})
