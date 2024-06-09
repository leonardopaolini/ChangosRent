# Generated by Django 5.0.6 on 2024-06-09 01:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_vehicle_year_alter_vehicle_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='buy_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 1, 58, 22, 93013)),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 1, 58, 22, 92823)),
        ),
    ]
