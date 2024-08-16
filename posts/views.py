"""
model.objects.all() - возвращает все записи из базы данных
model.objects.get() - возвращает одну запись из базы данных
model.objects.filter() - возвращает записи из базы данных по условию
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import Post
import random


def text_response(request):
    if request.method == "GET":
        return HttpResponse(f"Hello, world. You're at the polls list.{random.randint(0, 100)}")


def template(request):
    if request.method == "GET":
        return render(request, 'template.html')


def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'post_list.html', context={'posts': posts})


def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, 'post_detail.html', context={'post': post})


def post_create_view(request):
    if request.method == "GET":
        return render(request, 'post_create.html')
    if request.method == "POST":
        image = request.FILES.get('image')
        title = request.POST.get('title')
        content = request.POST.get('content')
        rate = request.POST.get('rate')
        Post.objects.create(
            image=image,
            title='title',
            content='content',
            rate=3,
        )
        return redirect('/posts/')

