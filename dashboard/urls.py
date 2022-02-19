
from django.urls import path
from register.views import registerPage
from .views import dashboardPage

urlpatterns = [
    path('', dashboardPage, name="dashboard"),
    path('register/', registerPage, name="register"),
]
