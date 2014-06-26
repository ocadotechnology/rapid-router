from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from website.forms import EmailForm

def home(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
    else:
        form = EmailForm()
    return render(request, 'website/home.html', {'form': form, 'submitted': request.GET.get('submitted', False)})

   
