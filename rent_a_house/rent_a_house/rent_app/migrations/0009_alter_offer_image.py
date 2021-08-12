# Generated by Django 3.2.5 on 2021-08-12 15:25

import cloudinary.models
from django.db import migrations
import rent_a_house.rent_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0008_auto_20210808_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, validators=[rent_a_house.rent_app.validators.validate_image_format]),
        ),
    ]
