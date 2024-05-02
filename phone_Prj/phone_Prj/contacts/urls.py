from django.urls import path
from .views import list, create, detail, update, delete, result, delete_confirm
# path() 함수는 URL 패턴을 정의하고 해당 URL에 대한 함수(views)를 지정하는 데 사용할 수 있음
# 다른 애플리케이션의 URL 설정을 현재 애플리케이션의 URL 설정에 포함할 때 사용되는 함수이다.

urlpatterns = [
    path('', list, name='list'),
    path('result/', result, name = 'result'),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update" ),
    path('delete/<int:id>/', delete, name = "delete" ),
    # URL 패턴
    path('delete_confirm/<int:id>/', delete_confirm, name='delete_confirm'),
]
