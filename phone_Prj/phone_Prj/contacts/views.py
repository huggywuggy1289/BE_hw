from django.shortcuts import render
from .models import Phone
from django.views.generic import ListView, TemplateView
from .models import Q

# # Create your views here.

# #FBV방식
# # def list(request):
# #     Phones = Phone.objects.all().order_by('name') # 이름순으로 정렬해서
# #     return render(request, "phone/list.html", {'Phones': Phones})

# # def search(request):
# #     data = request.GET.get('search', '')
# #     if not data.strip(): # 검색어가 빈 문자열인 경우
# #         Phones = [] # 빈 리스트 할당
# #     else:
# #         Phones = Phone.objects.filter(name__icontains=data)
# #     return render(request, "phone/search.html", {'Phones' : Phones, 'data' : data})

# #CBV방식
class PhoneListView(ListView): # 목록을 보여준다.
    model = Phone
    template_name = 'phone/list.html'
    context_object_name = 'Phones' # 템플릿에서 사용할 컨텍스트 변수명 설정
    ordering = ['name'] # 이름으로 정렬

class PhoneSearchView(TemplateView): # 검색을 수행한다.
    template_name = 'phone/search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = self.request.GET.get('search', '')
        if not data.strip(): # 검색어가 빈 문자열인 경우
            context['Phones'] = [] # 빈 리스트 할당
        else:
            context['Phones'] = Phone.objects.filter(name__icontains=data)
        context['data'] = data
        return context


