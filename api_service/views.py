from django.core import serializers
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
    print("test")
    dest = Destination.objects.all()

    art = request.query_params.get("art")
    if art is not None:
        dest = dest.filter(art=1)

    entertainment = request.query_params.get("entertainment")
    if entertainment is not None:
        dest = dest.filter(entertainment=1)

    sightings = request.query_params.get("sightings")
    if sightings is not None:
        dest = dest.filter(sightings=1)

    culinary = request.query_params.get("culinary")
    if culinary is not None:
        dest = dest.filter(culinary=1)

    shopping = request.query_params.get("shopping")
    if shopping is not None:
        dest = dest.filter(shopping=1)

    dest_list = serializers.serialize("json", dest)
    return Response(data=json.loads(dest_list))


@api_view(["GET"])
@permission_classes([AllowAny])
def destination_detail(request, destination_id):
    return Response(
        data={
            "destinationId": 1,
            "name": "destination one",
            "type": "Art",
            "location": "Kuta",
            "opening_time": "10.00-15.00",
            "description": "asdjfalskdj falskdjhf lkash jdlfkajsh dlfkajsh dlkfjah sdlkfjah sklf",
        },
    )
