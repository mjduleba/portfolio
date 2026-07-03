from rest_framework.routers import DefaultRouter
from .views import ExperienceViewSet

router = DefaultRouter()
router.register(r'experience', ExperienceViewSet)

urlpatterns = router.urls
