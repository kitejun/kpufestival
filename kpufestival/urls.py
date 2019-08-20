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
    path('boarddetail/',board.views.boarddetail,name="boarddetail"),
    path('boardnew/',board.views.boardnew,name="boardnew"),
    path('introduce/',board.views.introduce,name="introduce"),
    path('introdetail/',board.views.introdetail,name="introdetail"),
    path('developer/',info.views.developer,name="developer"),
]