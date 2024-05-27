from django.db import models
from django.db.models import Q
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(to = User, on_delete= models.CASCADE, related_name="posts")
    category = models.ManyToManyField(to = Category, through="PostCategory", related_name="posts")
    like = models.ManyToManyField(to = User, through="Like", related_name="liked_posts")

    def __str__(self):
        return f'[{self.id}] {self.title}'
    
class Comment(models.Model):
    post = models.ForeignKey(to = Post, on_delete= models.CASCADE, related_name="comments")
    content = models.TextField()
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