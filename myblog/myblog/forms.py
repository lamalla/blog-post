from django import forms
from blog.models import *


class CommentForm(forms.ModelForm):
        date = models.DateTimeField()
        author= models.CharField(max_length=200)
        text =  models.TextField(default="")
        class Meta:
            model = Comment
            fields= ('author', 'text')
