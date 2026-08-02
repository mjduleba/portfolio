from rest_framework import viewsets
from .models import Tool
from .serializers import ToolSerializer

class ToolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tool.objects.all()
    serializer_class = ToolSerializer
    lookup_field = 'slug'
