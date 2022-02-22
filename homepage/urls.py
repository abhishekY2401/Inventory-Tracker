
from django.urls import path
from register.views import registerPage
from homepage.views import homePage
from dashboard.views import dashboardPage

urlpatterns = [
    path('', homePage, name="homepage"),
    path('dashboard/', dashboardPage, name="dashboard"),
    path('register/', registerPage, name="register"),
]
