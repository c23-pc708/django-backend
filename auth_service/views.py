from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import User
from django_backend.utils import validate_body

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    is_valid = validate_body(
        request,
        ["first_name", "last_name", "username", "email", "password", "phone_number"],
    )

    if is_valid != None:
        return is_valid

    if (
        User.objects.filter(username=request.data.get("username")).exists()
        or User.objects.filter(email=request.data.get("email")).exists()
    ):
        return Response(data="User already exists", status=status.HTTP_409_CONFLICT)

    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    password = request.data.get("password")
    phone_number = request.data.get("phone_number")

    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )
    user_profile = user.userprofile
    user_profile.phone_number = phone_number
    user_profile.save()
    return Response(data="Registration successful", status=status.HTTP_201_CREATED)


def login(request):
    pass


def logout(request):
    pass


def get_user(request):
    pass
