from django.contrib import admin
from .models import Tool, SkillAgentEntry


class SkillAgentEntryInline(admin.TabularInline):
    model = SkillAgentEntry
    extra = 1


class ToolAdmin(admin.ModelAdmin):
    inlines = [SkillAgentEntryInline]


admin.site.register(Tool, ToolAdmin)
