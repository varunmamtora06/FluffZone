from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('identifyBreed', views.identifyBreed, name='identifyBreed'),
    path('blogs', views.blogs, name='blogs'),
    path('adoptions', views.adoptions, name='adoptions'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('writeBlog',views.writeBlog,name='writeBlog'),
    path('myBlogs',views.myBlog,name='myBlogs'),
    path('deleteBlog/<int:pk>',views.deleteBlog,name='deleteBlog'),
    path('editBlog/<int:pk>',views.editBlog,name='editBlog'),
    path('postAdoption',views.postAdoption,name='postAdoption'),
    path('myAdoptions',views.myAdoptions,name='myAdoptions'),
    path('deleteAdoption/<int:pk>',views.deleteAdoption,name='deleteAdoption'),
    path('editAdoption/<int:pk>',views.editAdoption,name='editAdoption'),
    # path('predictImage',views.predictImage,name='PredictImage')
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
