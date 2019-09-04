from django.urls import path
from . import views

urlpatterns = [
    path('', views.board,name="board"),
    path('board_detail/<int:board_id>/', views.board_detail,name="board_detail"),
    path('new/', views.new,name="new"),
    path('<int:board_id>/like/', views.like, name="like"),
    path('<int:board_id>/hate/', views.hate, name="hate"),

    path('detail/<int:board_id>/comment_write', views.comment_write, name="comment_write"),
    path('detail/<int:comment_id>/comment_delete', views.comment_delete, name="comment_delete"),
    path('<int:comment_id>/comment_like/', views.comment_like, name="comment_like"),
    path('<int:comment_id>/comment_hate/', views.comment_hate, name="comment_hate"),


    path('introduce/', views.introduce,name="introduce"),
    path('intro_detail/', views.intro_detail,name="intro_detail"),
]