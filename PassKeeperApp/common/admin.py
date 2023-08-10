from django.contrib import admin
from PassKeeperApp.common.models import Facts, Advices, Fun

admin.site.site_header = "PassKeeper Admin"
admin.site.site_title = "PassKeeper Admin Portal"
admin.site.index_title = "Welcome to PassKeeper Admin Portal"


class FactsAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']

    def has_delete_permission(self, request, obj=None):
        return False


class AdvicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']

    def has_delete_permission(self, request, obj=None):
        return False


class FunAdmin(admin.ModelAdmin):
    list_display = ['title']

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Facts, FactsAdmin)
admin.site.register(Advices, AdvicesAdmin)
admin.site.register(Fun, FunAdmin)