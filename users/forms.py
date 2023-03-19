from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class loginform(forms.Form):
    username=forms.CharField(max_length=65)
    password=forms.CharField(max_length=65,widget=forms.PasswordInput)

class regisform(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model=User
        fields = ['username','email','password1','password2']           