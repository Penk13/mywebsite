# Generated by Django 3.2 on 2021-08-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('like', models.IntegerField()),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
