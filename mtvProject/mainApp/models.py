from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    pub_date = models.DateField()
    body = models.TextField()

class User(models.Model):
    SEX = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=SEX)