from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def dashboardPage(request):
    return render(request, 'dash.html')


def addOrderPage(request):
    form = OrderForm()
    context = {'form': form}
    return render(request, 'addOrder.html', context)


def orderPage(request):
    return render(request, 'order.html')


def detailedOrderPage(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'orderDetails.html')


def createOrder(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            order = Order()
            order.title = request.POST.get('title')
            order.content = request.POST.get('content')
            order.save()

            return render(request, 'posts/create.html')

    else:
        return render(request, 'posts/create.html')
