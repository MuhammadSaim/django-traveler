from django.db import models
from .Hotel import Hotel
import string
import random
from hashlib import sha224
from datetime import datetime
from os.path import splitext
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


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


class HotelImage(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True)
    image = ProcessedImageField(upload_to=upload_to_id_image,
                                format='JPEG',
                                processors=[ResizeToFill(500, 500)],
                                options={
                                    'quality': 90
                                })
