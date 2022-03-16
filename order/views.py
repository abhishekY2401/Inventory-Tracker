from django.shortcuts import render
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def addOrderPage(request):
    form = OrderForm()
    context = {'form': form}
    return render(request, 'addOrder.html', context)


@login_required
def orderPage(request):
    return render(request, 'order.html')


@login_required
def detailedOrderPage(request):
    return render(request, 'orderDetails.html')
