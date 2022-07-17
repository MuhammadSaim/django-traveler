# Generated by Django 4.0.6 on 2022-07-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_hotelreview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelreview',
            name='is_negative',
        ),
        migrations.RemoveField(
            model_name='hotelreview',
            name='is_positive',
        ),
        migrations.AddField(
            model_name='hotelreview',
            name='emoji',
            field=models.CharField(default='neutral.png', max_length=20),
        ),
        migrations.AddField(
            model_name='hotelreview',
            name='emotion',
            field=models.CharField(default='Neutral', max_length=20),
        ),
    ]