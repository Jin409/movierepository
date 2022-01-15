from django.contrib import admin
from django.urls import path,include

from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name='post'

urlpatterns = [
    path('new',new,name="new"),
    path('post_detail/<int:id>',post_detail,name="post_detail"),
    path('post_delete/<int:id>',post_delete,name="post_delete"),
    
    
]
