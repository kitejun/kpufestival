from django.contrib import admin
from django.urls import path
import info.views

urlpatterns = [
    path('/temp',info.views.home,name="temp"),
]
