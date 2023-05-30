from django.urls import path
from .views import register, login, logout, get_user

app_name = "auth_service"

urlpatterns = [
    path("register", register, name="register"),
    path("login", login, name="token_obtain_pair"),
    path("logout", logout, name="logout"),
    path("user", get_user, name="user"),
]
