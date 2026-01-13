from django import forms
from .models import Issue
from .models import UserProfile
from django.contrib.auth.models import User



class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['category', 'description', 'image', 'location']

class ProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

