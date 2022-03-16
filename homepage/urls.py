from django.urls import path, include

# from login.views import loginRequest
from login.views import loginRequest
from register.views import registerPage
from homepage.views import homePage
from dashboard.views import dashboardPage
urlpatterns = [
    path('', homePage, name="homepage"),
    path('register/', registerPage, name="register"),
    path('login/',  loginRequest, name="login"),
    path('dashboard/', dashboardPage, name="dashboard")
]
