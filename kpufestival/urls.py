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
