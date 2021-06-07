from os import write
from django.db import models
from django.shortcuts import redirect, render
from .models import WeChatUser, Status
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

@login_required
def show_user(request):
    po = {
        'name': 'Mr. Po',
        'motto': 'I am the best!',
        'email': '869820505@qq.com',
        'region': 'Xi\'an',
        'pic': 'Po2.jpg'
    }
    return render(request, 'user.html', {'user': po})

@login_required
def show_status(request):
    statuses = Status.objects.all()
    return render(request, 'status.html', {'statuses': statuses})

@login_required
def submit_post(request):
    user = WeChatUser.objects.get(user=request.user) #得到用户
    text = request.POST.get('text') #得到内容
    pic = request.FILES.get('pic')
    
    if pic:
        picName = pic.name
        with open("./moments/static/image/{}".format(picName), 'wb') as f:
            for block in pic.chunks():
                f.write(block)
    else:
        picName = '' #没有图片就名字字段为空

    if text: #这个判断主要是因为submit_post会处理两个请求 一个是导航栏的请求，一个是post的submit按钮的请求  
        status = Status(user=user, text=text, pic=picName) #构建一条内容
        status.save() #保存数据库
        return redirect('/status') #重定向到status页面
    return render(request, 'my_post.html')

def friend(request):
    return render(request, "friends.html")

def register_user(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username == "":
            raise Exception, "username is null!"
        user = User(username=username, email=email)
        user.set_password(password) #设置密码
        user.save()
        WeChatUser.objects.create(user=user)
    except Exception as err:
        result = False
        message = str(err)
    else:
        result = True
        message = "Register Success!"

    return JsonResponse({"result": result, "message": message})