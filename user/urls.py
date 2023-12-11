from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="user"
urlpatterns = [
    #login
    path('login/',views.login,name='login'),
    #회원가입
    path('register/',views.register,name='register'),
    #로그아웃
    path("logout/",auth_views.LogoutView.as_view(),name='logout'),
    #유저 정보 조회
    path("me/",views.mypage,name="mypage"),
    #유저 정보 변경
    path("me/change",views.change,name="change"),
    #마이페이지 반품
    path("me/return_product/<int:productwithuser_id>",views.return_product, name="return_product"),

]
