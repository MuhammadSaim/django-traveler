# Generated by Django 4.0.6 on 2022-07-08 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, height_field=200, upload_to='users/%Y/%m/%d/', width_field=200),
        ),
    ]
