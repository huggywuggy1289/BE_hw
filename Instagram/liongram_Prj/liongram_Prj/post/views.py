from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post
from django.db.models import F  # F 객체를 사용하여 조회수 증가

# Create your views here.
def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "pist/list.html", {'posts': posts}) 
#pist/list.html에서 posts 변수명으로 사용할 수 있도록

def result(request):
    data = request.GET.get('result', '')
    if not data.strip():
        posts = [] # 빈 리스트 할당
    else:
        posts = Post.objects.filter(Q(title__icontains=data) | Q(contents__icontains=data))
    return render(request, 'pist/result.html', {'posts' : posts, 'data' : data})

def create(request):
    if request.method == "POST":

        # post(데이터명) 데이터에서 title과 content 값을 추출
        # = 왼쪽에 있는 변수는
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        views = request.POST.get('views')

        if title and contents:  # title과 contents가 모두 비어있지 않은 경우에만 객체 생성
            post = Post.objects.create(
                title=title,
                contents=contents,
                views = views,
            )
            return redirect('list')
    return render(request, 'pist/create.html')

def detail(request, id):
    # Post 데이터를 데이터베이스에서 찾으면 가져오고 못찾으면 404 띄우기
    post = get_object_or_404(Post, id = id)
    # 조회수 증가
    Post.objects.filter(id=id).update(views=F('views') + 1)
    return render(request, 'pist/detail.html', {'post' : post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        # post 데이터를 가져와서 띄운 다음에
        post.title = request.POST.get('title')
        post.contents = request.POST.get('contents')
        post.save()
        return redirect('detail', id)
    return render(request, 'pist/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('list')