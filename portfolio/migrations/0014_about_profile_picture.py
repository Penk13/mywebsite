# Generated by Django 3.2 on 2021-08-28 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_rename_portfolio_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='myphoto/'),
        ),
    ]
