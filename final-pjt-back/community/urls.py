from django.urls import path
from . import views

urlpatterns = [
    path('',views.reviews),
    path('reviews/',views.review_create),
    path('reviews/<int:review_pk>/',views.review_detail_update_or_delete),
    
    # 댓글 목록, 생성
    path('reviews/<int:review_pk>/comments/', views.comment_create), 
    # 댓글 수정, 삭제
    path('comments/<int:comment_pk>/', views.comment_update_or_delete),
]
