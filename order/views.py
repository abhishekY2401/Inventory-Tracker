from django.shortcuts import render

# Create your views here.


def addOrderPage(request):
    return render(request, 'addOrder.html')


def orderPage(request):
    return render(request, 'order.html')
