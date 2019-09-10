from django.contrib import admin
from .models import Board, Comment, Missing

# admin 디자인
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'title', 'context', 'pub_date',  'hits']

admin.site.register(Board, BoardAdmin)

# admin 디자인
class MissingAdmin(admin.ModelAdmin):
    list_display = ['id','author', 'context', 'pub_date',  'hits']

admin.site.register(Missing, MissingAdmin)

# admin 디자인
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'comment_body', 'comment_date', 'board']

admin.site.register(Comment, CommentAdmin)