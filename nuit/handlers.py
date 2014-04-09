'''Nuit Status Code Handlers'''
from django.shortcuts import render

def generic_handler(request, template, status, context=None):
    '''
    Return a response with a particular status code, rendering a template with a specified context.
    '''
    context = context or {}
    return render(request, template, context, status=status)

def handler500(request):
    '''
    View handling execeptions, to be used as :data:`django.conf.urls.handler500`
    '''
    return generic_handler(request, 'nuit/generic/500.html', 500)

def handler400(request):
    '''
    View handling bad requests, to be used as :data:`django.conf.urls.handler400`
    '''
    return generic_handler(request, 'nuit/generic/400.html', 400)

def handler403(request):
    '''
    View handling permission denied exceptions, to be used as :data:`django.conf.urls.handler403`
    '''
    return generic_handler(request, 'nuit/generic/403.html', 403)

def handler404(request):
    '''
    View handling invalid URLs, to be used as :data:`django.conf.urls.handler404`
    '''
    return generic_handler(request, 'nuit/generic/404.html', 404)
