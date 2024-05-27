from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
# Form 활용

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form' : form})
    
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        return redirect('BlogApp:list')
    else:
        #여전히 회원가입 폼에 머물게 함
        return render(request, 'accounts/signup.html', {'form' : form})
    
def login_view(request):
    if request.method == "GET":
        return render(request, 'accounts/login.html', {'form' : AuthenticationForm })
    form =AuthenticationForm(request, data = request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('BlogApp:list')
    return render(request, 'accounts/signup.html', { 'form' : form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('BlogApp:list')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def user_info(request):
    return render(request, 'accounts/user-info.html')

def myblog(request):
    posts = request.user.posts.all().order_by('-id')
    return render(request, 'accounts/myblog.html', {'posts' : posts})