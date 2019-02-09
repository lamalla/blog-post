from django.shortcuts import render, redirect
from django.http import HttpResponse
from myblog.forms import *
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == "POST":
        #form = CommentForm(request.POST)
        #if form.is_valid():
            # comment = form.save(commit=False)
            # comment.author = form.cleaned_data['author']
            # comment.text= form.cleaned_data['text']
            # comment.date = datetime.now()

            # comment = form.save(commit=False)
            author = request.POST['author']
            text= request.POST['text']
            date = datetime.now()
            comment = Comment.objects.create(author=author, text=text, date= date)


            #comment.save()
            postId= request.POST['id']
            curr_post= Post.objects.filter(id= postId)
            curr_post.comments.add(comment)
            curr_post.save()
            post_comments= curr_post.comments.all()
            return redirect('/blog/')
    else:
        form= CommentForm()
    posts= Post.objects.all()
    context={'blog_posts': posts, 'post_comments': post_comments, 'form': form}
    return render(request, "blog_page.html", context)
