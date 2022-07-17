from django.urls import path, include
from .views import (
    home_view,
    hotel_detail_view,
    make_reservation,
    reservations_view
)

urlpatterns = [
    path('', home_view, name="home"),
    path('<slug:slug>', hotel_detail_view, name="hotel.details"),
    path('reservation/<slug:slug>', make_reservation, name="hotel.reservation.create"),
    path('hotel/reservations', reservations_view, name="hotel.reservation"),
    path('admin/', include('hotel.admin_urls'))
]
