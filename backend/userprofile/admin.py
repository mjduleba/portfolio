from django.contrib import admin
from .models import Hobby, UserProfile


class HobbyInline(admin.TabularInline):
    model = Hobby
    extra = 1


class UserProfileAdmin(admin.ModelAdmin):
    inlines = [HobbyInline]


# Register UserProfile model in the admin site
admin.site.register(UserProfile, UserProfileAdmin)