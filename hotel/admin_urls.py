from django.urls import path, include
from .admin_views import (
    all_hotels,
    hotel_create,
    hotel_delete,
    hotel_status,
    hotel_edit,
    hotel_gallery,
    hotel_gallery_delete
)


urlpatterns = [
    path('hotels', all_hotels, name="admin.hotels"),
    path('hotel/create', hotel_create, name="admin.hotel.create"),
    path('hotel/delete/<slug:slug>', hotel_delete, name="admin.hotel.delete"),
    path('hotel/status/<slug:slug>', hotel_status, name="admin.hotel.status"),
    path('hotel/edit/<slug:slug>', hotel_edit, name="admin.hotel.edit"),
    path('hotel/gallery/<slug:slug>', hotel_gallery, name="admin.hotel.gallery"),
    path('hotel/gallery/delete/<int:id>/<slug:slug>', hotel_gallery_delete, name="admin.hotel.gallery.delete"),
]
