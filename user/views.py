from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from user.forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout


def register_view(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'user/register.html', context={'form': form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return render(request, 'user/register.html', context={'form': form})
        form.cleaned_data.__delitem__('confirm_password')
        User.objects.create(
            **form.cleaned_data,
        )
        return redirect('/')


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
