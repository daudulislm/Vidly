# Generated by Django 3.0.6 on 2020-05-17 08:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 17, 8, 27, 34, 593198, tzinfo=utc)),
        ),
    ]
