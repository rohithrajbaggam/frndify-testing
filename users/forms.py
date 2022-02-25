from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User 
from .models import UserProfile
# from pages.models import Post
 
class CreateNewUser(UserCreationForm):
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'email'}))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'placeholder':'username'}))
    password1 = forms.CharField(
        required= True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder':'Password'})
    )
    password2 = forms.CharField(
        required= True,
        label = "",
        widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'})
    )
    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')


class EditProfile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date',}))
    class Meta:
        model = UserProfile
        exclude = ('user',)


class UserProfileChange(UserChangeForm):
    class Meta:
        model = User 
        fields = ('username', 'email', 'password')