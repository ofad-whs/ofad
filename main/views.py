from django.shortcuts import render
from .models import *
from user.models import *
from .forms import ProductWithUserForm
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.
"""
 * API No. 1
 * API Name : 상품 불러오기 (리스트)
 * [GET] /
"""
def index(request):
    product_list = Product.objects.order_by('-create_date')
    #할인된 가격 계산
    for product in product_list:
        #나머지 없이 출력
        product.sale_price = int(product.price * 0.65)
        #round(product.price * 0.65, 2)      ## 나머지 2번째 자리까지 출력

    context = {'product_list': product_list }
    return render(request, 'main/index.html', context)


"""
 * API No. 2
 * API Name : 상품상세정보 불러오기
 * [GET] /detail/{productId}
"""
def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    context = {'product': product}



    return render(request, 'main/detail.html', context)


"""
 * API No. 3
 * API Name : 상품구매하기
 * [GET] /{productId}
"""
@login_required(login_url = 'user:login')
def product_purchase(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = get_object_or_404(SUser, pk=request.user.id)
    if request.method == 'POST':
        count = int(request.POST.get('count',0))
        print(count)
        #구매수량이 0이상이고 1000 미만이면
        if count > 0 and count < 1000:
            if user.point >= product.price * count:
                user.point -= product.price*count
                #상품-유저 모델 생성
                product_with_user = ProductWithUser.objects.create(
                    productId=product ,
                    userId = request.user ,
                    count = count,
                    total = product.price * count,
                    date= timezone.now()
                )
                product_with_user.save()
                user.point += product.price * count//10
                user.save()
                msg = "구매 완료되었습니다"
                return redirect('main:product_purchase', product_id=product_id)
            else:
                msg = "포인트가 부족합니다"
                return render(request,'main/detail.html',{'product':product,'m':msg})
        else:
            msg = "수량은 1이상 1000 미만이여야 합니다"
            return render(request,'main/detail.html',{'product':product, 'm':msg})

    return render(request, 'main/detail.html',{'product':product})
