from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=20, default="user")
    avatar = ProcessedImageField(upload_to='users/%Y/%m/%d/',
                                 blank=True,
                                 format='JPEG',
                                 processors=[ResizeToFill(200, 200)],
                                 options={
                                     'quality': 90
                                 }
                                 )
