from django.shortcuts import render

def game(request):
    '''Just a placeholder. If it's this simple, switch to Django's Generic Views.'''
    return render(request, 'game/game.html')

def submit_commands(request):
	if request.method == 'POST':
		return submit_reply(request)
	return render(request, 'game/submit_commands.html')

def submit_reply(request):
	return render(request, 'game/submit_reply.html')