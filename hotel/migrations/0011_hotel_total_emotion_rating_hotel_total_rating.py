# Generated by Django 4.0.6 on 2022-07-17 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0010_remove_hotelreview_is_negative_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='total_emotion_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='hotel',
            name='total_rating',
            field=models.FloatField(default=0.0),
        ),
    ]
