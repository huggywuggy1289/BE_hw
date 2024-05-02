from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone
from django.views.generic import ListView, TemplateView
from .models import Q

# # Create your views here.

# FBV방식
def list(request):
    Phones = Phone.objects.all().order_by('-id')
    return render(request, "phone/list.html", {'Phones': Phones}) 

def result(request):
    data = request.GET.get('result', '')
    if not data.strip():
        Phones = [] # 빈 리스트 할당
    else:
        Phones = Phone.objects.filter(Q(title__icontains=data) | Q(contents__icontains=data))
    return render(request, 'phone/result.html', {'Phones' : Phones, 'data' : data})

# def search(request):
#     data = request.GET.get('search', '')
#     if not data.strip(): # 검색어가 빈 문자열인 경우
#         Phones = [] # 빈 리스트 할당
#     else:
#         Phones = Phone.objects.filter(name__icontains=data)
#     return render(request, "phone/search.html", {'Phones' : Phones, 'data' : data})

def create(request):
    if request.method == "POST": # 사용자의 요청이 POST인지 확인
        # = 왼쪽에 있는 변수는
        name = request.POST.get('name')
        phone_num = request.POST.get('phone_num')
        email = request.POST.get('email')

        # Phone.objects.create를 사용하여 객체를 생성합니다. (Phones 대신 Phone)
        Phone.objects.create(
            name=name,
            phone_num=phone_num,
            email=email,
        )
        return redirect('list') # list.html인 urls로 이동한다는 의미
    return render(request, 'phone/create.html')

def detail(request, id):
    # Post 데이터를 데이터베이스에서 찾으면 가져오고 못찾으면 404 띄우기
    phone = get_object_or_404(Phone, id = id)
    return render(request, 'phone/detail.html', {'phone' : phone})

def update(request, id):  # 이름(name) 대신 id를 받음
    phone = get_object_or_404(Phone, id=id)
    if request.method == "POST":
        phone.name = request.POST.get('name')
        phone.phone_num = request.POST.get('phone_num')
        phone.email = request.POST.get('email')
        phone.save()
        return redirect('detail', id=id)  # 템플릿 이름을 'blog/update.html'에서 'phone/detail.html'로 수정
    return render(request, 'phone/update.html', {'phone': phone})  # 템플릿 이름을 'blog/update.html'에서 'phone/update.html'로 수정



def delete(request, id):  # 'name' 대신 'id'를 받음
    phone = get_object_or_404(Phone, id=id)
    phone.delete()
    return redirect('list')

# 뷰 함수
def delete_confirm(request, id):  
    phone = get_object_or_404(Phone, id=id)
    return render(request, 'phone/delete_confirm.html', {'phone': phone})


#-----------------------------------------------------------------
#CBV방식
# class PhoneListView(ListView): # 목록을 보여준다.
#     model = Phone
#     template_name = 'phone/list.html'
#     context_object_name = 'Phones' # 템플릿에서 사용할 컨텍스트 변수명 설정
#     ordering = ['name'] # 이름으로 정렬

# class PhoneSearchView(ListView):
#     model = Phone
#     template_name = "phone/search.html"
#     context_object_name = "Phones"

#     def get_queryset(self):
#         query = self.request.GET.get('search', '')
#         if query:
#             return Phone.objects.filter(name__icontains=query)
#         else:
#             return Phone.objects.none()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['data'] = self.request.GET.get('search', '')
#         return context


