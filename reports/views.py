from django.shortcuts import render

def reports(request):
    '''Just a placeholder. If it's this simple, switch to Django's Generic Views.'''
    return render(request, 'reports/reports.html')
