from django.shortcuts import render
from user.models import *
from django.http import HttpResponse

# Create your views here.
def home(request):
    user_id = request.session.get('user')
    info_msg = {}
    if user_id:
        user = User.objects.get(pk = user_id)
        info_msg['welcome'] = "%s님 환영합니다!"%user.user_nickname
       
    return render(request,'home.html',info_msg,user_id)
        

def detail(request):
    return render(request,'detail.html')