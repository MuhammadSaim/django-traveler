from django.urls import path, include
from .admin_views import (
    all_hotels,
    hotel_create
)


urlpatterns = [
    path('hotels', all_hotels, name="admin.hotels"),
    path('hotel/create', hotel_create, name="admin.hotel.create"),
]