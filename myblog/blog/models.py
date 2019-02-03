from django.db import models


class Comment(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateTimeField('date posted')
