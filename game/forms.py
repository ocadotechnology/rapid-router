import os
from django.forms import ModelForm
from models import Teacher
from django import forms

class AvatarUploadForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['avatar']

class AvatarPreUploadedForm(ModelForm):
	avatar = forms.ChoiceField()
	class Meta:
    	model = Teacher
    	fields = ['avatar']


	def __init__(self, *args, **kwargs):
		super(AvatarPreUploadedForm, self).__init__(*args, **kwargs)
		x = os.path.dirname(os.path.abspath(__file__))
		path = os.path.join(x, 'static/game/image/Avatars/')
		img_list = os.listdir(path)
		self.fields['avatar'].choices = img_list