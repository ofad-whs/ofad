from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    fields=['name','price','description','imgfile']
    
class ProductWithUserAdmin(admin.ModelAdmin):
    fields=['productId','userId','count','total','date']
    

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductWithUser,ProductWithUserAdmin)