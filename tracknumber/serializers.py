from rest_framework import serializers
from .models import NextTrackingNumber

class AddTrackingSerializer(serializers.ModelSerializer): 
    class Meta:
        model: NextTrackingNumber
        fields = [
            "origin_country_id",
            "destination_country_id",
            "weight",
            "created_at",
            "customer_id",
            "customer_name",
            "customer_slug",
        ]

class TrackingNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextTrackingNumber
        fields = [
            "origin_country_id",
            "destination_country_id",
            "weight",
            "created_at",
            "customer_id",
            "customer_name",
            "customer_slug",
        ]