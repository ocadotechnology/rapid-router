from django import forms
from website.models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email

class FeedbackForm(forms.Form):
    feedback_name = forms.CharField(label='Your name', max_length=100)
    feedback_email = forms.EmailField(label='Your email address')
    feedback_text = forms.CharField(label='Your message', widget=forms.Textarea)
