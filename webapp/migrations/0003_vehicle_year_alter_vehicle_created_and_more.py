# Generated by Django 5.0.6 on 2024-06-09 01:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_rename_typeofuses_vehicletype_type_of_uses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='year',
            field=models.IntegerField(default=0, max_length=4),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 1, 49, 9, 125941)),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 1, 49, 9, 125766)),
        ),
    ]
