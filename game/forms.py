from __future__ import absolute_import

import itertools

from django import forms
from .models import Episode


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
            choices=itertools.chain(episodes_choices),
            widget=forms.CheckboxSelectMultiple(),
        )


class LevelModerationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop("classes")
        super(LevelModerationForm, self).__init__(*args, **kwargs)
        classes_choices = [(c.id, c.name) for c in classes]

        self.fields["classes"] = forms.MultipleChoiceField(
            choices=classes_choices, widget=forms.CheckboxSelectMultiple()
        )
