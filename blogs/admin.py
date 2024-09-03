from django.contrib import admin
from .models import Comment,Category,Blog
# Register your models here.
class commentInline(admin.TabularInline):
  model = Comment

class blogAdmin(admin.ModelAdmin):
  inlines = [commentInline]
  
admin.site.register(Blog,blogAdmin)
admin.site.register(Category)