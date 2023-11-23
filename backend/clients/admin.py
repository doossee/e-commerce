from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['id', 'username', 'mobile']


admin.site.register(CustomUser, CustomUserAdmin)
