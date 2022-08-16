from django.db import models
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from os.path import splitext
from hashlib import sha224
import string
import random
from datetime import datetime


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str.encode('UTF-8')


def upload_to_id_image(instance, filename):
    extension = splitext(filename)[1].lower()
    return 'users/%(year)s/%(month)s/%(day)s/%(name)s%(extension)s' % {
        'year': datetime.now().strftime("%Y"),
        'month': datetime.now().strftime("%m"),
        'day': datetime.now().strftime("%d"),
        'name': sha224(get_random_string(10)).hexdigest(),
        'extension': extension,
    }


# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=20, default="user")
    avatar = ProcessedImageField(upload_to=upload_to_id_image,
                                 blank=True,
                                 format='JPEG',
                                 processors=[ResizeToFill(200, 200)],
                                 options={
                                     'quality': 90
                                 }
                                 )
    token = models.CharField(max_length=255, blank=True, default=None, null=True)


