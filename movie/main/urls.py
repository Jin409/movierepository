from django.urls import path
from .views import *

app_name='main'

urlpatterns=[

path('<int:id>',detail,name="detail"),
path('profile_update/<int:id>',profile_update,name="profile_update"),

    
]