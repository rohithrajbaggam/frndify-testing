from rest_framework.serializers import ModelSerializer
from pages.models import Page, Post, SavePost
from users.models import UserPost, UserProfile, Follow, UserSavePost
from django.contrib.auth.models import User 


class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = '__all__'


class UserSavedPostSerializer(ModelSerializer):
    class Meta:
        model = UserSavePost
        fields = '__all__'


class PageSerializer(ModelSerializer):
    class Meta:
        model = Page 
        fields = '__all__'


class PageSavedPostSerializer(ModelSerializer):
    class Meta:
        model = SavePost
        fields = '__all__'


class FollowSerializer(ModelSerializer):
    class Meta:
        model = Follow 
        fields = '__all__'


class PagePostSerializer(ModelSerializer):
    class Meta:
        model = Post 
        fields = '__all__'


class UserPostSerializer(ModelSerializer):
    class Meta:
        model = UserPost
        fields = '__all__'


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
