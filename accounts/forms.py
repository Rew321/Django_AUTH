from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserFormCreationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'First Name',
        'class': 'form-control'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Last Name',
        'class': 'form-control'
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
    student_id = forms.CharField(widget=forms.NumberInput(attrs={
        'placeholder': 'Student ID',
        'class': 'form-control'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm password',
        'class': 'form-control'
    }))
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'student_id', 'password1', 'password2']
        
        


class CustomAuthenticationForm(AuthenticationForm):        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control'
    }))
     
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control'
    }))