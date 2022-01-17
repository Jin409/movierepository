

from django.db import models

# Create your models here.

class User(models.Model):
  user_email = models.CharField(max_length=30)
  user_nickid = models.CharField(max_length=30)
  user_nickname = models.CharField(max_length=30)
  user_repassword = models.CharField(max_length=30)
  user_password = models.CharField(max_length=30)
  user_introduce = models.CharField(max_length=100,blank=True,null=True)
  user_image = models.ImageField(upload_to="user/",null=True, blank=True)