from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()
        messages.success(request, "Registration successful")
        return redirect('login')  
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
      name = request.POST.get('l-email')
      password = request.POST.get('l-password')
      user = authenticate(username=name, password=password)
      if user is not None:
          login(request, user)
          messages.success(request, "Login successful")
          return redirect('home') 
      else:
          messages.error(request, "something went wrong!!!")
    return render(request, 'login.html')

def custom_logout_view(request):
    logout(request)
    return redirect('home') 