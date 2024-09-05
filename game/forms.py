from __future__ import absolute_import

import itertools

from django import forms
from .models import Episode


class ScoreboardForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop("classes")
        language = kwargs.pop("language")
        super(ScoreboardForm, self).__init__(*args, **kwargs)
        classes_choices = [(c.id, c.name) for c in classes]

        self.fields["classes"] = forms.MultipleChoiceField(
            choices=classes_choices, widget=forms.CheckboxSelectMultiple()
        )

        episodes_range = (
            range(1, 10) if language == "blockly" else range(12, 16)
        )

        # Each tuple in choices has two elements, id and name of each level
        # First element is the actual value set on the model
        # Second element is the string displayed on the dropdown menu
        episodes_choices = (
            (episode.id, episode.name)
            for episode in Episode.objects.filter(pk__in=episodes_range)
        )
        self.fields["episodes"] = forms.MultipleChoiceField(
            choices=itertools.chain(episodes_choices),
            widget=forms.CheckboxSelectMultiple(),
        )


class LevelModerationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop("classes")
        teacher = kwargs.pop("teacher")
        super(LevelModerationForm, self).__init__(*args, **kwargs)

        # If the teacher is an admin, append teacher names or "(you)" to classes
        if teacher.is_admin:
            classes_choices = [
                (
                    c.id,
                    f"{c.name} "
                    + (
                        "(you)"
                        if c.teacher == teacher
                        else f"({c.teacher.new_user.first_name} {c.teacher.new_user.last_name})"
                    ),
                )
                for c in classes
            ]
        else:
            classes_choices = [(c.id, c.name) for c in classes]

        self.fields["classes"] = forms.MultipleChoiceField(
            choices=classes_choices, widget=forms.CheckboxSelectMultiple()
        )
