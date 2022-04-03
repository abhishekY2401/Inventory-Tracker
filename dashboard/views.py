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
        order.save()

        order.product.add(product)
        order.customer = cust
        order.vendor = vendor

        return redirect('dashboard:order')

    return render(request, 'addOrder.html')


def orderPage(request):
    order = Order.objects.all()
    
    return render(request, 'order.html', {'orders': order})


def detailedOrderPage(request, pk):
    order = Order.objects.get(id=pk)
    return render(request, 'orderDetails.html')
