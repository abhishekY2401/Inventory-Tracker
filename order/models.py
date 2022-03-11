from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField("Order_ID", primary_key=True)
    company_name = models.CharField(default="NULL", max_length=255)
    customer_id = models.IntegerField('Customer_ID')
    customer_name = models.CharField(default="NULL", max_length=255)
    address = models.TextField('Address', max_length=255)
    phone_no = models.IntegerField('Phone_no')
    email_id = models.EmailField('Email', max_length=50)
    product_id = models.IntegerField("Product_ID")
    product_name = models.CharField(default="NULL", max_length=255)
    quantity = models.IntegerField("Quantity", unique=True)
    price = models.IntegerField("Price", unique=True)
    invoice_no = models.IntegerField("Invoice_No", unique=True)
