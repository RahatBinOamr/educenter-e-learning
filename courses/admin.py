from django.contrib import admin
from .models import Interested,Department,Teacher
# Register your models here.


class InterestedInline(admin.TabularInline):
  model = Interested

class TeacherAdmin(admin.ModelAdmin):
  inlines =[InterestedInline]






admin.site.register( Teacher, TeacherAdmin)
admin.site.register(Interested)
admin.site.register(Department)