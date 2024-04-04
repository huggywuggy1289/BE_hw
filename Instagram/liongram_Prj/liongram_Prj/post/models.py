from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=20) #제목 최대길이 설정
    contents = models.TextField() #글의 본문
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) #날짜랑 시간까지 포함

    def __str__(self):
        return self.title
