"""
model.objects.all() - возвращает все записи из базы данных
model.objects.get() - возвращает одну запись из базы данных
model.objects.filter() - возвращает записи из базы данных по условию
"""

from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
import random


def text_response(request):
    return HttpResponse(f"Hello, world. You're at the polls list.{random.randint(0, 100)}")


def template(request):
    return render(request, 'template.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', context={'post': post})

