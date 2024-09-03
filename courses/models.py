from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
# Create your models here.
class Department(models.Model):
  name = models.CharField(max_length=250)
  image = models.ImageField(upload_to='department')
  description =  HTMLField()

  slug = AutoSlugField(populate_from='name')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  def __str__(self) -> str:
    return f"department-{self.name}"


class Interested(models.Model):
  name = models.CharField(max_length=250)
  teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE)
  def __str__(self) -> str:
    return f"interested-{self.name}"
  

class Teacher(models.Model):
  name = models.CharField(max_length=250)
  image = models.ImageField(upload_to='teacher')
  biography =  HTMLField()

  phone = models.PositiveIntegerField()
  email = models.EmailField(max_length=30)
  website = models.URLField(blank=True, null=True)
  facebook = models.URLField(blank=True, null=True)
  twitter = models.URLField(blank=True, null=True)
  stripe = models.URLField(blank=True, null=True)

  city = models.CharField(max_length=250)
  country = models.CharField(max_length=500)
  postal_code = models.CharField(max_length=250)
  present_address = models.CharField(max_length=250)

  department = models.ForeignKey(Department,on_delete=models.CASCADE)
  slug = AutoSlugField(populate_from='name')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  def __str__(self) -> str:
    return f"Teacher-{self.name}"


