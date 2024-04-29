from django.urls import path
from .views import list, create, detail, update, delete, result

urlpatterns = [
    path('', list, name='list'), # 일반 8000포트
    path('result/', result, name = 'result'),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update" ),
    path('delete/<int:id>/', delete, name = "delete" ),
]