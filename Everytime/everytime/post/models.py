from django.db import models
from django.conf import settings
from user.models import User #  user폴더안에 User모델
from django.db.models import Q
import os
from uuid import uuid4
from django.utils import timezone

# uuid라는 자동 고유 식별자 생성기를 이용하여 파일 경로의 중복을 방지
def upload_filepath(instance, filename):
    today_str = timezone.now().strftime("%Y%m%d")
    file_basename = os.path.basename(filename)
    return f'{instance._meta.model_name}/{today_str}/{str(uuid4())}_{file_basename}'

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank = True, null = True)

    def __str__(self):
        return f'{self.name}'

# class CategoryAdmin(admin.ModelAdmin):
#     prepoulated_fields = {'slug':('title',)}
    
# admin.site.register(Category, CategoryAdmin)

class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    is_anonymous = models.BooleanField(default="True")
    author = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name="posts")
    category = models.ManyToManyField(to = Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to = User, through="Like", related_name="liked_posts")
    image = models.ImageField(upload_to = upload_filepath, blank = True) # 이미지 업로드 모델
    video = models.FileField(upload_to = upload_filepath, blank = True)
    

    def __str__(self):
        return f'[{self.id}] {self.title}'
class Comment(models.Model):
    post = models.ForeignKey(to = Post, on_delete= models.CASCADE, related_name="comments")
    content = models.TextField()
    is_anonymous = models.BooleanField(default="True")
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to = User, on_delete= models.CASCADE, related_name="comments")

    def __str__(self):
        return f'[{self.id}] {self.content}'
    
class PostCategory(models.Model):
    category = models.ForeignKey(to = Category, on_delete=models.PROTECT, related_name="posts_postcategory")
    post = models.ForeignKey(to = Post, on_delete=models.CASCADE, related_name="posts_postcategory")

class Like(models.Model):
    post = models.ForeignKey(to = Post, on_delete= models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(to = User, on_delete= models.CASCADE, related_name= "user_likes")

class Scrap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    scrapped_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')