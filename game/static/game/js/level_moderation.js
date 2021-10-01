var levelID;
var classID;
var students;

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var saving = new ocargo.Saving();

function deleteLevel() {
    saving.deleteLevel(levelID,
        function () {
            document.forms["levelModerationForm"].submit();
        },
        console.error);
}

function showPopupConfirmation(title, text, confirm_handler) {
    var popup = $(".popup-wrapper");
    $(".popup-box__title").text(title);
    $(".popup-box__msg").append(text);
    $("#confirm_button").click(confirm_handler);

    popup.addClass("popup--fade");
}

function confirmDelete() {
    console.log(levelID);
    var title = 'Delete level';
    var text = '<p>' + gettext("This student's level will be permanently deleted. Are you sure?") + '</p>';

    showPopupConfirmation(title, text, deleteLevel);
}

$(document).ready(function() {
	$(".delete").click(function() {

	  	levelID = this.getAttribute('value');
	  	confirmDelete();
	});

	$('.play').click(function() {
		window.location.href = Urls.play_custom_level(this.getAttribute('value'));
	});

    $("#table").tablesorter();

    $('#id_classes').change(function() {
        classID = $(this).val();
        $.ajax({
            url: Urls.students_for_level_moderation(classID),
            type: 'GET',
            dataType: 'json',
            success: function(studentData) {
                $('#id_students').empty();

                var addStudentOption = function(value, text) {
                    var option = $('<option>');
                    option.attr({
                        'value': value
                    });
                    option.text(text);
                    $('#id_students').append(option);
                };

                addStudentOption("", "---------");

                for (var student in studentData) {
                    addStudentOption(student, studentData[student])
                }
            }
        });
        return false;
    });

    if (students) {
        $('#id_classes').change();
    }
});
