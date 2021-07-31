from django.contrib.auth import get_user_model
from django.db import models

from rent_a_house.rent_a_house_profiles.models import Profile

UserModel = get_user_model()


class Offer(models.Model):
    title = models.CharField(
        max_length=30,
    )
    city = models.CharField(
        max_length=30,
    )
    description = models.TextField(
        max_length=150,
    )
    price = models.FloatField()
    available = models.BooleanField(
        default=False,
    )
    image = models.ImageField(
        upload_to='offers',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class Rate(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
