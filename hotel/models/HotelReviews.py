from django.db import models
from authentication.models import User
from hotel.models.Hotel import Hotel


class HotelReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    location = models.FloatField(default=0.0)
    value_of_money = models.FloatField(default=0.0)
    cleanliness = models.FloatField(default=0.0)
    services = models.FloatField(default=0.0)
    avg_rating = models.FloatField(default=0.0)
    comment = models.TextField()
    emoji = models.CharField(max_length=20, default='neutral.png')
    emotion = models.CharField(max_length=20, default='Neutral')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    modified_at = models.DateTimeField(auto_now_add=True, blank=True)
