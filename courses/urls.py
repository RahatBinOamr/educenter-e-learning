from django.urls import path
from .views import views_courses,views_events,views_teachers


urlpatterns =[
  path('courses/',views_courses,name='courses'),
  path('events/',views_events,name='events'),
  path('teachers/',views_teachers,name='teachers')
]

