from django.shortcuts import render

def home(request):
    '''Just a placeholder. If it's this simple, switch to Django's Generic Views.'''
    return render(request, 'website/home.html')
