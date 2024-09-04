from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from tracknumber.serializers import *
from django.shortcuts import render

from .services import NextTracking
# Create your views here.
class NextTrackingNumber(APIView):
    def post(self, request):
        tracking_data = request.data
        serializer = AddTrackingSerializer(data=tracking_data)
        serializer.is_valid(raise_exception=True)
        result = NextTracking.tracking_add_update(serializer)
        context = {"data": result}
        return Response(context, status=status.HTTP_200_OK)

    def get(self, request, format=None):
        serializer = TrackingNumberSerializer(many=True)
        context = {"data": serializer.data,}
        return Response(context, status=status.HTTP_200_OK)