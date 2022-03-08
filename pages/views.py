from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Page, Post, SavePost
from .forms import CreatePostForm
from users.models import UserPost, Follow, UserSavePost, UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.decorators import login_required
from itertools import chain
# Create your views here.

def all_posts(request):
    pages_posts = Post.objects.all()
    users_posts = UserPost.objects.all()
    posts = [] 
    posts += pages_posts
    posts += users_posts
    post_list = sorted(chain(pages_posts, users_posts), key=lambda post : post.created, reverse=True)
    context = {
        'pages_posts' : pages_posts,
        'users_posts' : users_posts,
        'posts' : posts,
        'post_list' : post_list,
    }

        # cars_list = sorted(
        # chain(bmws, teslas),
        # key=lambda car: car.created, reverse=True)    
    return render(request, 'all_posts.html', context)

def home(request):
    pages = Page.objects.all()
    posts = Post.objects.all()
    if request.user.is_authenticated:
        following_list = Follow.objects.filter(follower=request.user)
        userposts = UserPost.objects.filter(posted_user__in=following_list.values_list('following'))
        save_post = SavePost.objects.filter(user=request.user)
        save_post_list = save_post.values_list('post', flat=True)
        user_save_post = UserSavePost.objects.filter(user=request.user)
        user_save_post_list = user_save_post.values_list('post', flat=True)
        context = {
        'pages' : pages,
        'posts' : posts,
        'save_post' : save_post,
        'save_post_list' : save_post_list, 
        'userposts' : userposts,
        'save_post_list' : save_post_list,
        'user_save_post_list' : user_save_post_list,
        }
        return render(request, 'pages/home.html', context)    


    else:
        context = {
            'pages' : pages,
            'posts' : posts,

        }

    return render(request, 'pages/home.html', context)


def search(request):
    keyword = ''
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        pages = Page.objects.filter(Q(page_title__icontains=keyword)|Q(field__icontains=keyword)|Q(about__icontains=keyword)|Q(description__icontains=keyword)|
                                Q(your_role__icontains=keyword)|Q(website__icontains=keyword)|Q(whatsapp__icontains=keyword)|Q(linkdin_profile_link__icontains=keyword)|
                                Q(facebook__icontains=keyword)|Q(instagram__icontains=keyword)|Q(email__icontains=keyword))
        posts = Post.objects.filter(Q(title__icontains=keyword)|Q(content__icontains=keyword))
        userposts = UserPost.objects.filter(Q(content__icontains=keyword))
        user_profile = UserProfile.objects.filter(Q(profile_pic__icontains=keyword)|Q(dob__icontains=keyword)|Q(full_name__icontains=keyword)|Q(full_name__icontains=keyword)|Q(Section__icontains=keyword)|
                            Q(Branch__icontains=keyword)|Q(year_joined__icontains=keyword)|Q(Hosteler_or_DayScholar__icontains=keyword)|Q(Hostel_Room_No__icontains=keyword)|Q(bio__icontains=keyword)|
                            Q(Native_Language__icontains=keyword)|Q(Languages_Known__icontains=keyword)|Q(Address__icontains=keyword)|Q(State__icontains=keyword)|Q(foreigners_can_enter_their_states_here__icontains=keyword)|
                            Q(Country__icontains=keyword)|Q(whatsapp__icontains=keyword)|Q(instagram_username__icontains=keyword)|Q(facebook__icontains=keyword)|Q(linkdin_profile_link__icontains=keyword)|Q(gmail__icontains=keyword))
    context = {
        'keyword' : keyword, 
        'pages' : pages,
        'posts' : posts,
        'userposts' : userposts,
        'user_profile_data' : user_profile,
    }
    return render(request, 'pages/lists/search.html', context)


class PageListView(ListView):
    model = Page 
    context_object_name = 'pages'
    ordering = ['-updated']

class PageDetailView(DetailView):
    model = Page 


# def pagedetailview(request, pk):
#     pages = Page.objects.get(id=pk)
#     context = {
#         'pages' : pages,
#     }
#     return render(request, 'lists/page_detail.html', pages)



class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page 
    fields = ['page_profile', 'page_title',
       'field','about', 'description', 'your_role', 'website', 
       'whatsapp', 'linkdin_profile_link', 'facebook',
      'instagram', 'email']

    def form_valid(self, form):
        form.instance.posted_user = self.request.user 
        return super().form_valid(form)



class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page 
    fields = ['page_profile', 'page_title',
       'field','about', 'description', 'your_role', 'website', 
       'whatsapp', 'linkdin_profile_link', 'facebook',
      'instagram', 'email']

    def form_valid(self, form):
        form.instance.posted_user = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        page = self.get_object() 
        if self.request.user == page.posted_user:
            return True 
        return False 


 
class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page 
    success_url = '/'
    def test_func(self):
        page = self.get_object() 
        if self.request.user == page.posted_user:
            return True 
        return False 


def page_profile(request, pk, page_title):
    page_data = Page.objects.get(id=pk)
    page_posts = Post.objects.filter(post_page=page_data)
    if request.user.is_authenticated:
        save_post = SavePost.objects.filter(user=request.user)
        save_post_list = save_post.values_list('post', flat=True)
        context = { 
            'pk' : pk,
            'page_title' : page_title,
            'page' : page_data,
            'posts' : page_posts,
            'save_post' :save_post,
            'save_post_list' : save_post_list,
        }
    else:
        context = { 
            'pk' : pk,
            'page_title' : page_title,
            'page' : page_data,
            'posts' : page_posts,
        }

    return render(request, 'pages/lists/page_profile.html', context)



@login_required(login_url='login')
def PostCreateView(request, pk): 
    form = CreatePostForm()
    page_rel = Page.objects.get(id=pk)
    if request.user != page_rel.posted_user:
        return HttpResponse('<h1>Your are allowed to create Post,Only admin can post..!<h1/>')
    else:
        if request.method == 'POST':
            form = CreatePostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.post_author = request.user
                post.post_page = page_rel
                post.save()
                return redirect('home') 
        
    context = {
        'form':form,
    }
    return render(request, 'pages/post_form.html', context)


class PostListView(ListView):
    model = Post 
    context_object_name = 'posts'
    ordering = ['-updated']

def postlistview(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        save_post = SavePost.objects.filter(user=request.user)
        save_post_list = save_post.values_list('post', flat=True)
        context = {
            'posts' : posts,
            'save_post' :save_post,
            'save_post_list' : save_post_list,
        }
    else:
        context = {
            'posts' : posts,
        }
    return render(request, 'pages/post_list.html', context)



# class PostDetailView(DetailView):
#     model = Post


def postdetailview(request, pk):
    posts = Post.objects.get(id=pk)
    if request.user.is_authenticated:
        save_post = SavePost.objects.filter(user=request.user)
        save_post_list = save_post.values_list('post', flat=True)
        context = {
            'object' : posts,
            'save_post' :save_post,
            'save_post_list' : save_post_list,
        } 
    else:
        context = {
        'object' : posts, 
        }
    return render(request, 'pages/post_detail.html', context)


@login_required(login_url='login')
def PostUpdateView(request, pk):
    # current_user = UserProfile.objects.get(user=request.user)
    current_user = Post.objects.get(id=pk)
    form = CreatePostForm(instance=current_user)
    if request.user != current_user.post_author:
        return HttpResponse('<h1>Your are allowed to Update Post,Only admin can Update post..!<h1/>')
    else:
        if request.method == 'POST':
            form = CreatePostForm(request.POST, request.FILES, instance=current_user)
            if form.is_valid():
                form.save(commit=True)
                form = CreatePostForm(instance=current_user)
                return redirect('home')
    return render(request, 'pages/post_form.html', context={'form':form})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'
    def test_func(self):
        post = self.get_object() 
        if self.request.user == post.post_author:
            return True 
        return False


@login_required(login_url='login')
def save_post(request, pk):
    post = Post.objects.get(pk=pk)
    already_saved = SavePost.objects.filter(post=post, user=request.user)
    if not already_saved:
        savepost = SavePost(post=post, user=request.user)
        savepost.save()
    return redirect('post-detail', pk=post.id)
    # return redirect('room', pk=room.id)

    # return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


@login_required(login_url='login')
def unsave_post(request, pk):
    post = Post.objects.get(pk=pk)
    already_saved = SavePost.objects.filter(post=post, user=request.user)
    already_saved.delete()
    return redirect('post-detail', pk=post.id) 



@login_required(login_url='login')
def savedPostList(request):
    save_posts = SavePost.objects.filter(user=request.user)
    save_post_list = save_posts.values_list('post', flat=True)
    context = { 
        'save_posts' : save_posts,
        'save_post_list' : save_post_list,
    }
    return render(request, 'pages/lists/savedposts.html', context)


def userprofilelist(request):
    user_profile_data = UserProfile.objects.all()
    context = {
        'user_profile_data' : user_profile_data,
    }
    return render(request, 'pages/lists/userprofilelist.html', context)


def userprofiledatadetail(request, pk):
    user_profile_data = UserProfile.objects.get(id=pk)
    context = {
        'data' : user_profile_data,
    }
    return render(request, 'pages/lists/userprofiledetail.html', context)


def about(request):
    return render(request, 'about.html')


def help(request):
    return render(request, 'help.html')


def mobnav(request):
    return render(request, 'mobnav.html')


def mobsug(request):
    return render(request, 'mobsug.html')


def apilistview(request):
    return render(request, 'apilist.html')


# @login_required(login_url='login')
# def edit_profile(request):
#     current_user = UserProfile.objects.get(user=request.user)
#     form = EditProfile(instance=current_user)
#     if request.method == 'POST':
#         form = EditProfile(request.POST, request.FILES, instance=current_user)
#         if form.is_valid():
#             form.save(commit=True)
#             form = EditProfile(instance=current_user)
#             return redirect('home')
#     return render(request, 'users/profile.html', context={'title':'edit-profile', 'form':form})



