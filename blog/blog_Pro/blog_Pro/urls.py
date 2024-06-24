"""
URL configuration for blog_Pro project.

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
from django.urls import path, include
# 미디어 파일 및 정적 경로 연결
from django.conf import settings
from django.conf.urls.static import static

#lionblog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BlogApp.urls')),
    # accounts앱 하위의 모든 url은 8000포트의 /accounts/~로 시작한다는 뜻
    path('accounts/', include('accounts.urls'))
    # 미디어 파일에 대한 url 제공
    # + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
