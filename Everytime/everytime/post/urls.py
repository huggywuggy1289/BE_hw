from django.urls import path
from . import views
from .views import list, create, detail, update, delete, create_comment, add_like, remove_like, mylike
#everytime
app_name = 'post'
urlpatterns = [ #views.list 안해도 됨. 이미 from .views import list에서 list함수 자체를 호출하고 있으므로
    path('', list, name="list"),
    # path('create/', create, name = "create"),
    path('create/<slug:slug>/', views.create, name = "create"),
    path('detail/<int:id>/', detail, name = "detail"),
    path('update/<int:id>/', update, name = "update" ),
    path('delete/<int:id>/', delete, name = "delete" ),
    # 댓글 작성 경로
    path('create-comment/<int:post_id>/', create_comment, name ="create-comment"),
    # 다대다 좋아요 경로
    path('add-like/<int:post_id>/', add_like, name ="add-like"),
    path('remove-like/<int:post_id>/', remove_like, name ="remove-like"),
    path('my-like', mylike, name = "my-like")
]