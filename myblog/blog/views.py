from django.shortcuts import render, redirect
from django.http import HttpResponse
from myblog.forms import *
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = form.cleaned_data['author']
            comment.text= form.cleaned_data['text']
            comment.date = datetime.now()
            comment.save()
            post_title= form.postId
            curr_post= Post.objects.filter(title= post_title)
            curr_post.comments.add(comment)
            curr_post.save()
            return redirect('/blog/')
    else:
        form= CommentForm()
    posts= Post.objects.all()
    context={'blog_posts': posts, 'form': form}
    return render(request, "blog_page.html", context)
