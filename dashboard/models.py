from django.db import models

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
