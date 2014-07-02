from django import forms
from website.models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
