from django.contrib import admin
from .models import Page, Like, Post, Song


# Register your models here.
@admin.register(Page)
class pageAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'page_cat', 'date', 'user']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['page_name', 'user', 'page_cat', 'date', 'likes']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'cat', 'date']

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'duration', 'written']
