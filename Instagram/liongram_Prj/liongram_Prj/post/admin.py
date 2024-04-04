from django.contrib import admin
from .models import Post #models.py에서 정의하고 등록한 모델을 불러오고

# Post클래스를 add할때 어떻게 보여질지 구현이 되야한다!
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['title'] #보여지고 싶은 모델의 필드만 선택
# 근데 이미 모델에서 명시해뒀으니까 쓸필요없을듯

# Register your models here.
admin.site.register(Post) #실제로 admin사이트에서 해당 모델을 접근할 수 있게 된다.
