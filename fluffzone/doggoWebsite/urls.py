from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='index'),
    path('identifyBreed', views.identifyBreed, name='identifyBreed'),
    path('blogs', views.blogs, name='blogs'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]

urlpatterns += static(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL)
