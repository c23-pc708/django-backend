from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
import json


# Create your views here.
@api_view(["GET"])
@permission_classes([AllowAny])
def destinations(request):
    return Response(
        data=[
            {
                "destinationId": 1,
                "name": "destination one",
                "type": ["food", "sightseeing"],
                "location": "Kuta",
                "description": "asdjfalskdj falskdjhf lkash jdlfkajsh dlfkajsh dlkfjah sdlkfjah sklf",
            },
            {
                "destinationId": 2,
                "name": "the second destination",
                "type": ["food", "sightseeing"],
                "location": "Pantai Kuta",
                "description": "asdjfalskdj falskdjhf lkash jdlfkajsh dlfkajsh dlkfjah sdlkfjah sklf",
            },
        ]
    )


@api_view(["GET"])
@permission_classes([AllowAny])
def destination_detail(request, destination_id):
    return Response(
        data={
            "destinationId": 1,
            "name": "destination one",
            "type": ["food", "sightseeing"],
            "location": "Kuta",
            "description": "asdjfalskdj falskdjhf lkash jdlfkajsh dlfkajsh dlkfjah sdlkfjah sklf",
        },
    )
