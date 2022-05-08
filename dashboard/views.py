
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
from datetime import date
import random


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

    invoice_no = random.randint(1000, 9999)
    print(invoice_no)

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
        order.invoice_no = invoice_no
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

class ViewInvoice(View):

    def get(self, request, pk, *args, **kwargs):

        taxes = {
            "electronics": {
                "import_duty": "30%",
                "cgst": "19%",
                "handling_charges": "6%"
            },
            "chemicals": {
                "import_duty": "20%",
                "cgst": "5%",
                "handling_charges": "2%"
            },
            "hazardous chemicals": {
                "import_duty": "25%",
                "cgst": "12%",
                "handling_charges": "3%"
            },
            "automobiles": {
                "import_duty": "15%",
                "cgst": "18%",
                "handling_charges": "6%" 
            },
            "clothes": {
                "import_duty": "5%",
                "cgst": "5%",
                "handling_charges": "4%"
            },
        }

        context = {}
        template = get_template('invoice.html')
        order = Order.objects.get(order_id=pk)
        products = order.product.all()
        today = date.today()

        context["id"] = pk
        context["vendor_name"] = order.vendor
        context["vendor_email"] = order.vendor.email_id
        context["invoice"] = order.invoice_no
        context["name"] = order.customer
        context["phone"] = order.customer.phone_no
        context["address"] = order.customer.address
        context["date"] = today
        context["products"] = products

        for i in products:
            category = i.category

        # CALCULATE FINAL AMOUNT BY ADDING handling charges, import duty
        for key in list(taxes.keys()):
            if key == category:
                context["category"] = taxes.get(key)
                
        print(taxes.get(key))

        return render(request, "invoice.html", context)


class GeneratePDF(View):

    def get(self, request, pk, *args, **kwargs):

        context = {}
        taxes = {
            "electronics": {
                "import_duty": "30%",
                "cgst": "19%",
                "handling_charges": "6%"
            },
            "chemicals": {
                "import_duty": "20%",
                "cgst": "5%",
                "handling_charges": "2%"
            },
            "hazardous chemicals": {
                "import_duty": "25%",
                "cgst": "12%",
                "handling_charges": "3%"
            },
            "automobiles": {
                "import_duty": "15%",
                "cgst": "18%",
                "handling_charges": "6%" 
            },
            "clothes": {
                "import_duty": "5%",
                "cgst": "5%",
                "handling_charges": "4%"
            },
        }

        template = get_template('invoice.html')
        order = Order.objects.get(order_id=pk)
        products = order.product.all()
        today = date.today()

        context["id"] = pk
        context["vendor_name"] = order.vendor
        context["vendor_email"] = order.vendor.email_id
        context["invoice"] = order.invoice_no
        context["name"] = order.customer
        context["phone"] = order.customer.phone_no
        context["address"] = order.customer.address
        context["date"] = today
        context["products"] = products

        for i in products:
            category = i.category

        # CALCULATE FINAL AMOUNT BY ADDING handling charges, import duty
        for key in list(taxes.keys()):
            if key == category:
                context["category"] = taxes.get(key)

        html = template.render(context)
        pdf = render_to_pdf('invoicePdf.html', context)
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
