# -*- coding: utf-8 -*-
# Code for Life
#
# Copyright (C) 2019, Ocado Innovation Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# ADDITIONAL TERMS – Section 7 GNU General Public Licence
#
# This licence does not grant any right, title or interest in any “Ocado” logos,
# trade names or the trademark “Ocado” or any other trademarks or domain names
# owned by Ocado Innovation Limited or the Ocado group of companies or any other
# distinctive brand features of “Ocado” as may be secured from time to time. You
# must not distribute any modification of this program using the trademark
# “Ocado” or claim any affiliation or association with Ocado or its employees.
#
# You are not authorised to use the name Ocado (or any of its trade names) or
# the names of any author or contributor in advertising or for publicity purposes
# pertaining to the distribution of this program, without the prior written
# authorisation of Ocado.
#
# Any propagation, distribution or conveyance of this program must include this
# copyright notice and these terms. You must not misrepresent the origins of this
# program; modified versions of the program must be marked as such and not
# identified as the original program.
from django import forms
from django.utils.translation import ugettext
from models import UserProfile, Level
from widgets import DropDownMenuSelectMultiple
import itertools


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
        choice_list = (
            (level.id, str(level)) for level in Level.objects.sorted_levels()
        )
        self.fields["levels"] = forms.MultipleChoiceField(
            choices=itertools.chain(choice_list), widget=forms.CheckboxSelectMultiple()
        )

        def validate(self):
            cleaned_data = super(ScoreboardForm, self).clean()
            classes = cleaned_data.get("classes")
            levels = cleaned_data.get("levels")
            return classes and levels


class LevelModerationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        classes = kwargs.pop("classes")
        super(LevelModerationForm, self).__init__(*args, **kwargs)
        self.fields["classes"] = forms.ModelChoiceField(
            queryset=classes,
            required=True,
            widget=forms.Select(attrs={"class": "form-control"}),
        )
        self.fields["students"] = forms.CharField(
            required=False, widget=forms.Select(attrs={"class": "form-control"})
        )

        def validate(self):
            cleaned_data = super(LevelModerationForm, self).clean()
            classes = cleaned_data.get("classes")
            return classes
