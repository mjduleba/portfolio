from rest_framework import viewsets
from .models import UserProfile
from .serializers import ProfileSerializer

class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
