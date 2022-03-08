from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Page(models.Model):
    posted_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pages')
    page_profile = models.ImageField(upload_to='page_profile', default='group.png')
    page_title = models.CharField(max_length=100, unique=True)
    about = models.TextField(max_length=500)
    field = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    your_role = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    # social media 
    whatsapp = models.CharField(max_length=10, blank=True)
    linkdin_profile_link = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page_title} Created by {self.posted_user}"

    class Meta:
        ordering = ['-updated', '-created']

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={'pk': self.pk})


class Post(models.Model):
    post_page = models.ForeignKey(Page, on_delete=models.CASCADE)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='page_posts')
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='page_post_images', blank=True)
    content = models.TextField(blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f'{self.title} by {self.post_author}'

    class Meta:
        ordering = ['-updated', '-created']


class SavePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='save_Post')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_user')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} Save {self.post} '

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.pk, self.id])





