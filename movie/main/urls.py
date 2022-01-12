from django.urls import path
from .views import *

app_name='main'

urlpatterns=[

path('<int:id>',detail,name="detail"),
    
]