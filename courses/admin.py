from django.contrib import admin
from .models import Interested,Department,Teacher,Course,Modules,Speaker,Event
# Register your models here.


class InterestedInline(admin.TabularInline):
  model = Interested

class TeacherAdmin(admin.ModelAdmin):
  inlines =[InterestedInline]


class ModuleInline(admin.TabularInline):
  model = Modules

class CourseAdmin(admin.ModelAdmin):
  inlines =[ModuleInline]


class SpeakerInline(admin.TabularInline):
  model = Speaker

class EventAdmin(admin.ModelAdmin):
  inlines =[SpeakerInline]

admin.site.register( Teacher, TeacherAdmin)
admin.site.register(Department)

admin.site.register(Course,CourseAdmin)
admin.site.register(Event,EventAdmin)