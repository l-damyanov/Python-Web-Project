from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from rent_a_house.rent_a_house_auth.models import RentAHouseUser


class Profile(models.Model):
    profile_image = models.ImageField(
        upload_to='profile_images',
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=15,
        blank=True,
    )

    last_name = models.CharField(
        max_length=15,
        blank=True,
    )

    phone_number = PhoneNumberField(
        max_length=15,
        region='BG',
        blank=True,
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
