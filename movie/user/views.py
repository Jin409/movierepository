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
            return render(request,'login.html',err_data)
        else:
            try:
                user = User.objects.get(user_email=user_email)
            except:
                err_data['nouser'] = '존재하지 않는 사용자입니다.'
                return render(request,'login.html',err_data)
            else:
                if check_password(user_password, user.user_password):
                    request.session['user'] = user.id
                else:
                    err_data['password'] = '비밀번호가 일치하지 않습니다.'
                    return render(request,'login.html',err_data)
            return redirect("home")
        
def email_checker(user_email):
    try:
        user = User.objects.get(user_email = user_email)
    except:
        return True
    return False

def nickid_checker(user_nickid):
    try:
        user = User.objects.get(user_nickid = user_nickid)
    except:
        return True
    return False

        

def signup(request):
    if request.method=="GET":
        return render(request,'signup.html')
    else:
        err_msg = {}
        new_user = User()
        new_user.user_nickid = request.POST['user_nickid']
        new_user.user_nickname = request.POST['user_nickname']
        new_user.user_password = request.POST['user_password']
        new_user.user_email = request.POST['user_email']
        new_user.user_repassword = request.POST['user_repassword']
        new_user.user_introduce = request.POST['introduce']
        new_user.user_image = request.FILES['image']
        if new_user.user_email =='' or new_user.user_nickid=='' or new_user.user_nickname=='' or new_user.user_password=='' or new_user.user_repassword=='':
            err_msg['blank'] = "모든 값을 입력해주세요. 빈칸이 존재합니다."
            return render(request,'signup.html',err_msg)
        duplicate = nickid_checker(new_user.user_nickid)
        if duplicate==False:
            err_msg['duplicate_nickid'] = "이미 존재하는 아이디입니다."
            return render(request,'signup.html',err_msg)
        duplicate = email_checker(new_user.user_email)
        if duplicate==False:
            err_msg['duplicate_email'] = "이미 존재하는 이메일입니다."
            return render(request,'signup.html',err_msg)
        if new_user.user_password!=new_user.user_repassword:
            err_msg['password'] = "비밀번호가 일치하지 않습니다."
            return render(request,'signup.html',err_msg)
        new_user.user_password = make_password(request.POST['user_password'])
        new_user.user_repassword = make_password(request.POST['user_repassword'])
        new_user.save()
    request.session['user'] = new_user.id
    return redirect("home")

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
        return redirect("home")
    




    
        
    

        

    
