from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post
from user.models import User

# Create your views here.
def new(request):
    user_id = request.session.get('user')
    user = User.objects.get(pk = user_id)
    if request.method=="POST":
        new_post = Post()
        new_post.user = user
        new_post.title = request.POST['title']
        new_post.body = request.POST['body']
        new_post.score = request.POST['score']
        new_post.image = request.FILES['image']
        new_post.pub_date = timezone.now()
        new_post.save()
        return redirect('post:post_detail',new_post.id)
    else:
        user = User.objects.get(pk = user_id)
        welcome=True
        return render(request,'new.html',context = {'welcome':welcome,'user':user})

def post_detail(request,id):
    post_detail = get_object_or_404(Post,pk=id)
    user_id = request.session.get('user')
    info_msg = {}
    if user_id:
        user = User.objects.get(pk = user_id)
        welcome = True
        return render(request,'post_detail.html',{"post_detail":post_detail,'welcome':welcome,"user":user})
    else:
        welcome = False
        return render(request,'post_detail.html',{"post_detail":post_detail,'welcome':welcome})

    
def post_delete(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("home")