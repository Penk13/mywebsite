# Generated by Django 3.2 on 2021-08-26 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_delete_blog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='me',
        ),
        migrations.RemoveField(
            model_name='project',
            name='me',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='me',
        ),
    ]