from django.conf import settings
from .models import NextTrackingNumber


class NextTracking:
    def tracking_add_update(request_data, pk=None):
        corporate = NextTrackingNumber.objects.create(request_data.data)
        return corporate
