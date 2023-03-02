from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class loginform(forms.Form):
    username=forms.CharField(max_length=65)
    password=forms.CharField(max_length=65,widget=forms.PasswordInput)

class regisform(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']           