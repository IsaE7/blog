from django.shortcuts import render
from django.http import HttpResponse
import random


def text_response(request):
    return HttpResponse(f"Hello, world. You're at the polls list.{random.randint(0, 100)}")


def template(request):
    return render(request, 'template.html')
