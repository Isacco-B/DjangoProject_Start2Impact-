# Generated by Django 4.1.5 on 2023-02-02 15:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_alter_certificate_date_of_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_profile',
        ),
        migrations.AlterField(
            model_name='certificate',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 15, 30, 42, 178542, tzinfo=datetime.timezone.utc)),
        ),
    ]
