from django.shortcuts import get_object_or_404, render
from .models import Course,Event,Teacher,Speaker,Modules,Department
# Create your views here.
def views_courses (request):
  courses = Course.objects.all()
  context ={
    "courses": courses
  }
  return render(request,'courses.html',context)

def single_course(request, slug):
    courses_with_slug = Course.objects.filter(slug=slug)
    if courses_with_slug.count() > 1:
        courses_to_delete = courses_with_slug[1:]
        for course in courses_to_delete:
            course.delete()
    course = get_object_or_404(Course, slug=slug)
    modules = Modules.objects.filter(course=course)
    context = {
        "course": course,
        "modules": modules,
    }
    return render(request, 'singleCourse.html', context)

def views_events (request):
  events = Event.objects.all()
  context ={
    "events": events
  }
  return render(request,'events.html',context)

def single_event(request,slug):
  event = Event.objects.get(slug=slug)
  speakers = Speaker.objects.filter(event=event)
  context = {"event": event,"speakers": speakers}
  return render(request,'singleEvent.html',context)

def views_teachers(request):
  departments = Department.objects.all()
  teachers = Teacher.objects.select_related('department')
  context ={
    'departments': departments,
    "teachers": teachers
  }
  return render(request,'teachers.html',context)

def single_teacher(request,slug):
  teacher = Teacher.objects.get(slug=slug)
  context ={
    "teacher": teacher
  }
  return render(request,'singleTeacher.html',context)

def create(request, *args, **kwargs):
 
  pass 