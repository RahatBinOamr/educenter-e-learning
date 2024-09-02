from django.urls import path
from .views import register,login_view,custom_logout_view
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', custom_logout_view, name='logout'),
]