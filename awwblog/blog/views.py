from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status="published")
    return render(request, 'post_list.html',{'posts':posts})
