# Generated by Django 5.0.1 on 2024-04-08 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='novosti',
        ),
    ]
