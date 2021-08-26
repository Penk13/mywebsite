from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class About(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.TextField(blank=False)
    motto = models.TextField()
    my_service = models.TextField()
    # skill
    # project
    # blog
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    image = models.ImageField(upload_to='project/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return 'My Contact Info'
