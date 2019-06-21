from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.utils import timezone
from .models import Album, Song, Review
#from forms import RestaurantForm, DishForm
from .views import index, detail
from django.views.generic import DetailView, ListView, UpdateView

urlpatterns = [
    # /music/
    path('', views.index, name=''),
    
    # /music/71/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
         
]
