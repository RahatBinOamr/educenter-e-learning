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


class Course(models.Model):
  department = models.ForeignKey(Department,on_delete=models.CASCADE)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
  title = models.CharField(max_length=500)
  banner = models.ImageField(upload_to='course')
  duration_month = models.PositiveIntegerField()
  duration_hours = models.DecimalField(max_digits=10, decimal_places=2)
  fee = models.DecimalField(max_digits=10, decimal_places=2)
  description = HTMLField()
  

  slug = AutoSlugField(populate_from='title')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __str__(self) -> str:
    return f"course title-{self.title}"
  

class Modules(models.Model):
  course = models.ForeignKey(Course,on_delete=models.CASCADE)
  title = models.CharField(max_length=500)
  content = models.URLField()

  slug = AutoSlugField(populate_from='title')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


  def get_video_embed_url(self):
        """Convert standard YouTube URL to embed URL."""
        if "youtube.com/watch?v=" in self.content:
            video_id = self.content.split("watch?v=")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in self.content:
            video_id = self.content.split("youtu.be/")[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return self.content

  def __str__(self) -> str:
    return f"module title-{self.title}"
  

class Event(models.Model):
  title = models.CharField(max_length=250)
  banner = models.ImageField(upload_to='events')
  description = HTMLField()
  location = models.CharField(max_length=500)
  date = models.DateField()
  time = models.TimeField()
  fee = models.DecimalField(max_digits=10,decimal_places=2)
  slug = AutoSlugField(populate_from='title')
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)


class Speaker(models.Model):
  event = models.ForeignKey(Event,on_delete=models.CASCADE)
  name = models.CharField(max_length=250)
  image = models.ImageField(upload_to='speaker')
  occupation = models.CharField(max_length=250)