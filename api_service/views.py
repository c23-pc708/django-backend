from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import Destination
import json


# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def destinations(request):
    dest = Destination.objects.all()
    exist_params = False
    dest_result = Destination.objects.none()

    art = request.query_params.get("art")
    if art is not None and int(art) == 1:
        exist_params = True
        dest_art = dest.filter(art=1)
        dest_result = dest_result.union(dest_art)

    entertainment = request.query_params.get("entertainment")
    if entertainment is not None and int(entertainment) == 1:
        exist_params = True
        dest_ent = dest.filter(entertainment=1)
        dest_result = dest_result.union(dest_ent)

    sightings = request.query_params.get("sightings")
    if sightings is not None and int(sightings) == 1:
        exist_params = True
        dest_sgt = dest.filter(sightings=1)
        dest_result = dest_result.union(dest_sgt)

    culinary = request.query_params.get("culinary")
    if culinary is not None and int(culinary) == 1:
        exist_params = True
        dest_cul = dest.filter(culinary=1)
        dest_result = dest_result.union(dest_cul)

    shopping = request.query_params.get("shopping")
    if shopping is not None and int(shopping) == 1:
        exist_params = True
        dest_shp = dest.filter(shopping=1)
        dest_result = dest_result.union(dest_shp)

    search = request.query_params.get("q")
    if search is not None:
        exist_params = True
        dest_result = dest.filter(name__icontains=search)

    if not exist_params:
        dest_result = dest

    dest = dest_result.values(
        "id",
        "name",
        "art",
        "entertainment",
        "sightings",
        "culinary",
        "shopping",
        "image_link",
        "location",
        "description",
        "weekdays_time",
        "weekend_time",
        "lowest_price",
        "highest_price",
        "rating",
        "location_link",
    )
    dest_list = list(dest)
    return Response(data=dest_list)


@api_view(["GET"])
@permission_classes([AllowAny])
def destination_detail(request, destination_id):
    try:
        dest = Destination.objects.get(id=destination_id)
        dest = Destination.objects.filter(id=destination_id).values()[0]
        return Response(data=dest)
    except Destination.DoesNotExist:
        return Response(status=404, data={"message": "Destination not found."})
