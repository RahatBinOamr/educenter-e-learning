# chatbot/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('chatbot/', views.chatbot_response, name='chatbot_response'),
    path('chatbot-page/', views.chatbot_page, name='chatbot_page'),
]
