from django import forms
from basicapp.models import Userinfo
from django.contrib.auth.models import User

class Userinfo(forms.ModelForm):
    portfolio=forms.URLField(required=False)
    picture=forms.ImageField(required=False)

    class Meta():
        model=Userinfo
        exclude=['user']

class user(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
     

    class Meta():
        model=User
        fields=('username','email','password')