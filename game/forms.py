from django import forms
from models import UserProfile, Level


class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']


class AvatarPreUploadedForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('my_choices')
        super(AvatarPreUploadedForm, self).__init__(*args, **kwargs)
        self.fields['avatars'] = forms.ChoiceField(choices=choices)

    class Meta:
        model = UserProfile
        fields = ('avatar',)


class ShareLevel(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    level = forms.IntegerField()


class ScoreboardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        teacher = kwargs.pop('teacher')
        super(ScoreboardForm, self).__init__(*args, **kwargs)
        self.fields['classes'] = forms.ModelChoiceField(queryset=teacher.class_teacher.all(),
                                                        required=False)
        self.fields['levels'] = forms.ModelChoiceField(queryset=Level.objects.filter(default=1))


