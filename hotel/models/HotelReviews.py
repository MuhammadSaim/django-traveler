from django.db import models
from authentication.models import User
from hotel.models.Hotel import Hotel


class HotelReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    emoji = models.CharField(max_length=20, default='neutral.png')
    emotion = models.CharField(max_length=20, default='Neutral')
