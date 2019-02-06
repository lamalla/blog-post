from django.db import models
from datetime import datetime


class Owner(models.Model):
    name = models.CharField(max_length=200)

class Post(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    author= models.ForeignKey(Owner, on_delete=models.CASCADE)
    text= models.TextField(default="")

class Comment(models.Model):
    date = models.DateTimeField()
    author= models.CharField(max_length=200)
    text =  models.TextField(default="")
    post=  models.ForeignKey(Post, on_delete=models.CASCADE)
