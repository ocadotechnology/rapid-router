from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError

from website.forms import EmailForm
from website.forms import FeedbackForm
from website.models import Email

def home(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            try:
                # Only save the form if the email isn't already in there.
                # Didn't want to use 'unique=True' at the database level
                # because I didn't want the 'email is already in database'
                # error showing up on the form on the web page.
                # This way, submitting your email is idempotent, no errors.
                Email.objects.get(email=form.cleaned_data['email'])
            except Email.DoesNotExist:
                form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = EmailForm()
    return render(request, 'website/home.html', {'form': form, 'submitted': request.GET.get('submitted', False)})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['feedback_name']
            sender = form.cleaned_data['feedback_email']
            message = form.cleaned_data['feedback_text']
            subject = 'CFL Feedback received from ' + name
            recipients = ['cfl.feedback@ocado.com']
            try:
                send_mail(subject, message, sender, recipients)
                subject = name + ', your CFL feedback has been received'
                message = 'Thank you for your feedback which has now been sent. A copy of your feedback follows: \n' + message
                recipients = [sender]
                sender = 'donotreply@ocado.com'
                try:
                    send_mail(subject, message, sender, recipients)
                except BadHeaderError:
                    return HttpResponse('Confirmation email error: invalid header found.')
            except BadHeaderError:
                return HttpResponse('Feedback email error: invalid header found.')
            form = FeedbackForm()
    else:
        form = FeedbackForm()

    return render(request, 'website/feedback.html', {'form': form})
