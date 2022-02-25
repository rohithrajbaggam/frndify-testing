from django.contrib import admin
from .models import Page, Post, SavePost
# Register your models here.

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(SavePost)
