from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

...


'''def loginRequest(request):
    return render(request, 'login.html')
# Create your views here.
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Member'''


# Create your views here.

def loginRequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username , password = password)
        if user is not None:
            login(request,user)
            return render(request, "dash.html", )
        else:
            messages.error(request, "Oops! Wrong Credentials")
            return redirect('home')

    return render(request, 'login.html')

