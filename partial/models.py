from autoslug import AutoSlugField
from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class Notice(models.Model):
  title = models.CharField(max_length=250)
  description = HTMLField()
  slug = AutoSlugField(populate_from='title')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def __str__(self) -> str:
    return f"notice-{self.title}"