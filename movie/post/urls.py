from django.contrib import admin
from django.urls import path,include

from .views import *

app_name='post'

urlpatterns = [
    path('',new,name="new"),
    
]