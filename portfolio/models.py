from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Portfolio(models.Model):
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
    me = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    percent = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    me = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    me = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    me = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.me.name
