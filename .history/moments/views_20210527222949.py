from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def show_user(request):
    po = {
        
    }
    return render(request, 'user.html')

def show_status(request):
    return render(request, 'status.html')

def submit_post(request):
    return render(request, 'my_post.html')