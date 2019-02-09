from django.db import models
from datetime import datetime


class Owner(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Comment(models.Model):
    date = models.DateTimeField()
    author= models.CharField(max_length=200)
    text =  models.TextField(default="")

    def __str__(self):
        return self.text

class Post(models.Model):
    id= models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    author= models.ForeignKey(Owner, on_delete=models.CASCADE)
    text= models.TextField(default="")
    comments= models.ManyToManyField(Comment)

    def __str__(self):
        return self.title
