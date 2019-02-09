from django.shortcuts import render, redirect
from django.http import HttpResponse
from myblog.forms import *
from .models import *
from datetime import datetime

# Create your views here.
def index(request):
    if request.method == "POST":
        #print('this is a post')
        form = CommentForm(request.POST)
        #if form.is_valid():
            # comment = form.save(commit=False)
            # comment.author = form.cleaned_data['author']
            # comment.text= form.cleaned_data['text']
            # comment.date = datetime.now()

            # comment = form.save(commit=False)
        author = request.POST['author']
        text= request.POST['text']
        postId= request.POST['post_Id']
        date = datetime.now()
        comment = Comment.objects.create(author=author, text=text, date= date)
        #print(comment)


            #comment.save()

            #postId= request.POST.get('id', 2)
            #print(postId)
        curr_post= Post.objects.get(id= postId)
        #print(curr_post)
        curr_post.comments.add(comment)
        #print(curr_post.comments)
        curr_post.save()
        return redirect('/blog/')
    else:
        form= CommentForm()

    posts= Post.objects.all()
    context={'blog_posts': posts, 'form': form}
    return render(request, "blog_page.html", context)
