# Generated by Django 5.0.6 on 2024-06-20 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_alter_vehicle_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicletype',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
