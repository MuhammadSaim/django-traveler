from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils.text import slugify
import string
import random
from django.urls import reverse
from os.path import splitext
from hashlib import sha224
from datetime import datetime


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str.encode('UTF-8')


def upload_to_id_image(instance, filename):
    extension = splitext(filename)[1].lower()
    return 'hotels/%(year)s/%(month)s/%(day)s/%(name)s%(extension)s' % {
        'year': datetime.now().strftime("%Y"),
        'month': datetime.now().strftime("%m"),
        'day': datetime.now().strftime("%d"),
        'name': sha224(get_random_string(10)).hexdigest(),
        'extension': extension,
    }


# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    feature_image = ProcessedImageField(upload_to=upload_to_id_image,
                                        format='JPEG',
                                        processors=[ResizeToFill(500, 500)],
                                        options={
                                            'quality': 90
                                        })
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    total_rating = models.FloatField(default=0.0)
    total_emotion_rating = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + rand_slug())
        super(Hotel, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('hotel.details', kwargs={'slug': self.slug})
