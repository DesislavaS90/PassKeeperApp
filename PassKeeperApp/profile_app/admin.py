from django.contrib import admin

from PassKeeperApp.profile_app.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name']
    list_per_page = 10
    fields = ('first_name', 'last_name')


admin.site.register(Profile, ProfileAdmin)
