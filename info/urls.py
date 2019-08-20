from django.contrib import admin
from django.urls import path, include
import info.views
import account.views
import board.views

urlpatterns = [

    path('', info.views.home,name="home"),
    path('developer/', info.views.developer,name="developer")
]