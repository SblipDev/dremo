from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='')
    email = forms.EmailField(max_length=254, help_text='')
    username = forms.CharField(max_length=30, help_text='')
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    
    class Meta:
        labels = {
            'first_name':'Name'
        }
        model = User
        fields = ('username', 'first_name', 'email', 'password1', 'password2')