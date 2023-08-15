from django.contrib import admin
from accounts.models import CustomUser
from posts.models import Category, Post

# Register your models here.

@admin.register(CustomUser)
class CategoryUser(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Post)
class CategoryPost(admin.ModelAdmin):
    ...
