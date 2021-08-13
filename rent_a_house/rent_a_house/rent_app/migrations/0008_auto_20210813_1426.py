# Generated by Django 3.2.5 on 2021-08-13 11:26

import cloudinary.models
from django.db import migrations, models
import rent_a_house.rent_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0007_alter_offer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='offer',
            name='title',
            field=models.CharField(max_length=30, validators=[rent_a_house.rent_app.validators.validate_title]),
        ),
    ]
