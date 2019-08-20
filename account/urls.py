from django.contrib import admin
from django.urls import path, include
import info.views
import account.views
import board.views

urlpatterns = [
    path('login/',account.views.login,name="login"),
    path('signup/',account.views.signup,name="signup"),
]