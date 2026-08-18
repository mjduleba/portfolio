from django.contrib import admin
from django.urls import path, include

# URL patterns for porfolio backend
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('api/', include('projects.urls')),
    path('api/', include('experience.urls')),
    path('api/', include('skills.urls')),
    path('api/', include('userprofile.urls')),
    path('api/', include('tools.urls')),
]
