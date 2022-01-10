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
        

    else:
        info_msg['please'] = "로그인을 해주세요!"
    return render(request,'home.html',info_msg)


        

def detail(request):
    user_id = request.session.get('user')
    info_msg = {}

    if user_id:
        user = User.objects.get(pk = user_id)
        info_msg['welcome'] = "%s님 환영합니다!"%user.user_nickname
        

    else:
        info_msg['please'] = "로그인을 해주세요!"
    

    return render(request,'detail.html',info_msg)