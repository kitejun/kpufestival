from django.contrib import admin
from django.urls import path, include
import info.views
import account.views
import board.views

urlpatterns = [
    path('developer/', info.views.developer,name="developer"),
    path('siru/', info.views.siru,name="siru"),
]