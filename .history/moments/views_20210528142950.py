from django.shortcuts import render
from .models import WeChatUser, Status
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

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
    return render(request, 'my_post.html')