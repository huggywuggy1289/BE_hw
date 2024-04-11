from django.contrib import admin
from django.urls import path
from contacts import views
# path() 함수는 URL 패턴을 정의하고 해당 URL에 대한 함수(views)를 지정하는 데 사용할 수 있음
# 다른 애플리케이션의 URL 설정을 현재 애플리케이션의 URL 설정에 포함할 때 사용되는 함수이다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PhoneListView.as_view(template_name = "phone/list.html")), # PhoneListView 클래스를 URL 패턴에 등록
    path('search/', views.PhoneSearchView.as_view(), name='search'), # PhoneSearchView 클래스를 URL 패턴에 등록
]
