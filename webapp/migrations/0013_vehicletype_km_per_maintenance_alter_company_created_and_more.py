# Generated by Django 5.0.6 on 2024-06-09 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_company_created_alter_person_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicletype',
            name='km_per_maintenance',
            field=models.IntegerField(auto_created=True, default=2000),
        ),
        migrations.AlterField(
            model_name='company',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 17, 37, 58, 811548)),
        ),
        migrations.AlterField(
            model_name='person',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 17, 37, 58, 811548)),
        ),
        migrations.AlterField(
            model_name='rent',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 17, 37, 58, 812688)),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 17, 37, 58, 812476)),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 9, 17, 37, 58, 812288)),
        ),
    ]
