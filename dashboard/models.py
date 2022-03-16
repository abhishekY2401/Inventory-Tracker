from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.IntegerField('Customer_ID')
    customer_name = models.CharField(max_length=255, null=True)
    address = models.TextField('Address', max_length=255)
    phone_no = models.CharField(max_length=255, null=True)
    email_id = models.EmailField('Email', max_length=50)

    def __str__(self):
        return self.customer_name


class Product(models.Model):
    product_id = models.IntegerField("Product_ID")
    product_name = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=255, null=True)
    unit = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField("Quantity")
    price = models.FloatField("Price", null=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered')
    )

    order_id = models.AutoField("Order_ID", primary_key=True)
    company_name = models.CharField(max_length=255, null=True)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(
        Customer, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    invoice_no = models.IntegerField("Invoice_No", unique=True)
    invoice = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.company_name
