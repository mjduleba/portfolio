from django.contrib import admin
from .models import Education, Hobby, UserProfile


class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [HobbyInline, EducationInline]


# Register UserProfile model in the admin site
admin.site.register(UserProfile, UserProfileAdmin)