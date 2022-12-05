#This file will help us to set our urls 

from django.urls import path
from . import views

# settting up home url
urlpatterns = [path('',views.index,name='index')] 
