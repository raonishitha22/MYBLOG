from django import forms
from .models import myblog,BlogComment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class blogform(forms.ModelForm):
    class Meta:
        model=myblog
        fields=['Title','Content','published_at']
        

class regisform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
class loginform(forms.Form):
    username=forms.CharField(max_length=65)
    password=forms.CharField(max_length=65,widget=forms.PasswordInput)
    
class commentform(forms.ModelForm):
    content=forms.CharField(widget=forms.Textarea(attrs={'rows':'4',}))
    class Meta:
        model=BlogComment
        fields=['content']    
          