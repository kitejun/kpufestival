from django.urls import path
from . import views

urlpatterns = [
    path('', views.board,name="board"),
    path('board_detail/<int:board_id>/', views.board_detail,name="board_detail"),
    path('new/', views.new,name="new"),
    path('introduce/', views.introduce,name="introduce"),
    path('intro_detail/', views.intro_detail,name="intro_detail"),

]