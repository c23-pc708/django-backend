from django.urls import path
from .views import register, login, logout

app_name = "auth_service"

urlpatterns = [
    path("register", register, name="register"),
]
