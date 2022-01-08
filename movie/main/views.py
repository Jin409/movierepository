from django.shortcuts import render
from user.models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    user_id = request.session.get('user')
    if user_id:
        user = User.objects.get(pk = user_id)
        return HttpResponse("Hello! %s님" % user)
    else:
        return HttpResponse("로그인 해주세요!")

def detail(request):
    return render(request,'detail.html')