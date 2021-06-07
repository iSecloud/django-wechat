from django.shortcuts import render
from .models import WeChatUser, Status

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

def show_status(request):
    statuses = Status.objects.all()
    return render(request, 'status.html', {'statuses': statuses})

def submit_post(request):
    return render(request, 'my_post.html')