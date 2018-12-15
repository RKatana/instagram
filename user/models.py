# from distutils.command.upload import upload
import datetime as dt
from builtins import classmethod

from django.db import models
from django.forms.fields import CharField, ImageField


# Create your models here.
class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='profile/')
    user_name = models.CharField(max_length=30)
    email=models.EmailField()
    bio= models.CharField(max_length=100)

    def __str__:
        return self.user_name

    @classmethod
    def search_user(cls,username):
        user=cls.objects.filter(user_name__iexact=username)
        return user

class Image(models.Model):
    image = models.ImageField(upload_to='articles/')
    image_name= models.CharField(max_length=60)
    image_caption =models.CharField(max_length=60)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    comments=models.TextField()
    user_profile =models.ForeignKey(Profile)

    # def __str__:
    #     return self.image_name
    # @classmethod
    # def save_image(self):
    #     cls.save()
    # @classmethod
    # def del_image(self):
    #     cls.delete()
    # def update_caption(self,image_caption):
    #     self.update()

  
