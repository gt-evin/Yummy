# Generated by Django 5.0.2 on 2024-02-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anything', '0003_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('exact', models.CharField(max_length=100)),
                ('people', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]