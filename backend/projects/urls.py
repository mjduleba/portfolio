from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

# Create router
router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

# Define URL patterns
urlpatterns = router.urls