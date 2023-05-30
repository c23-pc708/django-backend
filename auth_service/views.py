from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    pass


def login(request):
    pass


def logout(request):
    pass


def get_user(request):
    pass
