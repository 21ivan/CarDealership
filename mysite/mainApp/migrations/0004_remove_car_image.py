# Generated by Django 4.0.4 on 2022-06-07 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_remove_car_height_field_remove_car_width_field_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
    ]
