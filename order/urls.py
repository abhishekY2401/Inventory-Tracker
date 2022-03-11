from django.urls import path

from order.views import detailedOrderPage

urlpatterns = [
    path('order/<str:id>/', detailedOrderPage, name="order"),
]