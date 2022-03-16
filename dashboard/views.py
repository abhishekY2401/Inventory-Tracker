from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def dashboardPage(request):
    return render(request, 'dash.html')
