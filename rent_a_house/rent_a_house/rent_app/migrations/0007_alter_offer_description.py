# Generated by Django 3.2.5 on 2021-07-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent_app', '0006_alter_offer_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]
