from django.contrib import admin
from .models import Info

class ContactAdmin(admin.ModelAdmin):
    list_display = ['place', 'phone_number', 'email']
    
admin.site.register(Info, ContactAdmin)