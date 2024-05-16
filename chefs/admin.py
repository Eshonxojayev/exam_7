from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Chef, Cooker, Assistantcook
from django.contrib.admin.sites import AlreadyRegistered

@admin.register(Assistantcook)
class AssistantcookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email',)
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email')
    search_fields = ('id', 'first_name', 'last_name', 'username',)
    list_filter = ('id', 'first_name', 'last_name',)
    ordering = ('id', 'name')

@admin.register(Cooker)
class CookerAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email',)
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email')
    search_fields = ('id', 'first_name', 'last_name', 'username', 'email')
    list_filter = ('id', 'first_name', 'last_name', 'username', 'email')
    ordering = ('id', 'name')

@admin.register(Chef)
class ChefAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'username', 'email',)
    list_display_links = ('id', 'first_name', 'last_name', 'username', 'email')
    search_fields = ('id', 'first_name', 'last_name', 'username', 'email')
    list_filter = ('id', 'first_name', 'last_name', 'username', 'email')
    ordering = ('id', 'name')


admin.site.register(Chef, ChefAdmin)
admin.site.register(Cooker, CookerAdmin)
admin.site.register(Assistantcook, AssistantcookAdmin)
