from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from models import School, Teacher, Student, Class


def game(request):
    '''Just a placeholder. If it's this simple, switch to Django's Generic Views.'''
    return render(request, 'game/game.html')

def logged_students(request):
	""" Renders the page with information about all the logged in students."""
	return render_student_info(request, True)

def students_in_class(request):
	""" Renders the page with information about all the students enrolled in a chosen class."""
	return render_student_info(request, False)

def render_student_info(request, logged):
	""" Helper method for rendering the studend info for a logged-in teacher. """
	user = request.user
	message = "Choose a class you want to see."
	students = []
	if request.method == 'POST':
		cl = get_object_or_404(Class, id=request.POST.getlist('classes')[0])
		students = cl.get_logged_in_students() if logged else cl.students.all()
	try:
		classes = user.teacher.class_teacher.all()
 	except ObjectDoesNotExist:
 		message = "You don't have permissions to see this."

	context = RequestContext(request, {
		'classes' : classes,
		'message' : message,
		'students' : students
	})
	return render(request, 'game/logged_students.html', context)
