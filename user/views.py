from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from posts.models import Post
from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

from user.models import Profile


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST,
                            request.FILES)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})

        form.cleaned_data.pop('confirm_password', None)

        image = form.cleaned_data.pop('image', None)

        try:
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )

            Profile.objects.create(user=user, image=image)

            return redirect('/')
        except IntegrityError:
            form.add_error('username', 'Пользователь с таким именем уже существует')
            return render(request, 'user/register.html', context={'form': form})


def login_view(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', context={'form': form})
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/login.html', context={'form': form})
        user = authenticate(**form.cleaned_data)
        if user is None:
            form.add_error('username', f'User {form.cleaned_data.get('username')}not found')
            return render(request, 'user/login.html', context={'form': form})
        login(request, user)
        return redirect('/')


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def profile_view(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'user/profile.html', context={'posts': posts})
