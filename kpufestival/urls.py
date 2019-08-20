from django.contrib import admin
from django.urls import path, include
import info.views
import account.views
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),


    # URL을 연결하기 위한 import 부분
    path('account/',include('account.urls')),
    path('',include('board.urls')),
    path('',include('info.urls')),
    
]
