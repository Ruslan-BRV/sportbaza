# Generated by Django 5.0.1 on 2024-01-31 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programms', '0003_alter_typeprogramms_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeprogramms',
            old_name='typePrograms',
            new_name='typeProgramms',
        ),
    ]
