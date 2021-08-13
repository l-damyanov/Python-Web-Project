from django.contrib.auth import get_user_model
from django.db import models

from rent_a_house.rent_a_house_profiles.models import Profile
from rent_a_house.rent_app.validators import validate_image_format, validate_title

UserModel = get_user_model()


class Offer(models.Model):
    title = models.CharField(
        max_length=30,
        validators=[validate_title],
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
        validators=[validate_image_format],
        blank=False,
        null=False,
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
