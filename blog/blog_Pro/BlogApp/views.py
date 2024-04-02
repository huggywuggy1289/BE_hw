from django.shortcuts import render
from .models import Post

# Create your views here.
def list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, "blog/list.html", {'posts': posts})
#blog/index.html에서 posts 변수명으로 사용할 수 있도록
