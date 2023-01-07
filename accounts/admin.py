from django.contrib import admin
from .models import Profile , City

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'city', 'phone_number', 'image']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']
    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(City, CityAdmin)