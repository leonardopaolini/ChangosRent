# Generated by Django 5.0.6 on 2024-06-09 01:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicletype',
            old_name='typeOfUses',
            new_name='type_of_uses',
        ),
        migrations.AddField(
            model_name='vehicletype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 1, 16, 29, 241622)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 1, 16, 29, 241799)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='lock_for_rent',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
