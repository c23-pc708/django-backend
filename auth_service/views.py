from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from django_backend.utils import validate_body
from django.contrib.auth import authenticate

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
        return Response(
            data={"message": "User already exists"}, status=status.HTTP_409_CONFLICT
        )

    username = request.data.get("username")
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    password = request.data.get("password")
    phone_number = request.data.get("phone_number")

    user = User.objects.create_user(
        username=username,
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
    )
    user_profile = user.userprofile
    user_profile.phone_number = phone_number
    user_profile.save()
    return Response(
        data={"message": "Registration successful"}, status=status.HTTP_201_CREATED
    )


@api_view(["POST"])
@permission_classes([AllowAny])
def login(request):
    is_valid = validate_body(request, ["username", "password"])

    if is_valid != None:
        return is_valid

    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        tokens = {
            "access": str(access),
            "refresh": str(refresh),
        }

        data = get_user_data(user)
        data["tokens"] = tokens

        response = Response(data=data, status=status.HTTP_200_OK)
        response.set_cookie(
            key="refresh_token", value=str(refresh), httponly=True, samesite="Lax"
        )
        return response
    else:
        return Response(
            data={"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


@api_view(["POST"])
def logout(request):
    try:
        token = request.COOKIES.get("refresh_token")
        print(f"Token: {token}")
        token = RefreshToken(token)
        token.blacklist()
        return Response(
            data={"message": "Logged out successfully"}, status=status.HTTP_200_OK
        )
    except Exception as e:
        return Response(
            data={"message": "Logout failed", "error": str(e)},
            status=status.HTTP_401_UNAUTHORIZED,
        )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user(request):
    return Response(data=get_user_data(request.user))


def get_user_data(user):
    return {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "username": user.username,
        "email": user.email,
        "phone_number": user.userprofile.phone_number,
    }
