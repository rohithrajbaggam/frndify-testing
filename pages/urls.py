from unicodedata import name
from django.urls import path 
from . import views 
from .views import (PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView,
                     PostDeleteView ) 
urlpatterns = [ 
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('apilist/', views.apilistview, name='api-list'),
    path('help/', views.help, name='help'),
    path('search/', views.search, name='search'),
    path('userprofiledata', views.userprofilelist, name='user-profile-list'),
    path('userprofiledata/<int:pk>/', views.userprofiledatadetail, name='user-profile-detail'),
    # page urls

    path('pages/', PageListView.as_view(), name='page-list'),
    path("page/<int:pk>/", PageDetailView.as_view(), name='page-detail'),
    path('page/new', PageCreateView.as_view(), name='page-create'),
    path("page/<int:pk>/update/", PageUpdateView.as_view(), name='page-update'),
    path("page/<int:pk>/delete/", PageDeleteView.as_view(), name='page-delete'),
    path("page/profile/<int:pk>/<page_title>/", views.page_profile, name='page-profile'),
    # page post utls
    path("page/<int:pk>/create-post/", views.PostCreateView, name='post-create'),
    path("page/posts/", views.postlistview, name='post-list'),
    path("page/post/<int:pk>/", views.postdetailview, name='post-detail'),
    path("page/post/<int:pk>/update/", views.PostUpdateView, name='post-update'),
    path("page/post/<int:pk>/delete/", PostDeleteView.as_view(), name='post-delete'),
    # save and unsave
    path('page/saved-posts/', views.savedPostList, name='saved-posts'),
    path('Save/<pk>/', views.save_post, name='save' ),
    path('Unsave/<pk>/', views.unsave_post, name='unsave'), 
    path('navbar/', views.mobnav, name='mobnav'),
    path('suggestions/', views.mobsug, name='mobsug'),

]