from django.db import models


class Offer(models.Model):
    title = models.CharField(
        max_length=30,
    )
    city = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    price = models.FloatField()
    available = models.BooleanField(
        default=False,
    )
    image = models.ImageField(
        upload_to='offers',
    )
