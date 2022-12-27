from django.contrib import admin
from .models import Job, Category, Apply

# Register your models here.

# 1. To customize the way the model is displayed in the admin interface.
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'job_type', 'vacancy', 'salary', 'experience', 'category']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    
class ApplyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'cv', 'created_at']
    
# 2. Register the models with the admin interface
admin.site.register(Job, JobAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Apply, ApplyAdmin)
