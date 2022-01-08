from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *

def login(request):
    if request.method =='GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_email = request.POST.get('user_email', None)
        user_password = request.POST.get('user_password', None)
        err_data = {}
        if not(user_email and user_password):
            err_data['error'] = '모든 값을 입력해 주세요.'
            return render(request,'login.html',{'err_data':err_data})
        else:
            user = User.objects.get(user_email=user_email)
            if user!=None:
                if check_password(user_password, user.user_password):
                    request.session['user'] = user.user_id
                else:
                    err_data['error'] = '비밀번호가 일치하지 않습니다.'
                    return render(request,'login.html',{'err_data':err_data})
            else:
                err_data['nouser'] = '존재하지 않는 사용자입니다.'
                return render(request,'login.html',{'err_data':err_data})
            return redirect("home")
        

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
        
    

        

    
