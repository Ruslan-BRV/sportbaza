# Generated by Django 5.0.1 on 2024-03-23 15:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='upload_date',
            field=models.DateTimeField(db_column='upload_date', default=datetime.datetime(2024, 3, 23, 18, 18, 39, 317499), verbose_name='дата загрузки'),
        ),
    ]
