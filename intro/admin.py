from django.contrib import admin
from .models import Intro

# admin 디자인
class IntroAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'dename', 'introduce', 'pub_date',  'hits']

admin.site.register(Intro, IntroAdmin)
