from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def addOrderPage(request):
    form = OrderForm()
    context = {'form': form}
    return render(request, 'addOrder.html', context)


def orderPage(request):
    return render(request, 'order.html')


def detailedOrderPage(request):
    return render(request, 'orderDetails.html')
