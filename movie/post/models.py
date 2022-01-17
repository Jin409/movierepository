from django.db import models
from user.models import User
from movie import settings

# Create your models here.

STAR_CHOICES = (
    #첫번쨰는 모델에서 받아들이는, 두번째는 실제로 models.py 작성시에 뜨는
    ('&#11088',"&#11088"),
    ('&#11088&#11088',"&#11088&#11088"),
    ('&#11088&#11088&#11088',"&#11088&#11088&#11088"),
    ('&#11088&#11088&#11088&#11088',"&#11088&#11088&#11088&#11088"),
    ('&#11088&#11088&#11088&#11088&#11088',"&#11088&#11088&#11088&#11088&#11088")
)

class Post(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    score = models.CharField(null=False,max_length=1000,choices=STAR_CHOICES)
    image = models.ImageField(upload_to="post/",null=True, blank=True)
    def summary(self):
        return self.body[:10]
   



    

