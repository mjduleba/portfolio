from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = router.urls
