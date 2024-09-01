from django.shortcuts import render

# Create your views here.
def views_blogs(request):
  return render(request,'blogs.html')