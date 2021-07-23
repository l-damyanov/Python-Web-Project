from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from rent_a_house.rent_a_house_profiles.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        profile = Profile(
            user=instance,
        )

        profile.save()


@receiver(pre_save, sender=Profile)
def check_is_complete(sender, instance, **kwargs):
    if instance.first_name and instance.last_name and instance.phone_number:
        instance.is_complete = True
