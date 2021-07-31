from django.contrib.auth import get_user_model
from django.db import models

from rent_a_house.rent_app.models import Offer

UserModel = get_user_model()


class Comment(models.Model):
    text = models.TextField(
        max_length=250,
    )
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
