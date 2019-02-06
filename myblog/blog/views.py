from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    posts= Post.objects.all()
    context={'blog_posts': posts}
    return render(request, "blog_page.html", context)
