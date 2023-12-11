from django import forms
from main.models import Product, ProductWithUser

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        ## Product 모델 속성
        fields = ['name', 'price', 'description', 'imgfile']
        labels = {
            'name': '제목',
            'price': '내용',
            'description' : '설명',
            'imgfile': '이미지',
        } 


class ProductWithUserForm(forms.ModelForm):
    class Meta:
        model = ProductWithUser
        ## ProductWithUser 모델 속성
        fields = ['productId', 'userId', 'count']
        labels = {
            'productId': '제품 ID',
            'userId' : '사용자 ID',
            'count' : '개수',
        }