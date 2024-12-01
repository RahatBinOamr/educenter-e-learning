from django.shortcuts import render
from .models import Notice
# Create your views here.
def view_notices(request):
  notices = Notice.objects.all()
  context ={
    "notices":notices
  }
  return render(request, 'notices.html',context)
def singe_notices(request,slug):
  notice = Notice.objects.get(slug=slug)
  context ={
    "notice":notice
  }
  return render(request, 'singleNotice.html', context)
def view_research(request):
  return render(request, 'research.html')

def view_scholarship(request):
  return render(request, 'scholarship.html')