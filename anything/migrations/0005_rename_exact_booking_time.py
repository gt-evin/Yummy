# Generated by Django 5.0.2 on 2024-02-28 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anything', '0004_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='exact',
            new_name='time',
        ),
    ]
