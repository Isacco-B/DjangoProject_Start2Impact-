# Generated by Django 4.1.5 on 2023-02-02 20:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_user_user_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 2, 20, 24, 29, 301670, tzinfo=datetime.timezone.utc)),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
