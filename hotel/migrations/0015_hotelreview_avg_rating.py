# Generated by Django 4.0.6 on 2022-07-25 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0014_remove_hotelreview_rating_hotelreview_cleanliness_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotelreview',
            name='avg_rating',
            field=models.FloatField(default=0.0),
        ),
    ]