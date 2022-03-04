from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

'''def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message. '''