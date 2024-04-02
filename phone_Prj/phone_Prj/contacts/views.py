from django.shortcuts import render
from .models import Phone
from django.db.models import Q

# Create your views here.
def list(request):
    Phones = Phone.objects.all().order_by('name') # 이름순으로 정렬해서
    return render(request, "phone/list.html", {'Phones': Phones}) #list.html로 불러오기인데 왜 안되지!

def search(request):
    data = request.GET.get('search', '')
    if not data.strip(): # 검색어가 빈 문자열인 경우
        Phones = [] # 빈 리스트 할당
    else:
        Phones = Phone.objects.filter(name__icontains=data)
    return render(request, "phone/search.html", {'Phones' : Phones, 'data' : data})
