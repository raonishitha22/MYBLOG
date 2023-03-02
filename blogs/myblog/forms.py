from django import forms
from .models import myblog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blogform(forms.ModelForm):
    Content=forms.CharField(required=True,widget=forms.Textarea(attrs={"placeholder":"Enter your views on the subject","size":"200"}))
    class Meta:
        model=myblog
        fields=['ID','Title','Content','published_at']
        

class regisform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class loginform(forms.Form):
    username=forms.CharField(max_length=65)
    password=forms.CharField(max_length=65,widget=forms.PasswordInput)
          