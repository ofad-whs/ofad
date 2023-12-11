from django.shortcuts import render,redirect
from django.contrib.auth import login as l
from .forms import SUserChangeForm,RegisterForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .models import *
from main.models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.sessions.models import Session

"""
    * API Name : 회원가입
    *[GET] /user/register -> 회원가입 페이지 render
    *[POST] /user/register  -> 회원가입 제출시
"""

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'user/register.html',{"form":form})

"""
    *API Name : 로그인
    *[GET] /user/login ->로그인 페이지 렌더링
    *[POST] /user/login -> 로그인 검증
"""
    
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            l(request, form.get_user())

            ##셰션에 사용자 정보 추가
            '''
            session = Session.objects.get(session_key=request.session.session_key)
            user = SUser.objects.get(id=request.user.id)
            CustomSession.objects.create(session=session, user=user)
            '''


            return redirect('/')
        else:
            print('error')
    else :
        print('als')
        form = AuthenticationForm()
    return render(request, 'user/login.html',{'form':form})


"""
    *API Name: 유저정보조회 
    *[GET] /user/{user_id} ->유저 정보를 제공하는 페이지 렌더링 
    Login 했을 시에만
"""

@login_required(login_url = 'user:login')#로그인 확인
def mypage(request):

    p = ProductWithUser.objects.filter(userId=request.user.id)

    for pr in p:
        pr.total_price = pr.productId.price * pr.count
    
    return render(request,'user/mypage.html',{'p':p})


"""
    *API Name: 유저 정보 수정
    *[GET] /user/me/change 
"""

@login_required(login_url = 'user:login')
def change(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/user/{request.user.id}')
    else:
        suser = SUser.objects.get(id=request.user.id)

        form = PasswordChangeForm(request.user, request.POST)
    return render(request, "user/change.html", context={"form": form})


"""
    *API Name: 상품 반품하기
    *[POST] /user/me/return_product/{productwithuser_id} 
    Login 했을 시에만
"""
@login_required(login_url = 'user:login')
def return_product(request, productwithuser_id):
    if request.method == "POST":
        print(productwithuser_id)
        product_with_user = get_object_or_404(ProductWithUser, id=productwithuser_id)
        request.user.point += product_with_user.total //2
        request.user.save()
        product_with_user.delete()
    return redirect('user:mypage')


"""
    오류 페이지
"""
def page_not_found(request, exception):
    return render(request, 'errors/404.html', {})

def internal_server_error(request):
    return render(request, 'errors/500.html', {})