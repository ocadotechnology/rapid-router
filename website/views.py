from django.shortcuts import redirect

def home(request):
    '''Just a placeholder. If it's this simple, switch to Django's Generic Views.'''
    return redirect('/game')
