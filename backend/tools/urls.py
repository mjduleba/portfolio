from rest_framework.routers import DefaultRouter
from .views import ToolViewSet

# Create router
router = DefaultRouter()
router.register(r'tools', ToolViewSet)

# Define URL patterns
urlpatterns = router.urls
