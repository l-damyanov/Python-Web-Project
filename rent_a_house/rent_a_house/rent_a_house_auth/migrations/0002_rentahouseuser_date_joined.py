# Generated by Django 3.2.5 on 2021-07-21 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rent_a_house_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentahouseuser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
