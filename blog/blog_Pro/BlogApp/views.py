from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Category
from django.db.models import F  # F 객체를 사용하여 조회수 증가
from django.contrib.auth.decorators import login_required

# Create your views here.
def list(request):
    categories = Category.objects.all()

    category_id = request.GET.get('category')

    if category_id:
        category = get_object_or_404(Category, id = category_id)
        posts = category.posts.all().order_by('-id')
    else:
        posts = Post.objects.all().order_by('-id')
    return render(request, 'BlogApp:list.html', {'posts': posts, 'categories' : categories})

    # posts = Post.objects.all().order_by('-id')
    # return render(request, "blog/list.html", {'posts': posts})
#blog/index.html에서 posts 변수명으로 사용할 수 있도록

@login_required
def create(request):
    if request.method == "POST": # 사용자의 요청이 POST인지 확인
        categories = Category.objects.all()

        # post(데이터명) 데이터에서 title과 content 값을 추출
        # = 왼쪽에 있는 변수는
        title = request.POST.get('title')
        content = request.POST.get('content')
        # views = request.POST.get('views') 
               
        category_ids = request.POST.getlist('category')
        category_list = [get_object_or_404(Category, id = category_id) for category_id in category_ids]

        post = Post.objects.create(
            title = title, # 여기 = 오른쪽에 있는 변수와 일치
            content = content,
            author = request.user,
            # views = views,
        )
        #다대다 카테고리 연결
        for category in category_list:
            post.category.add(category)

        return redirect('BlogApp:list') # list.html인 urls로 이동한다는 의미
    return render(request, 'blog/create.html', {'categories': categories})

def detail(request, id):
    # Post 데이터를 데이터베이스에서 찾으면 가져오고 못찾으면 404 띄우기
    post = get_object_or_404(Post, id = id)
    return render(request, 'blog/detail.html', {'post' : post})

def update(request, id):
    post = get_object_or_404(Post, id = id)
    if request.method == "POST":
        # post 데이터를 가져와서 띄운 다음에
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('BlogApp:detail', id)
    return render(request, 'blog/update.html', {'post' : post})

def delete(request, id):
    post = get_object_or_404(Post, id = id)
    post.delete()
    return redirect('BlogApp:list')

def create_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.method == "POST":
        Comment.objects.create(
            content = request.POST.get('content'),
            author = request.user,
            post = post
        )
        return redirect('BlogApp:detail', post_id)
