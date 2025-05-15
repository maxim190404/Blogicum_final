from django import forms
from django.contrib.auth import get_user_model
from .models import Post, Comment
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email')
        model = User


class UserProfileForm(forms.ModelForm):
    class Meta:
        fields = ('username', 'email', 'first_name', 'last_name')
        model = User


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)
        widgets = {
            'pub_date': forms.DateInput(attrs={'type': 'datetime-local'})
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
