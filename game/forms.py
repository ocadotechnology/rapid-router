from django import forms
from models import UserProfile, Level, Theme, Student


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


class ShareLevelPerson(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ShareLevelPerson, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(max_length=100)
        self.fields['surname'] = forms.CharField(max_length=100)
        self.fields['level'] = forms.IntegerField()
        self.fields['level'].widget = forms.HiddenInput()


class ShareLevelChoosePerson(forms.Form):
    def __init__(self, *args, **kwargs):
        people = kwargs.pop('people')
        super(ShareLevelChoosePerson, self).__init__(*args, **kwargs)
        self.fields['people'] = forms.ModelChoiceField(queryset=people)
        self.fields['level'] = forms.IntegerField()
        self.fields['level'].widget = forms.HiddenInput()


class ShareLevelClass(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop('classes')
        super(ShareLevelClass, self).__init__(*args, **kwargs)
        self.fields['classes'] = forms.ModelChoiceField(queryset=classes)
        self.fields['levels'] = forms.IntegerField()
        self.fields['levels'].widget = forms.HiddenInput()


class ScoreboardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop('classes')
        super(ScoreboardForm, self).__init__(*args, **kwargs)
        self.fields['classes'] = forms.ModelChoiceField(queryset=classes,
                                                        required=False,
                                                        widget=forms.Select(attrs={'class': 'wide'}))
        self.fields['levels'] = forms.ModelChoiceField(queryset=Level.objects.filter(default=1),
                                                       required=False,
                                                       widget=forms.Select(attrs={'class': 'wide'}))

        def validate(self):
            cleaned_data = super(ScoreboardForm, self).clean()
            classes = cleaned_data.get('classes')
            levels = cleaned_data.get('levels')
            return classes or levels

class LevelModerationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop('classes')
        super(LevelModerationForm, self).__init__(*args, **kwargs)
        self.fields['classes'] = forms.ModelChoiceField(queryset=classes,
                                                        required=True,
                                                        widget=forms.Select(attrs={'class': 'wide'}))
        self.fields['students'] = forms.CharField(required=True,
                                                    widget=forms.Select(attrs={'class': 'wide'}))

        def validate(self):
            cleaned_data = super(LevelModerationForm, self).clean()
            classes = cleaned_data.get('classes')
            students = cleaned_data.get('students')
            return classes and students
