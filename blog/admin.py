from django.contrib import admin

# Register your models here.

from .models import Category, Tag, Post, Comment
from django.contrib import admin
from django.contrib.auth.models import User

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["id","title","text_min", "text","created", "timestamp"]
    list_display_links = ["id", "created"]
    list_editable = ["title"]
    list_filter = ["created", "timestamp"]
    search_fields = ["title", "text", "category"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
