from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduce,name="introduce"),
    path('intro_detail/', views.intro_detail,name="intro_detail"),
]