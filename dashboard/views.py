from django.shortcuts import render  

# Create your views here.

def dashboardPage(request):
    return render(request, 'sample.html')
