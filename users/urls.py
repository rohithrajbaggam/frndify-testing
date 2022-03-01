from django.contrib.auth import views as auth_views
from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views
from .views import UserPostCreateView, UserPostUpdateView, UserPostDeleteView
urlpatterns = [ 
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_user ,name='logout'),
    path('password-reset/', 
    auth_views.PasswordResetView.as_view(
        template_name='users/forgot_password/password_reset.html'), 
    name='password_reset'), 

    path('password-reset/done/', 
    auth_views.PasswordResetDoneView.as_view(
        template_name='users/forgot_password/password_reset_done.html'), 
    name='password_reset_done'), 

    path('password-reset-confirm/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(
        template_name='users/forgot_password/password_reset_confirm.html'), 
    name='password_reset_confirm'), 

    path('password-reset-complete/', 
    auth_views.PasswordResetCompleteView.as_view(
        template_name='users/forgot_password/password_reset_complete.html'), 
    name='password_reset_complete'), 

    path('myprofile/', views.myprofile, name='myprofile'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('profile/<username>/', views.user_other, name='user-other'),
    path('user_profile_change/', views.user_profile_change, name='user_profile_change'),
    path('password/', views.pass_change, name='pass_change'), 

    # path('user/posts/', UserPostListView.as_view(template_name='users/post/post_list.html'), name='user-post-list'),
    path('user/posts/', views.userpostlistview, name='user-post-list'),
    # path("user/post/<int:pk>/", UserPostDetailView.as_view(template_name='users/post/post_detail.html'), name='user-post-detail'),
    path("user/post/<int:pk>/", views.userpostdetailview, name='user-post-detail'),
    path('user/post/new', UserPostCreateView.as_view(template_name='users/post/post_form.html'), name='user-post-create'),
    path("user/post/<int:pk>/update/", UserPostUpdateView.as_view(template_name='users/post/post_form.html'), name='user-post-update'),
    path("user/post/<int:pk>/delete/", UserPostDeleteView.as_view(template_name='users/post/post_confirm_delete.html'), name='user-post-delete'),

    path('follow/<username>/', views.follow, name='follow'),
    path('unfollow/<username>/', views.unfollow, name='unfollow'),

    path('user/saved-posts/', views.usersavedPostList, name='user-saved-posts'),
    path('user/Save/<pk>/', views.user_save_post, name='user-save' ),
    path('user/Unsave/<pk>/', views.user_unsave_post, name='user-unsave'),

]