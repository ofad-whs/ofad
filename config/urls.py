"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.views.static import serve

"""
 *취약점 No.5
 * admin
 수정 전:path('admin/', admin.site.urls),
"""
urlpatterns = [
    path('secretonpageofadadministrator/',admin.site.urls),
    path('noticeBoard/', include('noticeBoard.urls')),
    path('',include('main.urls',namespace= 'main')),
    path('user/',include('user.urls', namespace="user")),
    path('reviewBoard/', include('reviewBoard.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # media 경로


#오류페이지
handler404 = 'user.views.page_not_found'
handler500 = 'user.views.internal_server_error'