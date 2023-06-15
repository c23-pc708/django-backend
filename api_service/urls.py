from django.urls import path
from .views import destinations, destination_detail, predict

app_name = "api_service"

urlpatterns = [
    path("destinations", destinations, name="destinations"),
    path(
        "destinations/<int:destination_id>",
        destination_detail,
        name="destination_detail",
    ),
    path("predict", predict, name="predict"),
]
