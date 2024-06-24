"""
URL configuration for wordCount_Pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from wordCountApp import views
# from blog import views

urlpatterns = [
    path('admin/', admin.site.urls), # admin사이트 주소 경로를 보여주고 이건 장고에서 제공하는 형식
    path('', views.index, name="index"), # views파일에서 이름이 index인 함수를 실행한다. 라고 명령
    path('wordCount/', views.wordCount, name="wordCount"), # wordCount사이트 경로를 만들고 views파일에서 이름이 wordCount인 함수를 실행한다. 라고 명령
    path('result/', views.result, name="result"), # result사이트 경로를 만들고 views파일에서 이름이 result인 함수를 실행한다. 라고 명령
    # path('result/', views.result1, name="result1" )
    path('hello/', views.hello, name="hello"),
]
