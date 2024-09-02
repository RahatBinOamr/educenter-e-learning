from django.urls import path
from .views import view_notices,view_research,view_scholarship


urlpatterns =[
  path('notices/',view_notices,name='notices'),
  path('research/',view_research,name='research'),
  path('scholarship/',view_scholarship,name='scholarship'),
]