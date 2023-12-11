from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as ul

from .forms import RegisterForm, SUserChangeForm
from .models import SUser

class UserAdmin(BaseUserAdmin):
    form = SUserChangeForm
    add_form = RegisterForm
    
    list_display= ('email','nickname', 'is_active','is_admin','point','is_authenticated','id')
    list_display_links = ('nickname',)
    list_filter = ('is_admin','is_active')
    fieldsets = (
        (None, {'fields':('email','password',)}),
        (ul('Personal info'),{'fields':('nickname','point',)}),
        (ul('Permissions'),{'fields':('is_active','is_admin',)}),
    )
    add_fieldsets= (
        (None, {
            'classes':('wide',),
            'fields':('email','nickname','point')
        }),
    )
    search_fields = ('email','nickname')
    ordering = ('point',)
    filter_horizontal=()
    

admin.site.register(SUser,UserAdmin)
    
