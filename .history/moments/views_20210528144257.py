from django.shortcuts import redirect, render
from .models import WeChatUser, Status
from django.contrib.auth.decorators import login_required

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
    
    if text: #这个判断主要是因为submit_post会处理两个请求 一个是导航栏的请求，一个是post的submit按钮的请求  
        status = Status(user=user, text=text, pic=pic) #构建一条内容
        status.save() #保存数据库
        return redirect('/status') #重定向到status页面
    return render(request, 'my_post.html')