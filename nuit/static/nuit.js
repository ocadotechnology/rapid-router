var nuit = {};

// Setup Functions

nuit.csrftoken = $.cookie('csrftoken');

nuit.csrfSafeMethod = function(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

nuit.setup = function() {

    // Enable AJAX requests in Django
    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function(xhr, settings) {
            if (!nuit.csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", nuit.csrftoken);
                xhr.setRequestHeader('Accept', 'application/json');
            }
        }
    });

    // Hightlight current page in menu
    $('.nuit-active-menu').each(function() {
        $('.menu-' + $(this).html()).addClass('active');
    });

    // Highlight current breadcrumb
    $('.nuit-breadcrumbs li:last-child').addClass('current');

    // Fix right-menu modals when they're closed
    $(document).on('closed', '[data-reveal]', function () {
        var modal = $(this);
        modal.attr('style', '');
    });

    // Add correct links for cog-menu
    $('.sidebar.on-right > section').each(function() {
        $this = $(this);
        if ($this.data('reveal') === "") {
            $('#right-menu-drop').append("<li><a href='#' data-reveal-id='" + $this.attr('id') + "'>" + $this.data('link') + "</a></li>");
        } else {
            $nav = $this.find('nav');
            if ($nav.length) {
                $nav.find('ul li').each(function() {
                    $li = $(this);
                    $('#right-menu-drop').append($li.clone());
                });
            }
        }
    });

    // Add left-menu links to application menu on small screens
    $('.sidebar.on-left > section').each(function() {
        $this = $(this);
        $nav = $this.find('nav');
        if ($nav.length) {
            $title = $this.find('h5');
            $append_to = $('#left-menu-drop');
            if ($title.length && !$this.hasClass('main-nav')) {
                $new_li = $('<li></li>').addClass('show-for-small-only').addClass('has-dropdown');
                $new_li.append("<a href='#'>" + $title.html() + "</a>");
                $append_to.append($new_li);
                $new_ul = $("<ul class='dropdown'></ul>");
                $new_li.append($new_ul);
                $append_to = $new_ul;
            }
            $nav.find('ul li').each(function() {
                $li = $(this);
                $append_to.append($li.clone().addClass('show-for-small-only'));
            });
            $('#left-menu-drop').append("<li class='show-for-small-only divider'></li>");
        }
    });

    nuit.trigger_responsive_tables();

    // Setup foundation
    $(document).foundation();

};

// User functions

nuit.trigger_responsive_tables = function() {
    // Set headers for grouped responsive tables
    $('table.responsive.grouped').find('td').each(function() {
        $td = $(this);
        $td.attr('data-title', $td.closest('table').find('th').eq($td.index()).html());
    });
    $('table.responsive.scroll').each(function () {
        $table = $(this);
        classes = 'responsive scroll';
        if ($table.hasClass('medium-down')) {
            classes += ' medium-down';
        }
        $table.wrap('<div class="' + classes + '"></div>');
    });
};

nuit.add_message = function(alert_type, message) {
    message_html = '<div data-alert class="alert-box ' + alert_type.toLowerCase() + '">' + message + '<a href="#" class="close">&times;</a></div>';
    var $message = $(message_html);
    $('.nuit-messages').append($message).foundation('reflow');
};

// Initialisation
nuit.setup();
