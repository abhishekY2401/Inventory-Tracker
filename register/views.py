from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def registerPage(request):
    return render(request, 'register.html')
