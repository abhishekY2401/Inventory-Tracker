from django.urls import path, re_path
from .views import *

app_name = 'dashboard'

urlpatterns = [
    re_path(r'^api/data/$', get_data, name="api_data"),
    re_path(r'^api/chart/data/$', ChartData.as_view()),
    path('order/', orderPage, name="order"),
    path('order/create/', addOrderPage, name="addOrders"),
    path('order/create/order_submission/',
         order_submission, name="order_submission"),
    path('order/<str:pk>/', detailedOrderPage, name="orderDetails"),
    path('order/<str:pk>/edit/', editOrder, name="editOrder"),
    path('order/<str:pk>/delete/', deleteOrder, name="deleteOrder"),
    path('order/<str:pk>/invoice/', ViewInvoice.as_view(), name="view_invoice"),
    path('order/<str:pk>/invoice/pdf', GeneratePDF.as_view(), name="invoice_pdf"),
]
