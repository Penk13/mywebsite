# Generated by Django 3.2 on 2021-08-25 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True),
        ),
    ]
