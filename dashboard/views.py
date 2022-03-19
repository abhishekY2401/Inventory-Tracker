from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def dashboardPage(request):
    return render(request, 'dash.html')


def addOrderPage(request):
    return render(request, 'addOrder.html')


def order_submission(request):
    print("Form Data Submitted!")
    return render(request, 'addOrder.html')


def orderPage(request):
    return render(request, 'order.html')


def detailedOrderPage(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'orderDetails.html')
