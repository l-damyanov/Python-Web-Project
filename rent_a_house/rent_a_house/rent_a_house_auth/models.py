from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from rent_a_house.rent_a_house_auth.managers import RentAHouseUserManager


class RentAHouseUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,

    )

    # profile_image = models.ImageField(
    #     upload_to='profile_images',
    #     blank=True,
    # )

    # first_name = models.CharField(
    #     max_length=15,
    # )

    # last_name = models.CharField(
    #     max_length=15,
    # )

    # phone_number = PhoneNumberField(
    #     null=True,
    #     max_length=15,
    #     region='BG',
    # )

    USERNAME_FIELD = 'email'

    objects = RentAHouseUserManager()
