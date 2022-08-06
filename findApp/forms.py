import email
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.db import transaction
from django import forms 

from .models import CustomUser, IdeaOwner

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)
        
class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = CustomUser
        fields = ('email',)
        
        
class InvestorSignUpForm(CustomUserCreationForm):
    class Meta: 
        model = get_user_model()
        fields = ('email', 'password')      
        
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_investor = True
        if commit:
            user.save()
        return user

class IdeaOwnerSignUpForm(CustomUserCreationForm):
    """user signup form"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_idea_owner = True
        user.save()
        return user
    
class CompanySignUpForm(CustomUserCreationForm):
    """user signup form"""
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ('email', 'password',)
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_company = True
        user.save()
        return user
        
class LoginForm(forms.Form):
    """User login form

    Args:
        forms (objectt]): An instance of django form
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())