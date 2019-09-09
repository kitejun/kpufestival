from django.urls import path
from . import views

urlpatterns = [
    path('', views.introduce,name="introduce"),
    path('intro_detail/<int:intro_id>/', views.intro_detail,name="intro_detail"),
    path('<int:intro_id>/intro_like/', views.intro_like, name="intro_like"),
]