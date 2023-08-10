from django.contrib import admin
from PassKeeperApp.my_credentials.models import Category, MyCredentials


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'comment')
    filter_fields = ('name', 'user',)
    ordering = ('user',)
    list_per_page = 10


admin.site.register(Category, CategoryAdmin)

