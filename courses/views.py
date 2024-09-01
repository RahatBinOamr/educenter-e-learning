from django.shortcuts import render

# Create your views here.
def views_courses (request):
  return render(request,'courses.html')


def views_events (request):
  return render(request,'events.html')