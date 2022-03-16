from secrets import choice
from django.db import models

# Create your models here.


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered')
    )

    order_id = models.AutoField("Order_ID", primary_key=True)
    company_name = models.CharField(max_length=255, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    invoice_no = models.IntegerField("Invoice_No", unique=True)

    def __str__(self):
        return self.order_id


class Customer(models.Model):
    customer_id = models.IntegerField('Customer_ID')
    customer_name = models.CharField(max_length=255, null=True)
    address = models.TextField('Address', max_length=255)
    phone_no = models.IntegerField('Phone_no')
    email_id = models.EmailField('Email', max_length=50)

    def __str__(self):
        return self.customer_id


class Product(models.Model):
    product_id = models.IntegerField("Product_ID")
    product_name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    unit = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField("Quantity")
    price = models.FloatField("Price", null=True)

    def __str__(self):
        return self.product_id
