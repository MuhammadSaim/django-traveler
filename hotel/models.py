from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
import string
import random


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    feature_image = ProcessedImageField(upload_to='hotels/%Y/%m/%d/', blank=True,
                                        format='JPEG',
                                        processors=[ResizeToFill(200, 200)],
                                        options={
                                            'quality': 90
                                        })
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + rand_slug())
        super(Hotel, self).save(*args, **kwargs)
