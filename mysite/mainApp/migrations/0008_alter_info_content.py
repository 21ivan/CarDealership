# Generated by Django 4.0.4 on 2022-06-13 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='content',
            field=models.TextField(max_length=900),
        ),
    ]
