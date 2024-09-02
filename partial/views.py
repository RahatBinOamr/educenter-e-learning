from django.shortcuts import render

# Create your views here.
def view_notices(request):
  return render(request, 'notices.html')

def view_research(request):
  return render(request, 'research.html')

def view_scholarship(request):
  return render(request, 'scholarship.html')