
from django.urls import path
import info.views

urlpatterns = [

    path('',info.views.temp,name="temp"),
    path('home/',info.views.home,name="home"),
]