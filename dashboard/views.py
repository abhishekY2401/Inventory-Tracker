
from ast import Bytes
import random
from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

@login_required
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

@login_required
def addOrderPage(request):
    return render(request, 'addOrder.html')

@login_required
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

@login_required
def orderPage(request):
    context = {}

<<<<<<< HEAD
    amount = Product.objects.values_list('price')
=======
    order = Order.objects.all()
    context['order'] = order
>>>>>>> cea638c8ac2eeacea4f97275228aaaa7db96b333

    return render(request, 'order.html', context)

@login_required
def detailedOrderPage(request, pk):
    context = {}
    
    order = Order.objects.get(order_id=pk)
    context['data'] = order
    context['products'] = order.product.all()

    return render(request, 'orderDetails.html', context)

@login_required
def editOrder(request, pk):
    context = {}

    order = Order.objects.get(order_id=pk)
    context['data'] = order
    context['products'] = order.product.all()

    return render(request, 'edit.html', context)

@login_required
def deleteOrder(request, pk):

    order = Order.objects.get(order_id=pk)
    products = order.product.all()
    cust = order.customer
    vend = order.vendor
    order.delete()
    products.delete()
    cust.delete()
    vend.delete()

    return redirect('dashboard:order')

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):

        template = get_template('invoice.html')
        context = {
            "invoice_no": 123,
            "customer_name": "Abhishek Yadav",
            "amount": 1389.98,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'dash.html', {})


def get_data(request, *args, **kwargs):

    data = {
        "warehouse_space": "5000 sq.ft",
        "fixed_quantity": 30000
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        data = {}

        orders = Order.objects.all()

        for id in orders:
            order = Order.objects.get(order_id=id.order_id)
            data['order'] = order
            data['products'] = order.product.all()
            print(data)

        return Response(data)
