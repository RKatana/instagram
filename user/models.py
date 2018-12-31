# from distutils.command.upload import upload
import datetime as dt
from builtins import classmethod
from django.contrib.auth.models import User

from django.db import models
from django.forms.fields import CharField, ImageField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    profile_photo=models.ImageField(upload_to='images/')
    email=models.EmailField()
    bio= models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

    @classmethod
    def search_user(cls,username):
        user=cls.objects.filter(user__username__icontains=username)
        return user
    
    def save_profile(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    image_name= models.CharField(max_length=60)
    image_caption =models.CharField(max_length=60)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    comments=models.TextField()
    user_profile =models.ForeignKey(User)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    
    def update_caption(self,image_caption):
        self.update()

  
