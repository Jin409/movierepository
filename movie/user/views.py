from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password


from .models import *

def login(request):
    return render(request,'login.html')

def signup(request):
    if request.method=="GET":
        return render(request,'signup.html')
    
    else:
        err_msg = {}
        new_user = User()
        new_user.user_id = request.POST['user_id']
        new_user.user_nickname = request.POST['user_nickname']
        new_user.user_password = request.POST['user_password']
        new_user.user_email = request.POST['user_email']
        new_user.user_repassword = request.POST['user_repassword']
        if new_user.user_password!=new_user.user_repassword:
            return redirect('user:signup')
        new_user.user_password = make_password(request.POST['user_password'])
        new_user.user_repassword = make_password(request.POST['user_repassword'])
        new_user.save()
    return render(request,'signup.html',{'err_msg':err_msg})
        
        

    
