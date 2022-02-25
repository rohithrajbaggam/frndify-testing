from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (PageSerializer, PagePostSerializer, UserPostSerializer, UserProfileSerializer, UserSerializer,
                          FollowSerializer, UserSavedPostSerializer, PageSavedPostSerializer)
from pages.models import Page, Post, SavePost
from users.models import UserPost, UserProfile, Follow, UserSavePost
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [ 
        'GET /api',
        'GET /api/pages',
        'GET /api/pages/:id',
        'GET /api/pages/savedposts',
        'GET /api/pages/savedposts/:id',
        'GET /api/pages/posts',
        'GET /api/pages/posts/:id',
        'GET /api/users',
        'GET /api/users/:id',
        'GET /api/users/follow',
        'GET /api/users/follow/:id',
        'GET /api/users/posts',
        'GET /api/users/posts/:id',
        'GET /api/users/savedposts/',
        'GET /api/users/savedposts/:id',
        'GET /api/users/userprofiles/',
        'GET /api/users/userprofiles/:id', 
    ]
    return Response(routes)


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getFollow(request):
    followuser = Follow.objects.all()
    serializer = FollowSerializer(followuser, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getFollowdetail(request, pk):
    followuser = Follow.objects.get(id=pk)
    serializer = FollowSerializer(followuser, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@login_required(login_url='login')
def getpagesavedposts(request):
    pagesavedposts = SavePost.objects.filter(request.user)
    serializer = PageSavedPostSerializer(pagesavedposts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@login_required(login_url='login')
def getpagesavedpost(request, pk):
    pagesavedposts = SavePost.objects.get(id=pk)
    serializer = PageSavedPostSerializer(pagesavedposts, many=False)
    return Response(serializer.data)


@api_view(['GET'])
@login_required(login_url='login')
def getusersavedposts(request):
    usersavedposts = UserSavePost.objects.filter(user=request.user)
    serializer = UserSavedPostSerializer(usersavedposts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@login_required(login_url='login')
def getusersavedpost(request, pk):
    usersavedposts = UserSavePost.objects.get(id=pk)
    serializer = UserSavedPostSerializer(usersavedposts, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPages(request):
    pages = Page.objects.all()
    serializer = PageSerializer(pages, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPage(request, pk):
    page = Page.objects.get(id=pk)
    serializer = PageSerializer(page, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPagePosts(request):
    posts = Post.objects.all()
    serializer = PagePostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPagePost(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PagePostSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUserPosts(request):
    posts = UserPost.objects.all()
    serializer = UserPostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserPost(request, pk):
    posts = UserPost.objects.get(id=pk)
    serializer = UserPostSerializer(posts, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUserProfiles(request):
    userprofiles = UserProfile.objects.all()
    serializer = UserProfileSerializer(userprofiles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUserProfile(request, pk):
    userprofiles = UserProfile.objects.get(id=pk)
    serializer = UserProfileSerializer(userprofiles, many=False)
    return Response(serializer.data)
