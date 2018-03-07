from django.db import models

# Create your models here.
class Book (models.Model):
    bid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    auther_id = models.ForeignKey('Auther', on_delete=models.CASCADE)
    publishedAt = models.CharField(max_length=100)
    summary = models.CharField(max_length=400)
    country = models.CharField(max_length=100)
    link = models.CharField(max_length=200)
    imageUrl = models.CharField(max_length=400, default="null")
class Auther (models.Model):
    aid=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    bornAt = models.CharField(max_length=100)
    diedAt = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    imageUrl = models.CharField(max_length=400, default="null")
class User (models.Model):
    uid=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200,unique=True)
    password=models.CharField(max_length=200)

