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
                "type": "Art",
                "location": "Kuta",
                "opening_type": "10.00-15.00",
                "description": "asdjfalskdj falskdjhf lkash jdlfkajsh dlfkajsh dlkfjah sdlkfjah sklf",
            },
            {
                "destinationId": 2,
                "name": "the second destination",
                "type": "Entertainment",
                "location": "Pantai Kuta",
                "opening_time": "10.00-15.00",
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
            "type": "Art",
            "location": "Kuta",
            "opening_time": "10.00-15.00",
            "description": "asdjfalskdj falskdjhf lkash jdlfkajsh dlfkajsh dlkfjah sdlkfjah sklf",
        },
    )
