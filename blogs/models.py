from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=250)
  slug = AutoSlugField(populate_from='name')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return f"Category-{self.name}"

class Blog(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ForeignKey(Category,on_delete=models.CASCADE)
  image = models.ImageField(upload_to='blogs')
  title = models.CharField(max_length=250)
  description = HTMLField()

  slug = AutoSlugField(populate_from='title')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return f"blog-{self.title}"

class Comment(models.Model):
  blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
  name = models.CharField(max_length=250)
  email = models.EmailField(max_length=250)
  message = models.TextField()

  slug = AutoSlugField(populate_from='name')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return f"message: {self.message}"