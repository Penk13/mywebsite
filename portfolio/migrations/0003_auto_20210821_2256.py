# Generated by Django 3.2 on 2021-08-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210821_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='motto',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='portfolio',
            name='my_service',
            field=models.TextField(blank=True),
        ),
    ]
