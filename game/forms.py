from __future__ import absolute_import

import itertools
from builtins import str

from django import forms

from .models import Episode


class ShareLevelPerson(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ShareLevelPerson, self).__init__(*args, **kwargs)
        self.fields["name"] = forms.CharField(max_length=100)
        self.fields["surname"] = forms.CharField(max_length=100)
        self.fields["level"] = forms.IntegerField()
        self.fields["level"].widget = forms.HiddenInput()


class ShareLevelChoosePerson(forms.Form):
    def __init__(self, *args, **kwargs):
        people = kwargs.pop("people")
        super(ShareLevelChoosePerson, self).__init__(*args, **kwargs)
        self.fields["people"] = forms.ModelChoiceField(queryset=people)
        self.fields["level"] = forms.IntegerField()
        self.fields["level"].widget = forms.HiddenInput()


class ShareLevelClass(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop("classes")
        super(ShareLevelClass, self).__init__(*args, **kwargs)
        self.fields["classes"] = forms.ModelChoiceField(queryset=classes)
        self.fields["levels"] = forms.IntegerField()
        self.fields["levels"].widget = forms.HiddenInput()


class ScoreboardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop("classes")
        super(ScoreboardForm, self).__init__(*args, **kwargs)
        classes_choices = [(c.id, c.name) for c in classes]

        self.fields["classes"] = forms.MultipleChoiceField(
            choices=classes_choices, widget=forms.CheckboxSelectMultiple()
        )
        # Each tuple in choices has two elements, id and name of each level
        # First element is the actual value set on the model
        # Second element is the string displayed on the drop down menu
        episodes_choices = (
            (episode.id, episode.name) for episode in Episode.objects.all()
        )
        self.fields["episodes"] = forms.MultipleChoiceField(
            choices=itertools.chain(episodes_choices), widget=forms.CheckboxSelectMultiple()
        )

        def validate(self):
            cleaned_data = super(ScoreboardForm, self).clean()
            classes = cleaned_data.get("classes")
            episodes = cleaned_data.get("episodes")
            return classes and episodes


class LevelModerationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop("classes")
        super(LevelModerationForm, self).__init__(*args, **kwargs)
        self.fields["classes"] = forms.ModelChoiceField(
            queryset=classes,
            required=True,
            widget=forms.Select(),
        )
        self.fields["students"] = forms.CharField(required=False, widget=forms.Select())

        def validate(self):
            cleaned_data = super(LevelModerationForm, self).clean()
            classes = cleaned_data.get("classes")
            return classes
