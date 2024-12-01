from django.urls import path
from .views import views_courses,views_events,views_teachers,create,single_teacher,single_course,single_event


urlpatterns = [
    path('courses/', views_courses, name='courses'),
    path('events/', views_events, name='events'),
    path('teachers/', views_teachers, name='teachers'),
    path('teacher/<slug:slug>/', single_teacher, name='teacher'),
    path('course/<slug:slug>/', single_course, name='course'),
    path('event/<slug:slug>/', single_event, name='event'),
    path('create/', create, name='create'),
]

