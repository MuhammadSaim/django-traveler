# Generated by Django 4.0.6 on 2022-07-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_hotel_total_emotion_rating_hotel_total_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='hotel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
