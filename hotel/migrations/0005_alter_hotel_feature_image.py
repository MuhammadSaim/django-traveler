# Generated by Django 4.0.6 on 2022-07-12 17:52

from django.db import migrations
import hotel.models.Hotel
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_remove_hotel_specifications_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='feature_image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=hotel.models.Hotel.upload_to_id_image),
        ),
    ]
