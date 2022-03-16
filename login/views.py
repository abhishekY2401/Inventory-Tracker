from django.contrib.auth import authenticate, login, logout
from django.core.checks import messages
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

...


# Create your views here.


# Create your views here.

def loginRequest(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Oops! Wrong Credentials")
            return redirect('homepage')

    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('homepage')
