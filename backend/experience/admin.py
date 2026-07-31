from django.contrib import admin
from .models import Experience, ExperienceBullet


class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1


class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceBulletInline]


# Register Experience model in the admin site
admin.site.register(Experience, ExperienceAdmin)
