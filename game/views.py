import os
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from forms import AvatarUploadForm, AvatarPreUploadedForm
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

def settings(request):
	x = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	path = os.path.join(x, 'static/game/image/Avatars/')
	img_list = os.listdir(path)
	avatar = None
	teacher = request.user.teacher
	avatarUploadForm = AvatarUploadForm(request.POST or None, request.FILES)
	avatarPreUploadedForm = AvatarPreUploadedForm(request.POST or None, my_choices=img_list)
	if request.method == 'POST':
		if "pre-uploaded" in request.POST:
			if avatarPreUploadedForm.is_valid:
				avatar = avatarPreUploadedForm.data.get('pre-uploaded', False)
		else:
			if avatarUploadForm.is_valid() and "user-uploaded" in request.POST:
				avatar = request.FILES.get('avatar', False)
		teacher.avatar = avatar
		teacher.save()

	context = RequestContext(request, {
		'avatarPreUploadedForm' : avatarPreUploadedForm,
		'avatarUploadForm' : avatarUploadForm,
		'user' : request.user,
	})
	return render(request, 'game/settings.html', context)


def render_student_info(request, logged):
	""" Helper method for rendering the studend info for a logged-in teacher. """
	user = request.user
	message = "Choose a class you want to see."
	currentClass = ""
	students = []
	avatar = '/static/game/image/avatars/ufo.png'
	if request.method == 'POST':
		cl = get_object_or_404(Class, id=request.POST.getlist('classes')[0])
		students = cl.get_logged_in_students() if logged else cl.students.all()
		currentClass = cl.name
	try:
		classes = user.teacher.class_teacher.all()
 	except ObjectDoesNotExist:
 		message = "You don't have permissions to see this."

	context = RequestContext(request, {
		'classes' : classes,
		'message' : message,
		'students' : students,
		'avatar' : avatar,
		'currentClass' : currentClass,
	})
	return render(request, 'game/logged_students.html', context)



"""	
avatarPreUploadedForm = AvatarPreUploadedForm(request.POST or None)
avatarPreUploadedFormAvatars = avatarPreUploadedForm.cleaned_data.avatarForm.choices
if request.method == 'POST':
if  avatarPreUploadedForm.is_valid() and "pre-uploaded" in request.POST:
avatar = request.POST.getlist('avatars')[0]
teacher.avatar = '/static/game/image/avatars/' + avatar
		    """

