from django.db import models
from user.models import User

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    