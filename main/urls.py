from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='main'

urlpatterns = [
 ## 메인 페이지 (상품 리스트 표시)
    path('',views.index, name='index'),
    ## 상품 조회
    path('detail/<int:product_id>', views.detail, name='detail'),
    ## 상품 구매
    path('product/purchase/<int:product_id>', views.product_purchase, name='product_purchase'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) ## 미디어 파일의 URL 및 파일 경로를 지정