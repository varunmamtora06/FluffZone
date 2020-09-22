from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import models

from .models import blog
# you can write from . import forms and then inside all functions forms=forms.CreateBlogForm()
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def identifyBreed(request):
    return render(request, 'identifBreed.html')

def blogs(request):
    return render(request, 'blogs.html')

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

