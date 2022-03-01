from django.db import models

# Create your models here.


class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True, max_length=255)
    company_name = models.CharField(max_length=50)
