from django.db import models
from django import forms
from django.forms import widgets

#Form Layout from Crispy Forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(
        max_length=255, default="unknown customer", blank=True)
    address = models.TextField('Address', max_length=255)
    phone_no = models.CharField(max_length=255, null=True)
    email_id = models.EmailField('Email', max_length=50)

    def __str__(self):
        return str(self.customer_name)


class Product(models.Model):
    product_name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField("Quantity")
    price = models.FloatField("Price", null=True)

    def __str__(self):
        return str(self.product_name)


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=255, null=True, blank=True)
    email_id = models.EmailField('Email', max_length=50, null=True)

    def __str__(self):
        return str(self.vendor_name)


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered')
    )

    order_id = models.AutoField("Order_ID", primary_key=True)
    product = models.ManyToManyField(Product)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    invoice_no = models.IntegerField("Invoice_No", unique=True, null=True)
    invoice = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.order_id)

class DateInput(forms.DateInput):
    input_type = 'date'

class InvoiceForm(forms.ModelForm):
    THE_OPTIONS = [
    ('14 days', '14 days'),
    ('30 days', '30 days'),
    ('60 days', '60 days'),
    ]
    STATUS_OPTIONS = [
    ('CURRENT', 'CURRENT'),
    ('OVERDUE', 'OVERDUE'),
    ('PAID', 'PAID'),
    ]

    title = forms.CharField(
                    required = True,
                    label='Invoice Name or Title',
                    widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Invoice Title'}),)
    paymentTerms = forms.ChoiceField(
                    choices = THE_OPTIONS,
                    required = True,
                    label='Select Payment Terms',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    status = forms.ChoiceField(
                    choices = STATUS_OPTIONS,
                    required = True,
                    label='Change Invoice Status',
                    widget=forms.Select(attrs={'class': 'form-control mb-3'}),)
    notes = forms.CharField(
                    required = True,
                    label='Enter any notes for the client',
                    widget=forms.Textarea(attrs={'class': 'form-control mb-3'}))

    dueDate = forms.DateField(
                        required = True,
                        label='Invoice Due',
                        widget=DateInput(attrs={'class': 'form-control mb-3'}),)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6'),
                Column('dueDate', css_class='form-group col-md-6'),
                css_class='form-row'),
            Row(
                Column('paymentTerms', css_class='form-group col-md-6'),
                Column('status', css_class='form-group col-md-6'),
                css_class='form-row'),
            'notes',

            Submit('submit', ' EDIT INVOICE '))

    class Meta:
        fields = ['title', 'dueDate', 'paymentTerms', 'status', 'notes']

