from django.shortcuts import render,get_object_or_404
from user.models import *
from django.http import HttpResponse

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
    user_id = request.session.get('user')
    info_msg = {}
    if user_id:
        user = User.objects.get(pk = user_id)
        welcome = True
        return render(request,'detail.html',{"user_detail":user_detail,'welcome':welcome,"user":user})
    else:
        welcome = False
        
        return render(request,'detail.html',{"user_detail":user_detail,'welcome':welcome})
    
def update(request):
    return render(request,'update.html')