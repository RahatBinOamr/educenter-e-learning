from django.urls import path
from .views import views_courses,views_events


urlpatterns =[
  path('courses/',views_courses,name='courses'),
  path('events/',views_events,name='events'),
]

