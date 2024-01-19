from django.contrib import admin
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','is_active','is_staff')


admin.site.register(CustomUser,CustomUserAdmin)