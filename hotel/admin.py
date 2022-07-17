from django.contrib import admin
from hotel.models.Hotel import Hotel
from hotel.models.HotelImage import HotelImage
from hotel.models.HotelReviews import HotelReview
from hotel.models.Reservation import Reservation


# Register your models here.
admin.site.register(Hotel)
admin.site.register(HotelImage)
admin.site.register(HotelReview)
admin.site.register(Reservation)
