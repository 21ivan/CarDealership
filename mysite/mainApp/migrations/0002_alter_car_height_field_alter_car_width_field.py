# Generated by Django 4.0.4 on 2022-06-07 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='height_field',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='width_field',
            field=models.IntegerField(null=True),
        ),
    ]