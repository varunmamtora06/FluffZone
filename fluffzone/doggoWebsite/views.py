from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import models as userModel

from .models import blog,breed
# you can write from . import forms and then inside all functions forms=forms.CreateBlogForm()
from .forms import *
# Create your views here.

# import tensorflow as tf
# import tensorflow_hub as hub
# import pandas as pd
# import numpy as np
# import os

def index(request):
    return render(request, 'index.html')






# IMG_SIZE = 224

# df = pd.read_csv("models/labels.csv")
# label = df['breed']


# custom_path = "media/"
# custom_image_paths = []
# print(custom_path)


# filepath = "media/g.jpeg"
# custom_image_paths.append(filepath)

def identifyBreed(request):
    if request.method == 'POST':
        form = CreateBreedForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            form = CreateBreedForm()  # wrote this line cuz after submit we should clear form fields
            global filepath
            filepath = str(instance.img.url)
            custom_path = "media/" + filepath
            f = filepath.lstrip('/')

            
            custom_image_paths[0] = f

            print(custom_image_paths)

            model1 = load_model(model_path1)

            custom_data = create_data_batches(custom_image_paths , test_data=True)

            preds = model1.predict(custom_data)

            preds1 = [get_pred_label(preds[i]) for i in range(len(preds))]


            

            
            #custom_image_paths = [custom_path +fname for fname in os.listdir(custom_path)]
            b  = plot_pred(preds , unique_breeds , n=0)
            percentage = int(b[0])
            lab = b[1] 

            if percentage < 30:
                 
                predBreed = "Please Enter a better image " #this to print

            else :
                predBreed = lab#this to print

            
            
            
            return render(request, 'identifBreed.html', {'form': form,'imag':instance,'filepath':filepath , 'breed':predBreed})
    else:
        form = CreateBreedForm()
        return render(request, 'identifBreed.html', {'form': form})


# def process_image(image_path):

#   image = tf.io.read_file(image_path)

#   image = tf.image.decode_jpeg(image , channels= 3)  # turning jpeg into numerical tensors with three color channels thar=t are (RGB) all images are RGB

#   # image as 255 colors so converting those values of 0-255 to 0-1 values
#   image = tf.image.convert_image_dtype(image , tf.float32)  ## you can check the steps below to see what exactly it does

#   image = tf.image.resize(image , size = [IMG_SIZE , IMG_SIZE])

#   return image


# def get_image_label(image_path , label):
#   image = process_image(image_path)
#   return image,label


# BATCH_SIZE =32

# # if the data is a test data shuffle the data but if it is a vaid data set dont shufffle it

# def create_data_batches(x,y = None , size=BATCH_SIZE , valid_data = False , test_data = False):
#   if test_data:
#     data = tf.data.Dataset.from_tensor_slices((tf.constant(x)))
#     data_batch = data.map(process_image).batch(BATCH_SIZE)
#     return data_batch
   
#   elif valid_data:
#     data = tf.data.Dataset.from_tensor_slices((tf.constant(x), # filepath
#                                                tf.constant(y))) # labels
#     data_batch = data.map(get_image_label).batch(BATCH_SIZE)
#     return data_batch

#   else:
#         data = tf.data.Dataset.from_tensor_slices((tf.constant(x), # filepath
#                                                tf.constant(y))) # labels

#         data = data.shuffle(buffer_size = len(x))

#         data = data.map(get_image_label)  # creates (Image,label) tuple (this also turns image path into preprocessed image)

#         data_batch = data.batch(BATCH_SIZE)

#         return data_batch



# def unbatch(data):
#   image_2 =[]
#   label_2 = []
#   for image , label in data.unbatch().as_numpy_iterator():
#     image_2.append(image)
#     label_2.append(unique_breeds[np.argmax(label)])
  
#   return image_2 , label_2

# unique_breeds = np.unique(label)

# def get_pred_label(prediction_probab):

#   return unique_breeds[np.argmax(prediction_probab)]



# model_path1 = "models/20200803-19021596481332-All images Images.h5"

# def load_model(model_path):

#   print("loading a Model")

#   model = tf.keras.models.load_model(model_path,
#                                     custom_objects = {"KerasLayer":hub.KerasLayer})
  
#   return model

# model1 = load_model(model_path1)

# custom_data = create_data_batches(custom_image_paths , test_data=True)

# preds = model1.predict(custom_data)

# preds1 = [get_pred_label(preds[i]) for i in range(len(preds))]







# def plot_read_conf(pred_probas , labels , n =0):

#   pred_prob , t_label = pred_probas[n] , labels[n]

#   pred_label = get_pred_label(pred_prob)

#   top_10_pred_indexes = pred_prob.argsort()[-10:][::-1]

#   top_10_pred_value = pred_prob[top_10_pred_indexes]

#   top_10_labels = unique_breeds[top_10_pred_indexes]

#   return top_10_labels

# def plot_pred(predict_probabs , labels , n=0):

#   pred_prob , t_label  = predict_probabs[n] , labels[n] 

#   pred_label = get_pred_label(pred_prob)
 
  
#   a = (np.max(pred_prob)*100 )
#   return a , pred_label

# b  = plot_pred(preds , unique_breeds , n=0)
# percentage = int(b[0])
# lab = b[1] 

# if percentage < 30:
    
                 
#     predBreed = "Please Enter a better image " #this to print

# else :
#     predBreed = lab #this to print




# print(custom_image_paths)


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

def writeBlog(request):
    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            form = CreateBlogForm()  # wrote this line cuz after submit we should clear form fields
            # wrote this blog fetching query here bcuz we are rendering the blogs page and after submitting new blog user
            blogs = blog.objects.all()
            # is redirected to blog page with the newly created blog and he should be able to see all the blogs
            return redirect('blogs')
    else:
        form = CreateBlogForm()
        return render(request, 'writeblog.html', {'form': form})


def blogs(request):
    blogs = blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs.order_by('-day')})

def myBlog(request):
    user_id = request.user.id
    try:
        blogs = blog.objects.filter(owner_id = user_id)
        return render(request,'myBlogs.html', {'blogs': blogs.order_by('-day')})
    except Exception:   
        return render(request,'myBlogs.html', {'blogs': None})
    return render(request,'myBlogs.html')

def editBlog(request, pk):
    selected_blog = blog.objects.get(id=pk)
    form = CreateBlogForm(instance = selected_blog)

    if request.method == 'POST':
        form = CreateBlogForm(request.POST, request.FILES, instance = selected_blog)
        
        if form.is_valid():
            ins = form.save(commit = False)
            ins.owner = request.user
            ins.save()
            
            # is redirected to blog page with the newly created blog and he should be able to see all the blogs
            return redirect('blogs')
    else:
        form = CreateBlogForm(instance = selected_blog)
    return render(request, 'writeblog.html', {'form': form})

def deleteBlog(request, pk):
    selectedBlog = blog.objects.get(id=pk)
    # print(selectedBlog.title)
    selectedBlog.delete()
    return redirect('myBlogs')