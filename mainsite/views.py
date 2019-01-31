from django.http import HttpResponse
from .models import Post
from django.shortcuts import render

def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_list.append("No.{}:".format(str(count)) + str(post)+"<br>")
    return HttpResponse(post_lists)
