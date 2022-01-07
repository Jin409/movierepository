

from django.db import models

# Create your models here.

class User(models.Model):
  user_email = models.CharField(max_length=30)
  user_id = models.CharField(max_length=30)
  user_nickname = models.CharField(max_length=30)
  user_repassword = models.CharField(max_length=30,blank=True,null=True)
  user_password = models.CharField(max_length=30)
  def __str__(self):
    return self.user_id