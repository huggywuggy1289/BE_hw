from django.urls import path
from .views import list, create, detail, update, delete, create_comment
#blog
app_name = 'BlogApp'
urlpatterns = [ #views.list 안해도 됨. 이미 from .views import list에서 list함수 자체를 호출하고 있으므로
    path('', list, name='list'),
    path('create/', create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update" ),
    path('delete/<int:id>/', delete, name = "delete" ),
    path('create-comment/<int:post_id>/', create_comment, name ="create-comment"),
]