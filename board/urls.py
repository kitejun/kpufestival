from django.contrib import admin
from django.urls import path, include
import info.views
import account.views
import board.views

urlpatterns = [
    path('board/', board.views.board,name="board"),
    path('boarddetail/', board.views.boarddetail,name="boarddetail"),
    path('boardnew/', board.views.boardnew,name="boardnew"),
    path('introduce/', board.views.introduce,name="introduce"),
    path('introdetail/', board.views.introdetail,name="introdetail"),

]