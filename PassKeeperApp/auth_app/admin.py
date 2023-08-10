from django.contrib import admin
from PassKeeperApp.auth_app.models import AppUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_superuser', 'is_staff', 'email', 'is_active']
    list_editable = ['is_superuser', 'is_staff', 'is_active']
    search_fields = ['username']


admin.site.register(AppUser, UserAdmin)
