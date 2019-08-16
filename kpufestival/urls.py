"""kpufestival URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import info.views
import account.views
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',info.views.home,name="home"),
    path('login/',account.views.login,name="login"),
    path('signup/',account.views.signup,name="signup"),
    path('board/',board.views.board,name="board"),
    path('detail/',board.views.detail,name="detail"),
    path('introduce/',board.views.introduce,name="introduce"),

]
