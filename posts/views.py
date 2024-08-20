"""
model.objects.all() - возвращает все записи из базы данных
model.objects.get() - возвращает одну запись из базы данных
model.objects.filter() - возвращает записи из базы данных по условию
"""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from posts.forms import PostForm
from posts.models import Post
import random


def text_response(request):
    if request.method == "GET":
        return HttpResponse(f"Hello, world. You're at the polls list.{random.randint(0, 100)}")


def template(request):
    if request.method == "GET":
        return render(request, 'template.html')


@login_required(login_url='login')
def post_list_view(request):
    if request.method == "GET":
        posts = Post.objects.all()
        return render(request, 'posts/post_list.html', context={'posts': posts})


@login_required(login_url='login')
def post_detail_view(request, post_id):
    if request.method == "GET":
        post = Post.objects.get(id=post_id)
        return render(request, 'posts/post_detail.html', context={'post': post})


@login_required(login_url='login')
def post_create_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, 'posts/post_create.html', context={'form': form})
    if request.method == "POST":

        # Post.objects.create(
        #     image=image,
        #     title='title',
        #     content='content',
        #     rate=3,
        # )
        return redirect('/posts/')

