from .models import  Profile,Image
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ImageUploadForm(forms.ModelForm):
     class Meta:
         model=Image
         exclude = ['comments','user_profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude= ['user']