from django.urls import path
from order.views import addOrderPage
from order.views import orderPage

urlpatterns = [
    path('order/', orderPage, name="order"),
    path('create/', addOrderPage, name="addOrders")
]
