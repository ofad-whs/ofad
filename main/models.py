from django.db import models
from user.models import SUser
from django import forms

# Create your models here.


"""
 * MODEL Name : Product
 * MODEL col : name(상품정보), price(가격), description(설명), imgfile(이미지)
"""
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    imgfile = models.ImageField(blank=True, upload_to="products", null=True)
    create_date = models.DateTimeField(auto_now_add=True)



"""
 * MODEL Name : ProductWithUser
 * MODEL col :  count(갯수), date(날짜)
"""
class ProductWithUser(models.Model):
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    userId = models.ForeignKey(SUser, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    total = models.IntegerField(default = 0)
    date = models.DateTimeField()