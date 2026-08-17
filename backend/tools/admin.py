from django.contrib import admin
from .models import Tool, SkillAgentEntry, GuidePattern, GuideExampleProblem


class SkillAgentEntryInline(admin.TabularInline):
    model = SkillAgentEntry
    extra = 1


class GuidePatternInline(admin.TabularInline):
    model = GuidePattern
    extra = 1
    show_change_link = True


class ToolAdmin(admin.ModelAdmin):
    inlines = [SkillAgentEntryInline, GuidePatternInline]


admin.site.register(Tool, ToolAdmin)


class GuideExampleProblemInline(admin.TabularInline):
    model = GuideExampleProblem
    extra = 1


class GuidePatternAdmin(admin.ModelAdmin):
    inlines = [GuideExampleProblemInline]


admin.site.register(GuidePattern, GuidePatternAdmin)
