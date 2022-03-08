from django.contrib import admin
from .models import UserProfile, Follow, UserPost, UserSavePost, Messages
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(UserPost)
admin.site.register(UserSavePost)
admin.site.register(Messages)

