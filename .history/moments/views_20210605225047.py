from os import write
from django.db import models
from django.shortcuts import redirect, render
from .models import Reply, WeChatUser, Status
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

@login_required
def show_user(request):
    user = WeChatUser.objects.get(user=request.user)
    email = User.objects.get(username=request.user).email #获取email信息
    po = {
        'name': user.user,
        'motto': user.motto,
        'email': email,
        'region': user.region,
        'pic': user.pic,
    }
    return render(request, 'user.html', {'user': po})

@login_required
def show_status(request):
    keyword = request.GET.get("keyword")
    user = WeChatUser.objects.get(user=request.user) #得到当前用户
    statuses = user.status_set.all() #得到用户的status列表
    if keyword:
        #statuses = statuses.filter(text__contains=keyword)
        #statuses = Status.objects.filter(text__contains=keyword)
        statuses = Status.objects.filter(Q(text__contains=keyword) | Q(user__user__username__contains=keyword)) #高级搜索用Q

    paginator = Paginator(statuses, 3)
    page = request.GET.get("page", "1") #有page页就获取，否则就为1
    statuses = paginator.get_page(page) #拿到当前页的信息

    return render(request, 'status.html',  {'statuses': statuses,
                                            'keyword': keyword,
                                            "page": int(page),
                                            "page_range": paginator.page_range, #页码数量
                                            })

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

@login_required
def friend(request):
    return render(request, "friends.html")

def register_user(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if username == "" or password == "":
            raise Exception("some information is null!")
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

    return JsonResponse({"result": result, "message": message}) #返回信息

@login_required
def update_user(request):
    try:
        region = request.POST.get("region")
        email = request.POST.get("email")
        motto = request.POST.get("motto")
        pic = request.POST.get("pic")
        user = WeChatUser.objects.filter(user=request.user) #为啥不能用get获取

        if region: user.update(region=region)
        if pic: user.update(pic=pic)
        if motto: user.update(motto=motto)

        if email:
            User.objects.filter(username=request.user).update(email=email)

    except Exception as err:
        result = False
        message = str(err)
    else:
        result = True
        message = "Update Success!"

    return JsonResponse({"result": result, "message": message}) #返回信息

@login_required 
def like(request):
    user = request.user.username
    status_id = request.POST.get("status_id")
    liked = Reply.objects.filter(author=user, status=status_id, type="0")
    
    #有点赞就取消，否则就加入数据库
    if liked:
        liked.delete()
    else:
        Reply.objects.filter(author=user, status=Status.objects.get(id=status_id), type="0")
    
    return JsonResponse({"result": True})

@login_required 
def comment(request):
    user = request.user.username
    status_id = request.POST.get("status_id")
    text = request.POST.get("text")
    at_person = request.POST.get("at_person")

    #创建一条评论
    Reply.objects.create(author=user, status=Status.objects.get(id=status_id), type="1", text=text, at_person=at_person)
    return JsonResponse({"result": True})

@login_required
def delete_comment(request):
    comment_id = request.POST.get("comment_id")
    #删除本条互动信息
    Reply.objects.filter(id=comment_id).delete()
    return JsonResponse({"result": True})