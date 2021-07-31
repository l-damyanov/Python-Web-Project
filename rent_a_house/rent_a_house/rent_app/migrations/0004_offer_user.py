# Generated by Django 3.2.5 on 2021-07-23 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent_app', '0003_remove_offer_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='user',
            field=models.ForeignKey(default=19, on_delete=django.db.models.deletion.CASCADE, to='rent_a_house_auth.rentahouseuser'),
            preserve_default=False,
        ),
    ]
