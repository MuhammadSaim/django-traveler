from django.urls import path, include
from .views import (
    home_view,
    hotel_detail_view
)

urlpatterns = [
    path('', home_view, name="home"),
    path('<slug:slug>', hotel_detail_view, name="hotel.details"),
    path('admin/', include('hotel.admin_urls'))
]
