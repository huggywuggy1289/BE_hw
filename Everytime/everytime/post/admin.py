from django.contrib import admin

from .models import Category, Post, Comment, PostCategory, Like

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Like)
admin.site.register(Comment)

