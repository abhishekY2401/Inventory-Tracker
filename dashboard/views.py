from itertools import count
from math import prod
from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.


def dashboardPage(request):
    order = Order.objects.all()

    order_count = Order.objects.count()
    print(order_count)

    delivered_order = Order.objects.filter(status="delivered")
    delivered_count = delivered_order.count()
    print(delivered_count)

    pending_order = Order.objects.filter(status="pending")
    pending_count = pending_order.count()
    print(pending_count)

    context = {'order': order, 'order_count': order_count, 'delivered_count': delivered_count, 'pending_count': pending_count}

    return render(request, 'dash.html', context)


def addOrderPage(request):
    return render(request, 'addOrder.html')


def order_submission(request):
    print("Form Data Submitted!")

    if request.method == 'POST':
        vendor = Vendor()
        vendor.vendor_name = request.POST.get('vendor-name')
        vendor.email_id = request.POST.get('vendor-email')
        vendor.save()

        product = Product()
        product.product_name = request.POST.get('item-name')
        product.category = request.POST.get('category')
        product.unit = request.POST.get('unit')
        product.quantity = request.POST.get('quantity')
        product.price = request.POST.get('price')
        product.save()

        cust = Customer()
        cust.customer_name = request.POST.get('cust-name')
        cust.phone_no = request.POST.get('phone-no')
        cust.email_id = request.POST.get('email-id')
        cust.address = request.POST.get('address')
        cust.save()

        order = Order()
        order.order_id = request.POST.get('order-id')
        order.date = request.POST.get('date')
        order.status = request.POST.get('status')
        order.invoice_no = request.POST.get('invoice_no')
        order.save()

        order.product.add(product)
        order.customer = cust
        order.vendor = vendor
        order.save()

        return redirect('dashboard:order')

    return render(request, 'addOrder.html')


def orderPage(request):
    context = {}

    order = Order.objects.all()
    context['order'] = order

    return render(request, 'order.html', context)


def detailedOrderPage(request, pk):
    context = {}
    
    order = Order.objects.get(order_id=pk)
    context['data'] = order
    context['products'] = order.product.all()

    return render(request, 'orderDetails.html', context)

def editOrder(request, pk):
    context = {}

    order = Order.objects.get(order_id=pk)
    context['data'] = order
    context['products'] = order.product.all()

    return render(request, 'edit.html', context)