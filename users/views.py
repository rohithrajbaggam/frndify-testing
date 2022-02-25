from django.shortcuts import redirect, render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CreateNewUser, EditProfile, UserProfileChange
from .models import UserProfile, Follow, UserPost, UserSavePost
from pages.models import Page, Post, SavePost
from django.contrib.auth.forms import  PasswordChangeForm
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView 
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def register(request):
    form = CreateNewUser()
    registered = True 
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = False
            user_profile = UserProfile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login'))
    context = {
        'form' : form,
    }
    return render(request, 'users/register.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            form = EditProfile(instance=current_user)
            return redirect('myprofile')
    return render(request, 'users/profile.html', context={'title':'edit-profile', 'form':form})


@login_required(login_url='login')
def myprofile(request):
    pages = Page.objects.filter(posted_user=request.user)
    posts = Post.objects.filter(post_author=request.user)
    save_post = SavePost.objects.filter(user=request.user)
    save_post_list = save_post.values_list('post', flat=True)
    user_save_post = UserSavePost.objects.filter(user=request.user) 
    user_save_post_list = user_save_post.values_list('post', flat=True)
    userposts = UserPost.objects.filter(posted_user=request.user)
    userprofile = UserProfile.objects.get(user=request.user)
   
    context= {
        'pages' : pages,
        'posts' : posts,
        'save_post' : save_post,
        'save_post_list' : save_post_list,
        'user_save_post' : user_save_post,
        'user_save_post_list' : user_save_post_list,
        'userposts' : userposts,
        'data' : userprofile,
        }
    
    return render(request, 'users/myprofile.html', context)


def user_other(request, username):
    user_other = User.objects.get(username=username)
    pages = Page.objects.filter(posted_user=user_other)
    posts = Post.objects.filter(post_author=user_other)
    userposts = UserPost.objects.filter(posted_user=user_other)

    save_post = SavePost.objects.filter(user=request.user)
    save_post_list = save_post.values_list('post', flat=True)
    user_save_post = UserSavePost.objects.filter(user=request.user) 
    user_save_post_list = user_save_post.values_list('post', flat=True)

    if request.user.is_authenticated:
        already_followed = Follow.objects.filter(follower=request.user, following=user_other)
        pages = Page.objects.filter(posted_user=user_other)
        posts = Post.objects.filter(post_author=user_other)
        userposts = UserPost.objects.filter(posted_user=user_other)
        if request.user.username == username:
            return redirect('myprofile')
        context = { 
        'user_other' : user_other,
        'pages' : pages,
        'posts' : posts,
        'already_followed' : already_followed,
        'userposts' : userposts,
        'save_post' : save_post,
        'save_post_list' : save_post_list,
        'user_save_post' : user_save_post,
        'user_save_post_list' : user_save_post_list,}
    else:
        context = { 
            'user_other' : user_other,
            'pages' : pages,
            'posts' : posts,
        }
    return render(request, 'users/user_other.html', context)



@login_required(login_url='login')
def user_profile_change(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
            return redirect('myprofile')
    return render(request, 'users/user_profile_change.html', context={'form': form,})



@login_required(login_url='login')
def pass_change(request):
    current_user = request.user
    changed = False
    form = PasswordChangeForm(current_user)
    if request.method == 'POST':
        form = PasswordChangeForm(current_user, data=request.POST)
        if form.is_valid():
            form.save() 
            changed = True 
            return redirect('myprofile')
    return render(request, 'users/pass_change.html', {'form': form, 'changed': changed})


@login_required(login_url='login')
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        follower_user = Follow(follower=follower_user, following=following_user)
        follower_user.save()
    return HttpResponseRedirect(reverse('user-other', kwargs={'username':username}))


@login_required(login_url='login')
def unfollow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_following = Follow.objects.filter(follower=follower_user, following=following_user)
    already_following.delete()
    return HttpResponseRedirect(reverse('user-other', kwargs={'username':username}))

# user post views 

class UserPostListView(ListView):
    model = UserPost 
    context_object_name = 'userposts'
    ordering = ['-updated']



def userpostlistview(request):
    userposts = UserPost.objects.all()
    if request.user.is_authenticated:
        user_save_post = UserSavePost.objects.filter(user=request.user) 
        user_save_post_list = user_save_post.values_list('post', flat=True)
        context = {
            'userposts' : userposts,
            'user_save_post' : user_save_post,
            'user_save_post_list' : user_save_post_list,
        }
    else:
        context = {
            'userposts' : userposts,
        }
    return render(request, 'users/post/post_list.html', context)


# class UserPostDetailView(DetailView):
#     model = UserPost 

def userpostdetailview(request, pk):
    posts = UserPost.objects.get(id=pk)
    if request.user.is_authenticated:
        user_save_post = UserSavePost.objects.filter(user=request.user) 
        user_save_post_list = user_save_post.values_list('post', flat=True)
        context = {
            'object' : posts,
            'user_save_post' : user_save_post,
            'user_save_post_list' : user_save_post_list,   
        }
    else:
            context = {
            'object' : posts,
            
        }
    return render(request, 'users/post/post_detail.html', context)


class UserPostCreateView(LoginRequiredMixin, CreateView):
    model = UserPost 
    fields = ['title', 'img', 'content']

    def form_valid(self, form):
        form.instance.posted_user = self.request.user 
        return super().form_valid(form)



class UserPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserPost 
    fields = ['title', 'img', 'content']

    def form_valid(self, form):
        form.instance.posted_user = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        page = self.get_object() 
        if self.request.user == page.posted_user:
            return True 
        return False 



class UserPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = UserPost 
    success_url = '/'
    def test_func(self):
        page = self.get_object() 
        if self.request.user == page.posted_user:
            return True 
        return False 


@login_required(login_url='login')
def user_save_post(request, pk):
    post = UserPost.objects.get(pk=pk)
    already_saved = UserSavePost.objects.filter(post=post, user=request.user)
    if not already_saved:
        savepost = UserSavePost(post=post, user=request.user)
        savepost.save()
    return redirect('user-post-detail', pk=post.id)


@login_required(login_url='login')
def user_unsave_post(request, pk):
    post = UserPost.objects.get(pk=pk)
    already_saved = UserSavePost.objects.filter(post=post, user=request.user)
    already_saved.delete()
    return redirect('user-post-detail', pk=post.id)



@login_required(login_url='login')
def usersavedPostList(request):
    save_posts = UserSavePost.objects.filter(user=request.user)
    save_post_list = save_posts.values_list('post', flat=True)
    context = { 
        'user_save_posts' : save_posts,
        'user_save_post_list' : save_post_list, 
    }
    return render(request, 'users/post/usersavedposts.html', context)