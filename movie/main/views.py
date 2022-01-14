from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.hashers import make_password, check_password
from user.models import *
from django.http import HttpResponse
from post.models import Post

# Create your views here.
def home(request):
    user_id = request.session.get('user')
    users = User.objects.all()
    
    if user_id:
        user = User.objects.get(pk = user_id)
        
        welcome=True
        return render(request,'home.html',context = {'welcome':welcome,'user':user,'users':users})
    else:
        welcome=False
        return render(request,'home.html',{'welcome':welcome,'users':users})

    


def detail(request,id):
    user_detail = get_object_or_404(User,pk=id)
    posts = Post.objects.filter(user = user_detail)
    user_id = request.session.get('user')
    info_msg = {}
    if user_id:
        user = User.objects.get(pk = user_id)
        welcome = True
        return render(request,'detail.html',{"user_detail":user_detail,'welcome':welcome,"user":user,'posts':posts})
    else:
        welcome = False
        return render(request,'detail.html',{"user_detail":user_detail,'welcome':welcome,'posts':posts})
    
def profile_update(request,id):
    profile_user = User.objects.get(id=id)
    if request.method=="POST":
        profile_user.user_nickid = request.POST['user_nickid']
        profile_user.user_nickname = request.POST['user_nickname']
        profile_user.user_password = make_password(request.POST['user_password'])
        profile_user.save()
        return redirect('home')
    else:
        user_id = request.session.get('user')
        if user_id:
            user = User.objects.get(pk = user_id)
            welcome=True
            return render(request,'profile_update.html',context = {'welcome':welcome,'user':user,'profile_user':profile_user})
        else:
            welcome=False
            return render(request,'profile_update.html',{'welcome':welcome})
    
##복붙
# user_id = request.session.get('user')
#     if user_id:
#         user = User.objects.get(pk = user_id)
        
#         welcome=True
#         return render(request,'home.html',context = {'welcome':welcome,'user':user,'users':users})
#     else:
#         welcome=False
#         return render(request,'home.html',{'welcome':welcome,'users':users})

def profile_delete(request,id):
    if request.session.get('user'):
        del(request.session['user'])
    profile_user = User.objects.get(id=id)
    profile_user.delete()
    
    return redirect("home")
    
