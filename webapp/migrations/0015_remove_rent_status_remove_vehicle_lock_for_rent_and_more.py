# Generated by Django 5.0.6 on 2024-06-18 22:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_alter_company_created_alter_person_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='status',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='lock_for_rent',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='ready_for_use',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='status',
            field=models.CharField(default='READY_FOR_USE', max_length=30),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 22, 15, 2, 275042, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 22, 15, 2, 275042, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 22, 15, 2, 276083, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 18, 22, 15, 2, 275687, tzinfo=datetime.timezone.utc)),
        ),
    ]
