from django.contrib import admin
from .models import Intent
# Register your models here.
class IntelAdmin(admin.ModelAdmin):
  list_display = ['question', 'answer']

admin.site.register(Intent,IntelAdmin)