# Generated by Django 4.0.6 on 2022-07-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('feature_image', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('description', models.TextField()),
                ('specifications', models.JSONField()),
            ],
        ),
    ]