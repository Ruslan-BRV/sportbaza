# Generated by Django 5.0.1 on 2024-04-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programms', '0005_programms_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='programms',
            name='is_checked',
            field=models.BooleanField(choices=[(False, 'Не проверено'), (True, 'Проверено')], default=False, verbose_name='Проверено'),
        ),
    ]
