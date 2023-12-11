from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Review, ReviewAdmin)