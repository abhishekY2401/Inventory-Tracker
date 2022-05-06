from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def login_user(request):
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request, ("There was error logging in, please try again"))
            return redirect('login')

    return render(request, "signin.html", context)

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out!"))
    return redirect('homepage')



