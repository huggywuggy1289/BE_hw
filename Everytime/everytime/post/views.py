from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.db.models import F  # F 객체를 사용하여 조회수 증가
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "post/list.html", {'posts': posts})
#blog/index.html에서 posts 변수명으로 사용할 수 있도록

@login_required
def create(request):
    if request.method == "POST": # 사용자의 요청이 POST인지 확인

        # post(데이터명) 데이터에서 title과 content 값을 추출
        # = 왼쪽에 있는 변수는
        title = request.POST.get('title')
        content = request.POST.get('content')
        created_at = request.POST.get('created_at')
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        # views = request.POST.get('views')

        post = Post.objects.create(
            title = title, # 여기 = 오른쪽에 있는 변수와 일치
            content = content,
            created_at = created_at,
            is_anonymous = is_anonymous,
            author = request.user, # 추가
            # views = views,
        )
        return redirect('post:list') # list.html인 urls로 이동한다는 의미
    return render(request, 'post/create.html')

def detail(request, id):
    # Post 데이터를 데이터베이스에서 찾으면 가져오고 못찾으면 404 띄우기
    post = get_object_or_404(Post, id = id)
    return render(request, 'post/detail.html', {'post' : post})

@login_required
def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        # post 데이터를 가져와서 띄운 다음에
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.created_at = request.POST.get('created_at')
        post.save()
        return redirect('post:detail', id)
    return render(request, 'post/update.html', {'post' : post})
@login_required
def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('post:list')

# 댓글작성 추가
def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        is_anonymous = request.POST.get('is_anonymous') == 'on'
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            is_anonymous = is_anonymous,
            post = post
        )
        return redirect('post:detail', post_id)
    
def add_like(request, post_id):
    # post객체가 Post 모델을 받아옴으로서  템플릿에서는 {{post.title(나 content 등)}}을 사용가능한것
    post = get_object_or_404(Post, id = post_id)
    post.like.add(request.user)
    return redirect('post:detail', post_id)

def remove_like(request, post_id):
    post = get_object_or_404(Post, id =post_id)
    post.like.remove(request.user)
    return redirect('post:detail', post_id)

def mylike(request):
    liked_posts = Post.objects.filter(like = request.user).order_by('-id')
    return render(request, 'accounts/myblog.html',{'posts': liked_posts})
#redirect는 url 경로 name
#render는 html경로라 템플릿안에 폴더 경로 입력해야함(get 요청된 페이지를 템플릿과 결합하여 반환한다.)