from django.contrib import admin
from PassKeeperApp.password_generator.models import PasswordGenerator


class PasswordGeneratorAdmin(admin.ModelAdmin):
    list_display = ('user', 'length', 'created_at', 'use_uppercase', 'use_numbers', 'use_special')
    filter_fields = ('length', 'use_uppercase', 'use_numbers', 'use_special')
    search_fields = ['length']
    list_per_page = 10


admin.site.register(PasswordGenerator, PasswordGeneratorAdmin)

