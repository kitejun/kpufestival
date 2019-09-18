from django.contrib import admin
from django.urls import path, include
import info.views
import account.views
import board.views

'''
from django.conf.urls import url, handler404, handler500
handler404 = "info.views.error404"
handler500 = "info.views.error500"
'''

urlpatterns = [
    path('developer/', info.views.developer, name="developer"),
    path('siru/', info.views.siru, name="siru"),
    path('promote/', info.views.promote, name="promote"),
]

