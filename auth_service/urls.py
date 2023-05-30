from django.urls import path
from .views import register, login, logout, get_user

app_name = "auth_service"

urlpatterns = [
    path("register", register, name="register"),
    path("user", get_user, name="user"),
]
