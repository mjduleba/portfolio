from django.contrib import admin
from .models import Project, ProjectBullet


class ProjectBulletInline(admin.TabularInline):
    model = ProjectBullet
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectBulletInline]


# Register Project model with the admin site
admin.site.register(Project, ProjectAdmin)
