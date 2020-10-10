from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import models as userModel

from .models import blog,breed
# you can write from . import forms and then inside all functions forms=forms.CreateBlogForm()
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'index.html')

def identifyBreed(request):
    if request.method == 'POST':
        form = CreateBreedForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            form = CreateBreedForm()  # wrote this line cuz after submit we should clear form fields
            filepath = instance.img.url
            return render(request, 'identifBreed.html', {'form': form,'imag':instance,'filepath':filepath})
    else:
        form = CreateBreedForm()
        return render(request, 'identifBreed.html', {'form': form})

def blogs(request):
    return render(request, 'blogs.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if userModel.User.objects.filter(username=username).exists():
                print('Usernme exists')
                messages.info(request, 'Username exists')
                return redirect('register')
            elif userModel.User.objects.filter(email=email).exists():
                print('email exists')
                messages.info(request, 'Email exists')
                return redirect('register')
            else:
                user = userModel.User.objects.create_user(
                    username=username, email=email, password=password1, first_name=fname, last_name=lname)
                user.save()
                return redirect('login')
        else:
            print('pass dosent match')
            messages.info(request, 'Password didn\'t match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = userModel.auth.authenticate(username=username, password=password)

        if user is not None:
            userModel.auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid details')
            return redirect('login')
    else:
        return render(request, "login.html")
    return render(request, "login.html")


def logout(request):
    userModel.auth.logout(request)
    return redirect('/')

