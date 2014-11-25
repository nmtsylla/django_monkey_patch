from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
UserAdmin.list_display += ('photo',)
UserAdmin.fieldsets[0][1]['fields'] += ('photo',)
