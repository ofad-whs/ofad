from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
app_name = 'reviewBoard'

urlpatterns = [
    ## 리뷰 불러오기
    path('', views.index, name='index'),
    ## 리뷰 조회
    path('<int:review_id>/', views.detail, name='detail'),
    ## 댓글 작성
    path('comment/create/<int:review_id>/', views.comment_create, name='comment_create'),
    ## 리뷰 작성
    path('review/create/', views.review_create, name='review_create'),
    ## 리뷰 삭제
    path('review/delete/<int:review_id>/', views.review_delete, name='review_delete'),
    ## 댓글 삭제
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) ## 미디어 파일의 URL 및 파일 경로를 지정
 ## 미디어 파일의 URL 및 파일 경로를 지정