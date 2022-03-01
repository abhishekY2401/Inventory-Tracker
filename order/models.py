from django.db import models

# Create your models here.


class Order(models.Model):
    order_id = models.AutoField("Order_ID", primary_key=True)
    company_name = models.CharField("Company_Name", max_length=255)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    invoice_no = models.IntegerField("Invoice_No")


class Product(models.Model):
    product_id = models.AutoField("Product_ID", primary_key=True)
    product_name = models.CharField("Product_Name", max_length=255)
    quantity = models.IntegerField("Quantity")
    price = models.IntegerField("Price")


class Customer(models.Model):
    customer_id = models.AutoField('Customer_ID', primary_key=True)
    customer_name = models.CharField('Customer_Name', max_length=255)
    address = models.CharField('Address', max_length=255)
    phone_no = models.IntegerField('Phone_no')
    email_id = models.EmailField('Email', max_length=50)
