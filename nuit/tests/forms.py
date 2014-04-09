from django import forms

class TestForm(forms.Form):
    title = forms.CharField()
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.CharField()
    url = forms.URLField()
    message = forms.CharField()