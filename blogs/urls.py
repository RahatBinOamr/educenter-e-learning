from django.urls import path
from .views import views_blogs


urlpatterns =[
  path('blogs/',views_blogs, name='blogs'),
]