from django.contrib import admin
from .models import *
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_number', 'start_date', 'status', 'optimized_process')
    list_filter = ('status', 'optimized_process')
    search_fields = ('name', 'registration_number', 'customer', 'process_owner', 'project_manager')

admin.site.register(Role)

admin.site.register(Department)