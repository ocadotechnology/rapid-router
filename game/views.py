from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from models import School, Teacher, Student, Class


def game(request):
    '''Just a placeholder. If it's this simple, switch to Django's Generic Views.'''
    return render(request, 'game/game.html')

def logged_students(request):
	klass = request.user.teacher.class_teacher.all()[0]
	students = klass.get_logged_in_students()
	context = context = RequestContext(request, {
		'students' : students
	})
	return render(request, 'game/logged_students.html', context)


def students_in_class(request):
	user = request.user
	message = "Choose a class you want to see."
	students = []
	if request.method == 'POST':
		selected_item = get_object_or_404(Class, id=request.POST.getlist('classes')[0])
		students = selected_item.students.all()
	try:
		classes = user.teacher.class_teacher.all()
 	except ObjectDoesNotExist:
 		message = "You don't have permissions to see this."

	context = RequestContext(request, {
		'classes' : classes,
		'message' : message,
		'students' : students
	})

	return render(request, 'game/students_in_class.html', context)

def submit_commands(request):
	if request.method == 'POST':
		return submit_reply(request)
	return render(request, 'game/submit_commands.html')

def submit_reply(request):
	return render(request, 'game/submit_reply.html')