from django.urls import path
from . import views


urlpatterns = [
    path('authenticate/login_user', views.login_user, name="login"),
    path('authenticate/logout_user', views.logout_user, name="logout"),
    path('authenticate/register_user', views.register_user, name="register_user")
]

