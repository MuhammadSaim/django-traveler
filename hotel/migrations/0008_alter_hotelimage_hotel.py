# Generated by Django 4.0.6 on 2022-07-15 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_rename_hotel_id_hotelimage_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotelimage',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel'),
        ),
    ]
