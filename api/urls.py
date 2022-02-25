from django.urls import path
from . import views

urlpatterns = [
    path('',  views.getRoutes),
    path('pages/', views.getPages),
    path('pages/<int:pk>/', views.getPage),
    path('pages/posts/', views.getPagePosts),
    path('pages/posts/<int:pk>/', views.getPagePost),
    path('pages/savedposts/', views.getpagesavedposts),
    path('pages/savedposts/<int:pk>/', views.getpagesavedpost),
    path('users/', views.getUsers),
    path('users/<int:pk>/', views.getUser),
    path('users/follow/', views.getFollow),
    path('users/follow/<int:pk>/', views.getFollowdetail),
    path('users/savedposts/', views.getusersavedposts),
    path('users/savedposts/<int:pk>/', views.getusersavedpost),
    path('users/posts/', views.getUserPosts),
    path('users/posts/<int:pk>/', views.getUserPost),
    path('users/userprofiles/', views.getUserProfiles),
    path('users/userprofiles/<int:pk>/', views.getUserProfile),
]
