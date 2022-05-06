from django.urls import path, include

from register.views import registerPage
from homepage.views import homePage
from dashboard.views import dashboardPage
from signin.views import login_user, logout_user

urlpatterns = [
    path('', homePage, name="homepage"),
    path('register/', registerPage, name="register"),
    path('signin/', login_user, name="login"),
    path('logout_user', logout_user, name="logout"),
    path('dashboard/', dashboardPage, name="dashboard")
]
