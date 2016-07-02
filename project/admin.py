from django.contrib import admin

# Register your models here.
from project.models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name')
    pass
