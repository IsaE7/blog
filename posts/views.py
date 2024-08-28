"""
model.objects.all() - возвращает все записи из базы данных
model.objects.get() - возвращает одну запись из базы данных
model.objects.filter() - возвращает записи из базы данных по условию
"""

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse

from posts.forms import PostForm, SearchForm
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
        search = request.GET.get('search')
        tags = request.GET.getlist('tags')
        orderings = request.GET.get('orderings')
        searchform = SearchForm(request.GET)
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        if search:
            posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
        if tags:
            posts = posts.filter(tags__id__in=tags)
        if orderings:
            posts = posts.order_by(orderings)

        limit = 2
        max_pages = posts.count()/limit
        if round(max_pages) < max_pages:
            max_pages = round(max_pages)+1
        else:
            max_pages = round(max_pages)

        start = (page-1)*limit
        end = page*limit
        posts = posts[start:end]
        context = {'posts': posts, 'search_form': searchform, 'max_pages': range(1, max_pages+1)}
        return render(request, 'posts/post_list.html', context=context)


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

    """posts = [post1, post2, post3, post4, post5, post 6, post7, post8, post9, post10, post11, post12
    limit = 3, page = 3
    formula :
    start = page-1*limit
    (3-1)*3 = 6
    end = 3*3 = 9
    """


