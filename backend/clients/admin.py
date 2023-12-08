from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['id', 'first_name', 'last_name', 'mobile']
    list_display_links = ['id', 'first_name', 'last_name']


admin.site.register(CustomUser, CustomUserAdmin)
