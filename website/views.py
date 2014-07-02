from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from website.forms import EmailForm
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

   
