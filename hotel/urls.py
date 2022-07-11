from django.urls import path, include
from .views import home_view

urlpatterns = [
    path('', home_view, name="home"),
    path('admin/', include('hotel.admin_urls'))
]
