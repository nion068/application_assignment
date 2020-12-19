from django.http import HttpResponseRedirect, HttpRequest
from functools import wraps

# Decorator Function to secure views by forcing to authenticate
def login_required(view_func):
    @wraps(view_func)
    def wrap(request, *args, **kwargs):
        if 'token' not in request.session.keys():
            return HttpResponseRedirect(redirect_to='/apply/')
        else:
            return view_func(request)
    return wrap