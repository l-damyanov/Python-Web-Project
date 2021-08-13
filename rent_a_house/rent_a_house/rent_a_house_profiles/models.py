from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from rent_a_house.rent_a_house_auth.models import RentAHouseUser
from cloudinary import models as cloudinary_models


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profile_images',
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=15,
        blank=False,
    )

    last_name = models.CharField(
        max_length=15,
        blank=False,
    )

    phone_number = PhoneNumberField(
        max_length=15,
        region='BG',
        blank=False,
    )

    is_complete = models.BooleanField(
        default=False,
    )

    user = models.OneToOneField(
        RentAHouseUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


from .signals import *
