from django.contrib import admin
from .models import Post

#클래스 추가
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'modified_at'] #나열하고 싶은 필드 선택
# Register your models here. 모델등록
    
admin.site.register(Post, PostAdmin) 