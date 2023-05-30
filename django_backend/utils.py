from rest_framework import status
from rest_framework.response import Response


def validate_params(request, params):
    """Validate URL query params"""
    for param in params:
        res = request.query_params.get(param)
        if res is None:
            return Response(
                data=f"{param} is required", status=status.HTTP_400_BAD_REQUEST
            )
    return None


def validate_body(request, attrs):
    """Validate request body for POST requests"""
    for attr in attrs:
        res = request.data.get(attr)
        if res is None:
            return Response(
                data=f"{attr} is required", status=status.HTTP_400_BAD_REQUEST
            )
    return None
