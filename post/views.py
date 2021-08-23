from os import truncate
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from post import models
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts': posts})

def post(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request,'blog-post.html', {'post': post})

def about(request):
    return render(request,'about.html')
