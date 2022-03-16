from django.urls import path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    path('order/', orderPage, name="order"),
    path('order/create/', addOrderPage, name="addOrders"),
    path('order/<str:pk>/', detailedOrderPage, name="orderDetails")
]
