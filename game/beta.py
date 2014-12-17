def has_beta_access(request):
    return is_on_beta_host(request) or is_developer(request)
    
def is_on_beta_host(request):
    return request.get_host().startswith("beta")

def is_developer(request):
    return ((not request.user.is_anonymous()) and request.user.userprofile.developer)