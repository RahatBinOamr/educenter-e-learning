from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  bio = models.TextField(blank=True,null=True)
  avatar = models.ImageField(upload_to='avatars',default='avatar.png')
  phone = models.CharField(max_length=11,null=True,blank=True)
  present_address = models.CharField(max_length=200,null=True,blank=True)
  city = models.CharField(max_length=250,null=True,blank=True)
  post_code = models.CharField(max_length=22,null=True,blank=True)
  country = models.CharField(max_length=250,null=True,blank=True)
  house_number = models.CharField(max_length=250,null=True,blank=True)
  previous_institution_name = models.CharField(max_length=250,null=True,blank=True)
  previous_result = models.CharField(max_length=250,null=True,blank=True)
  graduation_level = models.CharField(max_length=250,null=True,blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"profile of the user with {self.user.username}"