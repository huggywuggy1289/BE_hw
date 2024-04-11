"""
URL configuration for phone_Prj project.

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
# from contacts import views
# url('A',include('B.urls')) 는 ~A 인 url들은 B 어플리케이션 안에 있는 urls.py를 참고하라는 말과 같다.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')), #contacts 내부의 urls.py를 참조하라는 의미
]
