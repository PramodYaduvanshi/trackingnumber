from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('next-tracking-number', NextTrackingNumber.as_view(), name="nexttrackingnumber"),
    path('get-tracking-number', NextTrackingNumber.as_view(), name="gettrackingnumber")
]
