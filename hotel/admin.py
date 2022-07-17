from django.contrib import admin
from hotel.models.Hotel import Hotel
from hotel.models.HotelImage import HotelImage
from hotel.models.HotelReviews import HotelReview


# Register your models here.
admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(HotelReview)
