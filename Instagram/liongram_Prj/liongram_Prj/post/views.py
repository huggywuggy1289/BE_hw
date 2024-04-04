from django.shortcuts import render
from .models import Post
from django.db.models import Q

# Create your views here.
def list(request):
    posts = Post.objects.all()
    return render(request, "pist/list.html", {'posts': posts}) 
# request를 받고 pist폴더에 있는 list.html을 불러와라

def result(request):
    data = request.GET.get('result', '')
    if not data.strip():
        posts = [] # 빈 리스트 할당
    else:
        posts = Post.objects.filter(Q(title__icontains=data) | Q(contents__icontains=data))
    return render(request, 'pist/result.html', {'posts' : posts, 'data' : data})

