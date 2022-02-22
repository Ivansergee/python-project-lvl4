from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

UserAdmin.list_display = ('username', 'first_name', 'last_name', 'created_at')

admin.site.register(User, UserAdmin)