from django.contrib import admin
from hotel.models.Hotel import Hotel
from hotel.models.HotelImage import HotelImage


# Register your models here.
admin.site.register(Hotel)
admin.site.register(HotelImage)
