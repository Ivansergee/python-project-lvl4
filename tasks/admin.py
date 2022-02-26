from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Status

UserAdmin.list_display = ('username', 'first_name', 'last_name', 'created_at')

admin.site.register(User, UserAdmin)
admin.site.register(Status)