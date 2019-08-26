from django.contrib import admin
from django.urls import path, include

import info.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', info.views.home,name="home"),

    # URL을 연결하기 위한 import 부분
    path('account/',include('account.urls')),
    path('board/',include('board.urls')),
    path('info/',include('info.urls')),
    
]